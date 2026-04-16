import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Draft success stories — excluded from sitemap (pages render with noindex meta tag).
// Remove a slug from this list once the story has real content + photos.
const DRAFT_SUCCESS_STORY_SLUGS = [
  '8781-flora-ct-arvada',
  '22461-e-union-circle-aurora',
  '4360-w-wagon-trail-dr-denver',
  '9559-w-coal-mine-ave-littleton',
  '301-w-lehow-ave-englewood',
  '10315-ravenswood-ln-highlands-ranch',
];

export default defineConfig({
  site: 'https://selling303.com',
  output: 'static',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      filter: (page) => !DRAFT_SUCCESS_STORY_SLUGS.some((slug) =>
        page.includes(`/sell/success-stories/${slug}`)
      ),
    }),
  ],
  image: {
    // Sharp is Astro's default — handles WebP/AVIF generation at build time
    // All images in src/assets/ are auto-optimized when used via <Image> or getImage()
  },
  build: {
    assets: '_assets',
  },
});
