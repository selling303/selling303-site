# Visual Inventory — selling303.com

Tracking file for every page that uses a data visual. Source of truth for what visual types are present where, what schema is rendered, and when each was last verified against Google Rich Results Test.

**Maintenance protocol:**
- Updated by `aeo-visual-builder` skill every time it produces a visual.
- Updated by `seo-aeo-expert` skill during weekly audits when discrepancies are found.
- Manually update `Last verified` on the date you re-run Rich Results Test.

**Status values:**
- `optimized` — full no-compromise stack (semantic HTML + JSON-LD + Microdata + machine-readable values + responsive CSS via `/css/aeo-visuals.css`).
- `needs upgrade` — visual exists but uses legacy markup (styled divs, missing schema, inline `<style>`, no Microdata, no machine-readable values).
- `flag-only` — opportunity flagged with HTML comment, pattern not yet built in `aeo-visual-builder` (Phase 3 / 4 deps).
- `review needed` — automated scan flagged ambiguity; manual audit required.
- `no-visual` — post does not need a visual (or no opportunity identified).

---

## Reference template

`src/content/blog/spring-2026-move-up-market-report-south-denver.md` — first fully optimized comparison-table. Lift its `<figure class="aeo-comp-table">` block + preceding `<script type="application/ld+json">` Dataset block when building new comparison tables.

---

## Blog posts (33 total, scanned 2026-04-26)

