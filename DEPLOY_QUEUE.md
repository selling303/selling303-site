# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-09 production deploy — merge 03bb3fc, see DEPLOY_LOG.md.)_
- 2026-10-09 — FIX: lead tracking listener in `src/components/SEO.astro` detected Netlify forms by `data-netlify`, which Netlify strips from deployed HTML, so generate_lead/sign_up never fired on live. Now detects the hidden `form-name` input (kept by Netlify) and uses its value as form_name. Re-tested in Playwright with data-netlify stripped: contact, newsletter, and assumable forms fire; reload and direct visit don't. AFTER DEPLOY: submit one test lead and check GA4 Realtime/DebugView for generate_lead.
