# CSS delivery: external, embedded, or critical CSS

This comparison concerns how CSS reaches the browser, not where a folder happens to be named. The verified Oscean baseline is a shared external stylesheet at `links/main.css`; our Jekyll copy has used or considered inline/embedded CSS, but the earlier rationale is not currently confirmed.

Detailed evidence and test plan: [../research/css-architecture.md](../research/css-architecture.md).

## Options

| Option | Benefits | Costs / risks | Fit for the reference copy |
|---|---|---|---|
| A. One shared external stylesheet | One source of truth; browser can cache and reuse it; matches Oscean | First load fetches CSS; external CSS can block rendering | **Baseline / provisional recommendation** |
| B. Embed all CSS in every HTML page | Self-contained output; avoids a separate CSS request | Repeats CSS in every page; larger HTML; no independent stylesheet cache; risks divergence | Not justified without a concrete requirement |
| C. Embed only critical CSS and load the remainder externally | Can improve initial rendering in some cases while retaining shared CSS | More complex build; critical rules can drift or be duplicated; requires measurement | Optional optimization only after baseline measurement |
| D. Per-page embedded CSS | Allows page-specific standalone styling | Makes shared behavior harder to maintain and compare | Only for genuinely exceptional pages |

## Terminology

- External CSS: `<link rel="stylesheet" href="...">`.
- Embedded CSS: `<style>...</style>` in the HTML document.
- Inline style: `style="..."` on an individual element.
- `<head>` is a document section; it is not a synonym for embedded CSS.

## Decision

**Choose option A: one shared external stylesheet.** The active Jekyll layout was checked and currently embeds the full `_includes/style.css` into every generated page via `<style>{% include style.css %}</style>`. The CSS source is centralized, but its bytes are repeated in every HTML response. The original Oscean also uses a shared external file. For this multi-page static wiki, the external file is the simpler, more faithful baseline and enables browser caching across page visits.

Recommended path in the copy: `assets/main.css`. Keep CSS declarations unchanged while moving the delivery method. Critical CSS is not justified without measured evidence of a first-render problem.

Implementation is pending; this decision does not mean the site code has already been changed. See the task list in [research/css-architecture.md](../research/css-architecture.md).

See [../changes.md](../changes.md) for the discrepancy register and [../decisions.md](../decisions.md) for decision status.
