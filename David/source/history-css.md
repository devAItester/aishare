# Historical CSS snapshots

Original file: `links/main.css` in https://github.com/XXIIVV/oscean. Each block is a verbatim snapshot; commit refs and blob SHAs are listed above it.

## 2023 snapshot

- Upstream commit: `edf04d378ead7f89177686b379d2d5ec6c9f1383`
- Blob SHA: `929b4a2cfd51bfc509567ecb3ceb5ea358545fde`
- Background: no `html` halftone rule; older body and navigation geometry.

```css
* { margin:0;padding:0;box-sizing:border-box;text-decoration:none;color:#000 }
body { padding:30px;font-family:serif;font-size:16px }
body > *, body > * > *, main figure > *, main figure > div > *, main p { margin-bottom:30px }
body a.self, body a.parent { font-style:italic }
body a:hover, main a:hover > * { background-color:#000;color:#fff;text-decoration:none }
table td, table th { vertical-align:top;padding:2.5px 5px;text-align:left }
table td > pre, table th > pre { background:none;padding:0;margin:0 }
table tr img { margin-bottom:0 }
header { float:left;margin:5px 30px 0 0;min-height:90px }
header img { display:block }
nav { margin:0 0 30px }
nav ul { padding:0;margin:0 45px 30px 0;float:left }
nav ul li { list-style-type:none;white-space:pre }
nav ul li a { padding:0px 4px}
main { max-width:624px;clear:both }
main a { text-decoration:underline }
main a[target="_blank"] { text-decoration-style:dotted }
main article { border-left:5px solid #efefef;padding-left:25px;clear:both }
main cite { display:block;clear:both;margin-bottom:30px }
main cite:before { content:"— " }
main > figure:first-child img:first-child { margin-left:-30px;width:800px;max-width:100vw }
main iframe { width:100% }
main h1, main h2, main h3, main h4, main h5, main figure figcaption { max-width:400px }
main ul, main ol { margin:0 30px 30px 30px }
main ul ul { margin-bottom:0 }
main ul li, main ol li { line-height:25px;padding:0px 5px }
main p { line-height:160% }
main ::selection { background-color:#72dec2;color:#000;text-decoration:none }
main q { font-family:serif;font-size:18px;font-style:italic;display:block;max-width:400px }
main img, main svg { max-width:100%;display:inline-block;margin:0 0 25px }
main pre { overflow:auto;background:#efefef;padding:10px;font-size:80%;margin-bottom:30px }
main pre code, main pre i { color:#777 }
main code { white-space:pre }
main hr { clear:both }
main kbd { color:black;font-size:12px;display:inline-block;padding:2px 5px;font-weight:bold;border-radius:4px;margin-bottom:1px;line-height:16px;border:2px solid #000;background:white;vertical-align:middle }
footer { border-top:1.5px solid;padding:30px 0 0 0;line-height:30px;clear:both }
footer > * { display:inline-block;margin-right:5px }
footer img { margin:0 0 -10px 0;width:30px }
footer a:hover { background:white;color:black;opacity: 0.75 }
```

## 2024, immediately before halftone

- Upstream commit: `a3a7cfcd442e3e573a99cf8186d2dcc9e043dd48`
- Blob SHA: `b54cf1a57a390b733fc7628ccf1fcb08170edb0d`
- `html` is a flat `#efefef`; no GIF yet.

```css
* { margin:0;padding:0;text-decoration:none;box-sizing:border-box;color:#000 }
html { background:#efefef }
body { background:#fff; font-family:serif;font-size:16px;overflow-x: hidden }
body > *, body main > *, main figure > div > *, main p, main q, main cite, main pre { margin-bottom:30px }
body .right { float:right }
body a.self, body a.parent { font-style:italic }
main a:hover, main a:hover > *, nav a:hover, nav main a:hover > * { background-color:#000;color:#fff;text-decoration:none }
table td, table th { vertical-align:top;padding:2.5px 5px;text-align:left }
table td > pre, table th > pre { background:none;padding:0;margin:0 }
table tr img { margin-bottom:0 }
hr { clear:both;border:0 }
header { float:left;margin:30px 60px 30px 30px }
header img { display:block }
nav { padding:25px 45px 60px;margin:0 }
nav ul { padding:0;margin:0 45px 0 0;display:inline-block;vertical-align:top }
nav ul li { list-style-type:none;white-space:pre }
nav ul li a { padding:0 4px}
main { margin-left:30px;max-width:624px;clear:both }
main a { text-decoration:underline }
main a[target="_blank"] { text-decoration-style:dotted }
main article { border-left:1px dotted #000;padding-left:25px;clear:both }
main cite { display:block;clear:both }
main cite:before { content:"— " }
main iframe { width:100% }
main h1, main h2, main h3, main h4, main h5 { max-width:400px }
main ul, main ol { margin:0 0 30px 30px }
main ul ul { margin-bottom:0 }
main ul li, main ol li { line-height:25px;padding:0 5px }
main figure img { display:block;margin:0 }
main figure figcaption { padding:15px 0 }
main figure:first-child { max-width: 100vw;margin-left: -30px;width: 800px }
main figure:first-child figcaption { padding-left:30px }
main p { line-height:160% }
main ::selection { background-color:#72dec2;color:#000;text-decoration:none }
main q { font-family:serif;font-size:18px;font-style:italic;display:block;max-width:400px }
main img, main svg { max-width:100%;display:inline-block;margin:0 0 25px }
main pre { overflow:auto;background:#efefef;padding:10px;font-size:80% }
main pre code, main pre i { color:#888 }
main code { white-space:pre }
main hr { clear:both }
main kbd { font-size:12px;display:inline-block;padding:0 5px;font-weight:bold;border-radius:4px;line-height:20px;border:2px solid #222 }
footer { padding:30px;line-height:30px;clear:both;margin:0;border-top:1px solid #000 }
footer a { display:inline-block;margin-right:3px }
footer a:hover { text-decoration:underline }
footer img { height:30px;vertical-align:middle;margin:0 3px }
footer div.right img { margin-left:10px }
div.codeview { background:#eee;border-radius:4px;overflow:hidden }
div.codeview iframe { height:405px;border:0;margin:0;display:block }
div.codeview pre { margin:0;background:#000;color:#fff }
div.codeview pre.src { background:#efefef;color:#000}
div.codeview pre a { float:right;color:#72dec2;text-decoration:none;font-weight:bold }
@media (prefers-color-scheme:dark) {
 * { color:#fff }
 html { background:#fff }
 body { background:#000 }
 main a:hover, main a:hover > *, nav a:hover, nav a:hover > * { background-color:#fff;color:#000;text-decoration:none }
 img[src*="svg"], img[src*="png"] { background:#fff;filter:invert(1) hue-rotate(180deg) }
 main pre { background:#111 }
 main table { border-style:solid }
 main th, main td { border-style:dotted }
 .nodark { filter:invert(0) hue-rotate(0deg) !important;background:transparent !important }
 footer { border-top:1px solid #fff }
}
```

