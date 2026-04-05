# selling303.com — Project Rules

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
