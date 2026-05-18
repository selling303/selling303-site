# selling303.com — Project Rules

## Deploy Protocol (Mandatory)

### Before making changes

Read `DEPLOY_QUEUE.md` and `DEPLOY_LOG.md` to understand what's pending and what's already deployed. The GitHub API push script handles atomic commits — no need to sync or pull. If you need to verify the current state of a file on `main`, use the GitHub API: `curl -sf -H "Authorization: token $PAT" https://api.github.com/repos/selling303/selling303-site/contents/<path>?ref=main`.

### Two-branch system

- **`main`** — working branch. Pushes here do NOT trigger Netlify builds. Safe, free, always in sync.
- **`live`** — production branch. Pushes here trigger Netlify auto-deploy (15 credits per deploy). Only production-ready code.

### Pushing changes (Mandatory)

Every session that edits site files MUST push to `main` before closing. Use the `deploy-to-netlify` skill for all pushes — it uses the GitHub REST API (`scripts/github-api-push.sh`) to push changed files directly. Never use `git clone`, `git push`, or any git commands in the sandbox. The API approach uses zero disk space and has no FUSE issues.

### Deploying to production

**Never push to `live` without Jacob's explicit approval.** Production deploys cost 15 credits each and happen once per day, bundled with the nightly blog post. Use the `deploy-to-netlify` skill to:
1. Merge `main` → `live`
2. Push `live` to trigger Netlify build

When Jacob confirms changes are "good to go" or "ready to push," that means push to `main` only — not `live`. The nightly blog task handles the production deploy. If Jacob wants something live immediately, he will say so explicitly (e.g., "deploy now," "push this live," "make this live now").

**Exception:** if something is visibly broken on the live site, Jacob may approve a standalone production deploy — always confirm with him first.

### Logging changes

When making changes to the repo, log each change as a bullet in `DEPLOY_QUEUE.md` with the date and a brief description. Before logging, verify the change is actually needed — check `DEPLOY_LOG.md` to confirm it wasn't already deployed.

### Two-file system

- `DEPLOY_QUEUE.md` — pending changes waiting to ship. Cleared after each production deploy.
- `DEPLOY_LOG.md` — permanent record of deployed changes with dates and commit hashes. Check this to see if something was already deployed.

## Image Pipeline (Mandatory)

All images on the site MUST go through Astro's built-in image optimization pipeline. No exceptions for new pages, replacement images, or redesigns.

### Rules

1. **Store images in `src/assets/images/`** — never in `public/images/`. Files in `public/` bypass optimization entirely.
2. **Use `<Image>` for `<img>` tags** — import from `astro:assets` and pass the imported source. Astro auto-generates WebP and adds width/height.
   ```astro
   import { Image } from 'astro:assets';
   import myImage from '../assets/images/my-image.jpg';
   // ...
   <Image src={myImage} alt="Description" width={800} format="webp" quality={80} />
   ```
3. **Use `getImage()` for CSS background images** — import the source, call `getImage()` in frontmatter, inject the optimized URL via template literal.
   ```astro
   import { getImage } from 'astro:assets';
   import bgSrc from '../assets/images/bg.jpg';
   const bg = await getImage({ src: bgSrc, format: 'webp', quality: 80, width: 1920 });
   // ...
   <div style={`background-image: url('${bg.src}');`}></div>
   ```
4. **Hero images get a preload hint** — any above-the-fold hero/banner image must include `<link rel="preload" as="image" href={optimizedImg.src} type="image/webp" fetchpriority="high" />` in the `<head>`.
5. **Never lazy-load above-the-fold images** — use `loading="eager"` (or omit the attribute) for hero/banner images. Only use `loading="lazy"` for images below the fold.
6. **External URLs (Unsplash, etc.) are exempt** — images loaded from external CDNs can't go through the pipeline. Use standard `url()` or `<img>` for those.

### Why

Astro's Sharp-based pipeline converts to WebP at build time, reducing file sizes 40-60% with no visible quality loss. This directly improves LCP and page load performance across the site.

## Reusable Components with AEO Microdata (Mandatory)

Market stats and neighborhood cards have dedicated Astro components with Schema.org Microdata baked in. Always use these components — never write inline Microdata HTML.

### MarketStatTile

Location: `src/components/MarketStatTile.astro`

