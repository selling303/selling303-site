# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- **2026-04-13** — Added GA4 `page_not_found` custom event to 404.astro (tracks broken URL path, referrer, and full URL)
- **2026-04-13** — Updated CLAUDE.md deploy protocol to reference GitHub API instead of git commands (MUST be pushed to main before next deploy)
- **2026-04-13** — Hardened github-api-push.sh: added JSON escaping for commit messages and file paths (prevents silent failures on special characters)
- **2026-04-14** — Self-hosted Google Fonts (Inter + DM Serif Display): eliminated render-blocking @import chain, added @font-face declarations with font-display:swap, preloads in head
- **2026-04-14** — Lazy-load RealScout widget (205 KiB) via IntersectionObserver — removed from critical render path on all 4 pages
- **2026-04-14** — Updated CSP headers: font-src now 'self' only, added /fonts/* immutable cache rule (1yr)
- **2026-04-14** — Expected Lighthouse improvement: ~930ms FCP/LCP from font chain elimination, ~205 KiB off critical path from RealScout deferral
- **2026-04-14** — Added 301 redirects for all 27 GSC 404s: old Framer listing pages → /properties, old blog slugs → closest Astro posts, old static pages → Astro equivalents, old neighborhood paths → /neighborhoods/[slug]
