# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- 2026-04-14: Inlined critical above-the-fold CSS (8.6 KB minified) in BaseLayout.astro `<head>` — eliminates render-blocking stylesheet for first paint
- 2026-04-14: Deferred full stylesheet load via `media="print" onload="this.media='all'"` pattern with `<noscript>` fallback — full CSS at `/css/styles.css`
- 2026-04-14: Removed Astro CSS import from BaseLayout.astro (was creating a render-blocking `<link>` tag)
- 2026-04-14: Copied full styles.css to `public/css/styles.css` for deferred loading
- 2026-04-14: Fixed `.hero::before` background to use `var(--hero-bg)` CSS variable instead of hardcoded relative path — works with Astro's `getImage()` pipeline
- 2026-04-14: Removed RealScout preconnect from SEO.astro (widget is lazy-loaded, preconnect was wasted)
- 2026-04-14: Added `/css/*` cache header (24hr with revalidation)
- 2026-04-14: New success stories system — content collection schema, [slug].astro template (SCAR framework), index page with filter cards
- 2026-04-14: First success story: 14556 W 3rd Ave Golden (Buy Before You Sell, $55K over list)
- 2026-04-14: 46 listing photos with descriptive alt text in src/assets/images/success-stories/
- 2026-04-14: Hero image → clickable lightbox gallery with photo count badge, keyboard/swipe nav
- 2026-04-14: Sticky sidebar (property details + CTA float together), mid-page strategy CTA
- 2026-04-14: 6 JSON-LD schemas per page: RealEstateListing, Review, Article, ImageObject, BreadcrumbList, FAQPage
- 2026-04-14: FAQ uses site-wide accordion pattern (button/answer toggle, one-at-a-time)
- 2026-04-14: Success Stories added to Sell dropdown in Header.astro
- 2026-04-14: PhotoGallery.astro reusable component created (available for other pages)
- 2026-04-14: Made sqft optional in successStories schema + conditional display in template
- 2026-04-14: 8 new success story content files (SCAR framework, FAQs, Schema.org metadata):
  - 7307 S Birch St, Centennial — Buy and Sell Simultaneously ($82K over, 4 DOM)
  - 8965 E Phillips Dr, Centennial — Relocating Out of State ($25K over, 1 DOM, pre-market)
  - 7327 S Carr Ct, Littleton — As-Is / Lifestyle Change (Stony Creek, 9 DOM)
  - 6718 S Holland Way, Littleton — Quick Sale (Dutch Ridge, $5K over, 4 DOM)
  - 6720 S Holland Way, Littleton — Move-Up Seller (Dutch Ridge, multiple offers, 5 DOM)
  - 6566 S Flower St, Littleton — Pre-Sale Renovation (Woodmar Village, concierge program, 9 DOM)
  - 21069 Woodside Lane, Parker — Selling in a Tough Market (holiday season, $10K over, 10 DOM)
  - 2993 S Jericho Ct, Aurora — Life Transition (Conservatory Park, $31K over, 4 DOM)
- 2026-04-14: NOTE: All 8 new stories need listing photos added to src/assets/images/success-stories/
