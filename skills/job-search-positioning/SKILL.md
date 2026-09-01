---
name: job-search-positioning
description: Use when helping Mehdi with his job search.
version: 1.0.0
license: MIT
---

# Job Search Positioning (Mehdi)

## When to Use
When Mehdi asks to work on his job search — defining his target (clarity), positioning (LinkedIn/folio), prospection, or leveraging contacts. Also when scouting community skills for career/job-hunt tooling.

## Context
Mehdi is actively seeking Director/VP Product roles (Paris intramuros or partial remote, work/life balance essential, no long commute). The canonical target brief lives in `~/jobhunt/cible.md` (edit it, don't re-derive). Memory holds a compact pointer + hard filters. Plan (6 steps): ① clarity ✅ ② readings (his own) ③ positionnement (LinkedIn + folio) ④ prospection (recruiting firms + target companies) ⑤ leviers (ex-company client list + LinkedIn contacts).

## Clarity interview method (5 dimensions, in this order)
Run this conversationally, ONE dimension at a time — discuss, don't quiz. Mehdi dislikes bullet-point interrogations; a form-like `clarify` dump feels mechanical to him. Ask, let him talk, then mirror his answer back crisply to lock it in before moving on.

1. **Énergie (the engine)** — do NOT ask "what do you like doing" (craft). Ask what feels like play / energizes him, grounded in past moments (PayFit, Synthesion, CLUTCH, side businesses). Senior leaders are usually driven by **mission + people**, not a specific craft.
2. **Type de boîte** — do NOT offer headcount/series choices (50-150 vs 150-500 etc.). Senior candidates reject size framing; the real filter is **santé opérationnelle**: a company that ships, low bureaucracy, clear direction, product team already in place. Boundaries = neither over-processed (PayFit/Datadog/Edenred) nor fragile (~20-person Primo).
3. **Domaine** — for a mission-driven candidate, domain is a **comfort gradient, not an impact filter**. Ask comfort zones vs stretch (wants to be tested) vs avoid.
4. **Poste** — title scope (VP Product vs Director vs Head of Product ≈ VP depending on company size), team size they've led, hands-on level (flexible by role).
5. **Rémunération + contraintes** — floor (non-negotiable), target range, variable %, equity (usually secondary if no liquidity), remote policy (hybrid vs full-remote).

End by writing the full target brief to a file and keeping memory as a one-line pointer + hard filters — never dump the whole profile into memory.

## Key insights (do not re-learn)
- Senior leaders are often **stage-agnostic AND craft-agnostic** — they flex across discovery/prioritization/growth/build cyclically. The constant is mission clarity + team quality.
- **VP roles are mostly OFF-MARKET** — they flow through recruiting firms directly, not web listings. Prospection = reactivating recruiter contacts, not scraping job boards.
- **Positionnement comes BEFORE prospection** (LinkedIn + folio first, then reactivate recruiter contacts).
- A "big group" or "unfamiliar domain" veto can be soft if the story + execution + product are compelling (Revolut example).

## Community skills landscape (vetted 2026-08-31)
- `refoundai/lenny-skills@career-transitions` — ✅ INSTALLED (Trust Hub Pass). Lenny Rachitsky; best for clarity/transition framing.
- `paramchoudhary/resumeskills` pack — recommended for LinkedIn/folio: `linkedin-profile-optimizer`, `portfolio-case-study-writer`, `resume-ats-optimizer` (all Pass, repo ~2K⭐).
- `alirezarezvani/claude-skills@cpo-advisor` — Warn (Python scripts); strategic VP-level framing, optional.
- TRAPS: `alirezarezvani/claude-skills@senior-pm` = **Project** Management, not Product. Searching "portfolio" returns mostly crypto/finance noise. Full vetting detail in `references/community-skills-vetted.md`.

## Pitfalls
- Don't re-ask what's already known (criteria are in memory + user profile + `cible.md`).
- Community skill discovery: `npx skills find "<term>"`, then verify each candidate on skills.sh (installs, stars, **Gen Agent Trust Hub verdict**) before recommending. Check whether "pm" means Product or Project, and whether a promising keyword is polluted by another domain (finance/crypto).
- Install via `hermes skills install <owner/repo>/<skill> -y` (quarantine + `skills-guard-v2` scan runs automatically); confirm the SAFE verdict and the file list before telling the user it's done.
