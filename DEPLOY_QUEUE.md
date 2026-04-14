# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- **2026-04-13** — Added GA4 `page_not_found` custom event to 404.astro (tracks broken URL path, referrer, and full URL)
- **2026-04-13** — Updated CLAUDE.md deploy protocol to reference GitHub API instead of git commands (MUST be pushed to main before next deploy)
- **2026-04-13** — Hardened github-api-push.sh: added JSON escaping for commit messages and file paths (prevents silent failures on special characters)
