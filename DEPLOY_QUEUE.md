# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

## 2026-04-15 — Success Story placeholder hide

- Added optional `draft: z.boolean()` field to `successStories` Zod schema in `src/content.config.ts`.
- Marked 6 placeholder success stories as `draft: true` (listing data only, stories pending client interviews): 8781-flora-ct-arvada, 22461-e-union-circle-aurora, 4360-w-wagon-trail-dr-denver, 9559-w-coal-mine-ave-littleton, 301-w-lehow-ave-englewood, 10315-ravenswood-ln-highlands-ranch.
- `/sell/success-stories/` index page now filters out drafts from the card grid and CollectionPage ItemList schema.
- `[slug].astro` template: draft stories render with `<meta name="robots" content="noindex, nofollow" />` and skip all Schema.org structured-data scripts (RealEstateListing / Review / Article / ImageObject / FAQPage) to avoid thin-content + structured-data-mismatch flags.
- `astro.config.mjs`: added sitemap `filter` that excludes the 6 draft slugs. Single source of truth — remove a slug from the `DRAFT_SUCCESS_STORY_SLUGS` array when its story is completed.
- Verified via local build: 0 draft slugs in rendered index, 0 draft URLs in sitemap-0.xml, draft pages include the robots meta, non-draft pages unchanged.
- Ride-along with tomorrow's nightly blog deploy — no standalone production push needed.

## 2026-04-16 — Schema markup upgrade for AI entity recognition

- Homepage (`index.astro`): merged two duplicate `RealEstateAgent` schema blocks into one unified `["Person", "RealEstateAgent"]` block with `@id`, `jobTitle`, `alternateName`. Fixed stale `reviewCount` from 52 → 47 (matches current Google reviews). Added Homes.com and Nextdoor URLs to `sameAs` array.
- About page (`about.astro`): upgraded thin `Person` schema to full `["Person", "RealEstateAgent"]` with `@id` linking to homepage entity, `mainEntityOfPage`, `image`, `address`, `areaServed` (9 cities), `aggregateRating`, `hasCredential`, `knowsAbout`, and full `sameAs` array (12 URLs).
- Ride-along with nightly blog deploy.
- Added awards (DMAR Excellence 2024–2026, 5280 Black Diamond, Real Trends Verified), credentials (Who's Who in Luxury RE), and memberOf (DMAR, Who's Who) to both homepage and about page schema. Added Real Trends and 5280 directory URLs to `sameAs`.
- Added Wikidata entity URL (Q139385406) to `sameAs` on both homepage and about page.
- Added visual badge/awards section to about page: DMAR Excellence Gold, 5280 Top Producer, Real Trends Verified, Who's Who in Luxury RE, RENE. White background section between Track Record and CTA.
- Badge images: all five logos imported as PNGs through Astro `<Image>` pipeline (ea25_digitalawards_gold.png, 5280-magazine-black.png, rtv-black.png, WWLRE_BLACK.png, rene-color.png).
- Three badges linked to profile pages: DMAR → excellenceawards, 5280 → directory profile, Real Trends → agent profile.
- Added two new Track Record credential tiles: "Top 10 — Agent by Verified Sales — RealTrends" and "Top 1.5% — of U.S. Real Estate Professionals."
- CSS: fixed logo clipping (height-based sizing with width:auto), removed opacity fade on badges.

## 2026-04-16 — Two blog posts (Day 12 recovery + Day 13)

- Day 12 recovery: "South Denver Market Update: What April 2026 Means for Sellers Sitting on Expired Listings" (`src/content/blog/south-denver-market-update-april-2026-expired-listings-centennial.md`). Drafted 2026-04-15 in the nightly task but the session was interrupted before the calendar update, cluster-map update, and GitHub push ran. File is complete and schema-valid — recovering the bookkeeping in this push. Expired Listings pillar + Centennial geographic pillar. MOFU market update. DMAR March 2026 data (30.69% MoM pending growth, 16 median DIM, 99.13% CP/LP, $590K metro median), REcolorado Q1 2026 Centennial expired cohort (39 expired + 5 withdrawn, median original list $850K, 119 avg days before expiration), Centennial closed comps ($689K median, 13 median DOM, 94% CP/OLP avg).
- Day 13 new draft: "How Much Equity Do You Need to Move Up in Highlands Ranch?" (`src/content/blog/equity-to-move-up-highlands-ranch.md`). Move-Up Sellers pillar + Highlands Ranch geographic pillar. MOFU. REcolorado Q1 2026 Highlands Ranch closed data (198 sales, $742,500 median close, $873,461 avg, 16 median DIM, 98% CP/OLP), DMAR March 2026 rate/pending/CP-LP context. Payment comparison table ($325K @ 4% → $880K @ 6.25% = ~$3,870/mo increase), three payment-shrinking levers (more down, rate buydown, right-size target), sell-first vs. buy-first decision framework.
- Updated content-calendar-2026.md — marked Days 12 and 13 as drafted.
- Updated content-cluster-map.md — added Day 12 to Expired Listings cluster and Day 13 to Move-Up Sellers cluster.
- Ride-along with next production deploy — no standalone push needed.

