# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

- 2026-09-30 — New `src/data/agent.ts`: single source of truth for brokerage name/URL/logo, license line, and trust stats. Refactored 17 files (Footer, AuthorBio, TrustSignals, index/about JSON-LD, all pillar trust bars, success stories, seller promise, blog index/[slug], contact, home-equity calculator) to read from it. Inline JSON-LD on 4 pages converted to `set:html` consts. Build verified (103 pages, all JSON-LD valid).
- 2026-09-30 — Trust stats updated to current Orchard-deck figures: $50M+ volume, 101.8% list-to-close (added avgDaysOnMarket 19 to config, not yet displayed).
- 2026-09-30 — `public/_redirects`: vanity `/outgrown` → `/move-up-sellers` (301).
- 2026-09-30 — Families helped 83 → 84 (config). TrustSignals fully config-driven. Relocation page: replaced inaccurate "83+ families relocating" line. Homepage/about aggregateRating wired to config.
- 2026-09-30 — Removed Who's Who in Luxury Real Estate (8z partnership) from homepage credential row, about-page badge, and both pages' JSON-LD (hasCredential + memberOf).
- 2026-09-30 — `/move-up-sellers` rewritten as the "Outgrown Your Home?" hub (Prepare → Sell & Buy → Move Once, monologue, blockers, options table, investor-eye section, "how I deliver this today" w/ Orchard disclosures, 6-Q FAQ + schema, related posts pulled from collection). Links to 4 Phase 2 pillar URLs not yet built — DO NOT ship until pillars exist.
- 2026-09-30 — New `src/components/VideoEmbed.astro` (click-to-load YouTube, VideoObject schema, renders nothing without an ID). Config gained `bookingUrls` and `brokerage.disclosures`.
- 2026-09-30 — Hub: Sell & Buy → Buy & Sell (buy-first default), options table reordered, "Realtor + Renovator" section header + proof bullets. Hub CSS moved to global stylesheet (`.oyh-*`); FAQ/TOC script extracted to `src/components/PillarScripts.astro`.
- 2026-09-30 — NOTE: two copies of styles.css exist (`public/css/styles.css` is the one served; `src/styles/styles.css` appears unused). Both updated identically. Consider consolidating.
- 2026-09-30 — New pillar `/buy-before-you-sell` (HowTo + FAQPage schema, video slot, Move First facts from Orchard-approved materials + disclosure).
- 2026-09-30 — /buy-before-you-sell: "empty" language replaced (refreshed/cleaned/staged), Orchard name removed from body, new "What Families Worry About" (7 cards) and "Yes, There Are Fees… Pay for Itself" sections.
- 2026-09-30 — ⛔ `/buy-before-you-sell-options` PARKED at Jacob's request: moved to `drafts/` (outside src/pages, never built). NOT part of any deploy. All links to it repointed to /buy-before-you-sell and the hub's options table.
- 2026-09-30 — New pillar `/renovate-before-selling` (pre-listing updates, pay at closing; HowTo + FAQPage schema; Notable disclosure from config; no Orchard name in body).
- 2026-09-30 — New `src/data/cluster.ts`: `fixOrSkipUrl` temporarily → /blog/7-smartest-home-upgrades-before-selling-2026 until /what-to-fix-before-selling ships (one-line swap). Full build + internal link check clean (0 broken links on hub, pillars, home, about).
- 2026-09-30 — Jacob added `public/images/email/` (headshot.png, headshot2.png, badge-5280.png, badge-dmar-2025.png, badge-realtrends.png, badge-rene.png) for email signatures → served at https://selling303.com/images/email/<file>. MUST be included in the push file list (push script only sends listed files).
- 2026-09-30 — `public/_headers` CSP: allowed https://i.ytimg.com (img-src) and https://www.youtube-nocookie.com (frame-src) so VideoEmbed thumbnails/players aren't blocked once videos are added.
- 2026-09-30 — Hub: removed "How I deliver this today" box (Orchard programs + full disclosure). Renovation page: headline → "The Best Renovation Is the One That Pays You Back", "The Updates That Usually Make the List", short general financing disclaimer (`disclosures.renovationFinancingShort`).
