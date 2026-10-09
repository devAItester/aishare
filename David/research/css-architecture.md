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
5. The user recalls that our copy used inline/embedded CSS, but the reason for that earlier choice has not been recovered from historical conversation records in this pass. Do not invent a rationale or present it as a settled performance decision.
6. The exact current state of every deployed Jekyll template must be checked before changing it. A search of the connected GitHub index did not reliably establish whether all current pages use `<style>`, a shared stylesheet, or both.

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

**No final decision has been made yet.** The external stylesheet is the faithful baseline because it is what the inspected original source uses. The inline version in our copy must be treated as an unresolved implementation difference until we recover why it was introduced and compare the actual generated output.

Provisional recommendation for the reference-copy project: keep one shared external CSS file unless a measured, documented requirement justifies a narrowly scoped embedded critical-style block. Do not inline the entire stylesheet merely because it seems faster.

## Work required before closing the question

1. Inspect the active Jekyll layout and all CSS includes in the actual copy; identify where inline CSS was introduced.
2. Check Git history/commits for the change and its original rationale, if available.
3. Compare generated HTML from representative short and long pages; verify whether CSS is duplicated in every page and whether any external stylesheet is still loaded.
4. Test visual parity and responsive/dark-mode behavior after switching the delivery method without changing the CSS declarations themselves.
5. Compare cold-cache and warm-cache loading using browser DevTools; do not use a single subjective load as proof.
6. Decide explicitly between: A) shared external CSS, B) fully embedded CSS, or C) critical CSS embedded plus the rest external.
7. Record the decision in `../decisions.md` and update `../changes.md` with verified implementation and test status.

Until these checks are complete, the difference remains open.
