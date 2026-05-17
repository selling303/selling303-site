# Visual Patterns Library — selling303.com

The single source of truth for visuals on selling303.com blog posts, pillar pages, and neighborhood pages. The blog-post-writer and aeo-visual-builder skills both reference this file when selecting a pattern at draft time.

---

## The Tier System (READ THIS FIRST)

Visuals come in three interaction tiers. **Pick the tier first, then the pattern within that tier.** Tier selection comes from the post's funnel stage, narrative shape, and whether the value is computable from reader inputs.

### Tier 0 — Static

Schema-bound HTML, no animation, no JS state. The seven shipped patterns below all live here. Cheap, fast, AEO-baseline. The default for TOFU and most MOFU.

**Use when:** the visual's job is to display a fixed truth (a comparison, a tier breakdown, a fact map). The reader looks at it and learns something.

### Tier 1 — Animated / Responsive

Static structure plus CSS transitions, scroll-triggered reveals, hover states, smooth color transitions. No JS state — same content for every reader, just rendered with more life. Adds visual sophistication without the cost of full interactivity.

**Use when:** the visual benefits from a reveal moment (numbers counting up on scroll, a chart filling left-to-right as the reader enters viewport, hover tooltips on data points). Most MOFU posts where engagement matters but personalization doesn't.

**Library entries:** TBD. As Tier 1 patterns ship, document them here with the same shape as Tier 0.

### Tier 2 — Interactive Widget

Full state, user inputs, computed outputs. Reusable component or scoped inline JS. The widget is the value — the reader brings inputs, the visual computes a personalized answer.

**Use when:** the post's compelling question is computable from reader-supplied inputs. BOFU calculators, decision tools, lookup widgets. The reader uses the visual to make a real decision.

**Library entries:**
- **`interactive-calculator`** — lift-from `src/content/blog/2026-notice-of-valuation-protest-playbook-south-denver.md`. Gap Calculator: county selector + 2 currency inputs + live gap-percent readout + 3 path cards that highlight on recommendation + live JS countdown. Vanilla JS inline, no framework. Static SSR'd fallback shows all 3 paths fully visible without JS. Schema: outer Dataset + ItemList + 3× RecommendAction + JSON-LD Dataset block. Mobile responsive with input-grid stacking at <600px. AEO-positive — engagement signals plus "useful tool" quality signal, never compromising static-fallback content.

### How to pick a tier

| Post type | Default tier | Upgrade trigger |
|---|---|---|
| TOFU educational | Tier 0 | Almost never upgrades |
| MOFU comparison | Tier 0 or 1 | Tier 1 when scroll-triggered reveal amplifies the contrast |
| BOFU decision tool | Tier 2 | Default — when the reader has inputs to provide |
| BOFU case study | Tier 0 | Static prose visual; almost never Tier 2 |
| Market update / data | Tier 0 + chart | Tier 1 if chart benefits from animation |

State the chosen tier explicitly before brainstorming candidates. Brainstorm 3 within the chosen tier (≥2 library + ≥1 stretch).

### AEO doesn't suffer from interactivity (when done right)

Tier 2 widgets are AEO-positive when designed correctly:
- **Schema lives in the SSR'd HTML.** Never JS-injected. Crawlers see the full content regardless of JS execution.
- **Static fallback is complete.** All 3 path cards visible by default; the JS layer just highlights/dims based on inputs.
- **Engagement signals.** Time-on-page, scroll depth, interaction rate — all Google ranking factors that Tier 2 widgets generate naturally.
- **"Useful tool" quality signal.** AI engines reward content that demonstrates utility.

The bar: the static HTML must contain the full answer the AI engine would quote. The widget makes that answer feel alive, doesn't replace it.

---

## How to use this file

The writer arrives here AFTER answering the post's compelling question and one-sentence answer AND picking the tier. At that point, scan the chosen tier's library for the pattern that best pays off the question. Brainstorm 2 from library + 1 stretch within the chosen tier. Score all three. Ship the winner.