## 2024, after halftone was introduced

- Upstream commit: `fed78a8874079f01c7e0b4449874010f2a0c2e7c`
- Blob SHA: `3795bfe388f5dafa956380309cc5b2349998f748`
- The flat background is replaced by the repeating GIF. The commit message is only `*`, with no explanation.

```css
* { margin:0;padding:0;text-decoration:none;box-sizing:border-box;color:#000 }
html { background-image:url(../media/icon/halftone.gif);background-repeat:repeat }
body { background:#fff;font-family:serif;font-size:16px;overflow-x:hidden }
body > *, body main > *, main figure > div > *, main p, main q, main cite, main pre { margin-bottom:30px }
body .right { float:right }
body a.self, body a.parent { font-style:italic }
main a:hover, main a:hover > *, nav a:hover, nav main a:hover > * { background-color:#000;color:#fff;text-decoration:none }
table td, table th { vertical-align:top;padding:2.5px 5px;text-align:left }
table td > pre, table th > pre { background:none;padding:0;margin:0 }
table tr img { margin-bottom:0 }
hr { clear:both;border:0 }
header { float:left;margin:30px 60px 30px 30px }
header img { display:block }
nav { padding:25px 45px 60px;margin:0 }
nav ul { padding:0;margin:0 45px 0 0;display:inline-block;vertical-align:top }
nav ul li { list-style-type:none;white-space:pre }
nav ul li a { padding:0 4px}
main { margin-left:30px;max-width:624px;clear:both }
main a { text-decoration:underline }
main a[target="_blank"] { text-decoration-style:dotted }
main article { border-left:1px dotted #000;padding-left:25px;clear:both }
main cite { display:block;clear:both }
main cite:before { content:"— " }
main iframe { width:100% }
main h1, main h2, main h3, main h4, main h5 { max-width:400px }
main ul, main ol { margin:0 0 30px 30px }
main ul ul { margin-bottom:0 }
main ul li, main ol li { line-height:25px;padding:0 5px }
main figure img { display:block;margin:0 }
main figure figcaption { padding:15px 0 }
main figure:first-child { max-width:100vw;margin-left:-30px;width:800px }
main figure:first-child figcaption { padding-left:30px }
main p { line-height:160% }
main ::selection { background-color:#72dec2;color:#000;text-decoration:none }
main q { font-family:serif;font-size:18px;font-style:italic;display:block;max-width:400px }
main img, main svg { max-width:100%;display:inline-block;margin:0 0 25px }
main pre { overflow:auto;background:#efefef;padding:10px;font-size:80% }
main pre code, main pre i { color:#888 }
main code { white-space:pre }
main hr { clear:both }
main kbd { font-size:12px;display:inline-block;padding:0 5px;font-weight:bold;border-radius:4px;line-height:20px;border:2px solid #222 }
footer { padding:30px;line-height:30px;clear:both;margin:0;border-top:1px solid #000 }
footer a { display:inline-block;margin-right:3px }
footer a:hover { text-decoration:underline }
footer img { height:30px;vertical-align:middle;margin:0 3px }
footer div.right img { margin-left:10px }
div.codeview { background:#eee;border-radius:4px;overflow:hidden }
div.codeview iframe { height:405px;border:0;margin:0;display:block }
div.codeview pre { margin:0;background:#000;color:#fff }
div.codeview pre.src { background:#efefef;color:#000}
div.codeview pre a { float:right;color:#72dec2;text-decoration:none;font-weight:bold }
@media (prefers-color-scheme:dark) {
 * { color:#fff }
 body { background:#000 }
 main a:hover, main a:hover > *, nav a:hover, nav a:hover > * { background-color:#fff;color:#000;text-decoration:none }
 img[src*="svg"], img[src*="png"] { background:#fff;filter:invert(1) hue-rotate(180deg) }
 main pre { background:#111 }
 main table { border-style:solid }
 main th, main td { border-style:dotted }
 .nodark { filter:invert(0) hue-rotate(0deg) !important;background:transparent !important }
 footer { border-top:1px solid #fff }
}
```
