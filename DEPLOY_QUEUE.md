# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- 2026-04-20 Added "ClientClarity Portal" link to footer Quick Links (points to clients.selling303.com)
- 2026-04-21 New blog post: "Why Your Centennial Home Isn't Getting Offers — and How to Fix It Before Summer" (`/blog/why-centennial-home-not-getting-offers`) — diagnostic framework for stale Centennial listings, Q1 2026 REcolorado data, Expired Listings + Centennial cluster
- 2026-04-21 Added Cost of Living Calculator (Week 1 calc #3): new component `src/components/calculators/CostOfLivingCalculator.astro` comparing South Denver Metro to 27 major U.S. cities with category breakdown (housing, groceries, utilities, transportation, healthcare) + state income tax callout. Data sourced from BLS CPI, Tax Foundation, Zillow (April 2026, stamped with source links in disclaimer). New standalone page at `/tools/cost-of-living-calculator` with Colorado tax advantage, housing comparison, and "what $100K looks like" explainers + FAQ. Embedded on `/relocation` with new TOC entry "Cost of Living". Replaced Coming Soon card on `/tools` hub with active Cost of Living entry; updated ItemList schema. Week 1 of conversion sprint complete.
