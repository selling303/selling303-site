# Deploy Log

## 2026-05-17 — commit 41c237a / merge 5d3c8cb | Credits used: 15 | Build: triggered via hook 69de8373

### New blog posts (7 — May 10 → May 17 backlog bundled with tonight's nightly draft)

- **Day 13 May calendar — "Right-Size Inside Highlands Ranch: 3 New-Build Paths (2026)"** (`highlands-ranch-new-construction-empty-nester-right-size-2026.md`). New Construction × Highlands Ranch. MOFU. Tier 0 **profile-card-grid** (library, `.aeo-persona-grid` reuse from greenwood-village-empty-nester). 3 right-sizing format cards (single-level patio home $700K–$925K / paired villa $625K–$800K / low-maintenance townhome $465K–$650K) × format-band + sqft-band + community concentration + best-for tagline. Per-card Place Microdata + containedInPlace Douglas County + machine-readable price values; ItemList JSON-LD with 3 itemListElement entries; bound source row inside figure wrapper with strict-new-vs-near-new disclosure. Compelling Question Flow chose profile-card-grid (24) over two-path-diptych (22) and stretch sqft-shrink-comparison (20); overrode calendar `howto (flag-only)` advisory per writer-delegation contract. Anchored to REcolorado MLS April 2026 HR (n=131 closed, $725K median close, 99% CP/OLP, 12-day median DIM; 414 active+pending+coming-soon as of 5/3). blog-review: 1 readability HARD FAIL on initial run (Flesch 40.3, FK 12.6) → targeted sentence-splits applied, final 4/5 PASS with 1 SOFT FAIL on Flesch (46.7 vs target 55) — within shippable band per real-estate vocabulary syllable load. Also auto-fixed description (167→142 chars) and snippet (316→250 chars). Dimension 10 hit on "dozens of dual-transaction right-sizings" rephrased to "works with HR empty-nesters regularly" — removed unverified volume claim. Title shortened from 97→59 chars for SERP CTR; original preserved in `headline`. Companion piece to `greenwood-village-empty-nester-right-sizing-math-2026.md` (same life stage, different price tier, different replacement geography).

- **Day 12 May calendar — "Lone Tree Relocation for DTC Tech Professionals (2026)"** (`lone-tree-relocation-guide-dtc-tech-professionals-2026.md`). Relocation × Lone Tree. TOFU. Tier 0 **price-ladder-svg** — **first live shipment of the pattern** (lift-from updated in `docs/visual-patterns.md` from git commit `1dd3d0a` to this post). 4-tier Lone Tree price ladder tuned for relocating DTC tech professionals — Tier 1 $325K–$500K Park Meadows condos / Tier 2 $500K–$750K South Lone Tree townhomes & small detached / Tier 3 $750K–$1.2M RidgeGate move-up SFR / Tier 4 $1.2M+ RidgeGate / Heritage Hills luxury. Bar widths scale to median fin sqft (115→180→290→420px), colors graduate light-to-dark per spec, tier chips carry gold accent. Inline SVG viewBox 800×470, source `<text>` baked in + bound `<figcaption>` outside SVG. Outer `<figure itemscope itemtype="Dataset">` + parallel JSON-LD Dataset with spatialCoverage Lone Tree containedInPlace Douglas County, variableMeasured × 5, isBasedOn REcolorado MLS Lone Tree April 2026. Anchored to 74 active + 20 April closings (median close $760K, 98% CP/OLP, 12-day median DIM). Title shortened 96→54 chars for SERP CTR; original preserved in `headline`. Compelling Question Flow tied 24 vs 24 (profile-card-grid); tiebreaker on canonical fit + pattern freshness + library-first-live promotion value. Overrode calendar's `Visual: none` advisory.

- **Day 11 May calendar (FULL REWRITE 2026-05-17 after Jacob review) — "What a $650K Littleton Sale Actually Nets You (2026)"** (`littleton-first-time-seller-net-sheet-3-county-2026.md`). First-Time Home Sellers × Littleton. MOFU. Jacob's feedback on the original 2026-05-15 ship (comparison-table, 3-county column comparison): "It makes a really big deal out of the 3 counties, but there's no real insight that comes from it. That point needs a section at most, maybe even just a paragraph, but certainly not a whole blog post." Rewrite per Jacob's Option 2 choice: Tier 0 **settlement-statement** visual (library, lifted from lakewood-to-highlands-ranch styling), single-step sell-side variant at $650K median — navy header strip, 4 categorical sections (Sale Side / Brokerage / Title and Closing / Government and Tax), per-line PropertyValue Microdata, green-accent total row ($40,795 / 6.3%), navy-bg gold-accent punchline ($609,205 cash on table before mortgage payoff). Body restructured: net sheet visual → "which lines actually move the needle" (commission is 87% of typical cost) → "when do HOAs or the 3-county question change the math" (3-county content now one section) → "how do buyer concessions change the net" (the line first-time sellers miss; 2% concession = $13,000) → "what does a Littleton seller actually walk away with" (mortgage-payoff scenarios). FAQ rewritten to match new spine. Slug retained for URL stability on `main`. Em-dash discipline applied. Dimension 10 integrity: no fabricated client-mix percentages or "since 2023" personal-data-collection claims; only verified $46M+ trust signal. Anchored to REcolorado MLS April 2026 Littleton (n=292 closed, $650K median, 16-day DIM, 98% CP/OLP).

- **Day 10 May calendar — "Englewood to Centennial Move-Up: 2026 Trade Math"** (`englewood-to-centennial-move-up-trade-off-2026.md`). Move-Up Sellers × Englewood. MOFU. Tier 0 **two-path-diptych** (library). Sell-side Englewood ($599,950 median close, 1,603 fin sqft, $385 PSF Fin, 12-day DIM, 98% CP/OLP, n=68) vs. buy-side Centennial ($650,000 median close, 2,310 fin sqft, $288 PSF Fin, 12-day DIM, 98% CP/OLP, n=155). Headline deltas: +$50,050 median price gap (8.3% premium), +707 fin sqft (44% more space), -$97 PSF Fin (25% cheaper per foot). Question-led navy banner + gold answer-pointer. Per-path PropertyValue Microdata + Dataset wrapper + parallel JSON-LD with spatialCoverage × 2. Compelling Question Flow chose diptych (25) over comparison-table (21) and stretch single-metric-bar-chart (19). Three review passes — initial 8-dim blog-review passed with 2 soft watchpoints, then 10-dim re-review surfaced 1 Dim-10 hard fail (unverified subdivision-experience claim, cut per Jacob option-1) + 1 Dim-9 readability soft fail (resolved via targeted sentence-splits). Third pass — em-dash voice cleanup per Jacob's "too many em dashes = AI tell" flag — stripped 36→3 em-dashes, dropped n=X from Key Takeaways. Final readability: all 5 metrics PASS (avg 14.4, p90 28.0, Flesch 51.2 — first time clearing 50 soft ceiling, FK 9.7). Title shortened 80→48 chars for SERP CTR.

- **Day 9 May calendar (FULL REWRITE 2026-05-16) — "Why Lakewood Owners Choose Highlands Ranch Next (2026)"** (`lakewood-to-highlands-ranch-move-up-equity-carrying-cost-2026.md`). Move-Up Sellers × Lakewood. MOFU. Original 2026-05-12 draft was math-led ("Move Up From Lakewood to Highlands Ranch: 2026 Cost Math") with Tier 0 settlement-statement visual; Jacob feedback: "really mechanical and forced." Rewrite inverts the structure: leads with the WHY (commute, family, master-planned lifestyle, weather profile — almost never price), then identifies real "right-now" triggers (job change, caregiving, school-year deadline, ARM reset) vs. lifestyle-only reasons, then market data, then settlement-statement visual unchanged, then carrying-cost section, then sell-first vs. buy-first. Same visual, same data, same Schema.org payload — what changed is the prose frame. FAQ rewritten Q1→why-question. Snippet, heroSubtext, Key Takeaways all rewritten to lead with the why. Fair Housing compliance preserved on school references. Title 54 chars, original preserved in `headline`. Visual carries $39,375 net cash surplus punchline anchored to REcolorado MLS April 2026 Lakewood SFR n=199 @ $580K and HR SFR n=131 @ $737K.

