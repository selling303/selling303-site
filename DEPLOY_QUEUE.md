# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-04-25 production deploy — see DEPLOY_LOG.md)_

## Pending

- 2026-04-26 — New blog post: **Spring 2026 Move-Up Market Report: Where Are South Denver Families Upgrading To?** (`/blog/spring-2026-move-up-market-report-south-denver`). Q1 2026 DMAR + REcolorado data on Highlands Ranch, Parker, and Castle Pines as move-up landing spots. Move-Up Sellers cluster, Highlands Ranch geographic pillar.
- 2026-04-26 — Content calendar Day 22 (HR expired-listing case study) deferred 90 days pending anonymized real-deal data from Jacob; revisit on or after 2026-07-25.
- 2026-04-26 — Content cluster map updated: added new move-up sellers spoke for the spring market report.
- 2026-04-26 — Move-up market report comparison visual rewritten for maximum AEO/SEO pickup: replaced styled-div cards with real `<table>` (caption, thead, scoped th, tbody), wrapped in `<figure>` with `aria-labelledby` to the H3, added JSON-LD `Dataset` schema (temporalCoverage, spatialCoverage, variableMeasured, creator, publisher), Schema.org `Place` Microdata per row with `containedInPlace`, per-cell `<meta itemprop="value">` machine-readable values, sample sizes inline (n=499/448/176), spelled-out date range, and term definitions in the figcaption.
- 2026-04-26 — Comparison visual made fully responsive: removed `min-width: 720px` that forced horizontal scroll on mobile, scoped CSS via `.aeo-comp-table` class, added stacked card-style mobile layout (≤700px) using `display: block` on rows + `td::before { content: attr(data-label) }` for column labels. Same semantic table on every breakpoint — only the presentation changes.
