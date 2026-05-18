// Static OG image endpoint. Generates a 1200×630 PNG per page at build time and writes
// it to dist/og/<slug>.png. Pages reference these via og:image / twitter:image meta tags.
//
// URL → variant map:
//   /og/blog/<slug>.png            → blog variant   (title from blog frontmatter, badge = category)
//   /og/neighborhoods/<slug>.png   → neighborhood variant (title from frontmatter, badge = county)
//   /og/<static-page>.png          → default variant (title from OG_STATIC_TITLES map)
//
// Adding a new static page: also add an entry to OG_STATIC_TITLES below or it won't get
// an OG image. Adding a blog post or neighborhood is automatic — they come from
// getCollection().

import type { APIRoute, GetStaticPaths } from 'astro';
import { getCollection } from 'astro:content';
import { renderOG, countyFor, type OGVariant } from '../../lib/og';

// Short, OG-card-optimized titles for static pages. The pages' own <title> tags are
// SEO-tuned and often too long for a social card — these are the punchy versions.
const OG_STATIC_TITLES: Record<string, string> = {
  index: 'South Denver Metro Real Estate',
  about: 'About Jacob Stark',
  contact: 'Contact Jacob Stark',
  properties: 'Browse Properties',
  neighborhoods: 'South Denver Neighborhoods',
  'expired-listings': 'Expired Listings Specialist',
  'first-time-homebuyers': 'First-Time Homebuyers',
  'first-time-homesellers': 'First-Time Home Sellers',
  'investor-tools': 'Investor Tools',
  'move-up-sellers': 'Move-Up Sellers',
  'my-seller-promise': 'My Seller Promise',
  'new-construction': 'New Construction',
  relocation: 'Relocation to Denver',
  resources: 'Resources & Guides',
  tools: 'Free Real Estate Tools',
  'tools/closing-cost-estimator': 'Closing Cost Estimator',
  'tools/cost-of-living-calculator': 'Cost of Living Calculator',
  'tools/home-equity-calculator': 'Home Equity Calculator',
  'sell/success-stories': 'Recent Success Stories',
  blog: 'Selling 303 Blog',
  'clientclarity-demo': 'ClientClarity Demo',
};

interface PathProps {
  variant: OGVariant;
  title: string;
  badge: string | null;
}

export const getStaticPaths: GetStaticPaths = async () => {
  const paths: { params: { slug: string }; props: PathProps }[] = [];

  // Blog: title from frontmatter, badge = category
  const posts = await getCollection('blog');
  for (const post of posts) {
    paths.push({
      params: { slug: `blog/${post.id}` },
      props: {
        variant: 'blog',
        title: post.data.title,
        badge: post.data.category,
      },
    });
  }

  // Neighborhoods: title from frontmatter, badge = county (looked up by slug)
  const neighborhoods = await getCollection('neighborhoods');
  for (const n of neighborhoods) {
    paths.push({
      params: { slug: `neighborhoods/${n.id}` },
      props: {
        variant: 'neighborhood',
        title: n.data.title,
        badge: countyFor(n.id),
      },
    });
  }

  // Static pages: title from hardcoded map, no badge
  for (const [slug, title] of Object.entries(OG_STATIC_TITLES)) {
    paths.push({
      params: { slug },
      props: { variant: 'default', title, badge: null },
    });
  }

  return paths;
};

export const GET: APIRoute = async ({ props }) => {
  const { variant, title, badge } = props as unknown as PathProps;
  const png = await renderOG({ variant, title, badge });

  return new Response(new Uint8Array(png), {
    headers: {
      'Content-Type': 'image/png',
      // Long cache — Astro hashes the URL by slug, so a re-render with a new title
      // would land at the same URL. Force-rebuild Netlify clears this when needed.
      'Cache-Control': 'public, max-age=31536000, immutable',
    },
  });
};
