# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-04-24 production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-04-24** — New blog post: "What Out-of-State Buyers Get Wrong About the Denver Suburbs (and How to Avoid the Same Mistakes)" — `/blog/out-of-state-buyer-mistakes-denver-suburbs-centennial`. Day 21 calendar entry; Specialization `/relocation` + Geographic `/neighborhoods/centennial`. Uses Q1 2026 REcolorado MLS Centennial closed-sale data (n=269, $700K median, 13 day median DIM, 98% median CP/OLP) and DMAR March 2026 Market Trends report. Includes inline 5-card "misconceptions vs. reality" visual (commute, altitude, season, HOA + metro district stack, water restrictions). Calendar marked `[x]`; cluster map updated under Relocation pillar.
- **2026-04-24** — Added honeypot spam prevention to both forms (`contact.astro` and `Footer.astro`). Each form gets: `netlify-honeypot="bot-field"` attribute on `<form>` + hidden `bot-field` input off-screen (`position: absolute; left: -9999px`), `aria-hidden="true"` on container, `tabindex="-1"` and `autocomplete="off"` on the input so screen readers, keyboard users, and password managers don't trip it. Netlify strips the `netlify-honeypot` attribute at build time and rejects any submission where `bot-field` has a value. Goal: catch bots before they reach Akismet so fewer real submissions get false-positive spam-flagged (like Jacob's 2026-04-24 test submission). No code change to form submission logic — forms continue to work unchanged for real users.
- **2026-04-25 [SEO-AEO]** — Added global `tel_click` GA4 event listener to `src/components/SEO.astro` (capture-phase click delegate on `a[href^="tel:"]`). Fires `gtag('event', 'tel_click', {link_url, link_text, page_path})` for every phone-link tap sitewide — covers FloatingCTA, Footer, CTABanner, contact page, and all pillar-page CTAs without per-page changes. Pairs with `form_submit` already flagged as key event in GA4 Admin (also 2026-04-25). Together they unblock the Conversion category in the SEO/AEO weekly audit; before today, GA4 reported 0 conversions for 90 days because no events were flagged. Detailed entry in `~/Documents/Claude/Projects/AEO & SEO Expert/DEPLOY_QUEUE.md`.

