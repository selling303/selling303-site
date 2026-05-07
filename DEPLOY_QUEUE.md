# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-06 PM production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-05-06** — Three new GBP-image generator scripts in `scripts/`: `generate-gbp-image.py` (Numeric Hero Card — Tier-2 Option 1, reusable for every blog post), `generate-gbp-data-viz.py` (Live Data Snapshot — Tier-2 Option 3, deadline-spine template), `generate-gbp-phone-mockup.py` (Phone Mockup — Tier-2 Option 2, brand-faithful widget render). All Python+Pillow, system-font-only, zero external dependencies. Replaces Canva for GBP image generation. Awaiting Jacob's pick on which to use as the default for the 2026 NOV protest post.
- **2026-05-06** — New blog post: "Why Pricing Reductions in Highlands Ranch Don't Always Work — and What Does" (`src/content/blog/price-reductions-highlands-ranch-what-works-2026.md`). Day 3 of May content calendar. Expired Listings pillar + Highlands Ranch geographic pillar, BOFU seller advice. Built around April 2026 REcolorado MLS data for HR (n=150: 131 closed, 22 expired, 4 withdrawn). New Tier 0 single-metric-bar-chart: median DIM by 5 sale-outcome buckets (Sold ≥100% / 3 days, Sold 95–99% / 21 days, Sold 90–94% / 70 days, Sold <90% / 164 days, Expired / 87 days) with full Schema.org Microdata + parallel JSON-LD Dataset + bound source row. Updates: `content-calendar-2026.md` (Day 3 marked drafted, visual line revised post-Compelling Question Flow), `content-cluster-map.md` (added to Expired Listings cluster), `visual-inventory.md` (logged new optimized chart entry).