- **Day 8 May calendar (multiple revisions through 2026-05-16) — "Parker New Construction: Buy Off the Shelf or Build It?"** (`spec-home-vs-custom-build-parker-2026.md`). New Construction × Parker. MOFU. **Initial 2026-05-11 ship: comparison-table** (2 paths × 7 cost categories, spec vs. custom anchored in REcolorado MLS Parker n=181 + NAHB Cost of Constructing benchmarks). **2026-05-16 visual rebuild + LIBRARY PROMOTION: trade-off-frontier** — Jacob rejected the comparison-table on review ("one of the worst you've created") and also rejected two-path-diptych as "forcing a square peg into a round hole," then named the axes idea himself (time-to-move-in vs. design-decisions-controlled). New visual is inline SVG viewBox 700×500 with question-led navy hero ("Pick your corner — you can't have both"), gold answer-pointer subhead, navy Spec zone lower-left ($850K–$925K, 30–90 days, Few decisions), green Custom zone upper-right ($1.1M–$1.4M+, 12–18 months, Hundreds of decisions), dashed gray "DOESN'T EXIST" annotation in empty upper-left quadrant. **Library Promotion executed** — `trade-off-frontier` added as new pattern #1 in `docs/visual-patterns.md`; renumbered other 8 patterns; updated section header to "The Nine Patterns"; added cheat-sheet row. **2026-05-16 visual refinement round 2 after Jacob screenshot review:** removed dashed gold "frontier" curve + label (economic-frontier metaphor wrong because only 2 points are real, not a continuum), lightened DOESN'T EXIST box to ghost-placeholder weight, added quadrant labels (FAST + SIMPLE / SLOW + CUSTOM), removed "stalled spec inventory" annotation (third concept on 2-concept plot), added time-range whiskers (1–3 mo / 12–18 mo on x-axis), shortened SVG-baked source line. **2026-05-16 data-accuracy + integrity pass:** corrected closed-only-vs-all-flow conflation ($274→$275 PSF Fin median, 16-day→11-day median DIM, $345→$323 PSF Above-grade median, $223→$222 PSF Total median); removed 2 fabricated trust claims about Jacob personally collecting custom-build cost data since 2023; replaced fabricated 75/25 spec-vs-custom client-mix split with honest qualitative framing; defined "spec inventory" and "custom build" in Key Takeaways; rewrote "Spec inventory captures Parker's MLS pricing" bullet to data-asymmetry framing. **2026-05-16 reader-voice copy refresh:** title rewrite to "Parker New Construction: Buy Off the Shelf or Build It?" (55 chars, question framing, drops "spec build" insider vocab); heroSubtext + snippet + meta description rewritten to lead with reader-language. **2026-05-16 readability gate refresh:** all 5 metrics now PASS (avg 16.3, p90 29.5, Flesch 51.8, FK 10.1).

- **Day 7 May calendar (2026-05-10 ship + 2026-05-16 fabrication cleanup) — "Condo vs. Starter House in Littleton for First-Time Buyers"** (`condo-vs-single-family-littleton-first-time-buyer-2026.md`). First-Time Homebuyers × Littleton. MOFU. Tier 0 **stacked-cost-bar-comparison** (NEW PATTERN — Library Promotion executed 2026-05-10): two vertical bars side-by-side showing monthly all-in carrying cost segmented by P&I / property tax / homeowners insurance / HOA. Condo path ($380K median, $342K loan @ 10% down) = $2,831/mo all-in. Starter SFR path ($601,250 median, $541K loan) = $4,020/mo all-in. Gap = $1,190/mo, lives almost entirely in mortgage P&I segment (HOA delta is only $285/mo on $1,190 total gap — busts the "HOA fees are deciding factor" myth FTBs walk in with). Source REcolorado MLS April 2026 Littleton (condo n=53, starter SFR n=92). **2026-05-16 cleanup pass:** Removed fabricated 55/45 condo-vs-SFR client-mix split from picking-a-path section; replaced with honest qualitative framing (down-payment liquidity, hold horizon, monthly carrying capacity, lifestyle priorities — not a generalizable rule). No data changes; no visual impact.

### SEO + infrastructure fixes

- **GSC "Discovered, not indexed" fix (41 URLs: 16 pillars + 25 blog posts).** Root cause = crawl prioritization, not content quality. (1) **Sitemap lastmod added** — `astro.config.mjs` now passes a `serialize` callback to `@astrojs/sitemap` resolving each URL back to its source file and shelling out to `git log -1 --format=%cI` for per-file last-commit ISO timestamp. Cached per-build, falls back to build ISO if git lookup fails. (2) **Pillar "Related Articles" cards repointed** — neighborhood `[slug].astro` template hardcoded `href="/blog"` on every card (18 dead-end links across 9 neighborhoods). Schema updated to require `relatedPosts[].slug`; template renders `href={` + "`" + `/blog/${post.slug}` + "`" + `}`. All 9 neighborhood `.md` files re-populated with 2 real blog posts each. Also fixed 4 hardcoded `/blog` dead-ends on specialization pillars (expired-listings.astro + new-construction.astro). Net: every flagged blog post now has 1–2 real inbound internal links from a pillar, and every sitemap URL ships with a real `<lastmod>`. **Follow-up after deploy:** resubmit sitemap in GSC + manually Request Indexing on the 16 pillar URLs.

- **RSS feed at `/rss.xml`** (queued 2026-05-13) for Apple News Publisher ingest and general syndication (Feedly, Perplexity discovery). New `src/pages/rss.xml.js` using `@astrojs/rss` reads blog content collection, sorts by date desc, renders full post body via `markdown-it` + `sanitize-html`. Added autodiscovery `<link rel="alternate" type="application/rss+xml">` to `src/layouts/BaseLayout.astro` head. New deps: `@astrojs/rss ^4.0.18`, `markdown-it ^14.1.1`, `sanitize-html ^2.17.4`. First full Netlify build verification on this deploy.

### Tooling + skills

- **blog-review Dimension 10 cohort** (2026-05-16): new cohort at `~/Documents/Claude/brain/skills-source/2026-05-16-blog-review-personal-claim-integrity-cohort/` adds Dimension 10 (Personal-Authority Claim Integrity) to blog-review. Catches invented client-mix percentages, fabricated personal-data-collection claims, unverified experience claims, and volume claims beyond verified trust signals ($46M+ sold, 100.6% CP/OLP). Hard-fail with grep patterns; auto-fix path = none (always surface to Jacob). Also tightens Dimension 7 with explicit closed-only-vs-all-flow rule to prevent the conflation that surfaced on the Day 8 Parker post. **Pending action for Jacob:** paste `01-blog-review.md` body into `https://claude.ai/customize/skills` to deploy.

### Visual library momentum

