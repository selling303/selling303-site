# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-18 PM production deploy — see DEPLOY_LOG.md)_

## Pending

- 2026-05-18 [SEO-AEO] Week 5 audit: total 32.53 (+3.27 vs Wk4). Parker relocation blog ranks #1 organic Google SERP — first weekly-rotation win. PSI fix on why-house-not-selling-denver verified live (mobile 0.41 → 0.87). New CLS regression on relist-home-littleton-after-expired-listing desktop (CLS 0.594). See aeo-seo-expert/DEPLOY_QUEUE.md for full Sprint + carryover.
- 2026-05-18 [SEO-AEO] CLS-REGRESSION-RELIST queued — investigate width/height/font-swap layout shift on relist-home-littleton-after-expired-listing; deploy to main when found.
- 2026-05-18 [SEO-AEO] TITLE-LEN top-5 re-commit — drafts to be delivered Thu 2026-05-21 for Jacob review then push to main.
- 2026-05-18 [SEO-AEO] STATIC-SITEMAP-REMOVE carryover — `git rm` `sitemap.xml` + `robots.txt` at repo root on next deploy-to-netlify Mode 1 call (still blocked in sandbox).