If the stretch candidate wins, the delivery message flags it for library promotion and the new pattern gets added here on the next push. That's how the library grows — every post is potentially a library-growth moment, but only when the stretch genuinely outperforms.

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
- **Gold accent** `#c8965a` — answer pointers, "look here" callouts inside dark headers
- **Green accent** `#4a7c59` — labels, sub-headings, borders for positive rows
- **Light blue-gray bg** `#f4f7f9` — snippet block, alternating cards
- **Light green bg** `#f0f4f0` — Key Takeaways, tier chips
- **Border gray** `#d6e0e6` — card borders, dividers
- **Body text** `#333` — main copy
- **Secondary text** `#555` — captions, sources, secondary labels

---

## Visual Hero Rule (applies to every pattern)

**Every visual's hero element must lead with the compelling question the visual is answering — not a context label, not a category eyebrow, not a budget banner.** The hero is the question. The body of the visual is the answer.

This applies regardless of pattern:

- **`comparison-table`** — `<caption>` reads as the compelling question (or a tight paraphrase). Not "Q1 2026 South Denver Comparison." Yes "How do Highlands Ranch, Parker, and Castle Pines compare on Q1 2026 move-up data?"
- **`two-path-diptych`** — navy header banner is the question, prominent, large type. Below it, a 1-line gold-accent answer-pointer ("Two paths fit ↓" / "The right one depends on ___ ↓"). The eyebrow label, if any, only adds audience context ("FOR FIRST-TIME BUYERS").
- **`profile-card-grid`** — the H3 above the grid IS the question; no banner needed. If a banner is added, it must be the question.
- **`price-ladder-svg`** — SVG `<title>` element AND the visible chart title both read as the question ("What does $X buy at each Lakewood price tier?").
- **`single-metric-bar-chart`** — SVG `<title>` AND visible chart title both read as the question, naming the qualified entity AND the metric.
- **`decision-path`** — root node IS the question. Branches are the answers.
- **`settlement-statement`** — navy header strip is the question ("What does closing day actually cost on a $475K Littleton FHA purchase?"). Date and source go in a sub-strip below.

**The 5-second test:** a reader who sees only the hero of the visual should know exactly what question it answers. If they have to scan the body to figure out what the visual is FOR, the hero failed and the visual is wrong.

**Why:** AI engines look for question-shaped hooks in image alt text, captions, and SVG titles when ranking visuals as direct-answer surfaces. Question-led heroes also outperform on CTR for SERP image carousels and for scroll-pause behavior on the page itself. Both audiences (human and AI) reward the question.

---

## Source Placement Rule (applies to every pattern)

**Source attribution must live both structurally inside the Schema.org wrapper AND visually bound to the visual block — never as a floating paragraph below.** The visual is the unit; the source is part of the unit, not a footnote that follows it.

Two failure modes this rule prevents:

1. **Structural drift.** Source `<p>` lives OUTSIDE the `<div itemscope itemtype="https://schema.org/Dataset">` wrapper. Schema.org parsers bind props by DOM ancestry — a citation outside the wrapper is unbound, and Rich Results Test reports the citation as floating context rather than as part of the dataset. AEO concern: the source doesn't propagate to the dataset's `isBasedOn` / `citation` / `sourceOrganization` semantics.

2. **Visual detachment.** Source `<p>` sits below the visual block with margin-gap separating them. Reads as a footnote. Worse — when the visual gets scraped as an image (Google Images, AI engine, social share), the source line doesn't travel with the bitmap. The image circulates without provenance. AEO concern: source authority signal lost on image-scraped surfaces.

**Best-practice combination — applies to every pattern:**

