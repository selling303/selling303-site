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
- 2026-04-26 — [SEO-AEO] [TWITTER-MISSING] Added Twitter Card meta tags to `src/components/SEO.astro` (twitter:card=summary_large_image, twitter:site=@selling303, twitter:creator=@selling303, plus title/description/image). Forces large-image preview when selling303.com URLs are shared on X. Score lift: +0.4 (On-page +5).
- 2026-04-26 — [SEO-AEO] [BREADCRUMB-MISSING] Added BreadcrumbList JSON-LD to 8 templates: blog/[slug], neighborhoods/[slug], and 6 specialization pillars (expired-listings, move-up-sellers, first-time-homebuyers, first-time-homesellers, new-construction, relocation). Used the existing `Breadcrumbs.astro` component with a new `schemaOnly` prop (default false; preserves visible breadcrumbs on success-stories). Hierarchy: Home → Section → Page. Zero visual impact on the 8 new templates. Score lift: +1.0 (On-page +15 from 0/15).
- 2026-04-26 — [SEO-AEO] [PILLAR-GEO-MISSING] Added one contextual `/neighborhoods/<slug>` link in the intro of 9 blog posts that previously had no geo pillar link: 7-smartest-home-upgrades (HR), closing-costs-colorado-buyers (Centennial), cost-to-sell-house-colorado (HR), littleton-vs-highlands-ranch (both), parker-vs-castle-pines (both), what-happens-after-accepting-offer (Centennial), what-realtor-does-to-earn-commission (HR), why-homes-sit-on-market-south-denver (Centennial), why-house-not-selling-denver (HR). Single visible hyperlink per post, no other body changes. Score lift: +1.4 (Content 60.5 → ~67).
