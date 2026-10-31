# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-30 production deploy — merge 02a9d14, see DEPLOY_LOG.md.)_

- 2026-10-31 Grok SEO follow-ups on the buy-or-sell-first post:
  - src/pages/blog/[slug].astro: Article schema + microdata datePublished/dateModified now ISO 8601 (2026-10-30) via toIsoDate(); visible byline shows "Updated [date]" only when dateModified differs from date. Affects all blog posts.
  - src/pages/buy-before-you-sell.astro: link to /blog/buy-or-sell-first-south-denver-move-up/ under the buy-first vs sell-first table.
  - src/pages/move-up-sellers.astro: same link under the Your Options table.
  - src/content/blog/buy-or-sell-first-south-denver-move-up.md: 2 new FAQs (program cost; what if my house doesn't sell), visible + faqSchema. Bump dateModified on the live-deploy day.
