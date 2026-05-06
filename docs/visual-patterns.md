# Visual Patterns Library — selling303.com

The single source of truth for visuals on selling303.com blog posts, pillar pages, and neighborhood pages. Seven shipped patterns, each grounded in a real post that proved it works. The blog-post-writer and aeo-visual-builder skills both reference this file when selecting a pattern at draft time.

---

## How to use this file

The writer arrives here AFTER answering the post's compelling question and its one-sentence answer (per the blog-post-writer "Compelling Question Flow"). At that point, the writer scans this library for the pattern that best pays off the question, brainstorms 2 candidates from this library plus 1 stretch candidate not in this library, scores all three, and ships the winner.

If the stretch candidate wins, the delivery message flags it for library promotion and the new pattern gets added here on the next push. That's how the library grows — every post is potentially a library-growth moment, but only when the stretch genuinely outperforms the proven options.

---

## Library Promotion Protocol

A new pattern earns a spot in this library when ALL of the following are true:

1. It won a "stretch candidate vs. library" head-to-head on a real post (Jacob picked it over the library options).
2. It is structurally distinct from existing patterns — different visual logic, different narrative role. Color tweaks and minor layout variants do not qualify.
3. It carries full Schema.org structured data and brand-consistent styling.
4. The shipping post is referenced as the lift-from example.

When all four are true, the writer adds a new entry below using the same shape as the existing patterns. Mention the addition in the delivery message so the next session sees it.

---

## Brand color reference (used by every pattern)

- **Navy** `#002a3a` — primary, headers, text on light backgrounds, key bars
- **Green accent** `#4a7c59` — labels, sub-headings, borders for positive rows
- **Light blue-gray bg** `#f4f7f9` — snippet block, alternating cards
- **Light green bg** `#f0f4f0` — Key Takeaways, tier chips
- **Border gray** `#d6e0e6` — card borders, dividers
- **Body text** `#333` — main copy
- **Secondary text** `#555` — captions, sources, secondary labels

---

# The Seven Patterns

## 1. `comparison-table`

**Use when the compelling question is:** *"How does [Entity A] compare to [Entity B / B / C] across multiple dimensions?"*

**Narrative type:** Apples-to-apples data comparison. Best when there are 3+ entities × 4+ metrics and the value is in scanning the matrix. Worst when the post hangs on one insight that gets buried in cells.

**Raw data shape:** N rows × M columns of dimensional data. Each row is a place, time period, option, or property. Each column is a metric. Values can be currency, days, counts, ratios, or short descriptive phrases.

**Brand styling:**
- `<figure class="aeo-comp-table">` wrapper (CSS class lives in `/css/aeo-visuals.css`)
- `<caption>` names the dataset, date range, and source
- `<thead>` and scoped `<th>` for accessibility
- `<figcaption>` defines any domain terms (DOM, CP/OLP, etc.) and cites the source
- Mobile responsive — table flips to stacked card layout below 700px

**Schema.org payload:**
- `<figure itemscope itemtype="https://schema.org/Dataset">` wrapper
- `<meta>` props: name, temporalCoverage, spatialCoverage, variableMeasured, creator, publisher
- Each row: `<tr itemscope itemtype="https://schema.org/PropertyValue">` with row-level `name`
- Each cell: machine-readable value via `<meta itemprop="value">` or scoped span

**Lift from:** `src/content/blog/spring-2026-move-up-market-report-south-denver.md` — the canonical reference. Q1 2026 data across Highlands Ranch, Parker, Castle Pines × 4 metrics with full Dataset Schema.

**When NOT to use:** posts that hang on one insight, fork narratives (use `two-path-diptych`), or single-metric comparisons (use `single-metric-bar-chart`).

---

## 2. `two-path-diptych`

**Use when the compelling question is:** *"Which path / option fits my situation?"* — and the post's answer is a fork between two distinct choices, not a ranking on a continuum.

**Narrative type:** Decision-tree visualization. The reader has a budget / timeline / constraint and the post identifies that there are two legitimate paths within it. Each path has its own price band, attributes, and trade-off. The visual makes the choice obvious in 5 seconds.

**Raw data shape:** A shared constraint (budget, timeline, neighborhood) at the top. Two paths below, each with: price/range, key dimension (sqft, DOM, etc.), best-fit context (ZIPs, builder type, etc.), build era / vintage, and a labeled trade-off paragraph.

**Brand styling:**
- Navy header banner with shared constraint and SVG icon
- 2-column card grid below (auto-fit `minmax(280px, 1fr)` for mobile reflow)
- Left card: `#f4f7f9` background. Right card: white background. Subtle vertical divider between.
- Each card: 40×40 SVG icon, "Path 1 / Path 2" eyebrow label, headline, 2×2 attribute grid, labeled trade-off section
- Source attribution below

