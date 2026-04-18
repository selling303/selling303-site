# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

## 2026-04-17 — Day 14 blog post (Littleton first-time buyer bidding)

- **New blog post:** "What First-Time Buyers Should Know About Bidding in Littleton's Spring Market" (`src/content/blog/first-time-buyer-bidding-littleton-spring-2026.md`). Day 14 of content calendar. First-Time Homebuyers pillar + Littleton geographic pillar. MOFU buyer advice on offer strategy.
- **Data sourcing:** Littleton Q1 2026 REcolorado MLS (433 closed SFRs, $720K median close, 98% median CP/OLP, 23 median DIM) + DMAR March 2026 (99.13% CP/LP metro, 16 median DIM, pending +30.69% MoM, 63.14% concessions). Entry-level pattern documented for sub-$600K bracket — multiple closings at 100–107% of OLP in 1–10 DIM.
- **Structure:** Snippet answer + Key Takeaways + TOC + 7 H2 sections (all phrased as questions) + FAQ + CTA + data attribution.
- **Visual produced inline:** "First-Time Buyer's Offer Toolkit" — stacked three-card tiered visual (escalation clause / appraisal gap / inspection flexibility) using brand colors (#002a3a / #4a7c59 / #9e6b3a brick/olive accent palette), inline styles, text in DOM, source attribution beneath.
- **External authority links:** DMAR Market Trends.
- **Pillar links within first 200 words:** `/first-time-homebuyers` and `/neighborhoods/littleton` in the intro.
- Marked Day 14 `[x] (drafted 2026-04-17)` in content-calendar-2026.md.
- Added post to First-Time Homebuyers cluster in content-cluster-map.md.

### 2026-04-18 Jacob-review revisions (round 2 includes close-to-list dual scenario)
- **New second visual — "How to Read the Spring 2026 Littleton Numbers":** replaced the citywide-stats bullet list with a three-panel educational block that translates median, average, and close-to-original-list ratio into plain-English meaning. Panel 1 shows median as the middle value in a sorted row of Littleton home prices (bar heights scale with price, middle bar highlighted as MEDIAN). Panel 2 shows average skewed up by a luxury outlier (brick-colored $4.25M bar pulling the mean above the median, labeled OUTLIER). Panel 3 shows CP/OLP ratio in TWO paired scenarios — Scenario A (citywide median, 98% CP/OLP, dark brand bar shorter than list bar) and Scenario B (competitive entry-level bracket, 104% CP/OLP, brand-green bar extending past list bar). Both list bars rendered at the same fixed reference width so the visual communicates ratio, not absolute dollar size. Brand colors only, inline styles, text in DOM, source attribution line. Final layout revisions: values moved into their own dedicated column (110px) at the end of each row, empty gray "track" removed (was visually meaningless), bar reference widths tuned to 90% so bars end close to their value labels without dead space.
- **Inspection flexibility section rewrite:** removed the "informational-only inspection" bullet entirely. Added an explicit opening paragraph stating Jacob will never recommend skipping the inspection itself — a full professional inspection is non-negotiable, and the flexibility is only in how the buyer uses the findings. Kept "shorten the deadline" and "limit objection scope to material defects" bullets. Folded the concrete dollar-threshold option (no objection items under $1K / $2K / $5K) into the same bullet as scope-limiting, framed as a level-further extension of the same tactic (not a replacement) per Jacob's review note.
- **CAR Legal Hotline link removed:** the hotline is a Realtor-only resource, not a consumer resource. Sentence tightened to attribute the guidance to Jacob's coaching rather than an external link that would mislead readers.
- `dateModified: "April 18, 2026"` updated.

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
