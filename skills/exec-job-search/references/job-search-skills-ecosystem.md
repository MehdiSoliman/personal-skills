# Community skills for job search (vetted, as of Aug 2026)

## Discovery + vetting procedure
1. `npx skills find "<query>"` (e.g. "job search", "career", "resume", "linkedin", "portfolio", "case study").
2. Verify on the skills.sh detail page: **installs**, **repo stars**, **Trust Hub verdict** (Pass / Warn / Fail), and skim the SKILL.md.
3. Install with `hermes skills install <owner/repo>/<skill> -y` — this quarantines + scans with `skills-guard-v2` before landing.

## Known-good / relevant
- **`refoundai/lenny-skills@career-transitions`** — "Navigating Career Transitions" from 24 Lenny Rachitsky podcast/newsletter guests. 1.9K installs, repo 1.2K★, **Pass**. Maps to target-clarity (audit fit, energy sources, org quality, category-leader>title, VET your eng partner). INSTALLED.
- **`paramchoudhary/resumeskills`** (pack, repo 1.7K★, **Pass**) — `linkedin-profile-optimizer` (5.1K), `resume-ats-optimizer` (9.6K), `portfolio-case-study-writer` (5.1K), `resume-tailor`, `interview-prep-generator`. Useful for CV/LinkedIn/folio. (We judged `portfolio-case-study-writer` NOT worth installing — a VP folio needs real stories + sepia/humanizer, not a generic template.)

## Flagged / skip
- **`refoundai/lenny-skills@pm-career-growth`** — relevant but Trust Hub **Fail**.
- **`proficientlyjobs/proficiently-claude-skills@job-search`** — browser-automation daily search, **Warn**, heavy setup.
- **`whfjoshua/jobhunt`** (1★) — job-board orchestrator (Greenhouse/Lever/Ashby); test locally first.
- **`alirezarezvani/claude-skills@senior-pm`** — TRAP: it's **Project** Management (WSJF/RICE/risk), not Product. Skip.
- **`alirezarezvani/claude-skills@cpo-advisor`** (25K★, **Warn**) — strategic product leadership (vision/PMF/org design); useful reference for VP-level framing, not for the folio itself.

## Noise
Most `npx skills find "portfolio"` results are crypto/finance (OKX wallet, DeFi) — ignore.
