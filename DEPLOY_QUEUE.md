# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-21 production deploy — merge 54c6025, see DEPLOY_LOG.md.)_

- 2026-10-27 scripts/generate-gbp-data-viz.py: removed the hardcoded "Free calculator · 30 seconds" line under the question (left over from the Notice of Valuation post). New optional --tagline flag; --question now required; --headline/--hero-number no longer required. Script-only, no site build impact.
