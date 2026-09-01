# Design tooling (CV + site assets)

Recipes that worked for Mehdi's personal-brand assets. No browser needed for the PDF/PNG steps.

## Designed CV: WeasyPrint HTML → PDF

Clean monochrome layout lives in `/root/jobhunt/cv.html`. Regenerate with:

```bash
cd /root/jobhunt && weasyprint cv.html "Mehdi_Soliman_CV.pdf"
```

Check page count (must stay ≤ 2):

```bash
python3 -c "import pymupdf; print('pages:', pymupdf.open('/root/jobhunt/Mehdi_Soliman_CV.pdf').page_count)"
```

### CV design tokens (his approved look)

- Font: Helvetica Neue / Arial system stack. Body 10pt, line-height 1.5 (airy).
- Colors: name `#111827`, headline/headers `#374151`, body `#1f2937`, meta/dates `#6b7280`, borders `#e5e7eb`. **No blue.**
- Section headers: uppercase, letter-spacing 1.3px, bottom border.
- Company/role lines: company + role bold, dates inline in gray (`PayFit · Paris · Oct 2018 → Jan 2026`).
- Sub-block labels (People & leadership, 0 → Scale, PLG, Expand): bold, `#374151`.
- Bullets: `padding-left: 19px`, `margin-bottom: 4px`.
- Bold (`<b>`) only key metrics.

## Mockup previews without a browser: WeasyPrint HTML → PNG

When Chrome isn't running, render a single self-contained HTML mockup to a PNG using a px-sized page:

```python
import weasyprint, pymupdf
css = weasyprint.CSS(string="@page { size: 1000px 1400px; margin: 0 }")
weasyprint.HTML(filename="index.html").write_pdf("/tmp/_mock.pdf", stylesheets=[css])
d = pymupdf.open("/tmp/_mock.pdf")
d[0].get_pixmap(dpi=100).save("out.png")
```

Notes: WeasyPrint is print-oriented — fine for static layouts (flex/grid), but it will NOT run JS, so hover/scroll/motion won't show in the preview. For an interactive/motion pass, describe the animation in text or use a real browser.

## Site mockup stances (from `/root/jobhunt/sketches/`)

Three distinct directions to re-offer if he revisits the folio site:
1. `001-editorial-calm` — Fraunces serif, cream bg `#faf7f2`, terracotta `#c05a3a`.
2. `002-numbers-impact` — Inter, white, 4-up metrics strip, ink `#0b0f0e` + green `#0f766e`.
3. `003-mono-twist` — Space Grotesk + JetBrains Mono labels, off-white `#f7f6f3`, single orange accent `#e8551f`.

The "signature human" animation idea he liked: name fades in, the word "human" gets underlined by a hand-drawn SVG stroke ~0.8s after load, and a small dot follows the cursor with a ~0.2s ease (human lag vs instant agent).

## Final site (v1 landing page — `003-mono-twist` built)

Built in `~/jobhunt/site/`: `index.html` + `cv.pdf` (Download CV target) + `assets/mehdi.jpg`. Ship as a zip for local preview (`index.html` + `cv.pdf` + `assets/`).

Structure: `// vp · product leader` tag → name `Mehdi Soliman.` (orange dot) → 2-line headline (main sentence, then a smaller block `<span class="tags">Human-first · AI Product Strategy · Angel investor.</span>`) → portrait → `01 · About` → `02 · Talks` (placeholders) → `03 · Links` (LinkedIn / Download CV / Email) → footer.

Design tokens: Space Grotesk + JetBrains Mono, bg `#f7f6f3`, ink `#111`, muted `#6b6b6b`, accent orange `#e8551f`, hairline `#e2e0da`. Portrait = flex hero (text left, photo right; stacks on mobile), `aspect-ratio:4/5; object-fit:cover`, rounded 14px.

Animations implemented (JS, respect `prefers-reduced-motion`): CSS fade-in on name/tagline (stagger delays); hand-drawn "human" underline (SVG path `stroke-dasharray/offset = getTotalLength()`, animate `offset → 0` ~0.75s after load); cursor dot (fixed 12px orange circle, rAF lerp `dx += (mx-dx)*0.09`, only if `(hover:hover)` and not reduced-motion); scroll reveal via IntersectionObserver.

**No-js fallback (also makes WeasyPrint static previews show content that entrance animations would otherwise hide):** `<html class="no-js">` + `<script>document.documentElement.classList.remove('no-js')</script>` in `<head>`, plus CSS `.no-js .fade, .no-js .reveal{opacity:1;transform:none}`. Without it, WeasyPrint (no JS) renders `.fade/.reveal` at `opacity:0` → blank preview.

## Photo cropping (PIL, no browser)

Mehdi's hero portrait: **color** (he rejected B&W — color reads warmer and fits "human-first"), 4:5, centered on him. His face sits at ~70% of the source width (not frame-center), so naive centering puts him off.

Method: `vision_analyze` the source image asking for the face-center x-position as a % of width, then PIL-crop a 4:5 box centered on that x:

```python
from PIL import Image
im = Image.open(ORIGINAL)
w = int(0.8 * h)                      # 4:5 ratio
im.crop((face_x - w//2, 0, face_x + w//2, h)).save("assets/mehdi.jpg", quality=92)
```

Then re-render and let HIM confirm — the vision model can't verify fine centering, the user is ground truth (he iterates with "encore 50px" / "trop, reviens de 25px"). Direction rule: to move him RIGHT in the crop, move the crop box LEFT (and vice-versa).
