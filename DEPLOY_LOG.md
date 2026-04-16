# Deploy Log

Permanent record of deployed changes. The deploy-to-netlify skill moves items here from `DEPLOY_QUEUE.md` after each successful deploy.

---

## 2026-04-15 — commit 47824c8 | Credits used: 15 | Credits remaining: 200

### Performance
- Inlined critical above-the-fold CSS (8.6 KB minified) in BaseLayout.astro `<head>` — eliminates render-blocking stylesheet for first paint
- Deferred full stylesheet load via `media="print" onload="this.media='all'"` pattern with `<noscript>` fallback — full CSS at `/css/styles.css`
- Removed Astro CSS import from BaseLayout.astro (was creating a render-blocking `<link>` tag)
- Copied full styles.css to `public/css/styles.css` for deferred loading
- Fixed `.hero::before` background to use `var(--hero-bg)` CSS variable instead of hardcoded relative path — works with Astro's `getImage()` pipeline
- Removed RealScout preconnect from SEO.astro (widget is lazy-loaded, preconnect was wasted)
- Added `/css/*` cache header (24hr with revalidation)

### Success Stories System (new)
- New content collection schema + [slug].astro template (SCAR framework) + index page with filter cards
- First story: 14556 W 3rd Ave Golden (Buy Before You Sell, $55K over list) — 46 listing photos with descriptive alt text, hero lightbox gallery with photo count badge + keyboard/swipe nav, sticky sidebar, mid-page strategy CTA
- 6 JSON-LD schemas per page: RealEstateListing, Review, Article, ImageObject, BreadcrumbList, FAQPage
- FAQ uses site-wide accordion pattern (one-at-a-time toggle)
- Success Stories added to Sell dropdown in Header.astro
- PhotoGallery.astro reusable component created (available for other pages)
- Made sqft optional in successStories schema + conditional display in template
- 8 new SCAR-framework stories (FAQs + Schema.org metadata): 7307 S Birch St Centennial (Buy & Sell Simultaneously, $82K over, 4 DOM); 8965 E Phillips Dr Centennial (Relocation, $25K over, 1 DOM, pre-market); 7327 S Carr Ct Littleton (As-Is / Lifestyle, Stony Creek, 9 DOM); 6718 S Holland Way Littleton (Quick Sale, Dutch Ridge, $5K over, 4 DOM); 6720 S Holland Way Littleton (Move-Up, Dutch Ridge, multiple offers, 5 DOM); 6566 S Flower St Littleton (Pre-Sale Reno, Woodmar Village, concierge, 9 DOM); 21069 Woodside Lane Parker (Tough Market, holiday, $10K over, 10 DOM); 2993 S Jericho Ct Aurora (Life Transition, Conservatory Park, $31K over, 4 DOM)
- 6 listing-only placeholder stories (property + FAQs, story TBD via interview): 8781 Flora Ct Arvada ($919,900); 22461 E Union Circle Aurora ($689,000); 4360 W Wagon Trail Dr Denver ($625,000); 9559 W Coal Mine Ave Unit A Littleton ($385,000); 301 W Lehow Ave #14B Englewood ($300,000); 10315 Ravenswood Lane Highlands Ranch ($600,000)
- HOTFIX: Added missing closing `---` frontmatter delimiter to 3 placeholder stories (22461-e-union-circle-aurora, 4360-w-wagon-trail-dr-denver, 8781-flora-ct-arvada) — missing delimiter caused Astro content collection schema validation to fail
- NOTE: All 14 new stories need listing photos added to src/assets/images/success-stories/
- NOTE: 6 listing-only stories need real results data + client stories via interview skill

### SEO meta optimization
- Updated titles and descriptions on all 6 specialization pages: added "Colorado" to titles, neighborhood names to descriptions for long-tail query matching
- Updated descriptions on all 9 neighborhood pages: enriched with specialization keywords (buying, selling, relocating, relisting, new construction) and unique neighborhood character

### New blog post: Day 11
- "Selling Your First Home in South Denver: What No One Tells You About the Process" (`src/content/blog/selling-first-home-south-denver-process.md`). First-Time Home Sellers pillar + Centennial geographic pillar. MOFU. DMAR March 2026 data (63.14% concessions, $590K metro median, 16 DOM), REcolorado Q1 2026 Centennial closed data (269 sales, $689K median, 13 median DOM, 94% close-to-original-list).
- Net Sheet cost-breakdown visual: horizontal stacked bar on $689K Centennial sale — Seller Net (~91%, brand green), Agent Commissions, Concessions, Title+Closing, Pre-Listing Prep, plus Prorated Taxes as variable. Legend grid with $ ranges + %. Each legend item wrapped in Schema.org `PropertyValue` microdata (itemprop name, minValue, maxValue, unitCode=USD) for AEO structured-data signals — same pattern as MarketStatTile component.
- Selling Timeline: added encouragement for sellers facing tighter timelines (relocation, job change, family timing, personal deadline) to reach out for a compressed-timeline discussion before committing to a plan. Inline CTA links to calendly.

