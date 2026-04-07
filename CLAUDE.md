# selling303.com — Project Rules

## Deploy Queue Protocol (Mandatory)

When making changes to the repo, log each change as a bullet in `DEPLOY_QUEUE.md` with the date and a brief description. Before deploying, read `DEPLOY_QUEUE.md` and summarize all queued changes for Jacob. After a successful deploy, clear the list (keep the header). Use the `deploy-to-netlify` skill for all deploys — never attempt `git push` from the sandbox.

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