1. **Source row lives INSIDE the Schema.org itemscope wrapper.** No exception. The wrapper opens at the top of the visual block and closes after the source row, not before it.
2. **Visually bound to the visual block.** No `margin-top` gap. Light gray (`#f8f9fa`) or white background, flat top border (`border-top: 1px solid #d6e0e6`), bottom border-radius matching the visual's outer radius. Reads as the footer-of-the-visual, not a paragraph that happens to be below.
3. **For SVG-based patterns** (`price-ladder-svg`, `single-metric-bar-chart`), source ALSO baked into the SVG itself as a `<text>` element near the bottom — so when the SVG is rasterized and shared as an image, the source travels with the pixels.
4. **Source string format:** `Source: [data source] | [scope] | [date range] | [sample size] | selling303.com`. Inline `<strong>` on "Source:" for visual emphasis. Date range is always spelled out ("April 1–30, 2026" not "April 2026").

**Per-pattern source-row requirements:**

- **`comparison-table`** — source goes in the `<figcaption>`, which is structurally inside the `<figure>` wrapper. Visually bound by the `<figcaption>` styling — no extra paragraph below the figure.
- **`two-path-diptych`** — source row added immediately after the 2-column card grid, INSIDE the outer wrapper. Card grid loses its bottom border-radius; source row gets it. Light gray background, flat top border, no margin.
- **`profile-card-grid`** — source row added below the persona grid, INSIDE the `<figure>` wrapper, styled as a bound footer of the figure.
- **`price-ladder-svg`** — source baked into SVG `<text>` AND in `<figcaption>` outside the SVG. Both inside the `<figure>` wrapper.
- **`single-metric-bar-chart`** — same as price-ladder-svg.
- **`decision-path`** — source row at the bottom of the path block, INSIDE the wrapper, bound styling.
- **`settlement-statement`** — source goes in the navy/sub-strip footer of the statement block, INSIDE the wrapper.

**Verification check:** before shipping any visual, confirm by inspecting the rendered DOM that the source `<p>` (or `<text>` for SVG) is a child of the `itemscope` wrapper. If it's a sibling that follows the wrapper, the binding is broken.

---

# The Nine Patterns

## 1. `trade-off-frontier`

**Use when the compelling question is:** *"Can I have both [X] and [Y], or do I have to pick one?"* — when the post's answer is a fundamental trade-off between two variables that the reader instinctively wants to maximize together but cannot.

**Narrative type:** Two-dimensional positioning. Two real options exist as zones in a 2D space defined by the two axes. A third "ideal corner" (max-X and max-Y) does NOT exist as a real option, and the visual makes that explicit by labeling the empty quadrant. The frontier between the two real zones is the constraint the reader is actually facing.

**Raw data shape:** Two named options (e.g., Path A and Path B), each with: a value on Axis X (time, cost, size, etc.), a value on Axis Y (control, customization, certainty, etc.), a headline stat (typically total cost or total time), and a 1-line trade-off summary. Plus annotation for the empty "impossible" quadrant.

**Brand styling:**
- Navy header strip across the top with the post's compelling question as the hero headline (1.2rem+ bold) and a gold-accent answer-pointer underneath stating the impossibility ("You cannot do both" / "Pick a corner" / etc.)
- Plot area below the hero, light blue-gray background (`#f4f7f9`)
- 2-axis scaffold: navy axis lines, gray dashed gridlines, qualitative or quantitative tick labels on both axes
- Axis titles in navy uppercase with arrows showing direction of increase
- **The empty quadrant — this is where the visual earns its keep.** A dashed gray rounded rectangle sized to occupy the visual location where the "ideal but impossible" combination would sit, labeled with "DOESN'T EXIST" (bold gray) plus a 1-line explanation
- **Zone A (Path A)**: rounded rectangle, navy 2.5px stroke, navy fill at 8% opacity, positioned at the data location. Contains a small uppercase label, large dollar tag (1.4rem+ bold), a one-line cost-anchor descriptor, and a one-line trade-off summary
- **Zone B (Path B)**: same shape, green 2.5px stroke, green fill at 10% opacity, positioned in the opposite quadrant
- **Frontier line**: dashed gold curve connecting the two zones, with a small italic label ("the trade-off you actually have") above the curve mid-arc
- Optional subtle annotation in the unused empty quadrant (e.g., "stalled inventory sits here") in small gray italic
- Source row baked into the SVG at the bottom + bound figcaption source row outside the SVG inside the figure wrapper

