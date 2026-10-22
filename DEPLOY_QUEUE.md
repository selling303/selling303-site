# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-20 production deploy — merge fd2506e, see DEPLOY_LOG.md.)_

- 2026-10-20 — /about Person schema sameAs: reverted the GBP entry from the maps.app.goo.gl short link back to agent.googleProfileUrl (Maps CID link). Jacob chose the CID link as the one GBP URL sitewide going forward.
- 2026-10-21 — REVIEWS UPGRADE (Jacob approved featured picks 2026-10-21; pushed to main):
  - src/data/reviews.json: new fields per review — dealType (array: buyer / seller / move-up / investor / new-construction; set only where the text is clear, 13 left blank for Jacob), area (Jacob supplied 2026-10-21 for all 49 reviews; deal types also updated from his list, move-up reviews show a single "Move-up" pill), featured (5 = Mandie Hume, Dee, Kara Lindenmeyer, Jo-Ann McIntosh, jordan quinn), featuredQuote (verbatim excerpt, build-checked as a substring of the review). Backup of the previous file in _to_delete/reviews.backup-2026-10-21.json.
  - NEW src/lib/reviews.ts: shared helpers (sorting, featured order seller/move-up first, labels, /reviews#review-<name> anchors, excerpt ellipsis).
  - /reviews: "Featured Reviews From Sellers" section above the full list; deal-type tags (and area when set) on every card; each card has an id anchor; masonry script re-scrolls to a linked review after layout.
  - NEW src/components/ReviewQuotes.astro: two verbatim review quotes + "See all 49 Google reviews" link, placed directly above the bottom CTA on /buy-before-you-sell (Kara, Mandie), /move-up-sellers (Kara, Jo-Ann), /expired-listings (jordan, Dee), /first-time-homesellers (Jo-Ann, Mandie). Each links to that review on /reviews.
  - src/data/agent.ts: googleReviewCount now derived from reviews.json length (adding a review is the only step); new stats.reviewsVerifiedOn '2026-10-14'.
  - Tested in a stub build (reviews page + quote component, desktop and 390px, all 49 cards, anchors). Full local build still needed on Jacob's Mac.
