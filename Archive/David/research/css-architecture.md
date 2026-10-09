# CSS architecture: external stylesheet vs embedded CSS

Date: 2026-10-09

## Question

The original Oscean keeps its main stylesheet at `links/main.css` and links it from HTML. In our Jekyll copy, CSS was at some point moved or written inline in the HTML head. We need to decide whether to retain that difference or return to an external stylesheet.

## Verified facts from the local archive

1. The original project has a shared stylesheet at `links/main.css`. The exact upstream CSS is archived at [../source/current-main.css](../source/current-main.css).
2. The archived original Styleguide HTML includes this external reference in `<head>`:
   `<link href="../links/main.css" type="text/css" rel="stylesheet">`.
   See [../source/pages/styleguide.html](../source/pages/styleguide.html).
3. The original root `index.html` also links `links/main.css`; this is documented in [../source/original-project.md](../source/original-project.md).
4. The stylesheet is shared by the generated site pages. The local source specimen therefore demonstrates a centralized stylesheet, not CSS embedded separately in every page.
5. The active `devAItester/d00-jk-bc` layout has now been inspected. `_layouts/default.html` contains `<style>{% include style.css %}</style>`, and `_includes/style.css` holds the shared CSS source. Jekyll therefore embeds the full stylesheet into each generated HTML page; the source is centralized, but the browser receives it repeatedly as part of each page response.
6. The historical reason for introducing this arrangement has not been recovered. It may have been chosen to avoid a separate request or to keep the output self-contained, but neither motive is confirmed.

## Terminology

- **External stylesheet:** a separate `.css` file referenced by `<link rel="stylesheet" href="...">`, normally from `<head>`.
- **Embedded CSS:** rules inside a `<style>` element in the HTML document, often in `<head>`.
- **Inline style:** declarations in an element's `style="..."` attribute.
- **Head:** a part of the HTML document, not a CSS delivery method. A `<link>` inside `<head>` still loads an external stylesheet.

These mechanisms should not be conflated.

## Why an inline approach might have been considered

These are possible technical motivations, not confirmed historical reasons:

- Keep a single-file page self-contained.
- Avoid an additional stylesheet request for a tiny, one-off page.
- Embed critical styles to reduce the time before first rendering in some delivery situations.
- Make generated output easier to distribute as a standalone HTML file.

None of these alone establishes that inline CSS is better for this project. If every page receives the same full CSS block, it duplicates bytes and prevents that CSS from being cached as one shared file.

## Trade-offs

| Criterion | Shared external CSS | CSS embedded in each page |
|---|---|---|
| Shared visual system | One source of truth | Rules can drift or be duplicated |
| Browser cache | Reused across pages and navigations when cacheable | Repeated inside each HTML response |
| First visit | May require fetching CSS; stylesheet can block rendering | Avoids a separate CSS request, but enlarges HTML |
| Later page visits | Cached stylesheet can reduce transfer | Re-sends CSS with each page |
| Maintenance | Central edits apply to all pages | Generator/layout must keep embedded copies consistent |
| Single-file portability | HTML depends on a CSS resource | Page can be self-contained |
| Faithfulness to Oscean | Matches observed original architecture | An intentional deviation from the reference |

Actual speed depends on document size, cache state, network, browser, and whether styles are critical. It must be measured on the generated site, not inferred from the word “inline”.

## Browser and JavaScript engine distinction

CSS fetching, parsing, CSSOM construction, render-blocking behavior, and layout are browser-engine responsibilities. V8 is the JavaScript engine used by Chrome, not the engine that decides how an external stylesheet is organized or directly lays out CSS. Avoid attributing the external-vs-embedded choice to V8.

Useful primary references:
- HTML stylesheet link element: https://html.spec.whatwg.org/multipage/links.html#link-type-stylesheet
- HTML style element: https://html.spec.whatwg.org/multipage/semantics.html#the-style-element
- MDN: External stylesheets: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started
- Chrome render-blocking resources: https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources
- web.dev, optimize LCP: https://web.dev/articles/optimize-lcp
- V8 project: https://v8.dev/

## Current conclusion

**Decision for the target copy: use one shared external stylesheet.** This matches the observed Oscean architecture, avoids repeating the full CSS in every generated HTML response, allows browser caching across pages, and keeps one source of truth. The current embedded output is an implementation discrepancy to correct; this archive update does not itself modify the website code.

Recommended target path: `assets/main.css`, since the copy already has an `assets/` directory and only needs one shared stylesheet. Keep the CSS declarations unchanged during the delivery-method change so visual differences can be isolated. Do not add critical-CSS extraction unless later measurements show a real first-render bottleneck.

## Work required before closing the question

1. Inspect the active Jekyll layout and all CSS includes in the actual copy; identify where inline CSS was introduced.
2. Check Git history/commits for the change and its original rationale, if available.
3. Compare generated HTML from representative short and long pages; verify whether CSS is duplicated in every page and whether any external stylesheet is still loaded.
4. Test visual parity and responsive/dark-mode behavior after switching the delivery method without changing the CSS declarations themselves.
5. Compare cold-cache and warm-cache loading using browser DevTools; do not use a single subjective load as proof.
6. Move the shared source from `_includes/style.css` to the public `assets/main.css` path and change the layout to reference it with `<link rel="stylesheet">`, without changing CSS declarations.
7. Compare generated HTML and check that it no longer contains the full `<style>` block; verify the stylesheet URL works under the configured `baseurl`.
8. Check visual parity, dark mode, short and long pages, then compare cold-cache and warm-cache loading in DevTools if performance is still a concern.
9. Update `../changes.md` when the implementation and published result are verified. The architecture decision is made; implementation and visual verification remain pending.
