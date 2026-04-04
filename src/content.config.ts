import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const neighborhoods = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/neighborhoods' }),
  schema: z.object({
    title: z.string(),
    metaTitle: z.string(),
    description: z.string(),
    heroSubtext: z.string(),
    aboutHeading: z.string(),
    aboutParagraphs: z.array(z.string()),
    aboutImage: z.object({
      url: z.string(),
      alt: z.string(),
    }),
    stats: z.object({
      medianPrice: z.string(),
      avgDOM: z.string(),
      listPriceReceived: z.string(),
      activeListings: z.string(),
      source: z.string(),
      sourceDate: z.string(),
    }),
    realscoutSearchUrl: z.string(),
    amenities: z.array(z.object({
      icon: z.string(),
      title: z.string(),
      description: z.string(),
    })),
    showingTimeCharts: z.array(z.object({
      url: z.string(),
      alt: z.string(),
    })).optional(),
    relatedPosts: z.array(z.object({
      title: z.string(),
      tag: z.string(),
      description: z.string(),
      date: z.string(),
    })),
    cta: z.object({
      heading: z.string(),
      text: z.string(),
    }),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    headline: z.string().optional(),
    description: z.string(),
    date: z.string(),
    dateModified: z.string().optional(),
    category: z.string(),
    tag: z.string(),
    readTime: z.string(),
    heroLabel: z.string(),
    heroSubtext: z.string(),
    cardImage: z.object({ url: z.string(), alt: z.string() }),
    ogImage: z.string().optional(),
    aboutPlaces: z.array(z.string()).optional(),
    keywords: z.string().optional(),
    faqSchema: z.array(z.object({
      question: z.string(),
      answer: z.string(),
    })).optional(),
    relatedPosts: z.array(z.object({
      slug: z.string(),
      title: z.string(),
      tag: z.string(),
      description: z.string(),
      image: z.object({ url: z.string(), alt: z.string() }),
      date: z.string(),
    })).optional(),
  }),
});

export const collections = { neighborhoods, blog };
