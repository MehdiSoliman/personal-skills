# Personal site build recipe (mehdisoliman.me)

Static single-file site at `~/jobhunt/site/` — `index.html` (CSS+JS inline) + `assets/`. No framework, no server.

## Files
- `index.html` — self-contained. Fonts: Space Grotesk (display) + JetBrains Mono (labels/tags) via Google Fonts.
- `assets/mehdi.jpg` — hero portrait (4:5, cropped/centered).
- `assets/talk-article.jpg`, `talk-productcentric.jpg`, `talk-triforce.jpg` — talk thumbnails.
- `cv.pdf` — the download (rendered from `cv.html` via WeasyPrint).
- `~/jobhunt/render_site.py` — WeasyPrint → PDF → PNG preview + re-zips `mehdisoliman-site-v1.zip`.

## Design tokens
- bg `#f7f6f3` (cream), ink `#111`, muted `#6b6b6b`, accent `#e8551f` (orange), line `#e2e0da`.
- Cards: 1px `var(--line)` border, 12px radius, white bg; hover → accent border + text.
- Orange is a ONE-shot accent (dot after name, `//`, icons, underlines) — never a big color wash.

## Animations (all JS, guarded by prefers-reduced-motion)
- Staggered fade-in via `.fade.d1/.d2/.d3`.
- **Hand-drawn underline**: `.hl` span wraps the word; absolute `<svg>` under it, path `M3 8 C 18 3, 40 11, 62 6 S 100 3, 117 7`, viewBox `0 0 120 12`, `preserveAspectRatio="none"`. Draw = set `stroke-dasharray=len; stroke-dashoffset=len`, then transition `stroke-dashoffset`→0 over 0.7s. Reset (`hideUnderline`) before each redraw.
- **Rotating tagline**: `.phrase` elements absolutely stacked, `.active` opacity 1 (0.7s crossfade). `setInterval(4500)`. Per activation: add `.active`, reset underline, then draw after **700ms** (phrase shows FIRST, underline SECOND — he said the timing was too tight at 180ms). Initial draw at ~1200ms (after the headline fade-in).
- Cursor dot: fixed circle, rAF lerp `dx += (mx-dx)*0.08` ("human lag").

## Previewing without a browser (WeasyPrint HTML→PDF→PNG)
Two gotchas:
1. `.fade`/`.reveal` start at `opacity:0` → invisible in a static render. Fix: `<html class="no-js">` + early `<script>document.documentElement.classList.remove('no-js')</script>` + CSS `.no-js .fade,.no-js .reveal{opacity:1;transform:none}`. This is progressive enhancement (content visible without JS) AND makes WeasyPrint previews work.
2. WeasyPrint does not resolve `stroke="currentColor"` → hardcode `stroke="#e8551f"` on inline SVG icons (or they render black in previews; browsers are fine with currentColor).
Render with `@page { size: 1000px 1700px; margin: 0 }`, then pymupdf → PNG.

## Photo centering
Crop the FILE with PIL (deterministic), not `object-position`. Original 1280×853, face ~70% from left. To move the subject RIGHT in frame, move the crop window LEFT (smaller `left` value). Iterated on user "shift me Npx" feedback; final box ~`(555, 0, 1067, 640)`. Color, not B&W (he prefers warm/color).

## Re-packaging gotcha
After ANY change, re-zip `mehdisoliman-site-v1.zip` — I once sent a stale zip and the user saw the old version ("no rotation / missing links"). The zip must include `index.html`, `cv.pdf`, AND every `assets/*` referenced.

## Deploy (static)
- Domain `mehdisoliman.me` at **GoDaddy** (nameservers `domaincontrol.com`), currently parked.
- Host: **Netlify** (he uses it with Joseph). Path A: Netlify Drop drag-and-drop → Domain settings → GoDaddy DNS (CNAME www → netlify.app, A apex). Path B: GitHub repo → Netlify auto-deploy (maintainable).
- Google Docs CV sync: `scripts/push_cv_to_drive.py` (copy the "CV" doc + `files.copy` + Docs `batchUpdate` clear/insert) and `~/jobhunt/update_cv_drive.py` (clear+reinsert into the SAME doc id). Both import `get_credentials`/`build_service` from `google-workspace/scripts/google_api.py`.