- **trade-off-frontier promoted to library** (pattern #1, Day 8 Parker post 2026-05-16). Library now at **nine patterns** — trade-off-frontier / comparison-table / two-path-diptych / profile-card-grid / price-ladder-svg / single-metric-bar-chart / decision-path / stacked-cost-bar-comparison / settlement-statement.
- **price-ladder-svg first live shipment** (Day 12 Lone Tree post 2026-05-15). Pattern was in the library since the May 2026 cohort but had never shipped on a real post — lift-from updated from git commit `1dd3d0a` to the Lone Tree post.
- **profile-card-grid pattern freshness watch** — shipped 3× in 9 days (GV empty-nester 5/8, Moving to Littleton 5/9, HR right-sizing 5/16). Strong narrative fit dominated tiebreakers despite freshness concern. Worth a writer-skill calibration note: 3–8 self-select cards shape is winning more often than initial Compelling Question Flow scoring predicts.
- **settlement-statement** shipped twice in this batch (Day 9 Lakewood→HR original + Day 11 Littleton rewrite) — both at single-step sell-side or move-up-net variants. Pattern handles both shapes cleanly.
- **Em-dash discipline applied** across multiple posts after Jacob's flag ("too many em dashes = AI tell"). Day 10 post documented full strip (36→3 em-dashes, n=X removed from Key Takeaways); pattern now standard for all new drafts.

### SEO-AEO weekly + sprint context (queued items rolling forward — not this deploy's responsibility)

- 2026-05-11 SEO-AEO Week 4 audit ran with fresh pull_all data (first clean weekly run). Total 29.26 / 100 (Δ -5.39 vs Wk3 monthly). Real signals: UTM bleed 89% → 53%, surname-collision dropping, CTR check shows 19/21 ranking pages leaking. Details in `~/Documents/Claude/Projects/aeo-seo-expert/DEPLOY_QUEUE.md`.
- 2026-05-11 SEO-AEO Sprint #1: PSI fix on `/blog/why-house-not-selling-denver` — mobile perf 0.41 (LCP 4744ms). Single-blog regression. Profile + ship next week.
- 2026-05-11 SEO-AEO Sprint #2: TITLE-LEN top-5 rewrites. 19 of 21 ranking pages leak CTR. Claude drafts 3 candidates per blog; Jacob picks one each.
- 2026-05-11 SEO-AEO Sprint #3: PILLAR-SPEC-MISSING × 3 blogs (7-smartest, best-parks-trails, what-realtor-does). Insert spec-pillar link in first 200 words. Needs Jacob's spec-pillar choice approval per post.
- 2026-05-11 SEO-AEO queued: `git rm sitemap.xml robots.txt` at repo root (pre-Astro artifacts, not served). Sandbox `rm` blocked — next deploy-to-netlify Mode 1 should include explicit `git rm`.
- 2026-05-11 Three test files (`test-write.txt`, `test-overwrite-check.txt`, `test-empty.txt`) sit untracked in repo root from prior session's failed sandbox-rm attempts. `git clean -fd test-*.txt` whenever.

### Build wiring

- **Auto-fire of `gbp-post` for the nightly Day 13 HR post** — fires after this deploy per the standard nightly cadence. Earlier backlog posts (Days 7–12) shipped on prior nights without auto-fire and were left for a manual GBP batch if desired.

---

## 2026-05-09 — commit c194e706 / merge 4c3e823 | Credits used: 15 | Deploy ID: 6a0026ece243800008160194

### New blog posts (4 — backlog bundled with today's nightly draft)

- **Day 6 May calendar — "Englewood Listing Photos: When to Reshoot Before Relisting"** (`englewood-listing-photo-audit-photography-2026.md`). Expired Listings × Englewood. BOFU. Tier 0 **decision-path** visual: 4-question photography audit (hired pro? / 25+ photos? / twilight exteriors? / staged or decluttered?) routing each answer to "Reshoot" / "Photos likely fine" with Decision Rule tally footer ("3+ Reshoot → reshoot before relist") and bound source row inside HowTo wrapper. Compelling Question Flow chose decision-path over comparison-table (Sold vs Expired × 5 metrics) and single-metric-bar-chart (12 vs 76 DIM) because BOFU advice posts pay off harder when the visual gives the reader an actionable audit, not just a data wall — and validates generalization of decision-path beyond comparison-shopping into seller-audit framing. Source: REcolorado MLS Englewood SFR April 1–30, 2026 (n=416: 68 closed at 12-day median DIM, 27 expired at 76-day, 5 withdrawn, 233 active, 78 pending, 5 coming soon). Title shortened from calendar original "The Englewood Photography Audit: Why Visual Presentation Sinks More Listings Than Pricing" for SERP CTR (58 chars); original preserved in `headline` frontmatter. Updates: `content-calendar-2026.md`, `content-cluster-map.md`, `visual-inventory.md`.
- **Day 5 May calendar — "Moving to Littleton, Colorado: A Relocation Guide for 2026"** (`moving-to-littleton-colorado-relocation-guide-2026.md`). Relocation × Littleton. TOFU. Tier 0 **profile-card-grid** visual: 3 Littleton county segments (Arapahoe / Jefferson / Douglas) as self-select cards, each with a custom SVG icon (downtown buildings / foothills triangles / hill-country new build), accent-colored price chip, and navy/green/gold per-card top border. Question-led navy banner ("Which Littleton county actually fits you?") with audience eyebrow + gold answer-pointer, source row visually bound inside the outer figure wrapper. Two visual rebuilds during review: original comparison-table failed Visual Dignity Gate on mobile (5 cells of phrase-shaped prose collapsed columns) → swapped to profile-card-grid → rebuild #2 added question-led banner + bound source row per Visual Hero Rule + Source Placement Rule. Source: REcolorado MLS Littleton mailing-address April 2026 (n=292 closed residential, n=379 active SFR, n=246 active attached, n=48 expired, n=19 withdrawn). Drafted 2026-05-08, rebuilt 2026-05-08 (×2). Cross-skill suggestion logged: `.aeo-persona-grid` CSS doesn't ship a figure-bound source treatment by default; future CSS update would remove inline-override plumbing.
- **Day 4 May calendar — "The Greenwood Village Empty-Nester Right-Sizing Math (2026)"** (`greenwood-village-empty-nester-right-sizing-math-2026.md`). Move-Up Sellers × Greenwood Village. MOFU. Tier 0 **profile-card-grid** visual: 4 empty-nester personas (Network-Anchored / Lock-and-Leave Traveler / Asset-Maximizer / Family-Adjacent), each matched to a best-fit replacement path with price band + redeployable-equity chip. Question-led navy banner ("Which empty-nester are you — and which right-sizing path fits?"), `.aeo-persona-grid` CSS class, custom SVG per card, ItemList JSON-LD + Person/Place Microdata, bound source row. Replaced an earlier two-path-diptych (premise was tautological — redeployable-equity gap by destination too obvious as a binary). Mid-session schema fix: `category: "Selling"` (not in the Zod enum) → `"Costs & Pricing"`. Source: REcolorado MLS GV April 2026 (n=103) + comparative HR (n=157), Centennial (n=155), Parker (n=181). Drafted 2026-05-07, visual rebuilt 2026-05-09.
- **Day 3 May calendar — "Why Pricing Reductions in Highlands Ranch Don't Always Work — and What Does"** (`price-reductions-highlands-ranch-what-works-2026.md`). Expired Listings × Highlands Ranch. BOFU. Tier 0 **single-metric-bar-chart** visual: median DIM by 5 sale-outcome buckets (Sold ≥100% / 3 days, Sold 95–99% / 21 days, Sold 90–94% / 70 days, Sold <90% / 164 days, Expired / 87 days). Full Schema.org Microdata + parallel JSON-LD Dataset + bound source row. Source: REcolorado MLS HR April 2026 (n=150: 131 closed, 22 expired, 4 withdrawn). Drafted 2026-05-06.

### Tooling

- **GBP image generator scripts** in `scripts/`: `generate-gbp-image.py` (Numeric Hero Card — Tier-2 Option 1, reusable for every blog post), `generate-gbp-data-viz.py` (Live Data Snapshot — Tier-2 Option 3, deadline-spine template), `generate-gbp-phone-mockup.py` (Phone Mockup — Tier-2 Option 2, brand-faithful widget render). Python+Pillow, system-font-only, zero external dependencies. Replaces Canva for GBP image generation.

### Visual library momentum

- decision-path now has two shipped use cases (RidgeGate comparison-shopping on 2026-05-06, Englewood seller audit on 2026-05-09) — pattern validated as generalizable across narrative jobs.
- profile-card-grid is the most-shipped Tier 0 pattern this batch (Littleton + GV both rebuilt to it from initial picks) — the 3–8 self-select cards shape is winning more often than initial Compelling Question Flow scoring predicts. Worth a writer-skill calibration note.
- Tier 0 patterns shipped this batch: profile-card-grid (×2), single-metric-bar-chart, decision-path. No comparison-table this batch — first batch in a while without one.

### Build wiring

- Auto-fire of `gbp-post` deferred per Jacob — 4 newly-live posts is heavier than the standard 1-per-day cadence and warrants explicit template + sequence picks.

---

## 2026-05-06 (PM) — commit 4571cc8 / merge 7dfe407 | Credits used: 15 | Build: 39s

- **NEW POST:** South Denver Homeowner's 2026 Notice of Valuation Protest Playbook (`/blog/2026-notice-of-valuation-protest-playbook-south-denver`) — ad-hoc, not from calendar. Move-Up Sellers × Highlands Ranch, BOFU. Time-sensitive (June 1, 2026 protest deadline). Sourced from topic-intelligence.md Section 4 row 1.
- **FIRST TIER-2 INTERACTIVE WIDGET ON THE SITE:** Gap Calculator — county selector + 2 currency inputs + live gap-percentage readout + 3 path cards (Protest / Skip / Abate) that highlight on recommendation + live JS countdown to June 1 deadline. Vanilla JS inline (no framework). Static SSR'd fallback shows all 3 paths fully visible without JS — full Schema.org Dataset + ItemList + 3× RecommendAction + JSON-LD Dataset block. Mobile responsive (<600px stacking). AEO-positive, not compromised.
- **Visual rebuild:** original comparison-table v1 was scrapped at the Visual Dignity Gate (data wall, mostly identical rows across counties). Iterated through 3-option picker (decision-path / timeline / three-paths grid) → 2-widget A/B (Gap Calculator vs Live Cycle Tracker) → final pick = Gap Calculator with Jacob's edits ("Select Your County" label, value="0" on inputs, "Your potential path" header).
- **Library promotion candidate:** flag `interactive-calculator` as new Tier-2 pattern in `docs/visual-patterns.md` on next push (post is the lift-from). Triggers the broader library-tiering conversation Jacob flagged.
- Updated `content-cluster-map.md` (added entry under Move-Up Sellers) and `visual-inventory.md` (Tier-2 entry, Library Promotion flag).
- **Build wiring validated:** gbp-post auto-fires next.

---

## 2026-05-06 — commit 9e57692 | Credits used: 15

- **NEW POST:** RidgeGate vs. Heritage Hills in Lone Tree, 2026 (`/blog/ridgegate-vs-heritage-hills-lone-tree-new-construction-2026`) — Day 2 of May 5–June 3 calendar segment, New Construction × Lone Tree, MOFU, decision-flowchart visual (pattern #6 — Library Promotion). Q1 2026 REcolorado MLS data sourcing.
- **Pre-deploy blog-review fix on the same post:** title shortened 74→47 chars, original preserved via new `headline:` frontmatter for JSON-LD, snippet answer trimmed 546→235 chars. First real-world validation of mandatory blog-review wiring (build Step 1).
- **Visual System Overhaul (docs):** new canonical pattern library at `docs/visual-patterns.md` with 6 shipped patterns + Library Promotion Protocol + brand color spec + cheat sheet. Source of truth for the writer's Compelling Question Flow.
- **Visual Hero Rule + Source Placement Rule** added to `docs/visual-patterns.md` as global principles. Per-pattern hero requirements documented; source attribution must live both inside Schema.org wrapper AND visually bound to the visual block.
- **Lakewood FTHB post hero rebuild** — applied Visual Hero Rule (eyebrow → question-led headline → answer-pointer subhead) and Source Placement Rule (bound footer row inside Schema.org wrapper).
- **decision-path** added as pattern #6 in `docs/visual-patterns.md` (Library Promotion executed from RidgeGate post stretch candidate winner).
- **Visual swap on RidgeGate** — comparison-table → two-path-diptych → decision-path; Variant B picked.
- **Hero correction + A/B variants on RidgeGate** — full hero pattern update for all future visuals.
- Updated `content-calendar-2026.md`, `content-cluster-map.md`, `visual-inventory.md` with the new post and pattern.
- **Build wiring validation (Step 2):** auto-fire of `gbp-post` from `deploy-to-netlify` Mode 2 — RidgeGate post detected as the only new file in `src/content/blog/`, gbp-post invoked once.


Permanent record of deployed changes. The deploy-to-netlify skill moves items here from `DEPLOY_QUEUE.md` after each successful deploy.

---

## 2026-05-05 — commit fe83fa7 (merge into live) | Credits used: 15 | Credits remaining: ~50

### New blog post
- **Day 1 — "First-Time Home Buyer's Guide to Lakewood, Colorado (2026)"** (`first-time-home-buyer-guide-lakewood-colorado-2026.md`). First-Time Homebuyers × Lakewood. TOFU. April 2026 REcolorado MLS data. Visual: comparison-table (4 price tiers). 4 internal cross-links, 3 external authority links.
- Calendar and cluster map updated.

### Success stories migration
- 15 seller success stories migrated from Framer to Astro content collection. ~500 listing photos committed (filenames sanitized — `#` chars stripped for Vite compatibility).
- Index page redesigned: removed featured section + credibility tiles, added slim dark-blue trust ribbon with 5 stats ($46M+, 75+, 99.2%, 5.0★, 15+).
- 3 hero images fixed (Holland Way, Flower St, Woodside Ln — swapped floorplans for exterior photos).
- Carr St story hidden (`draft: true`) — showed $52K below-list outcome.

---

## 2026-05-04 — commit ab9b9ac (merge 515f6d5 on live) | Credits used: 15 | Credits remaining: ~65 | Deploy ID: 69f84481ba0fd50008eaa952

### New blog posts (7 — Days 26 through 31, 8-day backlog bundled)
- **Day 26 — "Is Greenwood Village Worth the Price Tag? A Relocation Buyer's Honest Assessment"** (`greenwood-village-worth-the-price-tag-relocation-2026.md`). Relocation × Greenwood Village. TOFU. Q1 2026 REcolorado MLS data. Visual: persona-card-grid (5 cards with hand-crafted SVG icons, ItemList JSON-LD, Person Microdata per card, Place Microdata for matched suburbs). Two visual iterations during review; Visual A (persona cards) shipped, Visual B (fingerprints) cut. New `.aeo-persona-grid` CSS class added to `public/css/aeo-visuals.css`. Title shortened in review pass to 51 chars; original preserved in `headline`. Snippet trimmed from ~373 → ~245 chars. 3 external authority links. Visual rebuild: replaced numerical comparison-table with 4-city × 6-dimension value trade-off matrix.
- **Day 27 — "The Expired Listing Trap: Why Switching Agents Alone Won't Sell Your Englewood Home"** (`expired-listing-trap-englewood-switching-agents-2026.md`). Expired Listings × Englewood. BOFU. Visual: comparison-table (Closed vs. Expired Englewood single-family Q1 2026 — 138 closed at 14-day median DIM vs. 39 expired at 69-day median DIM). Tier-list opportunity flagged inline as Phase 3 deferral.
- **Day 28 — "How to Time Your Move-Up Sale in Castle Pines Without Ending Up Homeless"** (`move-up-timing-castle-pines-2026.md`). Move-Up Sellers × Castle Pines. BOFU. Visual: **first svg-chart on the site** — single-metric horizontal bar chart of median DOM until sale (Castle Pines 77, Parker 62, HR 52 days; Feb 2026). SVG title + desc + in-SVG term definition + source text + parallel JSON-LD Dataset.
- **Day 29a — "What $500K Gets You in Centennial vs. Highlands Ranch vs. Parker (Spring 2026)"** (`500k-home-centennial-highlands-ranch-parker-2026.md`). First-Time Homebuyers × Centennial. TOFU. Visual: comparison-table (6 columns × 3 cities — Q1 closings, sqft, DMAR Feb 2026 SF median, SF DOM, typical home type). Post-draft `blog-review` pass applied 5 fixes: title shortened to 60 chars (calendar version preserved in `headline`), 2 inline /blog/ cross-links added, snippet trimmed to 245 chars, "has helped" → "has guided", closing rephrased for entity density.
- **Day 29b — "New Construction Buyer Representation in Colorado: What Changed in 2026 and Why It Matters"** (`new-construction-buyer-representation-colorado-2026.md`). New Construction × Parker. MOFU. Visual: comparison-table (5 rows × 3 columns — pre- vs. post-NAR settlement on written-agreement requirement, compensation disclosure, builder pre-registration enforcement, MLS-published offer of compensation, risk of unrepresented first visit). Sourced from NAR settlement practice-change documentation, REcolorado settlement implementation, Colorado Real Estate Commission guidance.
- **Day 30 — "Move-Up Seller Myth: 'I'll Wait Until the Market Gets Better' — Why That's Costing You Money in Lakewood"** (`move-up-seller-myth-waiting-market-better-lakewood-2026.md`). Move-Up Sellers × Lakewood. BOFU. Visual: comparison-table (3 rows × 6 metrics — Lakewood vs. Jefferson County vs. Denver Metro on Feb 2025 vs. Feb 2026 single-family residential). External: Freddie Mac PMMS for rate context.
- **Day 31 — "South Denver April 2026 Closings for Move-Up Sellers"** (`south-denver-april-2026-closings-move-up-sellers.md`). Move-Up Sellers × Highlands Ranch. TOFU. First post using the new monthly Stock/Flow MLS pull workflow — cross-suburb April 2026 closings (1,085), pending pipeline (1,208), active inventory (2,515), 20.6% withdrawn-plus-expired failure rate. HR led with 131 closings at $729,500 median, 8-day DIM, 99% close-to-list. Visual: comparison-table (9 suburbs × 4 metrics) with Schema.org Dataset JSON-LD + per-row Place Microdata + per-cell machine-readable values. Sourced from REcolorado MLS pulls dated May 3, 2026 (IRES dedup) + DMAR March 2026. Post-draft `blog-review` pass applied 4 fixes: title shortened from 84 → 52 chars (original preserved in `headline`), snippet trimmed to ~205 chars, Jacob Stark entity reinforced in 2 middle H2 sections (4 of 5 H2s now name the entity), Freddie Mac PMMS link added (3 external authority links total).

### SEO/AEO foundation
- **Surname-pollution disambiguation** — replaced inline Person/RealEstateAgent/author/publisher schema with `@id` refs to canonical entities (`#agent` on /, /about; new `#organization` added to /, /about) across 15 templates: blog/[slug], success-stories/[slug], 6 specialization pillars, my-seller-promise, 3 tools calculators, neighborhoods/[slug], plus index and about (Organization additions). Fixes Google knowledge-graph collision with other "Stark" public figures driving 78% of last week's GSC impressions.

### Visual upgrades on existing posts
- **`closing-costs-littleton-first-time-buyers-2026.md`** — replaced plain `<table>` with styled settlement-statement visual. Brand navy header strip, category sections (Down Payment, Lender Fees, Title Fees, Prepaid Items with 3 sub-items, Other Costs with 2 sub-items), navy total row ($32,000–$43,900). Inline styles, real text in DOM (AEO-friendly), source attribution baked in.

### Content infrastructure
- **May 5 – June 3, 2026 content calendar** added to `content-calendar-2026.md`. 30 entries (Day 1–30) generated by the new `content-calendar-planner` skill. Cluster mix held at 6/7/4/2/5/6. Geographic rebalance: Lakewood 1→4, Castle Pines 2→4, Lone Tree 1→3, GV 1→3; HR 8→3, Centennial 7→3, Parker 5→3 (HR override flagged inline). Funnel mix 30/40/30 TOFU/MOFU/BOFU. Visual mix biased toward comparison-table (10) + svg-chart (5) + flag-only patterns. Day 18 (May 22) reserved as MDW summer-market kickoff. Day 30 (June 3) reserved for monthly market update.
- **CLAUDE.md "Editing Skills" section rewrite** — documents the new claude.ai/customize/skills source-of-truth rule. Skills are managed exclusively via the web UI; never edit `~/.claude/skills/` (legacy local dir deleted 2026-04-30 after one-time bootstrap to cloud).

### Session notes
- 8-day backlog bundled into one credit charge — kept the workflow clean. Verified post-deploy via Netlify MCP: `currentDeploy.state: ready`, deploy ID `69f84481ba0fd50008eaa952`.
- New monthly Stock/Flow MLS pull workflow established this session: Active/CS/Pending pulled with no date filter (snapshot near 1st of month) + Closed/Withdrawn/Expired date-filtered. IRES cross-listings deduplicated at read time. 9 neighborhoods, ~5,132 listings tracked for April 2026.

---

## 2026-04-26 — commit 7b74623 (merge bd45f43 on live) | Credits used: 15 | Credits remaining: ~80

### Fix — Day 24 blog post (Littleton closing costs)
- **`closing-costs-littleton-first-time-buyers-2026.md`** — geographic accuracy + cost-range refresh after a post-deploy audit caught the issues:
  - **County Quirk section rewritten.** Original copy incorrectly placed Ken Caryl Ranch and Roxborough inside Littleton city limits — both are unincorporated areas (Jefferson and Douglas Counties respectively) with a Littleton mailing address. Reframed the section around the mailing-address-vs-city-limits distinction (ZIPs 80120–80129 cover three counties; incorporated Littleton is overwhelmingly Arapahoe with small extensions into Jeffco and Douglas).
  - **Removed inaccurate tax escrow example.** "A Littleton home in Highlands Ranch Metro District" was wrong — HR addresses are not Littleton. Replaced with an Arapahoe-vs-Ken-Caryl-vs-Roxborough mill-rate comparison that holds up.
  - **Fixed similar conflations** in the price-point section (Ken Caryl Ranch now correctly described as "unincorporated Jefferson County, with a Littleton mailing address") and the HOA section ("Littleton-area inventory" instead of "Littleton inventory").
  - **Cost ranges refreshed** to match current 2026 South Denver Metro reality: appraisal fee $550–$750 → $650–$900; HOA transfer/status letter fee $200–$500 → $250–$700 (also updated FAQ).
  - dateModified bumped to 2026-04-26.
- Verified post-deploy via Netlify MCP: `currentDeploy.state: ready`, deploy ID `69eef7b8e4908c00081cdd22`.

---

## 2026-04-27 — commit 8e273cf (merge 2561921 on live) | Credits used: 15 | Credits remaining: ~95

### New blog posts (2 — Days 23 and 24)
- **Day 23 — "Where South Denver Families Are Moving Up in 2026"** (`src/content/blog/spring-2026-move-up-market-report-south-denver.md`). Move-Up Sellers pillar + Highlands Ranch geographic pillar. TOFU market update. Uses Q1 2026 REcolorado MLS data for HR (n=499, $785K median, 18-day median DIM, 98% sale/list), Parker (n=448, $719K, 44 DIM, 98%), and Castle Pines (n=176, $1.07M, 43 DIM, 96%) plus DMAR March 2026 metro context (pending +30.69% MoM, DIM 16, CP/LP 99.13%). Visual: fully optimized comparison table — real `<table>` with `<caption>`, scoped `<th>`, JSON-LD `Dataset` schema (temporalCoverage, spatialCoverage, variableMeasured, creator, publisher), Schema.org `Place` Microdata per row with `containedInPlace`, per-cell `<meta itemprop="value">` machine-readable values, sample sizes inline (n=499/448/176), spelled-out date range, term definitions in `<figcaption>`. CSS scoped via `.aeo-comp-table` class in the new global stylesheet, fully responsive (table flips to stacked card layout at ≤700px). Title shortened from 80 → 49 chars for SERP CTR; original keyword-rich title preserved in `headline` field for JSON-LD.
- **Day 24 — "Closing Costs Breakdown for First-Time Buyers in Littleton (2026 Update)"** (`src/content/blog/closing-costs-littleton-first-time-buyers-2026.md`). First-Time Homebuyers pillar + Littleton geographic pillar. MOFU buyer advice. Q1 2026 REcolorado Littleton closed data (n=433) + March 2026 DMAR. Uses $475K entry-level price example, walks through 4 cost buckets with inline cost-breakdown visual, addresses Littleton's 3-county quirk (Arapahoe/Jefferson/Douglas), HOA transfer fees, and seller concession strategy.

### AEO Visual Standard Foundation (Phase 1)
- Created global stylesheet at `public/css/aeo-visuals.css` with `.aeo-comp-table` class (lifted from move-up post inline `<style>`) plus placeholder classes for `tier-list`, `process-steps`, `cost-breakdown`, `chart-figure`, `glossary-entry`, `review-card`. Wired into `BaseLayout.astro` via deferred-load pattern (`media="print" onload="this.media='all'"`) for Core Web Vitals.
- Refactored `spring-2026-move-up-market-report-south-denver.md` to drop its inline `<style>` block and rely on the global stylesheet. Visual parity preserved on desktop and mobile.
- Created `visual-inventory.md` with baseline scan of all 33 blog posts (1 optimized, 12 needs-upgrade, 20 review-needed) plus pillar-page placeholders for Phase 2 retroactive audit.
- Updated `content-calendar-2026.md` header to require a `Visual:` line per future entry, mapping to `aeo-visual-builder` pattern types.
- **Skill changes (outside this repo):** Created standalone `~/.claude/skills/aeo-visual-builder/SKILL.md` for visual construction. Updated `~/.claude/skills/blog-post-writer/SKILL.md` Visual Opportunity Check to delegate visual production to the new skill.

### SEO/AEO Foundation Improvements
- **Twitter Cards (`src/components/SEO.astro`):** Added `twitter:card=summary_large_image`, `twitter:site=@selling303`, `twitter:creator=@selling303`, plus title/description/image. Forces large-image preview when selling303.com URLs are shared on X. Score lift: +0.4 (On-page +5).
- **BreadcrumbList JSON-LD on 8 templates:** Added structured breadcrumb schema to `blog/[slug]`, `neighborhoods/[slug]`, and 6 specialization pillars (`expired-listings`, `move-up-sellers`, `first-time-homebuyers`, `first-time-homesellers`, `new-construction`, `relocation`). Used existing `Breadcrumbs.astro` component with new `schemaOnly` prop (default false; preserves visible breadcrumbs on success-stories). Hierarchy: Home → Section → Page. Zero visual impact on the 8 new templates. Score lift: +1.0 (On-page +15 from 0/15).
- **Geo pillar links added to 9 existing blog posts:** `7-smartest-home-upgrades-before-selling-2026` (HR), `closing-costs-colorado-buyers-2026` (Centennial), `cost-to-sell-house-colorado-2026` (HR), `littleton-vs-highlands-ranch` (both), `parker-vs-castle-pines` (both), `what-happens-after-accepting-offer` (Centennial), `what-realtor-does-to-earn-commission` (HR), `why-homes-sit-on-market-south-denver` (Centennial), `why-house-not-selling-denver` (HR). Single contextual `/neighborhoods/<slug>` link per post intro, no other body changes. Score lift: +1.4 (Content 60.5 → ~67).

### Visual + title polish on Day 23 post
- Move-up comparison visual went through 3 in-session iterations during Jacob's review: (1) initial three-card flex layout → (2) full no-compromise rebuild as real `<table>` with `<figure>`, JSON-LD `Dataset`, `Place` Microdata, and `figcaption` → (3) responsive mobile fix (removed `min-width: 720px`, added stacked card layout via `display: block` + `td::before { content: attr(data-label) }`). Final caption-width fix added `caption` to the mobile `display: block; width: 100%; box-sizing: border-box;` rule.
- Title shortened from "Spring 2026 Move-Up Market Report: Where Are South Denver Families Upgrading To?" (80 chars) → "Where South Denver Families Are Moving Up in 2026" (49 chars) for SERP CTR. Subtitle "in Q1 data" phrase removed (redundant). Original longer title preserved in `headline` frontmatter field for JSON-LD/AI engine pickup.
- Day 22 (HR expired-listing case study) deferred 90 days pending anonymized real-deal data from Jacob; revisit on or after 2026-07-25.

### Session notes
- Cowork session and SEO/AEO Expert project session pushed to `main` in parallel throughout the day. All commits intentional, no conflicts. Bundled deploy of 9 commits → live in one credit charge.
- Verified post-deploy via Netlify MCP: `currentDeploy.state: ready`, deploy ID `69eef42aff9f8200089a80bc`.
- Handoff doc created at `~/Library/Application Support/Claude/local-agent-mode-sessions/SEO-AEO-Visual-Standard-Handoff.md` for ongoing visual standard work in the SEO/AEO Expert project (Phases 2-5 still ahead: FAQ markup audit, retroactive comparison post upgrade, HowTo retrofit, glossary buildout, testimonials with Review schema, homepage Local Business audit, Author/Person schema in BaseLayout, title length audit across all existing posts).

---

## 2026-04-25 — commit 19e929e (merge b6326ff on live) | Credits used: 15 | Credits remaining: ~110

### New blog post (1 — Day 21)
- **Day 21 — "What Out-of-State Buyers Get Wrong About the Denver Suburbs (and How to Avoid the Same Mistakes)"** (`src/content/blog/out-of-state-buyer-mistakes-denver-suburbs-centennial.md`). Relocation pillar + Centennial geographic pillar. TOFU buyer advice for out-of-state relocation buyers, with Centennial as the running case study. Uses Q1 2026 REcolorado MLS Centennial single-family closed-sale data (n=269 closed, $700K median, 13-day median DIM, 98% median CP/OLP) and the DMAR March 2026 Market Trends Report (metro pending +30.69% MoM, DIM down 50% to 16 days, close-to-list 99.13%). Five misconceptions covered (commute, altitude, season, HOA + metro district stack, water restrictions / Stage 1 drought) with cross-links to `/relocation`, `/neighborhoods/centennial`, the Littleton vs. Centennial comparison, the closing-costs guide, and the South Denver watering restrictions guide. Visual: inline 5-card stacked color-band "Misconceptions vs. Reality" block using the brand red→clay→olive→green→navy progression with source attribution beneath.

### Form spam prevention (2026-04-24 work, deployed today)
- Added honeypot spam prevention to both forms (`contact.astro` and `Footer.astro`). Each form gets `netlify-honeypot="bot-field"` on the `<form>` plus a hidden `bot-field` input off-screen (`position: absolute; left: -9999px`), `aria-hidden="true"` on the container, `tabindex="-1"` and `autocomplete="off"` on the input so screen readers, keyboard users, and password managers don't trip it. Netlify strips the `netlify-honeypot` attribute at build time and rejects any submission where `bot-field` has a value. Goal: catch bots before Akismet so fewer real submissions get false-positive spam-flagged. No change to form submission logic — real users unaffected.

### GA4 tel_click event listener (Conversion sprint)
- Added global `tel_click` GA4 event listener to `src/components/SEO.astro` (capture-phase click delegate on `a[href^="tel:"]`). Fires `gtag('event', 'tel_click', {link_url, link_text, page_path})` for every phone-link tap sitewide — covers FloatingCTA, Footer, CTABanner, contact page, and all pillar-page CTAs without per-page changes. Pairs with `form_submit` flagged as key event in GA4 Admin (also 2026-04-25). Together they unblock the Conversion category in the SEO/AEO weekly audit; before today, GA4 reported 0 conversions for 90 days because no events were flagged. Detailed entry in `~/Documents/Claude/Projects/AEO & SEO Expert/DEPLOY_QUEUE.md`.

### Session notes
- Nightly blog task ran autonomously and pushed to `main`. Jacob approved a bundled production deploy ("deploy all to live") which merged `main` into `live`, triggered the build hook, and shipped all three pending items in one credit charge. Production verified — `https://selling303.com/blog/out-of-state-buyer-mistakes-denver-suburbs-centennial` returns 200 with fresh cache.

---

## 2026-04-24 — commit 5a0465a (merge eedf53c on live) | Credits used: 15 | Credits remaining: ~125

### New blog posts (3 — deploy bundle)
- **Day 18 — "The Hidden Costs of Selling Your Home in Arapahoe County — A First-Time Seller's Net Sheet"** (`src/content/blog/hidden-costs-selling-home-arapahoe-county-net-sheet-2026.md`). First-Time Sellers pillar + Centennial geographic pillar. MOFU seller advice. Uses Centennial Q1 2026 REcolorado MLS data (n=269 closed SFR). Visual: inline proportional net-sheet cost-breakdown bars.
- **Day 19 — "Move-Up Buyer's Checklist: Going from a Starter in Englewood to More Space in Parker"** (`src/content/blog/move-up-englewood-to-parker-checklist-2026.md`). Move-Up Sellers pillar + Englewood geographic pillar. MOFU. Uses Englewood + Parker Q1 2026 REcolorado MLS data (n=138 Englewood / n=330 Parker closed SFR) + DMAR March 2026. Visual: inline HowTo step-tracker (7-step move-up timeline, Days 0–120) with Schema.org HowTo microdata. Revised 2026-04-23 to remove fabricated stat and correct listing launch process (Thursday Coming Soon → following Thursday Active).
- **Day 20 — "New Build vs. Resale in Highlands Ranch: Which Makes More Financial Sense in 2026?"** (`src/content/blog/new-build-vs-resale-highlands-ranch-2026.md`). New Construction pillar + Highlands Ranch geographic pillar. MOFU buyer advice. Uses HR Q1 2026 REcolorado MLS (n=198 closed SFR, $742,500 median) + Lone Tree builder spec comp + DMAR March 2026. Head-to-head on price/sqft, timeline, warranty, Year 1 total cost. Visual: inline 2-column side-by-side comparison card (Resale vs. New Build) with 8 data points each.

### Netlify Forms detection enabled
- Prior to this deploy, Netlify Forms detection was OFF in the dashboard despite `data-netlify="true"` markup being correct on both `contact.astro` and `Footer.astro`. Form POSTs were landing at `/thank-you` and being silently discarded. GA4 recorded 4 `form_submit` events in the 83-day GA4 baseline window that were NOT captured by Netlify (lost leads, unrecoverable). Form detection enabled in Netlify UI before this deploy; deploy re-parsed forms at build time so submissions begin being captured from this deploy forward. Verified via Netlify MCP after deploy: `extraFeatures.forms: "enabled"`. Jacob still needs to configure email notifications (Site configuration → Notifications → Add notification → Email notification → New form submission → jacob@selling303.com) for both `contact` and `newsletter` forms.

### Skill update (outside this repo)
- `~/.claude/skills/deploy-to-netlify/SKILL.md` — removed obsolete Path B (Chrome MCP) workflow and April 21 PREFLIGHT block from Mode 2 Step 4. `api.netlify.com` has been reachable from the sandbox since the 2026-04-21 allowlist change, so direct curl to the build hook is now the only supported path.

### Session notes
- Deploy executed during SEO/AEO Expert project session. Netlify MCP had extended outages during the session — recovered after manual disconnect/reconnect + retries.

---

## 2026-04-21 — commit d0f6579 (merge 6bbba0a on live) | Credits used: 15 | Credits remaining: ~140

### New blog post (1)
- **Day 17 — "Why Your Centennial Home Isn't Getting Offers — and How to Fix It Before Summer"** (`src/content/blog/why-centennial-home-not-getting-offers.md`). Expired Listings pillar + Centennial geographic pillar. BOFU seller advice. Diagnostic framework for stale Centennial, Colorado listings anchored to real Q1 2026 REcolorado MLS data (n=269 closed, n=39 expired): 51.7% of closed homes went under contract within 13 days, 58.9% of expired listings sat past 68 days before expiration. AEO-optimized inline SVG histogram with in-visual source attribution, domain term definitions ("closed" / "expired"), and state-qualified entity references for disambiguation. Iterative refinement with Jacob: stacked-card first draft rejected, dual-curve distribution rejected (pseudo-statistical), real histogram built from extracted DIM values. Tier-pricing correction in body: round number ($800K) recommended over $799K for dual-tier search-filter reach (inclusive-at-boundary mechanic).

### Footer refinement
- `Footer.astro` — renamed ClientClarity link to "ClientClarity Portal." Combined form carries proprietary tech signal for curious visitors and functional anchor for existing clients.

### Conversion sprint Week 1 — final calculator
- **Cost of Living Calculator** — new component at `src/components/calculators/CostOfLivingCalculator.astro` comparing South Denver Metro to 27 major U.S. cities with category breakdown (housing, groceries, utilities, transportation, healthcare) + state income tax callout. Data sourced from BLS CPI, Tax Foundation, Zillow (April 2026, stamped with source links in disclaimer). New standalone page at `/tools/cost-of-living-calculator` with Colorado tax advantage, housing comparison, and "what $100K looks like" explainers + FAQ. Embedded on `/relocation` with new TOC entry. Replaced Coming Soon card on `/tools` hub with active entry; updated ItemList schema. Week 1 of conversion sprint complete.

### Skill update (blog-post-writer, outside this repo)
- Added Rule #10 to Visual Opportunity Check: no blank lines inside `<svg>` blocks (Astro MD parser silent-failure fix).
- Added AEO Optimization Checklist (Visuals) sub-section with 9 rules — entity disambiguation, citable `<title>`/`<desc>`, in-SVG source attribution, domain-term definitions, full date ranges, sample sizes in legend, population framing, headline stat in summary sentence, question-phrased H3 headings above charts.

### Session notes
- Build hook trigger required CORS workaround: fetching from `app.netlify.com` (same-origin to Netlify API) succeeded after selling303.com origin was blocked by CSP.

---

## 2026-04-20 — commit 03b0893 (merge a4af39d on live) | Credits used: 15 | Credits remaining: 155

### New blog posts (2)
- **Day 15 — "Lone Tree New Construction: Builder Incentives and What They Actually Mean for Your Bottom Line"** (`src/content/blog/lone-tree-new-construction-builder-incentives-2026.md`). New Construction pillar + Lone Tree geographic pillar. MOFU buyer advice decoding rate buydowns, closing cost credits, and upgrade packages. Data scoped to REcolorado MLS builder spec inventory (Year Built 2024+): 10 active / 5 closed / 2 pending, median DIM 122 days active vs. 77 days closed, 97% CP/OLP. Explicitly excludes build-to-order custom homes (methodology note included). Three inline visuals: (1) spec DIM divergence bar chart (sold vs. still-unsold), (2) permanent vs. 2-1 buydown side-by-side comparison, (3) upgrade credit "advertised $20K vs. real ~$8-12K" reality check, plus the original tiered incentive-value card (4-band ranking).
- **Day 16 — "Relocating to Parker, Colorado: What Families Moving from Out of State Need to Know"** (`src/content/blog/moving-to-parker-colorado-relocation-guide-2026.md`). Relocation pillar + Parker geographic pillar. TOFU family-focused relocation guide. Inline price-point table (4-tier entry/core/move-up/luxury). Data from REcolorado Q1 2026 Parker closed SFRs (330 sales, $717,450 median, 98% CP/OLP, 24 median DIM) and DMAR March 2026. Internal link to South Denver watering restrictions guide.

### Lone Tree post iteration (same session as deploy)
- Data rescoping mid-draft: original version used aggregate Lone Tree SFR data (44 active, 36 closed). Caught by Jacob that the "new construction DIM" thesis was unsupported by resale-inclusive data. Rescoped visual and prose to Year Built 2024+ spec inventory only. Methodology note added.
- Visual iteration: stat-tile grid → DIM-divergence bar chart → plain-English rewrite → 8th-grade-reading-level headline ("The longer a builder's spec home sits, the bigger the discount gets"). Markdown code-block rendering bug fixed (blank line between cards at 4-space indent was breaking parser).
- "Representation is not optional" closer rewritten to be accurate (cost is priced in either way; buyer's choice).

### Conversion sprint Week 1 — two new interactive calculators
- **Home Equity & Affordability Calculator** — new component at `src/components/calculators/HomeEquityCalculator.astro`, standalone page at `/tools/home-equity-calculator`, embedded on `/move-up-sellers` with a new TOC entry. Includes WebApplication + FAQPage schema, SMS-deeplink CTA to 303-997-0634 alongside the Calendly primary.
- **Closing Cost Estimator** — new component at `src/components/calculators/ClosingCostEstimator.astro` (buyer/seller toggle, Colorado-accurate line items, bundled 6% commission default), standalone page at `/tools/closing-cost-estimator`, embedded on `/first-time-homebuyers` (buyer default) and `/first-time-homesellers` (seller default).

### New hub pages
- `/tools` — ItemList schema, coming-soon cards for future calculators.
- `/resources` — CollectionPage schema, umbrella landing.
- `Header.astro` Resources dropdown updated with "All Resources" and "Tools" items.

### Seller Success Stories — index page rewrite + content tweaks
- `src/pages/sell/success-stories/index.astro` reworked (+90 / -72 lines).
- 4 success story content files updated: Woodside (Parker), Flower / Holland / Carr (Littleton).

### Session notes
- Two sessions contributed to this deploy: nightly blog task (Day 15 + Day 16 posts + conversion sprint calculators pushed via another session) and iterative data-quality refinement on the Lone Tree post with Jacob.
- Data-sourcing guardrail validated: Jacob caught the new-construction-vs-resale MLS filter issue mid-review, asked for methodology transparency, and approved the rescoped version. DEPLOY_QUEUE.md entry for Closing Cost Estimator was initially stale (files not yet pushed) but was resolved when the other session pushed commit a1d3463.

---

## 2026-04-18 — commit 642acdc (merge 52ca1b6 on live) | Credits used: 15 | Credits remaining: 170

### New blog post (1)
- **Day 14:** "What First-Time Buyers Should Know About Bidding in Littleton's Spring Market" (`src/content/blog/first-time-buyer-bidding-littleton-spring-2026.md`). First-Time Homebuyers pillar + Littleton geographic pillar. MOFU buyer advice on offer strategy. Data: Littleton Q1 2026 REcolorado MLS (433 closed SFRs, $720K median, 98% median CP/OLP, 23 median DIM) + DMAR March 2026 (99.13% CP/LP, 16 median DIM, pending +30.69% MoM, 63.14% concessions, rates back above 6%). Entry-level pattern for sub-$600K bracket documented (100–107% of OLP in 1–10 DIM).
- **Two inline visuals:** (1) "First-Time Buyer's Offer Toolkit" — stacked tiered cards mapping escalation clause / appraisal gap / inspection flexibility to the problem each solves; (2) "How to Read the Spring 2026 Littleton Numbers" — three-panel data translator explaining median (middle-of-sorted-row visual), average (skewed by luxury outlier), and close-to-original-list ratio (two paired scenarios: Scenario A citywide median 98% and Scenario B competitive entry-level bracket 104% — brand-green bar extending past list bar on Scenario B visualizes "over asking").
- **Jacob-review revisions (same-day):** dropped the "informational-only inspection" bullet, added explicit "inspection itself is non-negotiable" opening, folded dollar-threshold tactic ($1K/$2K/$5K objection floor) into scope-limiting bullet as a concrete extension. Removed CAR Legal Hotline external link (hotline is Realtor-only, not a consumer resource).
- Content calendar Day 14 marked `[x] (drafted 2026-04-17)(published 2026-04-18)`; added to First-Time Homebuyers cluster in content-cluster-map.md.

### Homepage PageSpeed fixes
- **LCP fix:** added `.hero::before` rule to critical inlined CSS in `BaseLayout.astro`. Previously `.hero::before` (which renders the hero background via `var(--hero-bg)`) only existed in deferred `/css/styles.css`, causing a late layout recalc that pushed LCP to ~2,460ms element render delay. Rule now in critical CSS so the positioning element exists at first paint.
- **Forced-reflow fix:** rewrote GA4 init in `SEO.astro` to defer until first user interaction (scroll/click/keydown/mousemove/touchstart) or idle/3s timeout. Eliminates 64ms of forced reflow on homepage line 154. Pageviews still register — only sub-3s zero-interaction bounces are missed. Preconnect to googletagmanager.com retained.
- Only affects homepage hero (the only page using `.hero` + `--hero-bg`).

### Day 13 HR equity post voice edits
- `equity-to-move-up-highlands-ranch.md` — removed direct Freddie Mac PMMS "check the rate" consumer CTA, replaced with recommendation to talk to a trusted local lender (Jacob can introduce). Timing-section closer reframed so DMAR/CAR appear only as Jacob's source attribution, not as research readers should do themselves.

### Seller Success Stories migration (Framer → Astro, second wave)
- **14 story content files** added in this batch: 8 full SCAR narratives (with FAQs, testimonials, Schema.org data) and 6 listing-only placeholders pending client interviews (marked `draft: true` so they're excluded from the index grid and sitemap). Counties: Centennial (Birch, Phillips), Littleton (Carr, Holland x2, Flower), Parker (Woodside), Aurora (Jericho), plus placeholders across Arvada/Aurora/Denver/Littleton/Englewood/HR.
- **`[slug].astro` template:** added auto-image-discovery via `import.meta.glob` — stories auto-find all images in their folder. Made sqft display conditional.
- **Index page rewrite:** hidden breadcrumbs (sr-only for SEO), 3 featured stories above credibility tiles, 6-stat credibility tiles matching About page, "Browse All Stories" filter + full grid below.
- Hero image paths wired for all 9 stories with photos. Content config `sqft` made optional.

### Session notes
- Chrome MCP disconnected partway through the deploy window because the Claude in Chrome extension was signed out post-update. Re-signing in restored the connection. Documented behavioral principle in `~/.claude/CLAUDE.md`: flag broken required tools, don't improvise around them.

---

## 2026-04-17 — commit 183e7a7 | Credits used: 15 | Credits remaining: 185

### New blog posts (2)
- **Day 12:** "South Denver Market Update: What April 2026 Means for Sellers Sitting on Expired Listings" (`src/content/blog/south-denver-market-update-april-2026-expired-listings-centennial.md`). Expired Listings pillar + Centennial geographic pillar. MOFU market update. DMAR March 2026 data (30.69% MoM pending growth, 16 median DIM, 99.13% CP/LP, $590K metro median) + REcolorado Q1 2026 Centennial expired cohort (39 expired + 5 withdrawn, median original list $850K, 119 avg days before expiration) + Centennial closed comps ($689K median, 13 median DOM, 94% CP/OLP avg). Includes inline 4-card stat strip visualizing MoM pending/DIM/price/new-listing deltas. Voice fix: replaced stray first-person "I pulled" with "Jacob Stark pulled" (commit 183e7a7).
- **Day 13:** "How Much Equity Do You Need to Move Up in Highlands Ranch?" (`src/content/blog/equity-to-move-up-highlands-ranch.md`). Move-Up Sellers pillar + Highlands Ranch geographic pillar. MOFU costs/pricing. REcolorado Q1 2026 Highlands Ranch closed data (198 sales, $742,500 median, $873,461 avg, 16 median DIM, 98% CP/OLP) + DMAR March 2026. Two inline visuals: horizontal stacked bar showing equity decomposition on a $725K HR sale (Seller Take-Home 47% / Mortgage Payoff 46% / Selling Costs 7%) and side-by-side payment comparison cards ($1,550/mo current vs. $5,420/mo new vs. $3,870/mo increase). Sell-first vs. buy-first framework.

### Success Story placeholder hide (from Apr 15 queue)
- Added optional `draft: z.boolean()` field to `successStories` Zod schema in `src/content.config.ts`.
- Marked 6 placeholder success stories as `draft: true` (listing data only, stories pending client interviews): 8781-flora-ct-arvada, 22461-e-union-circle-aurora, 4360-w-wagon-trail-dr-denver, 9559-w-coal-mine-ave-littleton, 301-w-lehow-ave-englewood, 10315-ravenswood-ln-highlands-ranch.
- `/sell/success-stories/` index page now filters out drafts from the card grid and CollectionPage ItemList schema.
- `[slug].astro` template: draft stories render with `<meta name="robots" content="noindex, nofollow" />` and skip all Schema.org structured-data scripts (RealEstateListing / Review / Article / ImageObject / FAQPage) to avoid thin-content + structured-data-mismatch flags.
- `astro.config.mjs`: added sitemap `filter` that excludes the 6 draft slugs. Single source of truth — remove a slug from the `DRAFT_SUCCESS_STORY_SLUGS` array when its story is completed.
- Verified via local build: 0 draft slugs in rendered index, 0 draft URLs in sitemap-0.xml, draft pages include the robots meta, non-draft pages unchanged.

### Schema markup upgrade for AI entity recognition (from Apr 16 queue)
- Homepage (`index.astro`): merged two duplicate `RealEstateAgent` schema blocks into one unified `["Person", "RealEstateAgent"]` block with `@id`, `jobTitle`, `alternateName`. Fixed stale `reviewCount` from 52 → 47 (matches current Google reviews). Added Homes.com and Nextdoor URLs to `sameAs` array.
- About page (`about.astro`): upgraded thin `Person` schema to full `["Person", "RealEstateAgent"]` with `@id` linking to homepage entity, `mainEntityOfPage`, `image`, `address`, `areaServed` (9 cities), `aggregateRating`, `hasCredential`, `knowsAbout`, and full `sameAs` array (12 URLs).
- Added awards (DMAR Excellence 2024–2026, 5280 Black Diamond, Real Trends Verified), credentials (Who's Who in Luxury RE), and memberOf (DMAR, Who's Who) to both homepage and about page schema. Added Real Trends and 5280 directory URLs to `sameAs`.
- Added Wikidata entity URL (Q139385406) to `sameAs` on both homepage and about page.
- Added visual badge/awards section to about page: DMAR Excellence Gold, 5280 Top Producer, Real Trends Verified, Who's Who in Luxury RE, RENE. White background section between Track Record and CTA.
- Badge images: all five logos imported as PNGs through Astro `<Image>` pipeline (ea25_digitalawards_gold.png, 5280-magazine-black.png, rtv-black.png, WWLRE_BLACK.png, rene-color.png).
- Three badges linked to profile pages: DMAR → excellenceawards, 5280 → directory profile, Real Trends → agent profile.
- Added two new Track Record credential tiles: "Top 10 — Agent by Verified Sales — RealTrends" and "Top 1.5% — of U.S. Real Estate Professionals."
- CSS: fixed logo clipping (height-based sizing with width:auto), removed opacity fade on badges.

### Housekeeping
- Deleted stale repo-root files: `blog-post-writer-SKILL-UPDATED.md` (0-byte stub) and `blog-post-writer.skill` (April 10 zip, superseded).

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