**Schema.org payload:**
- Outer `<div itemscope itemtype="https://schema.org/Dataset">` for the whole comparison
- Each path: `<div itemscope itemtype="https://schema.org/PropertyValue">` with name + machine-readable value range
- All key labels are real text (not images) for AI engine parseability

**Lift from:** `src/content/blog/first-time-home-buyer-guide-lakewood-colorado-2026.md` — `<h2 id="price-tiers">` section. Single-family path vs. condo/townhome path at $400–550K Lakewood budget.

**When NOT to use:** if the post has 3+ legitimate paths (use `profile-card-grid`), if the paths aren't actually distinct (use `comparison-table`), or if there's a ranking among them (use `single-metric-bar-chart`).

---

## 3. `profile-card-grid`

**Use when the compelling question is:** *"Which [entity / persona / place / option] is the best fit for me?"* — and the answer is "depends on you, here's how to self-select."

**Narrative type:** Entity enumeration. Each card is a self-contained profile with enough attributes to support self-selection but few enough to scan in one pass.

**Raw data shape:** N entities (typically 3–8), each with: name/headline, sub-label (location, role, era), 1 highlight attribute (price chip, key stat), 1–2 sentence description, and a "Best for ___" tagline that names the buyer / seller / persona type.

**Brand styling:**
- CSS Grid `repeat(auto-fit, minmax(220px, 1fr))` — 3-up desktop, 2-up tablet, 1-up mobile
- Each card: white background, navy top border (4px), light gray side/bottom border, 8px radius, ~1.25rem padding
- Top row: hand-crafted SVG icon (24–32px) + headline (1.5rem, navy, bold)
- Sub-label: uppercase 0.75rem, green accent
- Tier/highlight chip: `#f0f4f0` background, dark green text, rounded pill
- Body: 0.9rem, body gray
- "Best for:" footer: 0.8rem italic, navy strong

**Schema.org payload:**
- Outer `<div itemscope itemtype="https://schema.org/ItemList">` with `numberOfItems` meta
- Each card: `<div itemscope itemtype="https://schema.org/Place">` (or Person, Product, depending on entity type) with `itemprop="itemListElement"`
- Highlight chip: nested `PropertyValue` with name and value
- Hand-crafted SVG icons (no Font Awesome) for each entity type — store the icon source in this file when a new icon is created

**Lift from:** `src/content/blog/greenwood-village-worth-the-price-tag-relocation-2026.md` — 5-card persona grid with hand-crafted SVG icons for each persona, ItemList JSON-LD, Person Microdata per card, Place Microdata for matched suburbs.

**When NOT to use:** if there are exactly 2 entities (use `two-path-diptych`), if the comparison is along a single ranked metric (use `single-metric-bar-chart`), or if the post needs deep dimensional comparison (use `comparison-table`).

---

## 4. `price-ladder-svg`

**Use when the compelling question is:** *"What does $X actually buy at each tier?"* — and the post's narrative depends on visualizing scale (more dollars = more X).

**Narrative type:** Tiered progression with scale. The reader has a price-band question and the post answers by showing what each band gets you, with bar widths scaled to the dimension that matters (square footage, lot size, finish quality measured by attribute count).

**Raw data shape:** 3–5 price tiers, each with: band label, a scaling dimension (typical sqft, lot size, etc.) that drives bar width, a 1-line description of what's in the tier, and ZIP / location concentration.

**Brand styling:**
- Single inline SVG (viewBox 800×460) — keeps as one continuous block (no blank lines per Astro markdown rules)
- Title at top: 18px navy bold
- Subtitle below: 13px gray
- 4 horizontal rows starting at y=90, spaced 70px apart
- Each row: tier chip on left (navy background, 140×44, rounded), bar in middle (width scales with the dimension), home-type label and ZIP context inside/right of bar
- Bar colors graduate light-to-dark with tier: `#d6e0e6` → `#99adb8` → `#4a6a78` → `#002a3a`
- Bottom: divider line, headline summary stat, term definitions, source attribution baked into the SVG

**Schema.org payload:**
- `<figure itemscope itemtype="https://schema.org/Dataset">` wrapper around the SVG
- `<svg role="img">` with `<title>` (1-sentence summary) and `<desc>` (3–4 citable sentences with all key stats — this is what AI engines quote as alt text)
- Source baked into SVG as `<text>` element so it travels if scraped as image

**Lift from:** Reference SVG retained in commit `1dd3d0a` (now stripped from the live Lakewood post but preserved in git history). When ready to ship, lift the SVG block and adapt the data points.