Renders a single market stat with `PropertyValue` Microdata. Must be placed inside a parent element with `itemscope itemtype="https://schema.org/Place"`.

```astro
import MarketStatTile from '../components/MarketStatTile.astro';
// ...
<div itemscope itemtype="https://schema.org/Place">
  <meta itemprop="name" content="South Denver Metro, Colorado" />
  <MarketStatTile number="$605,000" label="Median Home Price" value="605000" unit="USD" trend="-2.3% YoY" trendDirection="down" />
</div>
```

Props: `number` (display string), `label`, `value` (machine-readable), `unit` ("USD" | "days" | "listings"), `trend?`, `trendDirection?` ("up" | "down").

### NeighborhoodCard

Location: `src/components/NeighborhoodCard.astro`

Renders a neighborhood card with `Place` + `PropertyValue` Microdata. Two variants:

- **`compact`** — homepage cards. Renders as `<a>` with `.card` classes.
- **`full`** — neighborhoods page. Renders as `<div>` with `.nbhd-card` classes, includes county, match badge, explore/search buttons.

```astro
import NeighborhoodCard from '../components/NeighborhoodCard.astro';
// Compact (homepage):
<NeighborhoodCard variant="compact" name="Littleton" slug="littleton"
  description="Historic downtown charm..." medianPrice={703000}
  medianPriceDisplay="$703K" dom={51} imageSrc={nbLittleton.src}
  imageAlt="Suburban home in Littleton, Colorado" />

// Full (neighborhoods page):
<NeighborhoodCard variant="full" name="Littleton" slug="littleton"
  county="Arapahoe County" description="Littleton is the Saturday-morning..."
  medianPrice={703000} medianPriceDisplay="$703,000" dom={51}
  imageSrc={nbLittleton.src} imageAlt="Suburban street in Littleton"
  searchUrl="https://selling303.realscout.com/search?city=Littleton" />
```

Props: `variant` ("compact" | "full"), `name`, `slug`, `county?` (required for full), `description`, `medianPrice` (number), `medianPriceDisplay` (string), `dom` (number), `imageSrc`, `imageAlt`, `searchUrl?` (required for full).

### Why

Schema.org Microdata helps answer engines (ChatGPT, Google AI Overviews, Perplexity) surface structured data about neighborhoods and market stats directly from the HTML. Baking it into components ensures every page gets correct structured data automatically — no manual Microdata required.

## Editing Skills (Mandatory)

**Skills are managed exclusively at https://claude.ai/customize/skills.** That web UI is the only source of truth for the skill registry that Cowork loads from at session start. The local `~/.claude/skills/` directory does NOT exist anymore — it was a legacy path that never synced to the cloud and was deleted on 2026-04-30 after a one-time bootstrap.

### Rules

1. **Never write or edit files under `~/.claude/skills/`.** The directory is gone; recreating it does nothing because Cowork doesn't read from it. Any session that tries this is wasting time.
2. **Never use `request_cowork_directory` to mount `~/.claude/skills/`.** Same reason.
3. **To edit an existing skill** (e.g., `blog-post-writer`, `seo-aeo-expert`): tell Jacob to open https://claude.ai/customize/skills, click the skill in the left list, edit the markdown inline, and save. 30 seconds, no file involved.
4. **To create a new skill**: tell Jacob to open https://claude.ai/customize/skills, click `+` → `Create skill` → `Write skill instructions` (or `Create with Claude` for chat-driven authoring), paste/type the markdown, and save.
5. **When you (Claude in a Cowork session) author or revise skill content**: write the markdown in the chat reply, then ask Jacob to paste it into the web UI editor. Cowork has no API to write to the registry directly. (When Anthropic ships an upsert tool, this rule changes — until then, paste-via-web-UI is the workflow.)
6. **The plugin cache** at `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/<session>/<user>/skills/` is a snapshot synced down from the cloud at session start. Read-only for diagnostic purposes. Never write to it — your writes get overwritten on the next sync.

## Output Formatting (Mandatory)

Always present terminal commands and preview URLs in fenced code blocks so Jacob can copy them easily. Never put commands or URLs in plain paragraph text.

**Example:**
```
cd ~/Documents/Claude/Projects/selling303-site
npx astro dev
```
Preview: `http://localhost:4321/blog/post-slug`