| Post | Current visuals | Schema | Status | Last verified |
|---|---|---|---|---|
| `7-smartest-home-upgrades-before-selling-2026` | none detected | — | review needed (likely tier-list candidate) | — |
| `best-neighborhoods-south-denver-move-up-buyers` | table (legacy) | unknown | needs upgrade — Phase 3 | — |
| `best-parks-trails-littleton-highlands-ranch` | svg-chart | unknown | review needed | — |
| `closing-costs-colorado-buyers-2026` | table (legacy), cost flow | unknown | needs upgrade — Phase 3 (cost-breakdown candidate) | — |
| `cost-to-sell-house-colorado-2026` | table (legacy), cost flow | unknown | needs upgrade — Phase 3 (cost-breakdown candidate) | — |
| `equity-to-move-up-highlands-ranch` | none detected | — | review needed (likely cost-breakdown candidate) | — |
| `expired-listing-highlands-ranch` | none detected | — | review needed | — |
| `price-reductions-highlands-ranch-what-works-2026` | single-metric-bar-chart (Tier 0) — 5-bucket median DIM by sale outcome, HR April 2026, n=150 | Dataset (outer) + PropertyValue per bar + machine-readable `<meta itemprop="value">` + parallel JSON-LD Dataset + temporalCoverage + spatialCoverage (Place + AdministrativeArea) + isBasedOn | **optimized** | 2026-05-06 |
| `500k-home-centennial-highlands-ranch-parker-2026` | comparison-table | Dataset + Place Microdata + per-cell value | **optimized** | 2026-04-30 |
| `expired-listing-trap-englewood-switching-agents-2026` | comparison-table | Dataset + Place Microdata + per-cell value | **optimized** | 2026-04-30 |
| `first-time-buyer-bidding-littleton-spring-2026` | tier-list (legacy) | unknown | needs upgrade — Phase 3 | — |
| `greenwood-village-worth-the-price-tag-relocation-2026` | persona-card-grid | ItemList JSON-LD + per-card Person Microdata + Place Microdata for matched suburbs | **optimized** | 2026-04-29 |
| `first-time-home-buyer-guide-englewood-colorado-2026` | none detected | — | review needed (likely howto candidate — Phase 4 flag-only) | — |
| `first-time-home-buyer-guide-lakewood-colorado-2026` | two-path-diptych (SFR vs. condo/townhome at $400-550K) — navy header + 2-column card grid + per-path icons + trade-off section | Dataset Microdata + per-path PropertyValue + machine-readable price ranges + source attribution | **optimized** | 2026-05-05 |
| `hidden-costs-selling-home-arapahoe-county-net-sheet-2026` | tier-list (legacy), cost flow | unknown | needs upgrade — Phase 3 (cost-breakdown candidate) | — |
| `littleton-vs-centennial-south-denver-relocation` | none detected | — | review needed (likely comparison-table candidate) | — |
| `littleton-vs-highlands-ranch` | table (legacy) | unknown | needs upgrade — Phase 3 (comparison-table candidate) | — |
| `lone-tree-new-construction-builder-incentives-2026` | tier-list (legacy) | unknown | needs upgrade — Phase 3 | — |
| `move-up-englewood-to-parker-checklist-2026` | none detected | — | review needed (howto candidate — Phase 4 flag-only) | — |
| `moving-to-highlands-ranch-relocation-guide-2026` | none detected | — | review needed | — |
| `moving-to-parker-colorado-relocation-guide-2026` | table (legacy), cost flow | unknown | needs upgrade — Phase 3 | — |
| `new-build-vs-resale-highlands-ranch-2026` | none detected | — | review needed (likely comparison-table candidate) | — |
| `new-construction-castle-pines-parker-2026` | none detected | — | review needed (likely comparison-table candidate) | — |
| `out-of-state-buyer-mistakes-denver-suburbs-centennial` | tier-list (legacy) | unknown | needs upgrade — Phase 3 | — |
| `parker-vs-castle-pines` | none detected | — | review needed (likely comparison-table candidate) | — |
| `ridgegate-vs-heritage-hills-lone-tree-new-construction-2026` | decision-path (4-question routing: new vs. established → RidgeGate or Heritage Hills / light-rail commute → RidgeGate or either / gated preference → Heritage Hills or RidgeGate / budget ceiling → RidgeGate or either) — question-led navy hero with location eyebrow + answer-shape subhead, white-bg card stack with 32px navy numbered circles, green-vs-navy answer pills with routing arrows, Decision Rule tally footer, bound source footer. **First library entry of the new `decision-path` pattern** — promoted from stretch on 2026-05-06 after winning A/B vs. corrected two-path-diptych. | HowTo + 4× HowToStep + per-pill itemListElement + bound source attribution inside HowTo wrapper | **optimized** | 2026-05-06 |
| `real-estate-agent-new-construction-colorado` | none detected | — | review needed | — |
| `relist-home-littleton-after-expired-listing` | none detected | — | review needed (howto candidate — Phase 4 flag-only) | — |
| `selling-centennial-buying-highlands-ranch-coordinate-transactions` | table (legacy), svg-chart, cost flow | unknown | needs upgrade — Phase 3 (howto + comparison-table + cost-breakdown candidate) | — |
| `selling-first-home-south-denver-process` | none detected | — | review needed (howto candidate — Phase 4 flag-only) | — |
| `south-denver-market-update-april-2026-expired-listings-centennial` | none detected | — | review needed | — |
| `south-denver-watering-restrictions-guide-2026` | none detected | — | review needed | — |
| `spring-2026-move-up-market-report-south-denver` | comparison-table | Dataset + Place Microdata + per-cell value | **optimized** (reference template) | 2026-04-26 |
| `new-construction-buyer-representation-colorado-2026` | comparison-table | Dataset + Place Microdata + per-cell value | **optimized** | 2026-05-02 |
| `move-up-seller-myth-waiting-market-better-lakewood-2026` | comparison-table (Lakewood YoY vs. Jeffco vs. Metro) | Dataset + Place/AdministrativeArea Microdata + per-cell value | **optimized** | 2026-05-02 |
| `south-denver-april-2026-closings-move-up-sellers` | comparison-table (9 South Denver suburbs × 4 metrics — Closed/Pending/Active/Failed, April 2026) | Dataset + Place Microdata + per-cell value | **optimized** | 2026-05-04 |
| `2026-notice-of-valuation-protest-playbook-south-denver` | **interactive Gap Calculator widget** (Tier 2 — first interactive widget on the site) — county selector + 2 currency inputs + live gap-percent readout + 3 path cards (Protest/Skip/Abate) that highlight on recommendation + live countdown to June 1 deadline. Vanilla JS inline, no framework. Static SSR'd fallback shows all 3 paths fully visible without JS. | Dataset (outer) + ItemList (3 paths) + 3× RecommendAction (per path) + JSON-LD Dataset block + 3× Place spatialCoverage + temporalCoverage 2026-05-01/2026-08-15 + bound source row | **optimized** (flag for Library Promotion as new `interactive-calculator` Tier-2 pattern; lift-from on next push) | 2026-05-06 |
| `what-happens-after-accepting-offer` | table (legacy), cost flow | unknown | needs upgrade — Phase 3 (howto candidate — Phase 4 flag-only) | — |
| `what-realtor-does-to-earn-commission` | none detected | — | review needed | — |
| `when-to-sell-parker-home-move-up` | none detected | — | review needed | — |
| `why-centennial-home-not-getting-offers` | svg-chart | unknown | review needed | — |
| `why-homes-sit-on-market-south-denver` | none detected | — | review needed | — |
| `why-house-not-selling-denver` | tier-list (legacy) | unknown | needs upgrade — Phase 3 | — |

---

## Pillar pages and other surfaces

To be inventoried during Phase 2 verification sweep.

