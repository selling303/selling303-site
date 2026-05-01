# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-04-26 production deploy — see DEPLOY_LOG.md)_

## Pending

- 2026-04-30 — [BLOG] Day 27 nightly post — `expired-listing-trap-englewood-switching-agents-2026.md`. BOFU expired-listing seller advice for Englewood (Specialization: `/expired-listings`, Geographic: `/neighborhoods/englewood`). Includes optimized comparison-table visual (Closed vs. Expired Englewood single-family Q1 2026 — 138 closed at 14-day median DIM vs. 39 expired at 69-day median DIM, sourced from REcolorado Q1 2026 export). Tier-list opportunity for root-cause severity flagged inline as Phase 3 deferral. Calendar entry [x] marked. Cluster map updated under Expired Listings pillar. Visual inventory updated.
- 2026-04-29 — [BLOG] Day 26 nightly post — `greenwood-village-worth-the-price-tag-relocation-2026.md`. TOFU relocation post for Greenwood Village (Specialization: `/relocation`, Geographic: `/neighborhoods/greenwood-village`). Includes optimized comparison-table visual (GV vs. Castle Pines vs. Highlands Ranch vs. metro median, Q1 2026 REcolorado MLS data). Calendar entry [x] marked. Cluster map updated under Relocation pillar. Visual inventory updated.
- 2026-04-26 — [VISUAL] `closing-costs-littleton-first-time-buyers-2026.md` — replaced the plain `<table>` "What does a $475K Littleton closing sheet actually look like?" with a styled settlement-statement visual. Brand navy header strip, category sections (Down Payment, Lender Fees, Title Fees, Prepaid Items with 3 sub-items, Other Costs with 2 sub-items), tabular dollar amounts, dashed sub-section dividers, prominent navy total row at the bottom ($32,000–$43,900). Inline styles only, real text in DOM (AEO-friendly), source attribution baked in. Differentiates visually from the upper bucket-overview cost-breakdown card.
- 2026-04-27 — [SEO-AEO] Surname-pollution disambiguation. Replaced inline Person/RealEstateAgent/author/publisher schema with `@id` refs to canonical entities (`#agent` on /, /about; new `#organization` added to /, /about) across 15 templates: blog/[slug], success-stories/[slug], 6 specialization pillars, my-seller-promise, 3 tools calculators, neighborhoods/[slug], plus index and about (Organization additions). Fixes Google knowledge-graph collision with other "Stark" public figures driving 78% of last week's GSC impressions. See project DEPLOY_QUEUE.md for full file list and rollback path.
