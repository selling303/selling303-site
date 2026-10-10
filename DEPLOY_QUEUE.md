# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-09 evening production deploy — merge 29e2159, see DEPLOY_LOG.md.)_
- 2026-10-09 — Schema address: agent PostalAddress changed from Greenwood Village, CO 80111 (old office, Orchard is remote) to Littleton, CO 80120 (no street address) on the homepage, /about, and the success-story template. Matches the GBP service-area setup (no public address).
- 2026-10-09 — /move-up-sellers: added the term "move-up buyers" (page never used it; SARA and AI search use it). Short Answer gained one sentence ("often called move-up buyers or move-up sellers…"); new FAQ #2 "What is a move-up buyer, and how is it different from a move-up seller?" (also flows into FAQPage schema). URL and H1 unchanged.
- 2026-10-09 — Internal links: linked the phrase "move-up buyers" to /move-up-sellers in body copy of 5 posts that mentioned it without linking to the hub (parker-move-up-listings-stall-pricing-strategy-2026, parker-vs-castle-pines, why-centennial-home-not-getting-offers, new-construction-buyer-representation-colorado-2026, best-parks-trails-littleton-highlands-ranch). Other mentions were related-post titles in frontmatter, not linkable.
- 2026-10-09 — CLEANUP BATCH (SEO plan): (1) Stats: $46M+/100.6% → $50M+/101.8% (Jacob confirmed) in 20 blog posts; none left sitewide. (2) Success-story schema: AggregateRating only emitted when a story has ≥1 testimonial (reviewCount 0 was invalid). (3) Sitemap: draft success stories now detected from `draft: true` frontmatter instead of a hand-kept list, which drops 7327 S Carr Ct (noindexed but was in sitemap-0.xml); the 8 published stories stay. (4) public/_redirects: /sellers2 → /move-up-sellers and /tax-valuations-ridgeview-hills-2023 → /blog/2026-notice-of-valuation-protest-playbook-south-denver (both were 404s still getting visits). (5) /properties: crawlable intro (H2 + 2 paragraphs, links to Seller Promise, success stories, /buy-before-you-sell) above the RealScout widget, which loads client-side and left Google ~26 words. Wording pending Jacob's OK.
- 2026-10-09 — public/_redirects: forced 301s from /<page>.html → /<page> for every top-level page, and /index.html → /. Tested on a free branch deploy (redirect-test): each .html URL redirects once to the clean URL, no loops; normal pages, sitemap, assets, and existing redirects unaffected. Trailing-slash 301s deliberately NOT added: tested and they loop (Netlify ignores trailing slashes when matching rules). Canonical tags already point to the no-slash URLs.

