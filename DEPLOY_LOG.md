# Deploy Log

Permanent record of deployed changes. The deploy-to-netlify skill moves items here from `DEPLOY_QUEUE.md` after each successful deploy.

---

## 2026-04-10 — commit 48b3fcc | Credits used: 15 | Credits remaining: 275

- New blog post: "How to Relist and Sell a Home in Littleton After an Expired Listing" (`src/content/blog/relist-home-littleton-after-expired-listing.md`). Day 7 of content calendar. Expired Listings pillar + Littleton geographic pillar. 93 expired + 18 withdrawn Q1 2026 data from REcolorado, DMAR Feb 2026 stats, step-by-step relist checklist, Seller Promise links.
- New page: My Seller Promise (`src/pages/my-seller-promise.astro`) — Apple-style scroll experience with hero, promise section, three-phase horizontal image carousels, ClientClarity demo button + ClearPrice cards, FAQ accordion with Schema.org markup, trust bar, areas served, CTAs to Calendly. 12 images in `src/assets/images/seller-promise/`.
- Updated Header nav — added "My Seller Promise" as first item in Sell dropdown.
- Updated water restrictions blog post with Denver Water drought surcharges (Tier 2/3 pricing, effective May 2026).
- Fixed clientclarity-demo page — replaced `<head slot="head">` with `<Fragment slot="head">` (fixed footer rendering at top) and added header-height padding to hero.
- Updated content-calendar-2026.md — marked Day 6 HR relocation as published, Day 7 Littleton relist as drafted.
- Updated content-cluster-map.md — added HR expired listing, HR relocation guide, Castle Pines new construction, and Littleton relist to respective clusters.
- Updated CLAUDE.md — added explicit live-branch approval rule.
- Fixed branch divergence — cherry-picked 3 live-only commits onto main, reset live to match.

## 2026-04-08 — commit 5e3b0bf | Credits remaining: 290

- Infrastructure: switched to two-branch deploy system (main/live)
- Netlify production branch changed from `main` to `live`
- Created build hook `deploy-selling303` (stored as NETLIFY_BUILD_HOOK env var)
- CLAUDE.md: rewritten deploy protocol for main/live architecture
- YAML quoting fixes across 5 blog posts (& character safety)
- Added missing cardStat/cardStatLabel to 2 older posts
- Added Neighborhoods filter button to blog index
- Deploy skill v4: two-branch push/deploy workflow

## 2026-04-08 — commit 57d5a78 | Credits remaining: 320

- HOTFIX: Added missing blog card CSS to styles.css (gradient backgrounds, card headers, hover reveal animations). Cards were rendering blank after previous deploy omitted the stylesheet additions.

## 2026-04-08 — commit a3a34f5 | Credits remaining: 335

- Blog tile redesign: category gradient headers, SVG icons, cardStat/cardStatLabel hover reveal
- Zod schema: cardStat, cardStatLabel fields; cardImage and relatedPosts image now optional
- 12 blog posts: added cardStat + cardStatLabel frontmatter
- SEO: removed FUB widget tracker and widgetbe.com preconnect
- Properties: full RealScout listing-status values
- CLAUDE.md: comprehensive deploy protocol + commit-before-closing rule

## 2026-04-08 — commit 4620b03 | Credits remaining: 350

- New blog post: "New Construction Communities in Castle Pines and Parker: What Buyers Need to Know in 2026" (`src/content/blog/new-construction-castle-pines-parker-2026.md`). Day 5 of content calendar. New Construction pillar + Castle Pines geographic pillar.