**When NOT to use:** if there are only 2 tiers (use `two-path-diptych`), if the scaling dimension isn't visually meaningful (use `comparison-table`), or if the tiers don't progress monotonically (use `profile-card-grid`).

---

## 5. `single-metric-bar-chart`

**Use when the compelling question is:** *"How does [city / option] compare on [one specific metric]?"* — when there is exactly one number that drives the post's argument.

**Narrative type:** Single-dimensional comparison across 3–5 entities. The chart's job is to make the gap obvious.

**Raw data shape:** 3–5 labeled rows, each with: entity name, single numeric value, optional sample size (`n=X`).

**Brand styling:**
- Inline SVG (viewBox 700×320 typical)
- Horizontal bar chart with bars sorted longest-to-shortest or by narrative argument
- Labels on the left of each bar (entity name, e.g. "Castle Pines, Colorado")
- Value labels at the right end of each bar (e.g., "77 days")
- Bar color: navy `#002a3a` for the highlighted/argued entity, mid-gray `#99adb8` for comparison entities
- Title at top names the entity AND the metric in plain language
- `<desc>` block in the SVG states all values as a citable sentence

**Schema.org payload:**
- `<figure itemscope itemtype="https://schema.org/Dataset">` wrapper
- `<title>` and `<desc>` inside SVG with full state qualifier ("Castle Pines, Colorado not Castle Pines")
- Optional parallel JSON-LD `<script type="application/ld+json">` Dataset block with the same numbers in machine-readable form
- Source attribution baked into the SVG bottom

**Lift from:** `src/content/blog/move-up-timing-castle-pines-2026.md` — first svg-chart on the site. Castle Pines 77 days vs. Parker 62 days vs. Highlands Ranch 52 days median DOM until sale, Feb 2026. SVG title + desc + in-SVG term definition + source text + parallel JSON-LD Dataset.

**When NOT to use:** if comparing on 2+ metrics (use `comparison-table`), if the data is tier-progressed (use `price-ladder-svg`), or if the entities have qualitative attributes that matter as much as the number (use `profile-card-grid`).

---

## 6. `decision-path`

**Use when the compelling question is:** *"How do I decide between [Path A] and [Path B]?"* — when the post answers a binary fork by routing the reader through 3–5 prioritized questions, each with answer pills that point to one path or the other.

**Narrative type:** Procedural decision routing. The reader has a real choice to make and the post identifies the 3–5 questions that actually drive that choice. Each question carries 2 (sometimes 3) answer pills that route to a named path. Best when the path-fit hinges on a small number of priority weights, not on dimensional comparison or square-footage scaling. Worst when the paths can be mapped on a clean continuum (use `single-metric-bar-chart` or `comparison-table` instead).

**Raw data shape:** 3–5 numbered question rows. Each row: a question (1 sentence, framed in second person), 2–3 answer pills with strong/qualifier text and a routing arrow to the named path. Plus a Decision Rule footer explaining how to read the tally (e.g., "3+ answers pointing to Path A → start there. Mixed answers → tour both.").

**Brand styling:**
- Question-led navy banner: location eyebrow (0.7rem uppercase, opacity 0.75) → question headline (1.6rem white bold, line-height 1.2) → answer-shape subhead (0.95rem opacity 0.9, max-width 540px)
- White-bg card stack with thin gray border (`#d6e0e6`)
- Each row: 32px navy numbered circle (left) + question text (top of right column) + answer-pill row (below)
- Pill colors carry routing weight:
  - Green-bordered pill (`#4a7c59` border on `#f0f4f0` bg) → routes to Path A (the green-coded path)
  - Navy-bordered pill (`#002a3a` border on `#f4f7f9` bg) → routes to Path B (the navy-coded path)
  - Gray pill (`#d6e0e6` border on `#f9fafb` bg) → "either path open" / neutral
- Decision Rule footer: light green (`#f0f4f0`) bg with green eyebrow label, navy body
- Source footer: light gray (`#f9fafb`) bg, flat top border touching the rule footer, gets bottom border-radius — bound flush, no margin gap, structurally inside the wrapper for `isBasedOn` propagation
- Mobile responsive: question rows reflow with `flex-wrap: wrap`; pill row wraps below question on narrow viewports

**Schema.org payload:**
- Outer `<div itemscope itemtype="https://schema.org/HowTo">` with `name`, `description`, `totalTime` (`PT5M` typical for a 4-question path)
- Each question row: `<div itemscope itemtype="https://schema.org/HowToStep" itemprop="step">` with `position` and `name` (the question text)
- Each answer pill: `itemprop="itemListElement"` for AI-engine parseability of the routing options
- Source attribution as bound footer inside the HowTo wrapper

