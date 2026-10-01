// ─────────────────────────────────────────────────────────────
// Agent + brokerage config — SINGLE SOURCE OF TRUTH
//
// Every brokerage mention, license line, and trust stat on the site
// reads from this file. If Jacob changes brokerages or a stat changes,
// edit it HERE (plus swap the logo file) — nothing else should need
// to change. Exceptions: blog post markdown bodies (src/content/blog)
// and one-off open-house pages, which are point-in-time content.
// ─────────────────────────────────────────────────────────────
import brokerageLogoWhite from '../assets/images/orchard-logo-white.png';

export const brokerage = {
  name: 'Orchard',
  legalName: 'Orchard Brokerage LLC',
  url: 'https://orchard.com',
  agentProfileUrl: 'https://orchard.com/agent/jacob-stark',
  logoWhite: brokerageLogoWhite,
  // How Jacob delivers each generic solution today. Content should name the
  // generic solution first and mention these only as "how I deliver it today."
  programs: {
    buyBeforeYouSell: 'Move First',
    managedRenovation: 'Concierge',
    renovationFinancingPartner: 'Notable',
    cashOffer: 'Orchard Offers',
  },
  // Required disclosures, verbatim from Orchard's pre-approved materials.
  // Show renovationFinancing anywhere pay-at-closing renovation funding is described.
  disclosures: {
    renovationFinancing:
      'Interest may apply. Rules and exclusions apply. Orchard Technologies Inc. and Notable Finance, LLC do not guarantee or warranty any results. Subject to the terms and conditions of your loan agreement with Notable Finance, LLC. Orchard Technologies Inc. is not providing loans as part of the Orchard Concierge program. Funds provided by Notable (plus interest, if any) are to be repaid once one of the following happens (whichever occurs first): your home sells, termination of your listing agreement, twelve months after origination or the date on which Notable otherwise suspends your loan for any reasons stated in your loan agreement, whichever occurs sooner. Orchard Advance loans are provided by Notable Finance, LLC, NMLS# 1824748 and are made or arranged pursuant to a California Finance Lenders Law license. Loan eligibility is not guaranteed and all loans are subject to credit approval and underwriting by Notable. Subject to terms and conditions https://orchardadvance.notablefi.com.',
    // Short, general version for pages that describe pay-at-closing financing generically (no program named).
    renovationFinancingShort:
      'Renovation financing is provided by third-party lenders and is subject to credit approval and loan terms. Interest may apply. Results are not guaranteed.',
    equityAdvance:
      'Equity advance eligibility is subject to approval and is not guaranteed. Advance amounts depend on your home equity and qualification.',
  },
} as const;

export const agent = {
  name: 'Jacob Stark',
  title: 'REALTOR®',
  titleLine: `REALTOR® at ${brokerage.name}`,
  phone: '303-997-0634',
  phoneHref: 'tel:3039970634',
  email: 'jacob@selling303.com',
  licenseNumber: 'FA100087287',
  licenseLine: 'CO Lic #FA100087287',
  // Google Calendar booking links. ⚠️ The site uses four different links —
  // Jacob to confirm which appointment type each one is.
  bookingUrls: {
    general: 'https://calendar.google.com/appointments/schedules/AcZssZ1IQnv63S33Xa9RM4uw0QVo3EfHmxpZeKBQQ33xNKijXnIQ-TXY_DHxc6BdCqpNlrFmGEsaF1gy',
    moveUp: 'https://calendar.google.com/appointments/schedules/AcZssZ2UpHf-eRXBp5EhsEaj3h4tdL6UFcyrAVj2Ml1tNyGDAGwLXKSq-61crE41j57Q41IFr7Xj9gyv',
  },
  // Updated 2026-09-30 from Jacob's Orchard listing deck (confirmed current).
  stats: {
    salesVolume: '$50M+',
    salesVolumeShort: '$50M',
    familiesHelped: '84',
    saleToList: '101.8%',
    avgDaysOnMarket: '19',
    googleRating: '5.0',
    googleReviewCount: '47',
  },
} as const;
