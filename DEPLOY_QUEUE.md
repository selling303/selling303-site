# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-09 late production deploy — merge f817563, see DEPLOY_LOG.md.)_
- 2026-10-14 — /contact text-first redesign: left column "The Fastest Way to Reach Me" with Text Jacob (sms: link with prefilled "Hi Jacob, I found you on selling303.com and"), Call, Email, and Book 30 Minutes buttons; right column photo of Jacob (src/assets/images/jacob-lifestyle-home.jpg via <Image>, eager). Service area moved to a slim band below the fold with pill links to the 9 /neighborhoods/ pages (local SEO + internal links). CONTACT FORM REMOVED per Jacob (real online leads text/call/email him directly; the form only received spam, 0 real leads YTD). Removed the Brokerage info row (footer still carries brokerage + license line) and the inaccurate "free 15-minute" call copy. /thank-you page stays (noindex, harmless) but nothing links to it now.
- 2026-10-14 — SEO.astro click tracking extended sitewide: tel_click (existing), plus sms_click, email_click, booking_click (Google Calendar appointment links). Each includes link_text + page_path. AFTER DEPLOY: once each appears in GA4 Admin → Events, mark sms_click, tel_click, email_click, booking_click as key events alongside generate_lead.
- Tested: local build (layout desktop + 390px, all 4 click events fire). reCAPTCHA was tested on a branch deploy, then dropped along with the form; public/_headers is unchanged from live.

