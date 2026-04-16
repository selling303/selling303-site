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

