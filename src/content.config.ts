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
    cardImage: z.object({ url: z.string(), alt: z.string() }).optional(),
    cardStat: z.string().optional(),
    cardStatLabel: z.string().optional(),
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
      image: z.object({ url: z.string(), alt: z.string() }).optional(),
      date: z.string(),
    })).optional(),
  }),
});

const successStories = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/success-stories' }),
  schema: z.object({
    title: z.string(),
    metaTitle: z.string(),
    description: z.string(),
    headline: z.string(),
    closeDate: z.string(),
    address: z.object({
      street: z.string(),
      city: z.string(),
      state: z.string(),
      zip: z.string(),
    }),
    situationType: z.string(),
    specializationPillar: z.string().optional(),
    neighborhoodPillar: z.string().optional(),
    results: z.object({
      listPrice: z.number(),
      closedPrice: z.number(),
      daysOnMarket: z.number(),
      percentOfList: z.number(),
    }),
    propertyDetails: z.object({
      bedrooms: z.number(),
      bathrooms: z.number(),
      sqft: z.number().optional(),
      lotSize: z.string().optional(),
      parking: z.string().optional(),
      yearBuilt: z.number().optional(),
      mls: z.string().optional(),
    }),
    story: z.object({
      situation: z.string(),
      challenge: z.string(),
      strategy: z.array(z.string()),
      strategyNarrative: z.string().optional(),
    }),
    testimonials: z.array(z.object({
      name: z.string(),
      text: z.string(),
      rating: z.number().default(5),
    })),
    heroImage: z.object({ src: z.string(), alt: z.string() }),
    images: z.array(z.object({
      src: z.string(),
      alt: z.string(),
      category: z.enum(['exterior', 'interior', 'kitchen', 'bathroom', 'bedroom', 'living', 'outdoor', 'detail', 'floorplan', 'other']).optional(),
    })),
    videoUrl: z.string().optional(),
    tour3dUrl: z.string().optional(),
    faqSchema: z.array(z.object({
      question: z.string(),
      answer: z.string(),
    })).optional(),
    ogImage: z.string().optional(),
    sortOrder: z.number().optional(),
    draft: z.boolean().optional(),
  }),
});

export const collections = { neighborhoods, blog, successStories };