**Lift from:** `src/content/blog/ridgegate-vs-heritage-hills-lone-tree-new-construction-2026.md` — first decision-path on the site. 4-question routing (new vs. established / light-rail commute / gated preference / budget ceiling) with green-vs-navy pill routing to RidgeGate vs. Heritage Hills, Decision Rule tally footer, bound source. Won a stretch-vs-library head-to-head against `two-path-diptych` (corrected hero) on 2026-05-06. Promoted to the library on 2026-05-06.

**When NOT to use:** if the choice is dimensional with multiple metrics that all matter (use `comparison-table`); if the paths split cleanly on price-band trade-offs alone (use `two-path-diptych`); if the data is single-metric (use `single-metric-bar-chart`); if the question is "what does it cost?" (use `settlement-statement`).

---

## 7. `settlement-statement`

**Use when the compelling question is:** *"What does [a transaction] actually cost, line by line?"* — when the post is a financial breakdown and the reader needs to see categories and a total.

**Narrative type:** Categorical financial breakdown. The visual mimics a familiar document (settlement statement, net sheet, closing disclosure) so the reader recognizes the format immediately.

**Raw data shape:** 4–6 categories (Down Payment, Lender Fees, Title Fees, Prepaid Items, Other Costs, etc.), each with 2–5 line items, each line with a label and a dollar range or value. Plus a total row at the bottom.

**Brand styling:**
- Brand navy `#002a3a` header strip across the top with title and date
- Category section headers: light navy `#1f4254` background, white text, uppercase
- Line items: white background, alternating very light gray for readability, 0.95rem text
- Right-aligned dollar amounts in monospace or tabular numerals
- Sub-items indented under category parents
- Total row: navy background with white text, larger font, bold

**Schema.org payload:**
- `<table itemscope itemtype="https://schema.org/Table">` (or wrapped in `<figure itemscope itemtype="https://schema.org/Dataset">` if it's a generalized example with named source)
- Each category section: `<tr>` with `role="rowheader"`
- Each line item: `<tr itemscope itemtype="https://schema.org/PropertyValue">` with name and value/amount
- Source attribution in `<figcaption>`

**Lift from:** `src/content/blog/closing-costs-littleton-first-time-buyers-2026.md` — Down Payment, Lender Fees, Title Fees, Prepaid Items (with sub-items), Other Costs (with sub-items), navy total row $32,000–$43,900.

**When NOT to use:** if it's not financial (obvious — use any other pattern), if the categories don't add to a meaningful total (use `comparison-table`), or if the post is comparing two cost scenarios (use `two-path-diptych`).

---

# Pattern Selection Cheat Sheet

A quick lookup for the writer's brainstorming step:

| Compelling question shape | Recommended pattern |
|---|---|
| "How do A and B compare on multiple dimensions?" (3+ entities × 4+ metrics) | `comparison-table` |
| "Which of two paths fits me?" (binary fork) | `two-path-diptych` |
| "Which entity / persona / place is right for me?" (3–8 self-select options) | `profile-card-grid` |
| "What does $X buy at each tier?" (tiered progression with scale) | `price-ladder-svg` |
| "How does X compare on this one metric?" (single number across 3–5 entities) | `single-metric-bar-chart` |
| "How do I decide between Path A and Path B?" (3–5 priority-routing questions) | `decision-path` |
| "What does a transaction actually cost?" (financial line-by-line breakdown) | `settlement-statement` |
| None of the above is a strong fit | **Library Gap trigger — prototype 2–3 stretch candidates** |

---

# Stretch Candidate Examples (not yet in library — use as inspiration only)

These are visual concepts that have been brainstormed but have not yet won a real-post head-to-head against the library. They live here for inspiration when prototyping new stretch candidates. Promotion to the library above requires winning a real post per the protocol.

- **Timeline / process flow** — for "how does [process] unfold over time?" (listing-to-close, relist workflow). Not yet shipped.
- **Tier list** — for "which [option] is in which severity / quality tier?" (price reductions, listing problems). Was Phase 3 deferred; not yet shipped on a real post.
- **Map-like ZIP grid with location icons** — was Option A on the Lakewood FTHB post, lost to two-path-diptych. Held as a stretch candidate for relocation posts where ZIP enumeration IS the point.

---

# Maintenance

- This file lives at `~/selling303-site/docs/visual-patterns.md`.
- The blog-post-writer skill reads it during Stage 1 visual brainstorming.
- The aeo-visual-builder skill references the lift-from posts to assemble new visuals.
- New pattern promotions are added at the top of the relevant section with the new lift-from post and a delivery-message note.
- Audited monthly during seo-aeo-expert weekly audits; flagged for refresh if a pattern's lift-from post gets restructured.