**Schema.org payload:**
- `<figure itemscope itemtype="https://schema.org/Dataset">` wrapper
- `<meta>` props: name, temporalCoverage, spatialCoverage
- Each zone: hidden `<div itemprop="hasPart" itemscope itemtype="https://schema.org/PropertyValue">` with name, value, minValue, maxValue, unitText, and description (carrying the trade-off attributes)
- Parallel JSON-LD Dataset block in `<script type="application/ld+json">` with full variableMeasured array — the two axes plus the total cost dimension
- `<title>` and `<desc>` inside SVG with the full insight in citable sentence form (this is what AI engines quote as alt text — write it as a complete narrative paragraph)
- Source attribution baked into SVG as `<text>` element so it travels if scraped as an image

**Lift from:** `src/content/blog/spec-home-vs-custom-build-parker-2026.md` — first trade-off-frontier on the site. Spec Home zone (lower-left: 30–90 days, few decisions, $850K–$925K) vs. Custom Build zone (upper-right: 12–18 months, hundreds of decisions, $1.1M–$1.4M+). Empty upper-left labeled "DOESN'T EXIST — There is no fast custom build." Dashed gold frontier curve connecting the two zones. Won a stretch-vs-library head-to-head on 2026-05-16 after Jacob explicitly rejected `comparison-table` (the initial pick that failed the Visual Dignity Gate on review) and `two-path-diptych` (proposed alternative) as "forcing a square peg into a round hole" — then named the axes idea (time vs. design choices) himself.

**When NOT to use:** if the trade-off isn't a real constraint (i.e., the "ideal corner" actually IS achievable — use `two-path-diptych` instead); if the two options exist on a single continuum rather than in different quadrants (use `single-metric-bar-chart`); if the comparison has 3+ dimensions that all matter (use `comparison-table`); if there are 3+ legitimate paths positioned across the space rather than a binary fork (use `profile-card-grid`).

---

## 2. `comparison-table`

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

## 3. `two-path-diptych`

**Use when the compelling question is:** *"Which path / option fits my situation?"* — and the post's answer is a fork between two distinct choices, not a ranking on a continuum.

**Narrative type:** Decision-tree visualization. The reader has a budget / timeline / constraint and the post identifies that there are two legitimate paths within it. Each path has its own price band, attributes, and trade-off. The visual makes the choice obvious in 5 seconds.

**Raw data shape:** A shared constraint (budget, timeline, neighborhood) at the top. Two paths below, each with: price/range, key dimension (sqft, DOM, etc.), best-fit context (ZIPs, builder type, etc.), build era / vintage, and a labeled trade-off paragraph.

**Brand styling:**
- **Navy header banner leads with the post's compelling question, not a context label.** Question is large (1.5rem+), bold, white-on-navy. Optional small uppercase eyebrow above for audience context (e.g., "FOR FIRST-TIME BUYERS"). Below the question, a 1-line gold-accent (`#c8965a`) answer-pointer with a downward arrow ("Two paths fit. Pick your trade-off ↓"). NO wallet/budget icons, NO generic banner copy. The question is the visual identity. See Visual Hero Rule above.
- 2-column card grid below (auto-fit `minmax(280px, 1fr)` for mobile reflow). Card grid has no bottom border-radius — the source row gets it.
- Left card: `#f4f7f9` background. Right card: white background. Subtle vertical divider between.
- Each card: 40×40 SVG icon, "Path 1 / Path 2" eyebrow label, headline, 2×2 attribute grid, labeled trade-off section
- **Source row bound to the card grid** (no margin gap) per the Source Placement Rule — light gray (`#f8f9fa`) background, flat top border, bottom border-radius (`0 0 8px 8px`) matching the original card-grid radius, INSIDE the outer Schema.org wrapper. Format: `<strong>Source:</strong> ...` per the standard source string format.

