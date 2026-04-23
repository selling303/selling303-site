# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-04-21 production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-04-21** — New blog post: "The Hidden Costs of Selling Your Home in Arapahoe County — A First-Time Seller's Net Sheet" (`/blog/hidden-costs-selling-home-arapahoe-county-net-sheet-2026`). Cluster: `/first-time-homesellers` + `/centennial`. Uses Centennial Q1 2026 REcolorado MLS data (n=269 closed SFR). Visual: inline proportional net-sheet cost-breakdown bars.
- **2026-04-21** — Content calendar marked Day 18 drafted. Cluster map updated with new post in First-Time Home Sellers cluster.
- **2026-04-22** — New blog post: "Move-Up Buyer's Checklist: Going from a Starter in Englewood to More Space in Parker" (`/blog/move-up-englewood-to-parker-checklist-2026`). Cluster: `/move-up-sellers` + `/englewood`. MOFU. Uses Englewood + Parker Q1 2026 REcolorado MLS data (n=138 closed SFR Englewood / $634K median / 14 DIM / 97% CP/OLP; n=330 closed SFR Parker / $717,450 median / 24 DIM / 98% CP/OLP) and DMAR March 2026. Visual: inline HowTo step-tracker (7-step move-up timeline, Days 0–120) with Schema.org HowTo microdata. Internal cross-links: move-up-sellers pillar, Englewood neighborhood, equity-to-move-up-HR, Centennial-to-HR coordination, cost-to-sell-Colorado, watering-restrictions-guide, moving-to-Parker-relocation-guide, when-to-sell-Parker.
- **2026-04-22** — Content calendar marked Day 19 drafted. Cluster map updated with new post in Move-Up Sellers cluster.
- **2026-04-22** — Skill update (`~/.claude/skills/deploy-to-netlify/SKILL.md`, outside this repo): removed obsolete Path B (Chrome MCP) workflow and April 21 PREFLIGHT block from Mode 2 Step 4. `api.netlify.com` has been reachable from the sandbox since the 2026-04-21 allowlist change (verified this session with 401 from `/api/v1/sites`), so direct curl to the build hook is now the only supported path.

