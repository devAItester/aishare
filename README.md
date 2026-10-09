# Field Notes

A curated, text-first knowledge site about building a small, linked website inspired by [Oscean](https://github.com/XXIIVV/oscean).

- **Start reading:** [index.html](index.html)
- [Project purpose](project.html)
- [Architecture](architecture.html)
- [Navigation and backlinks](navigation.html)
- [Visual language and CSS](styling.html)
- [Publishing checks](publishing.html)
- [Decision register](decisions.html)
- [Sources and evidence](sources.html)
- [Archive map](archive.html)

## Repository layout

- Root HTML pages and `assets/main.css` are the curated site.
- `Archive/` preserves the files that existed before the site was created, keeping their former paths under one directory.
- The archive is source material, not a guarantee that every old note is current or correct. Use the curated pages and decision register for the current direction.

## Publishing

The repository currently contains a static HTML/CSS site suitable for GitHub Pages. Enable Pages in **Settings → Pages** and select **Deploy from a branch → main → /(root)**. The `_config.yml` excludes the archive from the generated website; archive links point back to the repository.

The source and link structure have been checked through the GitHub API. A live browser/deployment check is still pending until Pages is enabled and the deployment is available.
