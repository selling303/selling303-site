// OG image generator for selling303.com.
//
// Three template variants — blog, neighborhood, default — composed into a 1200×630 PNG
// using Satori (JSX → SVG) and @resvg/resvg-js (SVG → PNG). Called from the build-time
// endpoint at src/pages/og/[...slug].png.ts, which produces a static PNG per page under
// dist/og/. Pages set og:image to https://selling303.com/og/<slug>.png.
//
// Visual design approved 2026-05-18 against a Pillow mockup. If you change the layout,
// regenerate the mockups first — see /Users/jacobstark/Library/.../outputs/og-mockup.py.
//
// Fonts: Satori does NOT support WOFF2 (only TTF/OTF/WOFF). The site-wide fonts in
// public/fonts/ are WOFF2 and unusable here — keep TTF copies isolated in this folder
// rather than duplicating in public/fonts/. OFL license permits redistribution.

import fs from 'node:fs/promises';
import path from 'node:path';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';

// Resolve assets against the project root, NOT import.meta.url. At build time this
// module gets bundled into dist/.prerender/chunks/ and import.meta.url points there;
// '../assets' from that location resolves to dist/.prerender/assets/ which doesn't
// exist (Astro doesn't copy src/assets/ into the prerender output). process.cwd() is
// the project root during `astro build` both locally and on Netlify.
const ASSETS = path.resolve(process.cwd(), 'src/assets');

// Brand tokens — keep in sync with brand-style-guide skill. The gold accent (#c8965a)
// is sampled from the wordmark; document there once we update the brand skill.
const NAVY_DARK = '#001825';
const NAVY = '#002a3a';
const GOLD = '#c8965a';
const WHITE = '#ffffff';

// Card geometry — Open Graph standard 1.91:1.
const W = 1200;
const H = 630;

// Cache binary assets at module scope so each render reuses the same buffers.
// Astro's build calls the endpoint once per slug; without caching we'd re-read every time.
let cached: {
  wordmark: string;
  headshot: string;
  fontSerif: Buffer;
  fontSans: Buffer;
} | null = null;

async function loadAssets() {
  if (cached) return cached;

  const wordmarkBuf = await fs.readFile(
    path.join(ASSETS, 'selling303-logo/selling303-wordmark-on-dark.png')
  );
  const headshotBuf = await fs.readFile(
    path.join(ASSETS, 'og/jacob-stark_headshot_800x800.png')
  );
  const fontSerif = await fs.readFile(
    path.join(ASSETS, 'og/fonts/DMSerifDisplay-Regular.ttf')
  );
  const fontSans = await fs.readFile(
    path.join(ASSETS, 'og/fonts/Inter-SemiBold.ttf')
  );

  // Satori accepts data: URLs for raster images. Encode once.
  cached = {
    wordmark: `data:image/png;base64,${wordmarkBuf.toString('base64')}`,
    headshot: `data:image/png;base64,${headshotBuf.toString('base64')}`,
    fontSerif,
    fontSans,
  };
  return cached;
}

// Slug → county map for the neighborhood variant. Mirrors the hardcoded mappings in
// src/pages/neighborhoods.astro (NeighborhoodCard county prop). Source of truth lives
// there; this is a denormalized copy for OG rendering. If counties drift, update both.
const NEIGHBORHOOD_COUNTY: Record<string, string> = {
  littleton: 'Arapahoe County',
  'highlands-ranch': 'Douglas County',
  centennial: 'Arapahoe County',
  englewood: 'Arapahoe County',
  parker: 'Douglas County',
  lakewood: 'Jefferson County',
  'lone-tree': 'Douglas County',
  'castle-pines': 'Douglas County',
  'greenwood-village': 'Arapahoe County',
};

export function countyFor(slug: string): string | null {
  return NEIGHBORHOOD_COUNTY[slug] ?? null;
}

export type OGVariant = 'blog' | 'neighborhood' | 'default';

export interface OGInput {
  variant: OGVariant;
  title: string;
  badge?: string | null; // category for blog, county for neighborhood, omitted for default
}

// Tiny createElement equivalent. Satori accepts {type, props} trees where props.children
// are nested elements. This avoids pulling React in just for JSX.
function h(type: string, props: Record<string, unknown> = {}, ...children: unknown[]): unknown {
  return {
    type,
    props: { ...props, children: children.length === 1 ? children[0] : children },
  };
}

function buildTemplate(input: OGInput, assets: NonNullable<typeof cached>): unknown {
  const { title, badge } = input;

  // Letter-space the badge by inserting hair-spaces between characters. Satori's
  // letterSpacing CSS prop is supported but render quality on uppercase tracking is
  // more reliable when we control the spacing directly.
  const spacedBadge = badge ? badge.toUpperCase().split('').join(' ') : null;

  return h(
    'div',
    {
      style: {
        display: 'flex',
        width: '100%',
        height: '100%',
        background: `linear-gradient(135deg, ${NAVY_DARK} 0%, ${NAVY} 100%)`,
        position: 'relative',
        fontFamily: 'Inter',
      },
    },
    // Wordmark — top-left. The source PNG is 924×540 with content in the upper band;
    // displaying at 280×164 keeps the wordmark legible without dominating the card.
    h('img', {
      src: assets.wordmark,
      width: 280,
      height: 164,
      style: { position: 'absolute', top: 40, left: 72 },
    }),
    // Headshot — bottom-right, bleeding past the right and bottom edges to give depth.
    h('img', {
      src: assets.headshot,
      width: 560,
      height: 560,
      style: { position: 'absolute', right: -40, bottom: -50 },
    }),
    // Text block — left side, vertically centered, max width 620 so it doesn't
    // overlap the headshot which begins around x≈720.
    h(
      'div',
      {
        style: {
          display: 'flex',
          flexDirection: 'column',
          position: 'absolute',
          left: 80,
          top: 240,
          width: 620,
        },
      },
      spacedBadge
        ? h(
            'div',
            {
              style: {
                color: GOLD,
                fontFamily: 'Inter',
                fontWeight: 600,
                fontSize: 24,
                marginBottom: 24,
              },
            },
            spacedBadge
          )
        : null,
      h(
        'div',
        {
          style: {
            color: WHITE,
            fontFamily: 'DM Serif Display',
            fontSize: 72,
            lineHeight: 1.15,
            // No font-weight here — DM Serif Display has only one weight, and setting
            // weight: 700 makes Satori synthesize fake bold which prints lumpy serifs.
          },
        },
        title
      )
    )
  );
}

export async function renderOG(input: OGInput): Promise<Buffer> {
  const assets = await loadAssets();

  const svg = await satori(buildTemplate(input, assets) as Parameters<typeof satori>[0], {
    width: W,
    height: H,
    fonts: [
      { name: 'DM Serif Display', data: assets.fontSerif, weight: 400, style: 'normal' },
      { name: 'Inter', data: assets.fontSans, weight: 600, style: 'normal' },
    ],
  });

  const resvg = new Resvg(svg, {
    fitTo: { mode: 'width', value: W },
    font: { loadSystemFonts: false }, // deterministic builds — never accidentally pull a system font
  });
  return resvg.render().asPng();
}
