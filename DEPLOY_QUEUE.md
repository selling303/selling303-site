# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-18 PM production deploy — see DEPLOY_LOG.md)_

## Pending

- 2026-05-18 [BLOG — Day 15 nightly] New post: "Castle Pines New Construction 2026: Community Deep Dive" (`/blog/castle-pines-new-construction-builder-community-deep-dive-2026`). New Construction × Castle Pines, MOFU, buyer advice. Tier 0 **price-ladder-svg** (library, 2nd live ship after Lone Tree 2026-05-15) — 4-tier Castle Pines new construction ladder (Lennar Merseyside paired $475K–$580K / mid-Canyons Shea+Tri Pointe $700K–$950K / Canyons move-up Toll+Shea $1M–$1.5M / Canyons Luxe + CP Village custom $1.5M+). Bars scale linearly to median fin sqft (120/210/310/420px). Anchored to REcolorado MLS Castle Pines + Castle Pines North April 2026 (n=23 closed, median $1,011,000 at 97% CP/OLP, 18 DIM, 108 active). Compelling Question Flow chose price-ladder-svg (24) over profile-card-grid (21, freshness penalty) and comparison-table (15, Phrase-Cell Density Trip-Wire risk). blog-review: 1 readability HARD FAIL on initial run (FK 12.1, avg 22.3, p90 38.0) → targeted sentence-splits applied (8 long sentences split at conjunctions / em-dashes), final 5/5 PASS (avg 16.1, p90 27.0, Flesch 55.1, FK 9.6, para 69.5). Dimension 10 pre-checked CLEAN — no fabricated client-mix or volume claims; only verified $46M + 100.6% CP/OLP trust signals. Calendar Day 15 marked [x]; cluster map updated under New Construction; visual inventory updated.
- 2026-05-18 [SEO-AEO] Week 5 audit: total 32.53 (+3.27 vs Wk4). Parker relocation blog ranks #1 organic Google SERP — first weekly-rotation win. PSI fix on why-house-not-selling-denver verified live (mobile 0.41 → 0.87). New CLS regression on relist-home-littleton-after-expired-listing desktop (CLS 0.594). See aeo-seo-expert/DEPLOY_QUEUE.md for full Sprint + carryover.
- 2026-05-18 [SEO-AEO] CLS-REGRESSION-RELIST queued — investigate width/height/font-swap layout shift on relist-home-littleton-after-expired-listing; deploy to main when found.
- 2026-05-18 [SEO-AEO] TITLE-LEN top-5 re-commit — drafts to be delivered Thu 2026-05-21 for Jacob review then push to main.
- 2026-05-18 [SEO-AEO] STATIC-SITEMAP-REMOVE carryover — `git rm` `sitemap.xml` + `robots.txt` at repo root on next deploy-to-netlify Mode 1 call (still blocked in sandbox).
