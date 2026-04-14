# Deploy Queue

Changes waiting to be pushed to production. Each conversation logs what it changed here. When Jacob approves a deploy, summarize everything below, push, then clear the list.

---

- 2026-04-14 Updated `why-house-not-selling-denver.md`: added overpricing diagnostic framework (showing-activity-to-price tiers table, NAR Confidence Index link) as new H3 subsection within Reason #1
- 2026-04-14 Updated overpricing tier visual with brand-aligned muted color palette (#8b3a3a → #9e6b3a → #8a7a3a → #4a7c59)
- 2026-04-14 HOTFIX: Converted inline SVG in parks blog post from `<style>`/class-based to inline styles — `<style>` tag inside SVG `<defs>` caused Astro content collection to silently skip the page (404 on production). Same fix applied to standalone SVG asset
