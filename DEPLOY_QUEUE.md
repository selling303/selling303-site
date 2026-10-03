# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-02 late production deploy — merge 61a56ad, see DEPLOY_LOG.md.)_
- 2026-10-02 — FIX: desktop nav dropdowns closed when moving the mouse from the menu name to the submenu (12px gap between toggle and menu). Added an invisible ::before hover bridge on .dropdown-menu (min-width 901px) in public/css/styles.css and src/styles/styles.css. Tested with a slow mouse move in Playwright.
- 2026-10-02 — Hub /move-up-sellers: "Sound Familiar?" monologue now a text-message thread between a couple (new `src/components/TextThread.astro`; bubbles reveal one at a time on scroll, static for reduced motion/no JS). Same words, the long "I don't know…" line split into three quick texts.
- 2026-10-02 — Hub text thread: closing 🤷 emoji reply (large, no bubble, like a real emoji-only text).
