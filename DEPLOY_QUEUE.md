# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-06 production deploy — merge 57deeaa, see DEPLOY_LOG.md.)_
- 2026-10-03 — `/assumable-loans`: "Why Everyone's Asking" moved under the Short Answer with two 3%-loan scenarios (balance ~92% / 70%), old cash-to-close table removed, TOC gained "The Numbers." Edits exist locally only — NOT yet pushed to main. Scenario payments are hard-coded; recompute if `rate` changes.
- 2026-10-07 — `/blog/moving-to-littleton-colorado-relocation-guide-2026`: added a paragraph after the mailing-address section noting that the City of Littleton's At Your Door hazardous waste pickup (WM, launched April 1, 2026) is for City residents only, so unincorporated Jeffco/DougCo addresses don't qualify. Cites the City's hazardous materials page. Pushed to main.
- 2026-10-09 — Homepage (`src/pages/index.astro`): SEO title → "Jacob Stark | Littleton, CO REALTOR® | Outgrown Your Home?" (58 chars, was 79); meta description → "Outgrown your home? Jacob Stark, a Littleton, Colorado REALTOR®, helps South Denver Metro families buy first, sell later, and move just once." Per SARA audit (title should name primary market). OG title/description unchanged.
- 2026-10-09 — LEAD PATH FIX (SEO plan #1). /contact posted to /thank-you, which didn't exist (404 for every real lead). NEW `src/pages/thank-you.astro` (contact confirmation, booking + call/text CTAs) and `src/pages/thank-you-newsletter.astro`; both noindex and excluded from the sitemap (astro.config.mjs filter). Footer newsletter form now posts to /thank-you-newsletter (had no action). Assumable form action → /assumable-loans/list (no trailing slash, matches trailingSlash: 'never').
- 2026-10-09 — GA4 lead tracking: SEO.astro adds a global submit listener on Netlify forms that stores form name + lead type in sessionStorage; new `src/components/LeadConfirm.astro` on the confirmation pages fires `generate_lead` (contact, assumable-list) or `sign_up` (newsletter) once, only after a real in-browser submit (refreshes, direct visits, and no-JS bot POSTs don't count). Params: form_name, lead_type (buyer / seller / move-up / investor / valuation / other / buyer-assumable / newsletter), form_page. `window.s303InitGA` exposed so GA is configured before the event. Tested in Playwright against a local build: all 3 forms fire correctly; reload and direct visit fire nothing. AFTER DEPLOY: Jacob marks generate_lead as a key event and un-marks form_submit in GA4 Admin, then submits one real test lead.
