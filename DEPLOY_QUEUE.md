# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-09 production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-05-10 (nightly blog task — Day 7 May calendar):** New blog post — "Condo vs. Starter House in Littleton for First-Time Buyers" (`condo-vs-single-family-littleton-first-time-buyer-2026.md`). First-Time Homebuyers × Littleton. MOFU. Tier 0 **comparison-table** visual: 2 first-time-buyer cohorts × 6 metrics — Littleton condo / townhome under $600K (n=53, $380K median, 24-day median DIM, 97% CP/OLP, 1,198 median sqft, $317 $/sqft) vs. starter SFR $500K–$700K (n=92, $601,250 median, 14-day median DIM, 99% CP/OLP, 2,063 median sqft, $291 $/sqft). Source: REcolorado MLS April 2026 closed residential transactions for Littleton, Colorado (n=292 total closed; full-segment context: condo/attached n=57 at $382,500 median, SFR n=235 at $710,000 median). Caption reads as the compelling question ("How does a $400K Littleton condo stack up against a $600K starter SFR?"); source row bound inside figcaption; per-row PropertyValue Microdata + parallel JSON-LD Dataset block. Title shortened from "Condo vs. Single-Family Residence in Littleton's Spring Market: Which Makes Sense for First-Time Buyers?" (97 chars) to "Condo vs. Starter House in Littleton for First-Time Buyers" (58 chars) for SERP CTR; original preserved in `headline` frontmatter. Compelling Question Flow chose comparison-table (23) over two-path-diptych (22) and a stretch equity-curve mini-chart (18) because the FTB's job is scanning ≥6 dimensions where each reshuffles the decision, not picking a binary fork. Updates: `content-calendar-2026.md`, `content-cluster-map.md`, `visual-inventory.md`.
