# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-21 production deploy — merge 54c6025, see DEPLOY_LOG.md.)_

- 2026-10-27 scripts/generate-gbp-data-viz.py: removed the hardcoded "Free calculator · 30 seconds" line under the question (left over from the Notice of Valuation post). New optional --tagline flag; --question now required; --headline/--hero-number no longer required. Script-only, no site build impact.
- 2026-10-30 Outgrown Your Home follow-ups:
  - src/pages/og/[...slug].png.ts: added buy-before-you-sell, renovate-before-selling, what-to-fix-before-selling, and assumable-loans to OG_STATIC_TITLES (their /og/*.png share images were 404ing).
  - content-cluster-map.md: added sections 7 (three move-up pillars) and 8 (/assumable-loans) with link-when guidance, plus cross-link table rows. Doc only, no build impact.
  - src/pages/first-time-homebuyers.astro: contextual /assumable-loans link in the Pre-Approval step.
  - src/content/blog/price-cut-vs-2-1-buydown-south-denver-metro-2026.md: new short paragraph after the seller recorded-price paragraph linking to /assumable-loans#sellers.
- 2026-10-30 New blog post: src/content/blog/buy-or-sell-first-south-denver-move-up.md ("Buy or Sell First? 5 Ways to Move Up in the South Denver Metro"). Equity-advance-first decision hub with Tier 2 path-finder tool and cost table. Also content-calendar-2026.md (off-calendar entry), content-cluster-map.md (Move-Up spoke), visual-inventory.md (entry). Follow-up idea: rework /buy-before-you-sell so it doesn't overlap.
