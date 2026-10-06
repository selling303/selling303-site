# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-02 late production deploy — merge 61a56ad, see DEPLOY_LOG.md.)_
- 2026-10-02 — FIX: desktop nav dropdowns closed when moving the mouse from the menu name to the submenu (12px gap between toggle and menu). Added an invisible ::before hover bridge on .dropdown-menu (min-width 901px) in public/css/styles.css and src/styles/styles.css. Tested with a slow mouse move in Playwright.
- 2026-10-02 — Hub /move-up-sellers: "Sound Familiar?" monologue now a text-message thread between a couple (new `src/components/TextThread.astro`; bubbles reveal one at a time on scroll, static for reduced motion/no JS). Same words, the long "I don't know…" line split into three quick texts.
- 2026-10-02 — Hub text thread: closing 🤷 emoji reply (large, no bubble, like a real emoji-only text).
- 2026-10-03 — `agent.ts` bookingUrls labeled per Jacob: general (30 min, any topic), listingConsult (was moveUp), buyerConsult, showing (neighborhood pages, type unconfirmed). Move-up pillars now reference bookingUrls.listingConsult (same URL as before, no visible change).
- 2026-10-03 — NEW `/assumable-loans` guide (public: short answer, cash-to-close illustration at Freddie Mac 7.28%, loan-type table, timeline, pros/cons, 6 steps, seller section, 6-Q FAQ schema, sources) + gated lead magnet: Netlify form `assumable-list` (name, email, phone, max price, timeline, areas, cash) posts to hidden `/assumable-loans/list/` (noindex, excluded from sitemap) with the RealScout shared-search link. Buy nav dropdown: added "Assumable Loans". After deploy: submit a test form and confirm the email notification arrives (Netlify form notifications may be per-form).
- 2026-10-03 — `/assumable-loans`: cash-reorder commit 6c6c31e (cash-available options) also pending. "Why Everyone's Asking" moved up under the Short Answer (above the list form) and now includes two side-by-side scenarios on a $600K home at 3% with ~25 yrs left vs. a new loan at the page's `rate` const, same cash down: balance ~92% ($50K cash, saves ~$1,155/mo) and balance 70% ($180K cash, saves ~$880/mo). Old 3-column cash-to-close table removed; #cash-to-close now covers second loans when the buyer lacks the equity cash. TOC gained "The Numbers". Compare table fits at 390px (no sideways scroll). NOTE: scenario payments are hard-coded; recompute if `rate` changes.
- 2026-10-06 — New blog post `src/content/blog/price-cut-vs-2-1-buydown-south-denver-metro-2026.md` — 2-1 buydown vs. price cut for South Denver Metro sellers (Sept 2026 DMAR + REcolorado data, Freddie Mac 7.28% rate, Tier 2 buydown calculator). Also content-cluster-map.md and visual-inventory.md entries. Approved by Jacob to go live 2026-10-06.
