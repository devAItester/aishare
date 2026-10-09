# Oscean: project source and build notes

## Original README

The verbatim upstream README is archived at [README-original.md](README-original.md); its blob SHA is `2359e44418753a8a7af12b41666035979eb9a78a`.

> This is the repository for the Oscean wiki. The on-site documentation is the source for more up-to-date details. Oscean is a static site written in Uxntal, a stack-machine assembly language designed for a portable virtual machine. The database tables are plain-text files designed to fit in Uxn's 64kb of memory. The `main` branch is the live version.

The original README gives the engine build command:

```sh
uxnasm src/oscean.tal bin/oscean.rom
```

and run command:

```sh
uxncli bin/oscean.rom
```

The verbatim upstream Makefile is archived at [makefile](makefile); its blob SHA is `a2aa54f2eb1817237353930de848e7b5fc3e40bc`.

## Makefile structure (checked from upstream)

- `run` depends on `bin/oscean.rom`, generated RSS feeds, `docs/index.html`, `etc/index.html`, and several repls. It clears temporary files and `site/*`, then runs the Oscean ROM to generate HTML.
- `clean` removes built binaries, temporary files, and generated site files.
- `bal` and `lint` run Uxn tools against source files.
- `links/img.xml` and `links/log.xml` are generated from ROMs and source diaries.
- `docs/index.html` and `etc/index.html` are generated from the corresponding directories.
- The Makefile also generates JavaScript sources for embedded repls from Uxntal source files; those repls are separate from the generated wiki pages.

## Root index

Upstream `index.html` links `links/main.css`, sets metadata, and contains a small redirect script that routes the root page to `site/<filename>.html` based on the URL hash. The no-script fallback redirects to `site/home.html`.

Original files:
- [README.md](https://github.com/XXIIVV/oscean/blob/main/README.md)
- [makefile](https://github.com/XXIIVV/oscean/blob/main/makefile)
- [index.html](https://github.com/XXIIVV/oscean/blob/main/index.html)
- [Oscean engine page](https://wiki.xxiivv.com/site/oscean.html)
- [About page](https://wiki.xxiivv.com/site/about.html)

The README and Makefile are archived verbatim. The root index is summarized here rather than copied as an executable HTML/JavaScript file. The exact full current CSS and a representative original HTML specimen are archived separately.
