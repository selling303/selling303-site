# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-09 late production deploy — merge f817563, see DEPLOY_LOG.md.)_
- 2026-10-14 — /contact text-first redesign: left column "The Fastest Way to Reach Me" with Text Jacob (sms: link with prefilled "Hi Jacob, I found you on selling303.com and"), Call, Email, and Book 30 Minutes buttons; right column photo of Jacob (src/assets/images/jacob-lifestyle-home.jpg via <Image>, eager). Service area moved to a slim band below the fold with pill links to the 9 /neighborhoods/ pages (local SEO + internal links). CONTACT FORM REMOVED per Jacob (real online leads text/call/email him directly; the form only received spam, 0 real leads YTD). Removed the Brokerage info row (footer still carries brokerage + license line) and the inaccurate "free 15-minute" call copy. /thank-you page stays (noindex, harmless) but nothing links to it now.
- 2026-10-14 — SEO.astro click tracking extended sitewide: tel_click (existing), plus sms_click, email_click, booking_click (Google Calendar appointment links). Each includes link_text + page_path. AFTER DEPLOY: once each appears in GA4 Admin → Events, mark sms_click, tel_click, email_click, booking_click as key events alongside generate_lead.
- Tested: local build (layout desktop + 390px, all 4 click events fire). reCAPTCHA was tested on a branch deploy, then dropped along with the form; public/_headers is unchanged from live.

- 2026-10-14 — NEW /reviews page: all 49 Google reviews (pulled from Google Business Profile Manager 2026-10-14), verbatim, newest first, rendered as static HTML (no widget, no CSP changes). Data in src/data/reviews.json; rating/count read from agent.ts. WebPage schema only (no Review/aggregateRating, intentionally). Includes family/partner reviews and the two old-brokerage mentions (ExpRealty, 8z) verbatim per Jacob. Added "Client Reviews" footer link and to the About dropdown in the header nav; homepage hero "★ 5.0 from 49 Google reviews" now links to /reviews; added agent.googleProfileUrl (Maps CID link) and swapped it into the sameAs arrays on / and /about (replacing the ?q= search URL). Compiled + layout checked in a stub build; full local build not yet run.
- 2026-10-14 — Review schema cleanup: removed aggregateRating from the Person/RealEstateAgent schema on / and /about; removed the homepage Review schema block (8 success-story testimonials that weren't visible on the page) and its script tag; removed the one-review aggregateRating from the success-story template (sell/success-stories/[slug].astro — per-story Review stays since the quote is visible). /reviews title + H1 now lead with "Jacob Stark Reviews". Visible "5.0 from 49 Google reviews" text unchanged.
- 2026-10-14 — Visible Google Business Profile links: Google "G" icon added to the footer social row (all pages, links agent.googleProfileUrl); all 6 footer social icons now open in a new tab (target=_blank, rel=noopener, "(opens in a new tab)" in aria-label); /contact gets a "Find me on Google · ★ 5.0 from 49 Google reviews" line under the contact buttons (Google profile + /reviews).
- 2026-10-14 — /contact: "Find me on Google · ★ 5.0 from 49 Google reviews" line under the buttons (links to GBP + /reviews; added in another session), now spaced out: 2rem above, thin divider, centered under the buttons; button gap 0.875rem.
