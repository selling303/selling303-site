# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

## 2026-04-17 — Homepage PageSpeed fixes

- **LCP fix:** Added `.hero::before` rule to the critical inlined CSS in `BaseLayout.astro`. Previously `.hero::before` (which renders the hero background image via `var(--hero-bg)`) only existed in the deferred `/css/styles.css`. This caused a late layout recalc when the deferred stylesheet loaded, pushing out the subtitle's LCP timestamp to ~2,460ms element render delay per PSI. With the rule in critical CSS, the hero image positioning element exists at first paint and the subtitle's LCP fires at the correct moment.
- **Forced-reflow fix:** Rewrote the GA4 init script in `SEO.astro` to defer initialization until first user interaction (scroll/click/keydown/mousemove/touchstart) or idle/3s timeout. Previously the inline `gtag('config', ...)` call fired during initial HTML parse, triggering 64ms of forced reflow on selling303.com line 154 (plus GTM's own internal reflows). Pageviews still register — only very short zero-interaction bounces under 3s are missed. Preconnect to googletagmanager.com kept for fast TLS handshake when GA does fire.
- Only affects the homepage hero (only page using `.hero` + `--hero-bg`). Other pages use `.page-hero`, unaffected.
