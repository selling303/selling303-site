#!/usr/bin/env bash
# github-api-push.sh — Push file changes to GitHub via REST API
# Replaces git clone + commit + push workflow in Cowork sandbox
# Zero disk usage, no FUSE issues, no lock files
#
# Usage: github-api-push.sh <commit_message> <file1> [file2] [file3] ...
#
# Environment:
#   GITHUB_PAT    — GitHub personal access token (required)
#   GITHUB_REPO   — Owner/repo (default: selling303/selling303-site)
#   GITHUB_BRANCH — Target branch (default: main)
#
# Files are read from the FUSE mount path and pushed to GitHub.
# The script translates between FUSE mount paths and repo-relative paths.

set -euo pipefail

# --- Config ---
REPO="${GITHUB_REPO:-selling303/selling303-site}"
BRANCH="${GITHUB_BRANCH:-main}"
API="https://api.github.com"
COMMIT_MSG="${1:?Usage: github-api-push.sh <commit_message> <file1> [file2] ...}"
shift
FILES=("$@")

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "Error: No files specified" >&2
  exit 1
fi

if [[ -z "${GITHUB_PAT:-}" ]]; then
  echo "Error: GITHUB_PAT environment variable not set" >&2
  exit 1
fi

AUTH="Authorization: token ${GITHUB_PAT}"
ACCEPT="Accept: application/vnd.github.v3+json"

# --- Helper: JSON-escape a string ---
json_escape() {
  python3 -c "import json,sys; print(json.dumps(sys.argv[1]))" "$1"
}

# Pre-escape the commit message for safe JSON embedding
# Returns a quoted string like "my message" — strip outer quotes when embedding
COMMIT_MSG_ESCAPED=$(json_escape "$COMMIT_MSG")

# --- Helper: API call ---
gh_api() {
  local method="$1" endpoint="$2" data="${3:-}"
  local url="${API}/repos/${REPO}${endpoint}"

  if [[ -n "$data" ]]; then
    curl -sf -X "$method" -H "$AUTH" -H "$ACCEPT" \
      -H "Content-Type: application/json" \
      -d "$data" "$url"
  else
    curl -sf -X "$method" -H "$AUTH" -H "$ACCEPT" "$url"
  fi
}

# --- Detect mount prefix ---
# In Cowork sandbox, the repo is mounted at a path like:
#   /sessions/<name>/mnt/selling303-site/
# We need to strip this prefix to get repo-relative paths.
# Also handles direct repo paths like /Users/.../selling303-site/
detect_mount_prefix() {
  local file="$1"
  # Match sandbox mount path
  if [[ "$file" =~ ^/sessions/[^/]+/mnt/selling303-site/ ]]; then
    echo "${file%%selling303-site/*}selling303-site/"
  # Match macOS local path
  elif [[ "$file" =~ ^/Users/[^/]+/selling303-site/ ]]; then
    echo "${file%%selling303-site/*}selling303-site/"
  else
    echo ""
  fi
}

# --- Step 1: Get current commit SHA of branch ---
echo "Getting current HEAD of ${BRANCH}..."
REF_JSON=$(gh_api GET "/git/refs/heads/${BRANCH}")
HEAD_SHA=$(echo "$REF_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['object']['sha'])")
echo "  HEAD: ${HEAD_SHA}"

# --- Step 2: Get the tree SHA from that commit ---
COMMIT_JSON=$(gh_api GET "/git/commits/${HEAD_SHA}")
BASE_TREE_SHA=$(echo "$COMMIT_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['tree']['sha'])")
echo "  Base tree: ${BASE_TREE_SHA}"

# --- Step 3: Create blobs for each file ---
TREE_ENTRIES="["
FIRST=true

for FILE_PATH in "${FILES[@]}"; do
  # Determine repo-relative path
  PREFIX=$(detect_mount_prefix "$FILE_PATH")
  if [[ -n "$PREFIX" ]]; then
    REL_PATH="${FILE_PATH#$PREFIX}"
  else
    # Assume it's already a repo-relative path
    REL_PATH="$FILE_PATH"
  fi

  echo "Creating blob for ${REL_PATH}..."

  # Read file and base64 encode it
  CONTENT_B64=$(base64 < "$FILE_PATH")

  # Create blob via API
  BLOB_JSON=$(gh_api POST "/git/blobs" "{\"content\":\"${CONTENT_B64}\",\"encoding\":\"base64\"}")
  BLOB_SHA=$(echo "$BLOB_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
  echo "  Blob: ${BLOB_SHA}"

  # Add to tree entries
  if [[ "$FIRST" == "true" ]]; then
    FIRST=false
  else
    TREE_ENTRIES+=","
  fi
  REL_PATH_ESCAPED=$(json_escape "$REL_PATH")
  TREE_ENTRIES+="{\"path\":${REL_PATH_ESCAPED},\"mode\":\"100644\",\"type\":\"blob\",\"sha\":\"${BLOB_SHA}\"}"
done

TREE_ENTRIES+="]"

# --- Step 4: Create new tree ---
echo "Creating tree..."
TREE_JSON=$(gh_api POST "/git/trees" "{\"base_tree\":\"${BASE_TREE_SHA}\",\"tree\":${TREE_ENTRIES}}")
NEW_TREE_SHA=$(echo "$TREE_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  New tree: ${NEW_TREE_SHA}"

# --- Step 5: Create commit ---
echo "Creating commit..."
COMMIT_CREATE_JSON=$(gh_api POST "/git/commits" "{\"message\":${COMMIT_MSG_ESCAPED},\"tree\":\"${NEW_TREE_SHA}\",\"parents\":[\"${HEAD_SHA}\"]}")
NEW_COMMIT_SHA=$(echo "$COMMIT_CREATE_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  Commit: ${NEW_COMMIT_SHA}"

# --- Step 6: Update branch ref ---
echo "Updating ${BRANCH} to ${NEW_COMMIT_SHA}..."
gh_api PATCH "/git/refs/heads/${BRANCH}" "{\"sha\":\"${NEW_COMMIT_SHA}\"}" > /dev/null
echo ""
echo "Pushed to ${BRANCH}: ${NEW_COMMIT_SHA}"
echo "  ${COMMIT_MSG}"
echo "  Files: ${FILES[*]}"
