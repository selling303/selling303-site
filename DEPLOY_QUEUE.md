# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-18 production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-05-18 [Force dynamic OG card site-wide for blog posts]:** Post-deploy verification on the Parker move-up post via Facebook's Sharing Debugger revealed that 57 of 58 blog posts had `ogImage:` frontmatter (51 generic Unsplash filler from blog-post-writer defaults + 6 broken `/images/og-*.jpg` refs), which bypassed the dynamic Selling 303 card via the precedence chain `data.ogImage || data.cardImage?.url || dynamic`. Fix in `src/pages/blog/[slug].astro` strips the override chain so every blog post uses the dynamic card — both the Schema.org Article `image` field and the BaseLayout `ogImage` prop. Frontmatter fields untouched (no 57-file mass edit). cardImage continues to drive the blog-index thumbnail. Follow-up after deploy: re-scrape affected blog URLs in Facebook Sharing Debugger; update `blog-post-writer` skill at claude.ai/customize/skills to stop adding auto-Unsplash `ogImage:` to new posts.

- **2026-05-18 [Chunk B — repo portion: case-drift + stale skill-ref comment]:** In-repo half of Chunk B from the 2026-05-17 dead-infra audit. (1) `CLAUDE.md:138` — corrected `~/Documents/Claude/projects/` to capital P. (2) `public/css/aeo-visuals.css:4` — updated stale "Source of truth" comment pointing at the dead `~/.claude/skills/aeo-visual-builder/SKILL.md` (deleted 2026-04-30) to reference `claude.ai/customize/skills` + the working copy under `brain/skills-source/`. Off-repo half already applied: scheduled task wrapper for `seo-aeo-weekly-audit` (removed `~/.claude/skills` mount + capitalized path — fixes Monday's failing first step) and 11 files under `brain/skills-source/` with 40 case-drift occurrences (will ship with future paste-to-cloud cycles per the skill source-of-truth model).

- **2026-05-18 [Chunk C — delete dead root-level twins + orphan components]:** Per 2026-05-17 dead-infra audit. Twenty-four files removed from the repo: root-level dead `_headers`, `favicon.ico/svg`, `robots.txt`, `sitemap.xml`, `css/styles.css`, `js/main.js`, 8 files under `images/` (all functional duplicates already in `public/`); the legacy `success-stories/time-for-more-space.html` Framer page (not in nav, not in sitemap); `watering-guide-research.md` (orphan research note from April); and orphan components `src/components/AuthorBio.astro` + `TrustSignals.astro` (zero references repo-wide). Production behavior unchanged — none of these were ever in Astro's build path. Just removing the landmine surface area so the dead-twins bug class can't recur. Root `_redirects` already deleted on 2026-05-17.
