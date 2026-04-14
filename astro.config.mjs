import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://selling303.com',
  output: 'static',
  trailingSlash: 'never',
  integrations: [
    sitemap(),
  ],
  image: {
    // Sharp is Astro's default — handles WebP/AVIF generation at build time
    // All images in src/assets/ are auto-optimized when used via <Image> or getImage()
  },
  build: {
    assets: '_assets',
  },
});
