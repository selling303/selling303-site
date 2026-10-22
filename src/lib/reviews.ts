// Shared helpers for Google review data (src/data/reviews.json).
// Used by /reviews and the ReviewQuotes component on seller pages.
import reviews from '../data/reviews.json';

export type Review = (typeof reviews)[number];

export const dealTypeLabels: Record<string, string> = {
  buyer: 'Buyer',
  seller: 'Seller',
  'move-up': 'Move-up',
  investor: 'Investor',
  'new-construction': 'New construction',
};

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
export const formatReviewDate = (d: string) => {
  const [y, m] = d.split('-');
  return `${months[Number(m) - 1]} ${y}`;
};

// Stable anchor for a review on /reviews, e.g. /reviews#review-jo-ann-mcintosh
export const reviewAnchor = (name: string) =>
  'review-' + name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

export const reviewInitials = (n: string) =>
  n.replace(/[^A-Za-z&\s]/g, '').trim().split(/\s+/).slice(0, 2).map((w) => w[0]?.toUpperCase()).join('');

export const allReviews: Review[] = [...reviews].sort((a, b) => b.date.localeCompare(a.date));

// Featured: seller and move-up reviews first, then newest first.
const typeRank = (r: Review) => (r.dealType.includes('move-up') || r.dealType.includes('seller') ? 0 : 1);
export const featuredReviews: Review[] = allReviews
  .filter((r) => r.featured)
  .sort((a, b) => typeRank(a) - typeRank(b) || b.date.localeCompare(a.date));

export const reviewsByName = (names: string[]) =>
  names.map((n) => {
    const r = allReviews.find((x) => x.name === n);
    if (!r) throw new Error(`Review not found in reviews.json: ${n}`);
    return r;
  });

// featuredQuote is a verbatim excerpt; if it starts mid-sentence, lead with an ellipsis.
export const excerpt = (q: string) => (/^[a-z]/.test(q) ? `…${q}` : q);

// Labels to show on a card. "Move-up" already means sold and bought, so when a review is
// tagged move-up we hide the redundant seller/buyer pills (the data keeps all tags).
export const displayTypes = (r: Review) =>
  r.dealType.includes('move-up') ? r.dealType.filter((t) => t !== 'seller' && t !== 'buyer') : r.dealType;
