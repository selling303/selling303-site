// RSS feed for Selling 303 blog
// Used by RSS readers, Apple News Publisher (channel ingest), Feedly, and AI engines
// that crawl feeds for fresh-content discovery (Perplexity, etc.)

import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import MarkdownIt from 'markdown-it';
import sanitizeHtml from 'sanitize-html';

const parser = new MarkdownIt({ html: true, linkify: true });

export async function GET(context) {
  const posts = await getCollection('blog');

  const sorted = posts.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  return rss({
    title: 'Selling 303 — South Denver Real Estate',
    description:
      "Market data, neighborhood guides, and seller/buyer advice for the South Denver metro from Realtor Jacob Stark.",
    site: context.site,
    items: sorted.map((post) => ({
      title: post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.description,
      link: `/blog/${post.id}`,
      content: sanitizeHtml(parser.render(post.body || ''), {
        allowedTags: sanitizeHtml.defaults.allowedTags.concat([
          'img',
          'figure',
          'figcaption',
        ]),
        allowedAttributes: {
          ...sanitizeHtml.defaults.allowedAttributes,
          '*': ['class', 'id', 'itemscope', 'itemtype', 'itemprop'],
          img: ['src', 'alt', 'width', 'height', 'loading'],
          a: ['href', 'name', 'target', 'rel'],
        },
      }),
      categories: [post.data.category, post.data.tag].filter(Boolean),
    })),
    customData: `<language>en-us</language><copyright>© ${new Date().getFullYear()} Jacob Stark, Selling 303. All rights reserved.</copyright>`,
    stylesheet: false,
  });
}
