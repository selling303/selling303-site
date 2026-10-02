# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-09-30 production deploy — merge fd57268, see DEPLOY_LOG.md.)_
- 2026-10-02 — New pillar `/what-to-fix-before-selling` (three-layer walkthrough, Next-Rung method + ladder visual, Jacob's cost table, Mountain-region Cost vs. Value table, snowball trap, big systems w/ C.R.S. 6-22-105 note, staging section w/ NAR 2025 stats, 3 success-story cards, 6-Q FAQ + HowTo schema, cited sources). `src/data/cluster.ts` fixOrSkipUrl now → /what-to-fix-before-selling (hub, buy-first, renovate pages all link to it). New `.oyh-*` styles in both stylesheets.

- 2026-10-02 — Success stories: added Google reviews — Dee (2993 S Jericho Ct) and Daniel K. (21069 Woodside Ln); added "fresh interior paint" to Jericho strategy (per Jacob). Fix-or-skip page: Jericho added as lead story card; review quotes on Jericho + Parker cards.
- 2026-10-02 — Before/after: Jacob's Jericho Ct before photos saved to `src/assets/images/before-after/` (kept out of the success-story folder so they don't auto-load into that listing gallery). New `src/components/BeforeAfter.astro`; two pairs (living room, primary bedroom) on /what-to-fix-before-selling Results section.
- 2026-10-02 — Fix-or-skip page: Jericho living-room before/after moved to the top (under the short answer); buy-first Aurora story card added (18302 E Hampden Pl, no public story page yet); Charli's before photos saved to Website Build/before-after-photos/18302-e-hampden-pl-aurora/ awaiting matching listing photos.
- 2026-10-02 — Fix-or-skip page: top hero now Hampden family room before/after (painted brick fireplace + staging); Results adds Hampden bedroom pair, keeps both Jericho pairs. Before crops in src/assets/images/before-after/hampden-*.jpg; afters from success-stories/18302-e-hampden-pl-aurora (#18, #32). NOTE: that folder has no success-story .md yet — fine (images only).
- 2026-10-02 — Fix-or-skip page: "What we skipped" callout (popcorn ceilings + hall bath) under Hampden bedroom pair; Hampden story card notes skips (confirmed by Jacob).
