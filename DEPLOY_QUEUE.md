# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- **2026-04-07** — Added 18 Framer legacy redirect rules to `_redirects` (fixes 7 GSC 404s, 4 noindex ghost pages, 5 "crawled not indexed" pages)
- **2026-04-07** — **[BROKEN ON LIVE]** Moved `.nbhd-card` styles from `neighborhoods.astro` into `NeighborhoodCard.astro` — fixes Astro scoped CSS mismatch that made neighborhood card images and styling invisible
- **2026-04-07** — **[BROKEN ON LIVE]** Added `width: 100%` to RealScout widget on properties page — widget was collapsing to zero width
