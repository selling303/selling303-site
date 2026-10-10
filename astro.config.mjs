import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { execSync } from 'node:child_process';
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

// Draft success stories — excluded from sitemap (pages render with noindex meta tag).
// Derived from `draft: true` in each story's frontmatter, so a story leaves the
// sitemap automatically while it's a draft and returns once the flag is removed.
const SUCCESS_STORY_DIR = new URL('./src/content/success-stories/', import.meta.url);
const DRAFT_SUCCESS_STORY_SLUGS = readdirSync(SUCCESS_STORY_DIR)
  .filter((f) => f.endsWith('.md'))
  .filter((f) => {
    const frontmatter = readFileSync(new URL(f, SUCCESS_STORY_DIR), 'utf8').split(/^---\s*$/m)[1] || '';
    return /^draft:\s*true\s*$/m.test(frontmatter);
  })
  .map((f) => f.replace(/\.md$/, ''));

// Build-time fallback for lastmod when git lookup fails (e.g., un-tracked files).
const BUILD_ISO = new Date().toISOString();

// Map a public URL path back to the source file(s) most likely to be its source.
// Returns the first candidate that exists on disk.
const REPO_ROOT = path.dirname(fileURLToPath(import.meta.url));
function urlPathToSourceFile(urlPath) {
  const clean = urlPath.replace(/^\/+|\/+$/g, '');
  if (!clean) return 'src/pages/index.astro';

  // Dynamic content collections — check before the generic pages fallback.
  if (clean.startsWith('blog/')) {
    const slug = clean.slice('blog/'.length);
    return `src/content/blog/${slug}.md`;
  }
  if (clean.startsWith('neighborhoods/')) {
    const slug = clean.slice('neighborhoods/'.length);
    return `src/content/neighborhoods/${slug}.md`;
  }
  if (clean.startsWith('sell/success-stories/')) {
    const slug = clean.slice('sell/success-stories/'.length);
    return `src/content/success-stories/${slug}.md`;
  }

  // Static .astro pages — try index.astro first, then bare .astro.
  const candidates = [
    `src/pages/${clean}/index.astro`,
    `src/pages/${clean}.astro`,
  ];
  for (const rel of candidates) {
    if (existsSync(path.join(REPO_ROOT, rel))) return rel;
  }
  return null;
}

// Cache git lookups so a build doesn't shell out 80+ times.
const gitDateCache = new Map();
function gitLastModISO(relPath) {
  if (!relPath) return null;
  if (gitDateCache.has(relPath)) return gitDateCache.get(relPath);
  let iso = null;
  try {
    const out = execSync(`git log -1 --format=%cI -- "${relPath}"`, {
      cwd: REPO_ROOT,
      encoding: 'utf-8',
      stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    iso = out || null;
  } catch {
    iso = null;
  }
  gitDateCache.set(relPath, iso);
  return iso;
}

export default defineConfig({
  site: 'https://selling303.com',
  output: 'static',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      // Exclude unlisted open house pages (noindex, texted to attendees only).
      filter: (page) =>
        !page.includes('/open-house/') &&
        !page.includes('/assumable-loans/list') &&
        !page.includes('/thank-you') &&
        !DRAFT_SUCCESS_STORY_SLUGS.some((slug) =>
          page.includes(`/sell/success-stories/${slug}`)
        ),
      serialize(item) {
        try {
          const u = new URL(item.url);
          const rel = urlPathToSourceFile(u.pathname);
          const iso = gitLastModISO(rel) || BUILD_ISO;
          item.lastmod = iso;
        } catch {
          item.lastmod = BUILD_ISO;
        }
        return item;
      },
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
