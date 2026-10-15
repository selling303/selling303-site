# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-09 late production deploy — merge f817563, see DEPLOY_LOG.md.)_
- 2026-10-14 — /contact text-first redesign: left column "The Fastest Way to Reach Me" with Text Jacob (sms: link with prefilled "Hi Jacob, I found you on selling303.com and"), Call, Email, and Book 30 Minutes buttons + service area; form moved to a secondary right-column card ("Prefer to Send a Message?"). Removed the Brokerage info row (footer still carries brokerage + license line) and the inaccurate "free 15-minute" call copy. Contact form now has Netlify reCAPTCHA (data-netlify-recaptcha). Real form leads were 0 YTD; spam ~2/mo got past the honeypot. Revisit in ~90 days (mid-Jan 2027): if the form still has 0 real leads, remove it.
- 2026-10-14 — public/_headers CSP: added https://www.google.com + https://www.gstatic.com to script-src and https://www.google.com + https://recaptcha.google.com to frame-src (needed for reCAPTCHA).
- 2026-10-14 — SEO.astro click tracking extended sitewide: tel_click (existing), plus sms_click, email_click, booking_click (Google Calendar appointment links). Each includes link_text + page_path. AFTER DEPLOY: once each appears in GA4 Admin → Events, mark sms_click, tel_click, email_click, booking_click as key events alongside generate_lead.
- Tested: local build (layout desktop + 390px, all 4 click events fire) and free branch deploy redirect-test@aff69b8 (reCAPTCHA renders, no CSP errors).

