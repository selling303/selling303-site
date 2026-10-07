# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-09-29 production deploy — merge c7353b9, see DEPLOY_LOG.md.)_

## Pending

_(queue cleared after 2026-10-06 production deploy — merge 57deeaa, see DEPLOY_LOG.md.)_
- 2026-10-03 — `/assumable-loans`: "Why Everyone's Asking" moved under the Short Answer (above the list form) with two side-by-side 3%-loan scenarios on a $600K home vs. a new loan at the page's `rate` const, same cash down: balance ~92% ($50K cash, saves ~$1,155/mo) and 70% ($180K cash, saves ~$880/mo). Old 3-column cash-to-close table removed; #cash-to-close now covers second loans. TOC gained "The Numbers". Table fits at 390px. NOTE: scenario payments are hard-coded; recompute if `rate` changes.
