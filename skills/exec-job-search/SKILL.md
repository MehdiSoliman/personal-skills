---
name: exec-job-search
description: Use when positioning an exec for a job search (LinkedIn/CV).
version: 1.0.0
author: curator
license: MIT
---

# Executive Job Search Positioning

## When to Use

When a senior product/exec leader (especially Mehdi) is running an active Director/VP Product search and needs positioning help — target-profile clarity, LinkedIn headline/About, CV alignment, folio, prospection, or interview prep. Trigger words: "job search", "positionnement", "LinkedIn", "CV", "recherche d'emploi", "VP Product".

Help a senior product leader (default user: **Mehdi**, a Director/VP Product leader) position themselves for an active Director/VP Product search. This is an **ongoing multi-session project** — artifacts live in `~/jobhunt/` (`cible.md` target brief, `cv.md`, plus a Google Doc "CV - v2 Hermes").

## Workflow (order matters)

1. **Target clarity FIRST** — before any positioning or prospection. Extract in conversation: energy source, company type/operating model, domain, role, compensation, constraints. Save to a `cible.md` brief (see `references/mehdi-target-profile.md`). The "clarity first" rule avoids prospecting before knowing what/who we're selling.
2. **Skills discovery** — check the community skills ecosystem before hand-crafting (`npx skills find "job search"` etc., verify on skills.sh incl. the Trust Hub security audit, install via `hermes skills install` with quarantine + `skills-guard-v2` scan). See `references/job-search-skills-ecosystem.md`.
3. **LinkedIn positioning** — headline then About, iteratively, with `sepia` (architecture) + `humanizer` (surface).
4. **CV alignment** — mirror the LinkedIn positioning; ADD people/management content for VP roles.
5. **Folio / portfolio** — he wants a **simple personal landing page first** (v1 = who he is + talks links + CV download + LinkedIn), NOT case studies yet (deferred). Chosen direction: `003-mono-twist` (monochrome + orange accent + mono labels + hand-drawn "human" underline), with his photo (color, 4:5 portrait) and subtle "human" animations. Domain `mehdisoliman.me`, deployment later (Netlify). Site lives in `~/jobhunt/site/`. Build + crop recipes in `references/design-tooling.md`.
6. **Prospection** — VP roles are mostly **off-market** (recruiting firms reach out directly), not job boards.

## Mehdi's hard preferences (embed these — he WILL correct you)

- **Anti-AI-slop**: every draft goes through `sepia` + `humanizer`. Never write "passionate about building products that matter" or clever/performative hooks ("I can show the numbers").
- **Headline**: no numbers, no "PLG" (he considers it passé), no "ex-PayFit" (avoids boxing him in as "the PayFit guy"). Keep "Human-first" + AI as its OWN section + "Angel investor". Title = "VP / Product Leader" (NOT "Director of Product"). Final: `VP / Product Leader — Human-first · AI Product Strategy · Angel investor`.
- **About**: narrative/positioning, NOT an achievement list — that's the Experience section's job (he will flag redundancy). Keep the "Beyond product" closer (investor at Upscalers, restaurants, father's fruit-and-veg shop). "coach first, manager second" is a STRENGTH (SVPG/Cagan), not a soft signal.
- **Numbers**: never invent. Verify — public estimates (GetLatka etc.) can be WRONG; trust his insider numbers.
- **Career facts**: PayFit Oct 2018 → shown as "Jan 2026" (his choice, to shorten the unemployment gap); employee ~#100; ARR ~$80M **and profitable** (he prefers leading with "profitability" over the ARR figure); **Synthesio** (NOT "Synthesion"), acquired by Ipsos; **Primo** (Feb–Jul 2026, a 20-person startup that stalled on the human side) is intentionally OMITTED from CV/LinkedIn — keep it as an interview talking point only.

## Design rules (CV / site)

- **No dashes** — no em-dashes ("—") or en-dashes ("–") anywhere; use commas, periods, "·", "→". He hates the dash punctuation style.
- **Monochrome** — no blue. Near-black + grays, no color accent unless he asks.
- **Airy** — generous line-height, bullets indented with a gap from titles (not flush-left with them).
- **Dates inline** with titles, NOT a right-aligned far column (he finds that hard to read).
- **Bold key metrics only** ($2.1B, €15M ARR, −20% churn, "coach first") — bolding everything kills the effect.
- **Max 2 pages** for the CV.
- **Skills section (VP)**: add a distinct "Product Strategy" (vision, trajectory, roadmap, positioning) separate from "AI Product Strategy"; consolidate the IC craft skills (Discovery/Prioritization/Delivery/Design) into ONE "Product craft" line — four IC lines read "PM, not VP". Avoid "portfolio" as a strategy term (collides with the folio he's building) → use "positioning".
- **Tooling**: designed CV = WeasyPrint HTML→PDF; mockup previews without a browser = WeasyPrint HTML→PNG (page size in px) + pymupdf. See `references/design-tooling.md`.

## Pitfalls

- Don't re-list achievements in the About (redundant with Experience).
- Don't box him into one company/domain — he's "mission-first, domain-open", NOT "ex-PayFit".
- VP = manager: the CV MUST show people leadership (grew people, coached, hired), not just product metrics.
- "coach over manager" is a differentiator, not a demotion signal.
- VP roles are off-market — don't waste time scraping job boards; route through recruiting firms.
- When asked "how do you define the product role?" (Cagan's Rorschach test), his answer should be his thesis (human-first + people→agents + "knowing what should exist"), not generic "discover/deliver".

## References

- `references/mehdi-target-profile.md` — full target brief (moteur, boîte, domaine, poste, rému).
- `references/svpg-product-role-insights.md` — Cagan/Evans: the 3 product skills, the Rorschach interview question, "most people aren't tool builders".
- `references/job-search-skills-ecosystem.md` — community skills for job search + how to vet them.
- `references/design-tooling.md` — WeasyPrint HTML→PDF/PNG recipes, CV design tokens, site mockup stances.
- `scripts/google_doc_replace.py` — copy/replace a Google Doc with a local markdown file (publish CVs to Drive for review).
