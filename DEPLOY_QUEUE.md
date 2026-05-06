# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-05 production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-05-05** — New blog post: "RidgeGate vs. Heritage Hills: A Lone Tree New Construction Update for 2026" (`src/content/blog/ridgegate-vs-heritage-hills-lone-tree-new-construction-2026.md`). Day 2 of May 5–June 3 calendar segment. New Construction pillar + Lone Tree geographic pillar. MOFU. Q1 2026 REcolorado MLS new construction export (Lone Tree, Year Built 2024+) — 17 listings, 5 closings at $1.176M median, 97% close-to-list, 77 days median DIM. April 2026 Lone Tree all-status MLS export for Heritage Hills active inventory and recent closings. Comparison-table visual (RidgeGate vs. Heritage Hills × 6 metrics) with full Schema.org Dataset + Place Microdata + per-cell PropertyValue. Honest reframe — Heritage Hills had zero new construction in Q1 2026, so the post positions the comparison as new construction (RidgeGate) vs. resale luxury (Heritage Hills) for the buyer cross-shopping both.
- **2026-05-05** — Updated `content-calendar-2026.md` — marked Day 2 (May 6) as drafted.
- **2026-05-05** — Updated `content-cluster-map.md` — added RidgeGate vs. Heritage Hills post to New Construction cluster.
- **2026-05-05** — Updated `visual-inventory.md` — logged the comparison-table visual as `optimized`, last verified 2026-05-06.

### 2026-05-05 — Visual System Overhaul

- **NEW: `docs/visual-patterns.md`** — Canonical visual pattern library. 6 shipped patterns (`comparison-table`, `two-path-diptych`, `profile-card-grid`, `price-ladder-svg`, `single-metric-bar-chart`, `settlement-statement`) with full template specs, brand color reference, Library Promotion Protocol, and pattern-selection cheat sheet. Source of truth for the writer's Compelling Question Flow. Read by `aeo-visual-builder` for construction templates and by `blog-post-writer` during Stage 1 visual brainstorming.
- **Skill updates saved at https://claude.ai/customize/skills** (managed in cloud, not in repo) — `aeo-visual-builder` (catalog rewrite + Visual Quality tier added to standard + Visual Dignity Gate first in verification), `content-calendar-planner` (replaces Visual Type Distribution with Narrative Job declaration; calendar no longer pre-specifies patterns), `blog-post-writer` (Visual Opportunity Check replaced with Compelling Question Flow + Stretch Candidate Rule + Library Gap Trigger + hard Visual Dignity Gate before delivery; Jacob Stark entity reinforcement guardrail and inline-external-link guardrail added).
- **Effect:** starting with the next nightly task run, every post produces a visual that pays off the post's compelling question in 5 seconds, brainstorms 3 candidates (≥2 from library + ≥1 stretch), scores them on narrative payoff + visual distinctiveness + schema density + mobile responsiveness, and ships the winner only if it passes the Dignity Gate. Library grows organically as stretch candidates win head-to-heads.
