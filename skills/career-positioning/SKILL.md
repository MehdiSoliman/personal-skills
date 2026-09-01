---
name: career-positioning
description: Use when crafting Mehdi's job-search positioning docs.
version: 1.0.0
author: curator
license: MIT
---

# Career Positioning (Mehdi's job search)

Crafting Mehdi's executive positioning for his Director/VP Product search. The target profile lives in `~/jobhunt/cible.md` — **read it first, never re-ask what's already there**. Locked headline/About/CV text lives in `references/approved-positioning.md`.

## When to Use
- Editing Mehdi's LinkedIn (headline, About, Experience dates/skills).
- Aligning or drafting his CV or folio.
- Any job-search positioning or career-narrative work for Mehdi.

## Workflow (order matters)
1. **Clarify the target first** (energy/motivation → company type → domain → role → compensation). Done for Mehdi — see `~/jobhunt/cible.md`. Don't draft copy before the target is locked.
2. **Then position, in this order**: headline → About → CV → folio.
3. **Iterate, don't hand one answer.** Mehdi co-creates in small passes. Give 2–4 concrete options per decision, state your pick, let him steer. 2–3 sharp questions at a time, never a wall.

## Validated positioning
- **Title**: "VP / Product Leader" — NOT "Director of Product" (undersells his target). He's open to Director/Head of Product as *roles*, but the headline leads VP/Product Leader.
- **Three tags he validated**: "Human-first" · "AI Product Strategy" · "Angel investor".
  - "AI Product Strategy" beat "AI-native", "AI-driven", and "AI Builder" (those read techy/IC; "Builder" undermines the leader signal — flag if he floats it again).
  - "Human-first" is his signature differentiator — keep it prominent.
- **PayFit framed as IMPACT, not affiliation**: "helped scale PayFit into a $2.1B unicorn (employee ~#100)", not "ex-PayFit" or "7 years at PayFit". He rejected "ex-PayFit" in the headline.
- **Management/people is a first-class VP signal.** "Coach first, manager second" is his leadership identity — frame coaching as a strength (SVPG-style), not softness. Facts: 10+ direct reports; promoted 3 PMs junior→senior, a Senior PM→Group PM, a designer→Design Director; heavy hiring as PayFit scaled from ~100 people.
- **Skills list restructure (VP-first)**: lead with "Product Strategy" (vision/trajectory/roadmap/positioning — distinct from "AI Product Strategy"), then Leadership & coaching, then AI Product Strategy, then ONE "Product craft" line (discovery/prioritization/delivery/design). Four separate IC craft skills read "PM", not "VP".

## Style rules (anti-slop — applies to his OWN profile)
- No "passionate about building products that matter" or any generic LinkedIn-speak.
- No clever/performative hooks (he rejected "…and I can show the numbers").
- No filler ("most of it at PayFit" — "ça sert à rien").
- **NO em-dashes (—).** He dislikes them ("je n'aime pas quand il y a des dash"). Use periods, commas, or "·" instead — everywhere: LinkedIn, CV, site copy. (Avoid en-dashes in date ranges too; use hyphens.)
- Don't box him in: avoid the "PayFit guy" framing AND avoid committing statements ("It's the problem I want to work on" locks him to one topic; his positioning is open/mission-first).
- **About section = positioning + narrative + thinking**, not a re-list of achievements (redundant with the Experience section). Use a condensed "Track record:" block (Sylvain/CPO-PayFit style) for greatest hits instead.
- Emojis: 1–2 max, only on warm/personal parts (restaurants, shop), never on AI/tech. He ended up dropping them — if in doubt, omit.
- Write his copy in **English** (profile is English); converse with him in **French**.

## Numbers (verify, never invent — sepia rule)
- **12+ years** in B2B SaaS (NOT 10 — he's ~12y8m: Synthesio Mar 2013 → PayFit Nov 2025).
- PayFit: **$2.1B** unicorn (NOT $2.2B), ~$496M raised, employee ~#100, ARR under $10M → $80M (**he prefers NOT to print the $80M — lead with "to profitability"**), 5,000 → 20,000+ customers.
- Signature wins: HR+ plan 0 → €15M+ ARR / 3,000+ customers; salary-payments feature >€1B processed; PLG ~30% of new acquisitions.
- Synthesio: dashboards redesign → -20% churn (Experience only, NOT the track record — dilutes the scale story).
- Verify public company figures via web before writing; Mehdi's friend-provided numbers had errors ($2.2B vs actual $2.1B).

## Decisions already made (don't relitigate unless asked)
- **Primo is OUT** of LinkedIn + CV (20-person co that stalled on a human problem; "Founding PM" = downgrade from Product Director). Interview talking point only.
- **PayFit end date shown as "Jan 2026"** (he extended from Nov 2025 to shorten the gap; his call — reference-check risk flagged once, don't re-flag).
- **Investor/Upscalers**: in About ("angel investor at Upscalers"), not in CV body.
- Removed "Claude code" from LinkedIn top skills (dev-flavored, wrong signal for a VP).

## Personal site / folio (mehdisoliman.me)
Single self-contained `index.html` at `~/jobhunt/site/` (Space Grotesk + JetBrains Mono, no framework). Static deploy: Netlify + GoDaddy DNS. Full build recipe in `references/personal-site.md`.
- **Design taste (validated)**: "épuré, light, petite touche sympathique" = clean/light + one memorable accent. Monochrome, NOT blue (he disliked the blue). Accent = warm orange `#e8551f`. Cards (rounded, subtle border), not full-width rows. Bold ONLY key metrics — if everything's bold nothing pops.
- **Structure**: `// vp · product leader` → name (orange dot) → rotating tagline → photo (hero right) → 01 About → 02 Talks & writing (cards w/ thumbnails) → 03 Links (cards w/ orange icons).
- **Rotating tagline** (crossfade ~4.5s, NOT typewriter): 5 phrases, one word hand-underlined per phrase, underline REDRAWN each time, phrase-first-then-underline (~700ms). Phrases: "I build products that feel human." / "I turn 0-to-1 ideas into €15M+ ARR." / "I think about users becoming agents." / "I coach product people into leaders." / "Reality is what's shipped."
- **Photo**: warm/color (NOT B&W), centered crop.
- **Pending**: Twitter + GitHub handles (cards are placeholder `#`); talk-2 link/image; favicon + OG tags.

## Pitfalls
- LinkedIn goes stale fast: before drafting, check headline (still "@PayFit"?), "Present" dates, and odd top skills.
- Two CVs exist — one has Primo, one doesn't. The no-Primo one is the base.
- His memory/profile says "Synthesion" but the company is **"Synthesio"** (acquired by Ipsos).

## Files
- `~/jobhunt/cible.md` — full target profile + 6-step plan.
- `~/jobhunt/cv.md` — approved aligned CV (markdown).
- `references/approved-positioning.md` — locked headline, About, CV summary.
- `scripts/push_cv_to_drive.py` — copies the "CV" Google Doc and replaces its content with `~/jobhunt/cv.md` (Drive `files.copy` + Docs `batchUpdate`).
