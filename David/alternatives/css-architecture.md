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

## Status

Open. No final decision has been recorded. The original source establishes what Oscean does, but not why our earlier copy used inline CSS. Recover the change history and measure generated output before closing the decision.

See [../changes.md](../changes.md) for the discrepancy register and [../decisions.md](../decisions.md) for decision status.
