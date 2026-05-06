# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

_(queue cleared after 2026-05-06 PM production deploy — see DEPLOY_LOG.md)_

## Pending

- **2026-05-06** — Three new GBP-image generator scripts in `scripts/`: `generate-gbp-image.py` (Numeric Hero Card — Tier-2 Option 1, reusable for every blog post), `generate-gbp-data-viz.py` (Live Data Snapshot — Tier-2 Option 3, deadline-spine template), `generate-gbp-phone-mockup.py` (Phone Mockup — Tier-2 Option 2, brand-faithful widget render). All Python+Pillow, system-font-only, zero external dependencies. Replaces Canva for GBP image generation. Awaiting Jacob's pick on which to use as the default for the 2026 NOV protest post.