### Updates to existing blog post
- `why-house-not-selling-denver.md` Reason #7 (Market Timing): replaced bullet list of Feb 2026 DMAR stats with 4-card horizontal stat strip (Active Listings, Median DOM, Median Sale Price, Under Contract). Directional YoY trend pills (brick for down, green for up), brand-aligned colors, same shadow system as overpricing diagnostic. Added interpretive paragraph covering buyer behavior shift and selective demand.

### Git hygiene
- NOTE: Force-pushed `live` to match `main` to resolve divergence left over from the April 14 netlify.toml-bug recovery chain. Three commits were dropped from live's history (no content loss — all changes already on main): `ffb959c` (deploy-trigger comment in DEPLOY_QUEUE.md), `56cc089` (netlify.toml plugins-block fix — identical version already on main), `683c68` (merge commit). See April 14 entry for context on the original chain. Live and main are now fully synchronized; future deploys should fast-forward cleanly.

---

## 2026-04-14 — commit 683c688 | Credits used: 30 | Credits remaining: 215

- Added GA4 `page_not_found` custom event to 404.astro (tracks broken URL path, referrer, and full URL)
- Updated CLAUDE.md deploy protocol to reference GitHub API instead of git commands
- Hardened github-api-push.sh: added JSON escaping for commit messages and file paths
- Self-hosted Google Fonts (Inter + DM Serif Display): eliminated render-blocking @import chain, added @font-face declarations with font-display:swap, preloads in head
- Lazy-load RealScout widget (205 KiB) via IntersectionObserver — removed from critical render path on all 4 pages
- Updated CSP headers: font-src now 'self' only, added /fonts/* immutable cache rule (1yr)
- Added 301 redirects for all 27 GSC 404s: old Framer listing pages → /properties, old blog slugs → closest Astro posts, old static pages → Astro equivalents, old neighborhood paths → /neighborhoods/[slug]
- Fixed trailing slash redirects: set trailingSlash:'never' in Astro config, disabled Netlify Pretty URLs. Resolves 12 "Page with redirect" issues in GSC
- New blog post: "Best Parks and Trails Near Littleton and Highlands Ranch" (`src/content/blog/best-parks-trails-littleton-highlands-ranch.md`). Day 19 of content calendar. Best Of / Neighborhoods. TOFU lifestyle. Inline branded SVG map. Web-verified stats from HRCA, CPW, SSPRD, High Line Canal Conservancy.
- New SVG asset: `src/assets/images/littleton-highlands-ranch-parks-trails-map.svg`
- HOTFIX: Converted inline SVG in parks blog post from `<style>`/class-based to inline styles — `<style>` tag inside SVG `<defs>` caused Astro content collection to silently skip the page (404 on production). Same fix applied to standalone SVG asset
- Updated `why-house-not-selling-denver.md`: added overpricing diagnostic framework (showing-activity-to-price tiers, brand-aligned color palette, NAR Confidence Index link) as new H3 subsection within Reason #1
- Fixed `netlify.toml`: removed empty `[[plugins]]` block that was causing all builds to fail at config parsing stage
- Created Netlify build hook `deploy-selling303-live` for programmatic production deploys
- NOTE: Previous deploy attempts (commits e5445c2, b585c85, ffb959c) all failed due to the netlify.toml bug. The Apr 13 deploy (12ab884) was the last successful production deploy before this one. Two successful deploys in this batch: 56cc089 (toml fix) + 683c688 (full merge) = 30 credits

## 2026-04-13 — commit 12ab884 | Credits used: 15 | Credits remaining: 245

- New blog post: "Do You Need a Real Estate Agent for New Construction in Colorado?" (`src/content/blog/real-estate-agent-new-construction-colorado.md`). Day 9 of content calendar. New Construction pillar + Highlands Ranch geographic pillar. MOFU.
- New blog post: "Littleton vs. Centennial: Which South Denver Suburb Fits Your Relocation?" (`src/content/blog/littleton-vs-centennial-south-denver-relocation.md`). Day 10 of content calendar. Relocation pillar + Littleton geographic pillar. TOFU. Q1 2026 REcolorado MLS data (Littleton 433 closed/$700K median, Centennial 269 closed/$690K median), DMAR March 2026 report.
- Updated content-calendar-2026.md — marked Days 9 and 10 as drafted.
- Updated content-cluster-map.md — added posts to New Construction and Relocation clusters.

## 2026-04-11 — commit afb29ea | Credits used: 15 | Credits remaining: 260

- New blog post: "Selling in Centennial and Buying in Highlands Ranch: How to Coordinate Two Transactions" (`src/content/blog/selling-centennial-buying-highlands-ranch-coordinate-transactions.md`). Day 8 of content calendar. Move-Up Sellers pillar + Centennial geographic pillar. BOFU. DMAR Feb 2026 data (Centennial $699K median / 48 DOM, HR $718.5K / 52 DOM), inline SVG timeline graphic, comparison table, three bridge strategies, equity math framework.
- Updated content-calendar-2026.md — marked Day 8 as drafted.
- Updated content-cluster-map.md — added post to Move-Up Sellers cluster.

## 2026-04-10 — commit 48b3fcc | Credits used: 15 | Credits remaining: 275

- New blog post: "How to Relist and Sell a Home in Littleton After an Expired Listing" (`src/content/blog/relist-home-littleton-after-expired-listing.md`). Day 7 of content calendar. Expired Listings pillar + Littleton geographic pillar. 93 expired + 18 withdrawn Q1 2026 data from REcolorado, DMAR Feb 2026 stats, step-by-step relist checklist, Seller Promise links.
- New page: My Seller Promise (`src/pages/my-seller-promise.astro`) — Apple-style scroll experience with hero, promise section, three-phase horizontal image carousels, ClientClarity demo button + ClearPrice cards, FAQ accordion with Schema.org markup, trust bar, areas served, CTAs to Calendly. 12 images in `src/assets/images/seller-promise/`.
- Updated Header nav — added "My Seller Promise" as first item in Sell dropdown.
- Updated water restrictions blog post with Denver Water drought surcharges (Tier 2/3 pricing, effective May 2026).
- Fixed clientclarity-demo page — replaced `<head slot="head">` with `<Fragment slot="head">` (fixed footer rendering at top) and added header-height padding to hero.
- Updated content-calendar-2026.md — marked Day 6 HR relocation as published, Day 7 Littleton relist as drafted.
- Updated content-cluster-map.md — added HR expired listing, HR relocation guide, Castle Pines new construction, and Littleton relist to respective clusters.
- Updated CLAUDE.md — added explicit live-branch approval rule.
- Fixed branch divergence — cherry-picked 3 live-only commits onto main, reset live to match.

## 2026-04-08 — commit 5e3b0bf | Credits remaining: 290

- Infrastructure: switched to two-branch deploy system (main/live)
- Netlify production branch changed from `main` to `live`
- Created build hook `deploy-selling303` (stored as NETLIFY_BUILD_HOOK env var)
- CLAUDE.md: rewritten deploy protocol for main/live architecture
- YAML quoting fixes across 5 blog posts (& character safety)
- Added missing cardStat/cardStatLabel to 2 older posts
- Added Neighborhoods filter button to blog index
- Deploy skill v4: two-branch push/deploy workflow

## 2026-04-08 — commit 57d5a78 | Credits remaining: 320

- HOTFIX: Added missing blog card CSS to styles.css (gradient backgrounds, card headers, hover reveal animations). Cards were rendering blank after previous deploy omitted the stylesheet additions.

## 2026-04-08 — commit a3a34f5 | Credits remaining: 335

- Blog tile redesign: category gradient headers, SVG icons, cardStat/cardStatLabel hover reveal
- Zod schema: cardStat, cardStatLabel fields; cardImage and relatedPosts image now optional
- 12 blog posts: added cardStat + cardStatLabel frontmatter
- SEO: removed FUB widget tracker and widgetbe.com preconnect
- Properties: full RealScout listing-status values
- CLAUDE.md: comprehensive deploy protocol + commit-before-closing rule

## 2026-04-08 — commit 4620b03 | Credits remaining: 350

- New blog post: "New Construction Communities in Castle Pines and Parker: What Buyers Need to Know in 2026" (`src/content/blog/new-construction-castle-pines-parker-2026.md`). Day 5 of content calendar. New Construction pillar + Castle Pines geographic pillar.
