# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-04-26 production deploy — see DEPLOY_LOG.md)_

## Pending

- 2026-04-26 — [VISUAL] `closing-costs-littleton-first-time-buyers-2026.md` — replaced the plain `<table>` "What does a $475K Littleton closing sheet actually look like?" with a styled settlement-statement visual. Brand navy header strip, category sections (Down Payment, Lender Fees, Title Fees, Prepaid Items with 3 sub-items, Other Costs with 2 sub-items), tabular dollar amounts, dashed sub-section dividers, prominent navy total row at the bottom ($32,000–$43,900). Inline styles only, real text in DOM (AEO-friendly), source attribution baked in. Differentiates visually from the upper bucket-overview cost-breakdown card.
