# Reference-page index and extracted source facts

This is a curated research index. The full original Styleguide HTML specimen is stored in [pages/styleguide.html](pages/styleguide.html). Other pages are summarized here with source URLs and verified facts; they are not presented as verbatim local copies.

## Styleguide

- Local full source: [pages/styleguide.html](pages/styleguide.html)
- Upstream: https://github.com/XXIIVV/oscean/blob/main/site/styleguide.html
- Blob SHA: `90ced50ac941900f39514dcad6e9d855fd8910e5`
- Purpose: practical specimen of h1–h5, paragraphs, inline formatting, kbd, article, images, nested lists, tables, pre, q, cite, figures/captions, and footer icons.
- Its navigation explicitly contains three adjacent groups; the third is empty: `<ul></ul>`.
- It links to Oscean for engine details and About for architecture philosophy.

## Oscean engine documentation

- Upstream: https://github.com/XXIIVV/oscean/blob/main/site/oscean.html
- Blob SHA: `296c29bac23b6575b836ba5a17a69cc532780f0a`
- Describes Oscean as a wiki engine written in Uxntal and the build pipeline that reads lexicon, diary, and HTML sources, then emits generated HTML.
- The page states that generated pages are accessible to screen readers and terminal browsers, use no JavaScript, and depend on a very small stylesheet. This statement describes generated pages; the root index has a small redirect script.
- The upstream README and Makefile are summarized in [original-project.md](original-project.md).

## About / project philosophy

- Upstream: https://github.com/XXIIVV/oscean/blob/main/site/about.html
- Blob SHA: `6d294344fb9e0e5cd74361d602a3c04c0d523204`
- Describes the wiki as a personal library for updates, journal logs, project notes, and curated knowledge; explains the Uxntal/UXN implementation and licenses.
- This is project context, not a complete CSS specification.

## Navigation specimen: Shavian

- Upstream: https://github.com/XXIIVV/oscean/blob/main/site/shavian.html
- Blob SHA: `719fd7a126ff153d16f133a6b4f016ebe9a84811`
- The original navigation begins with three sibling lists. The third is empty. In source, the relevant structure is:
  
```html
<nav>
  <ul><!-- first navigation group --></ul>
  <ul><!-- current branch; current page has class="self" --></ul>
  <ul></ul>
</nav>
```

The full page has a large Shavian alphabet table and footer icons. Use the upstream URL if exact page content beyond the navigation specimen is required; the relevant layout behavior is already captured here.

## Other inspected pages

| Page | Upstream source | Use |
|---|---|---|
| Documentation | https://github.com/XXIIVV/oscean/blob/main/site/documentation.html | General project documentation |
| Ethics | https://github.com/XXIIVV/oscean/blob/main/site/ethics.html | Project/community principles |
| Sitemap | https://github.com/XXIIVV/oscean/blob/main/site/sitemap.html | Page inventory and relationships |
| Typography | https://github.com/XXIIVV/oscean/blob/main/site/typography.html | Typography-specific reference |
| Web | https://github.com/XXIIVV/oscean/blob/main/site/web.html | Web-related notes |
| Essentials | https://github.com/XXIIVV/oscean/blob/main/site/essentials.html | General reference notes |
| Research | https://github.com/XXIIVV/oscean/blob/main/site/research.html | Research practices and topics |
| Reading | https://github.com/XXIIVV/oscean/blob/main/site/reading.html | Reading notes |

The CSS and representative source pages are the primary local evidence. These links are retained for provenance and to identify any future gaps; do not re-fetch them unless the local archive is insufficient or the user asks about newer upstream content.