**Schema.org payload:**
- Outer `<div itemscope itemtype="https://schema.org/Dataset">` for the whole comparison
- Each path: `<div itemscope itemtype="https://schema.org/PropertyValue">` with name + machine-readable value range
- All key labels are real text (not images) for AI engine parseability

**Lift from:** `src/content/blog/first-time-home-buyer-guide-lakewood-colorado-2026.md` — `<h2 id="price-tiers">` section. Question-led navy banner ("What does $400K–$550K actually buy in Lakewood, Colorado?"), single-family path vs. condo/townhome path below.

**When NOT to use:** if the post has 3+ legitimate paths (use `profile-card-grid`), if the paths aren't actually distinct (use `comparison-table`), or if there's a ranking among them (use `single-metric-bar-chart`).

---

## 4. `profile-card-grid`

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

## 5. `price-ladder-svg`

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

**Lift from:** `src/content/blog/lone-tree-relocation-guide-dtc-tech-professionals-2026.md` — **first live shipment of `price-ladder-svg`** (2026-05-15). 4-tier ladder for Lone Tree, Colorado relocating tech professionals — Tier 1 $325K–$500K Park Meadows condos / Tier 2 $500K–$750K South Lone Tree townhomes / Tier 3 $750K–$1.2M RidgeGate move-up SFR / Tier 4 $1.2M+ RidgeGate / Heritage Hills luxury. Bar widths scale to median finished square footage at each tier (115→180→290→420px). Tier chips on the left carry a gold accent (`#c8965a`) on the price-band line per the brand color spec. Source `<text>` baked into the SVG at y=450 plus a bound `<figcaption>` outside the SVG (both inside the `<figure>` wrapper). Won Compelling Question Flow over `profile-card-grid` (tied at 24, tiebreaker on canonical fit + pattern freshness — 2 profile-card-grids shipped in the prior 8 days, 0 price-ladder-svg ships ever) and `comparison-table` (21). Reference SVG retained in commit `1dd3d0a` is now superseded — lift from this post instead.

**When NOT to use:** if there are only 2 tiers (use `two-path-diptych`), if the scaling dimension isn't visually meaningful (use `comparison-table`), or if the tiers don't progress monotonically (use `profile-card-grid`).

---

## 6. `single-metric-bar-chart`

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

## 7. `decision-path`

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

## 8. `stacked-cost-bar-comparison`

