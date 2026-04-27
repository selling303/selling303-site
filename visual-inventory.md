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
| `first-time-buyer-bidding-littleton-spring-2026` | tier-list (legacy) | unknown | needs upgrade — Phase 3 | — |
| `first-time-home-buyer-guide-englewood-colorado-2026` | none detected | — | review needed (likely howto candidate — Phase 4 flag-only) | — |
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
| `real-estate-agent-new-construction-colorado` | none detected | — | review needed | — |
| `relist-home-littleton-after-expired-listing` | none detected | — | review needed (howto candidate — Phase 4 flag-only) | — |
| `selling-centennial-buying-highlands-ranch-coordinate-transactions` | table (legacy), svg-chart, cost flow | unknown | needs upgrade — Phase 3 (howto + comparison-table + cost-breakdown candidate) | — |
| `selling-first-home-south-denver-process` | none detected | — | review needed (howto candidate — Phase 4 flag-only) | — |
| `south-denver-market-update-april-2026-expired-listings-centennial` | none detected | — | review needed | — |
| `south-denver-watering-restrictions-guide-2026` | none detected | — | review needed | — |
| `spring-2026-move-up-market-report-south-denver` | comparison-table | Dataset + Place Microdata + per-cell value | **optimized** (reference template) | 2026-04-26 |
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
