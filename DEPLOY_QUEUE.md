# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

## 2026-04-17 — Homepage PageSpeed fixes

- **LCP fix:** Added `.hero::before` rule to the critical inlined CSS in `BaseLayout.astro`. Previously `.hero::before` (which renders the hero background image via `var(--hero-bg)`) only existed in the deferred `/css/styles.css`. This caused a late layout recalc when the deferred stylesheet loaded, pushing out the subtitle's LCP timestamp to ~2,460ms element render delay per PSI. With the rule in critical CSS, the hero image positioning element exists at first paint and the subtitle's LCP fires at the correct moment.
- **Forced-reflow fix:** Rewrote the GA4 init script in `SEO.astro` to defer initialization until first user interaction (scroll/click/keydown/mousemove/touchstart) or idle/3s timeout. Previously the inline `gtag('config', ...)` call fired during initial HTML parse, triggering 64ms of forced reflow on selling303.com line 154 (plus GTM's own internal reflows). Pageviews still register — only very short zero-interaction bounces under 3s are missed. Preconnect to googletagmanager.com kept for fast TLS handshake when GA does fire.
- Only affects the homepage hero (only page using `.hero` + `--hero-bg`). Other pages use `.page-hero`, unaffected.

## 2026-04-17 — Day 13 HR equity post voice edits (Jacob review)

- Payment section: removed direct Freddie Mac PMMS "check the rate" call-to-action; replaced with recommendation to talk to a trusted local lender for a specific pre-approval/payment scenario, and noted Jacob can make an introduction.
- Timing section closer: stopped directing readers to DMAR and CAR as research they should do themselves. Reframed as "reach out to Jacob for a move-up conversation — he pulls from these sources to build the local read." Links retained as source attribution only.
- Illustrative-calculations footnote: swapped "check the Freddie Mac PMMS" for "a trusted local lender should run the specific scenario for your situation."
- Voice pattern captured for future reviewer-skill corpus: *direct-to-consumer source references and generic authority-site recommendations instead of lender/agent recommendations.*

## 2026-04-17 — Seller Success Stories migration (Framer → Astro)

- **8 full success story content files** created with SCAR narratives, 5 FAQs each, testimonials, structured data: Golden, Centennial (Birch St), Centennial (Phillips Dr), Littleton (Carr Ct), Littleton (Holland Way x2), Littleton (Flower St), Parker (Woodside Ln), Aurora (Jericho Ct)
- **6 listing-only placeholder content files** for stories pending client interviews: Arvada (Flora Ct), Aurora (Union Circle), Denver (Wagon Trail), Littleton (Coal Mine), Englewood (Lehow), Highlands Ranch (Ravenswood)
- **[slug].astro template**: Added auto-image-discovery via `import.meta.glob` — stories auto-find all images in their folder. Only Golden uses manual frontmatter image list (46 custom alt texts). Made sqft display conditional.
- **content.config.ts**: Made `sqft` optional in successStories schema
- **Index page rewrite**: Hidden breadcrumbs (sr-only for SEO), 3 featured stories above credibility tiles, 6-stat credibility tiles matching about page, "Browse All Stories" heading + filter + full grid below
- **Hero image paths wired** for all 9 stories with photos to match actual filenames in each folder
