# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-02 production deploy — merge a62b785, see DEPLOY_LOG.md.)_

- 2026-10-02 — **Homepage redesign (D3, "Outgrown Your Home?")** — `src/pages/index.astro` rewritten: question-only H1, "Did you know you can…" hero list with approval/financing footnote from `agent.ts` disclosures, Hampden family-room before/after, guide strip with stats, Prepare/Buy & Sell/Move Once cards, Hampden primary-bedroom before/after, 3 real testimonials, 6-tile success-story strip, "What's your situation?" router, tools, neighborhoods, home-value widget (#home-value kept), final CTA. All schema blocks kept. Removed: stale Feb 2026 market tiles, RealScout search widget, old blog cards, old testimonial list, "Recognized By" row. Old version backed up at `_to_delete/index.astro.bak-2026-10-02`.
- 2026-10-02 — New image `src/assets/images/before-after/hampden-primary-bedroom-before.jpg` (cropped from Jacob's phone photo).
- 2026-10-02 — `agent.ts`: googleReviewCount 47 → 49 (Jacob confirmed).
- 2026-10-02 — `move-up-sellers.astro`: testimonial attribution fixed "Jacque" → "Matthew S." (quote is from the 7307 S Birch St story).
- 2026-10-02 — Homepage mobile hero: "you can" list becomes a slow rotating drum on phones (active line full, neighbors faded; tap to advance; static list on desktop and for reduced-motion). Tighter mobile hero spacing, full-width CTA, text-link secondary.
- 2026-10-02 — New pages `/privacy-policy` and `/terms` (`src/pages/privacy-policy.astro`, `src/pages/terms.astro`); footer links now point to them. Content reflects what the site actually uses: Netlify Forms (contact + newsletter), Google Analytics (G-WLGW57VN8C), RealScout widgets, Google Calendar booking, YouTube nocookie embeds, client-side calculators. Disclosures pulled from `agent.ts`. Not attorney-reviewed; Jacob to run past Orchard compliance.
- 2026-10-02 — Privacy policy: named data flows per Jacob (contact forms → his email via Netlify; RealScout widget → RealScout + Follow Up Boss; texting section kept since he texts leads).