**Use when the compelling question is:** *"Where does the cost / financial gap between [Path A] and [Path B] actually live?"* — when the post compares two scenarios on a totaled financial metric AND the component breakdown is the punch line (which segment dominates, which segment shrinks the reader's intuition).

**Narrative type:** Vertical stacked-bar comparison. Two bars side by side. Total bar height carries the headline metric (monthly all-in, total deal cost, net-sheet bottom line). Stacked segments break the total into components. The altitude difference between bars makes the gap physically felt; the segment proportions bust intuition mistakes about which component drives the gap.

**Raw data shape:** Two scenarios. Each scenario has 3–5 component values (e.g., P&I, tax, insurance, HOA for a monthly carrying-cost compare; OR commission, concessions, title, prep, prorated tax for a net-sheet compare). Each scenario also carries a total and a 1–2-line identifier (price, down payment, scenario label).

**Brand styling:**
- Single inline SVG (viewBox 700×500 default; keep as one continuous block, no blank lines per Astro markdown rules)
- Visible title (17–20px navy bold) at top leads with the comparison name AND the gap number AND the qualified entity (Visual Hero Rule). Subtitle (12–13px gray) carries the assumption block plus entity qualifier so the bitmap travels self-contained when scraped by AI or image-search engines.
- Bar geometry: two bars, 140px wide, side by side with ~120px gap between. Scale chosen so the larger bar's total height is ~300–350px. Both bars baseline-aligned at the bottom.
- Segment colors (bottom-up, by financial weight): navy `#002a3a` for the dominant segment (P&I, mortgage, commission), mid-gray `#99adb8` for the secondary segment (taxes, concessions), light gray `#d6e0e6` for the tertiary segment (insurance, title), gold accent `#c8965a` for the differentiator segment (HOA, prep budget). The gold segment is the one whose size relative to expectation drives the visual surprise.
- Per-bar headline stat (`$X/mo` or `$Xk total`) in 22px navy bold floats above each bar's top, NOT inside the bar.
- Sub-label below each bar (city + scenario identifier in two 12–14px lines).
- Diagonal gold dashed line connects the two bar tops to a delta callout in the middle (`+$X/mo` in 14px gold bold inside a small white pill with gold border).
- Legend across the bottom (4 small rectangles + 11px labels) keyed to segment colors.
- Source baked into figcaption (NOT in SVG `<text>`, per Source Placement Rule) inside the same `<figure>` wrapper.

**Schema.org payload:**
- `<figure itemscope itemtype="https://schema.org/Dataset">` wrapper
- Parallel JSON-LD `Dataset` block BEFORE the figure with full metadata (temporalCoverage, spatialCoverage, isBasedOn, creator, publisher, variableMeasured for each scenario's total + the delta)
- SVG `<title>` and `<desc>` carry citable summary sentences with every key number (P&I, tax, insurance, HOA, totals, delta) so AI engines can quote them verbatim
- NO `<meta>` void elements inside the SVG (per rule 13b in aeo-visual-builder) — all per-segment Microdata lives in the parallel JSON-LD only

**Lift from:** `src/content/blog/condo-vs-single-family-littleton-first-time-buyer-2026.md` — first stacked-cost-bar-comparison on the site. Two Littleton, Colorado scenarios (condo $2,831/mo all-in vs. starter SFR $4,020/mo all-in) segmented by P&I, tax, insurance, HOA. The bars showed P&I as the dominant segment on both sides; the HOA segment on the condo bar is small relative to the mortgage stack — busting the "HOA fees are the deciding factor" myth most first-time buyers walk in with. Promoted to the library on 2026-05-10 after winning a stretch-vs-library A/B/C review against Variant B (5-year wealth projection) and Variant C (two-path-diptych).

**When NOT to use:** if the compelling question is "which path fits me?" (use `two-path-diptych` for the persona fork or `decision-path` for routing); if there's only one total to compare (use `single-metric-bar-chart`); if there are 3+ scenarios (use `comparison-table`); if the post hangs on a tiered progression rather than a binary financial compare (use `price-ladder-svg`).

---

## 9. `settlement-statement`

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
| "Can I have both X and Y, or do I have to pick one?" (binary trade-off with an "impossible" corner) | `trade-off-frontier` |
| "How do A and B compare on multiple dimensions?" (3+ entities × 4+ metrics) | `comparison-table` |
| "Which of two paths fits me?" (binary fork) | `two-path-diptych` |
| "Which entity / persona / place is right for me?" (3–8 self-select options) | `profile-card-grid` |
| "What does $X buy at each tier?" (tiered progression with scale) | `price-ladder-svg` |
| "How does X compare on this one metric?" (single number across 3–5 entities) | `single-metric-bar-chart` |
| "How do I decide between Path A and Path B?" (3–5 priority-routing questions) | `decision-path` |
| "Where does the financial gap between two scenarios actually live?" (two scenarios × component breakdown) | `stacked-cost-bar-comparison` |
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

- This file lives at `~/Documents/Claude/projects/selling303-site/docs/visual-patterns.md`.
- The blog-post-writer skill reads it during Stage 1 visual brainstorming.
- The aeo-visual-builder skill references the lift-from posts to assemble new visuals.
- New pattern promotions are added at the top of the relevant section with the new lift-from post and a delivery-message note.
- Audited monthly during seo-aeo-expert weekly audits; flagged for refresh if a pattern's lift-from post gets restructured.