| Surface | Path | Visuals expected | Status | Last verified |
|---|---|---|---|---|
| Homepage | `src/pages/index.astro` | LocalBusiness, MarketStatTile, NeighborhoodCard | needs audit (Phase 2) | — |
| `/neighborhoods/{slug}` (9 pages) | `src/pages/neighborhoods/[slug].astro` | NeighborhoodCard, MarketStatTile (uses existing components) | likely partial — needs audit (Phase 2) | — |
| `/expired-listings` | `src/pages/sell/expired-listings.astro` | tbd | needs audit (Phase 2) | — |
| `/move-up-sellers` | `src/pages/sell/move-up-sellers.astro` | tbd | needs audit (Phase 2) | — |
| `/first-time-homebuyers` | `src/pages/buy/first-time-homebuyers.astro` | tbd | needs audit (Phase 2) | — |
| `/first-time-homesellers` | `src/pages/sell/first-time-homesellers.astro` | tbd | needs audit (Phase 2) | — |
| `/new-construction` | `src/pages/buy/new-construction.astro` | tbd | needs audit (Phase 2) | — |
| `/relocation` | `src/pages/buy/relocation.astro` | tbd | needs audit (Phase 2) | — |
| `/glossary` | not yet built | DefinedTerm + DefinedTermSet | Phase 4 build target | — |
| `/reviews` *(or homepage section)* | not yet built | Review + AggregateRating | Phase 4 build target | — |
| `/about` (author detail) | tbd | Person | Phase 4 build target | — |

---

## Coverage summary (2026-04-26 baseline)

- **Optimized:** 1 of 33 blog posts (3%)
- **Needs upgrade:** 12 posts with legacy visuals (36%)
- **Review needed:** 20 posts likely missing visual opportunities (61%)
- **Visual type coverage on optimized posts:** comparison-table only

The 2026-04-26 baseline shows the size of the Phase 3 retroactive cleanup and the variety gap that Phases 3 + 4 are meant to close.

**Updates since baseline:**
- 2026-04-29 — `greenwood-village-worth-the-price-tag-relocation-2026` shipped optimized comparison-table.
- 2026-04-30 — `expired-listing-trap-englewood-switching-agents-2026` shipped optimized comparison-table (Closed vs. Expired Englewood single-family Q1 2026). Tier-list opportunity flagged inline (root-cause severity scale) — pending Phase 3 build.
- 2026-04-30 — `move-up-timing-castle-pines-2026` shipped optimized **svg-chart** (single-metric horizontal bar chart of median DOM until sale: Castle Pines 77 days, Parker 62, Highlands Ranch 52 — Feb 2026). SVG `<title>` + 4-sentence `<desc>` + in-SVG term definition + source `<text>` line + parallel JSON-LD `Dataset` block. Severity coloring: amber (slowest) → olive → green (fastest). Replaces an earlier 5-column comparison-table draft (over-broad for the article's timing thesis). First svg-chart visual on the site — establishes the canonical pattern for `aeo-visual-builder`'s svg-chart catalog entry. Source: DMAR / CAR Local Market Update Feb 2026.
- 2026-05-06 — `price-reductions-highlands-ranch-what-works-2026` shipped optimized **single-metric-bar-chart Tier 0** (5-bucket horizontal bar of median DIM by sale outcome: Sold ≥100% n=65 / 3 days, Sold 95–99% n=44 / 21 days, Sold 90–94% n=9 / 70 days, Sold <90% n=10 / 164 days, Expired n=22 / 87 days — Highlands Ranch April 2026, n=150 single-family residential). SVG `<title>` + paragraph-length `<desc>` with all 5 bucket stats + per-bar `PropertyValue` Microdata with `<meta itemprop="value">` machine-readable values + source `<text>` baked into SVG + parallel JSON-LD `Dataset` block with `temporalCoverage`, `spatialCoverage` (Highlands Ranch + Douglas County containedInPlace), `creator`, `publisher`, `isBasedOn`. Severity coloring: green (fastest) → olive → amber → red → gray (expired). Source row visually bound inside outer `Dataset` itemscope wrapper (figcaption with strong source line, no margin gap). Source: REcolorado MLS Market Analysis Summary, April 1–30, 2026, Highlands Ranch, deduplicated for IRES cross-listings. Compelling Question Flow: chosen over comparison-table and stretch outcome-distribution-bar candidates because the bimodal "quick or stuck" narrative pays off in 5 seconds when bars are scaled linearly to DIM.
- 2026-04-30 — `500k-home-centennial-highlands-ranch-parker-2026` shipped optimized comparison-table (6-column $500K market comparison — Centennial / Highlands Ranch / Parker single-family). Q1 2026 closings count, typical sqft, DMAR Feb 2026 SF median sale, SF DOM, typical home type. Place Microdata per row, per-cell `<meta itemprop="value">`, parallel JSON-LD Dataset block with `temporalCoverage`, `spatialCoverage`, `variableMeasured`, `creator`, `publisher`, `isBasedOn`. Source: REcolorado MLS Q1 2026 + DMAR/CAR Feb 2026 LMU.
