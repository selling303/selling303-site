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

