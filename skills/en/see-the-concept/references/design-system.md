# Design language: reuse the code

**Copy the CSS, HTML, and JS below, then replace the project content.** The code defines colors, type, spacing, and breakpoints. Maintain one shared `styles.css` and `main.js`. Preserve project vocabulary; use the font fallbacks or local files in `assets/`.

## styles.css: tokens and layout

```css
:root {
  --color-bg: #FAF7F2;
  --color-bg-warm: #F5F0E8;
  --color-bg-code: #1E1E2E;
  --color-text: #2C2A28;
  --color-text-secondary: #6B6560;
  --color-text-muted: #9E9790;
  --color-border: #E5DFD6;
  --color-border-light: #EEEBE5;
  --color-surface: #FFFFFF;
  --color-surface-warm: #FDF9F3;
  --color-accent: #D94F30;
  --color-accent-hover: #C4432A;
  --color-accent-light: #FDEEE9;
  --color-accent-muted: #E8836C;
  --color-success: #2D8B55;
  --color-success-light: #E8F5EE;
  --color-error: #C93B3B;
  --color-error-light: #FDE8E8;
  --color-info: #2A7B9B;
  --color-info-light: #E4F2F7;
  --color-actor-1: #2A7B9B;
  --color-actor-2: #7B6DAA;
  --color-actor-3: #D4A843;
  --color-actor-4: #2D8B55;
  --font-display: 'Bricolage Grotesque', 'Noto Serif SC', Georgia, serif;
  --font-body: 'DM Sans', 'Noto Sans SC', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
  --text-xs: .75rem; --text-sm: .875rem; --text-base: 1rem;
  --text-lg: 1.125rem; --text-xl: 1.25rem; --text-2xl: 1.5rem;
  --text-3xl: 1.875rem; --text-4xl: 2.25rem;
  --text-5xl: 3rem; --text-6xl: 3.75rem;
  --leading-tight: 1.15; --leading-snug: 1.3;
  --leading-normal: 1.6; --leading-loose: 1.8;
  --space-1: .25rem; --space-2: .5rem; --space-3: .75rem;
  --space-4: 1rem; --space-5: 1.25rem; --space-6: 1.5rem;
  --space-8: 2rem; --space-10: 2.5rem; --space-12: 3rem;
  --space-16: 4rem; --space-20: 5rem; --space-24: 6rem;
  --content-width: 800px; --content-width-wide: 1000px;
  --nav-height: 50px;
  --radius-sm: 8px; --radius-md: 12px;
  --radius-lg: 16px; --radius-full: 9999px;
  --shadow-sm: 0 1px 2px rgb(44 42 40 / 5%);
  --shadow-md: 0 4px 12px rgb(44 42 40 / 8%);
  --shadow-lg: 0 8px 24px rgb(44 42 40 / 10%);
  --shadow-xl: 0 16px 48px rgb(44 42 40 / 12%);
  --ease-out: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
  --duration-fast: 150ms; --duration-normal: 300ms;
  --duration-slow: 500ms; --stagger-delay: 120ms;
  --code-keyword: #CBA6F7; --code-string: #A6E3A1;
  --code-function: #89B4FA; --code-comment: #A6ADC8;
  --code-number: #FAB387; --code-property: #F9E2AF;
  --code-operator: #94E2D5; --code-tag: #F38BA8;
  --code-attr: #F9E2AF; --code-value: #A6E3A1;
}
* { box-sizing: border-box; }
html { scroll-padding-top: calc(var(--nav-height) + 16px); }
body { margin: 0; padding-top: var(--nav-height); background: var(--color-bg);
  color: var(--color-text); font: 18px/1.6 var(--font-body); }
h1, h2, h3 { font-family: var(--font-display); line-height: 1.3; }
h1 { font-size: clamp(36px, 6vw, 60px); }
h2 { margin: 0 0 16px; font-size: 36px; font-weight: 700; }
h3 { font-size: 24px; font-weight: 600; }
p { margin: 0 0 16px; }
a { color: var(--color-accent-hover); text-underline-offset: 3px; }
button, summary { font: inherit; cursor: pointer; }
button { padding: 8px 16px; border: 0; border-radius: var(--radius-sm);
  background: var(--color-accent-hover); color: #fff;
  transition: transform var(--duration-fast) var(--ease-out); }
button:hover { transform: translateY(-2px); }
button:disabled { opacity: .6; cursor: default; transform: none; }
:focus-visible { outline: 3px solid var(--color-accent-hover); outline-offset: 3px; }
.chapter { padding: 64px 24px; }
.chapter:nth-of-type(even) { background: var(--color-bg-warm); }
.content { width: 100%; max-width: var(--content-width); margin-inline: auto; }
.wide { max-width: var(--content-width-wide); }
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.card, .aha { padding: 24px; border: 1px solid var(--color-border);
  border-radius: var(--radius-md); background: var(--color-surface);
  box-shadow: var(--shadow-sm); }
.aha { background: var(--color-accent-light); border-inline-start: 4px solid var(--color-accent); }
.actor { border-inline-start: 4px solid var(--actor); }
[data-actor="1"] { --actor: var(--color-actor-1); }
[data-actor="2"] { --actor: var(--color-actor-2); }
[data-actor="3"] { --actor: var(--color-actor-3); }
[data-actor="4"] { --actor: var(--color-actor-4); }
.status[data-status="success"] { color: var(--color-text); border-inline-start: 3px solid var(--color-success); background: var(--color-success-light); }
.status[data-status="error"] { color: var(--color-text); border-inline-start: 3px solid var(--color-error); background: var(--color-error-light); }
.status[data-status="info"] { color: var(--color-text); border-inline-start: 3px solid var(--color-info); background: var(--color-info-light); }
.chapter-nav { position: fixed; inset: 0 0 auto; height: var(--nav-height); z-index: 10;
  background: var(--color-bg); border-bottom: 1px solid var(--color-border); }
.nav-links { display: flex; align-items: center; gap: 16px; height: 100%;
  padding-inline: 16px; overflow-x: auto; white-space: nowrap; font-size: 14px; }
.nav-links a { flex: none; padding: 4px; color: var(--color-text-secondary); }
.nav-links a:focus-visible { outline-offset: -2px; }
.nav-links a[aria-current="location"] { color: var(--color-accent-hover); font-weight: 700; }
.nav-links a[data-visited]::after { content: " ·"; }
.reading-progress { position: fixed; inset: var(--nav-height) 0 auto; width: 100%;
  height: 3px; border: 0; appearance: none; z-index: 11; background: var(--color-border); }
.reading-progress::-webkit-progress-bar { background: var(--color-border); }
.reading-progress::-webkit-progress-value { background: var(--color-accent); }
.reading-progress::-moz-progress-bar { background: var(--color-accent); }
.code-pair { margin: 24px 0; border: 1px solid var(--color-border); border-radius: var(--radius-md); }
.code-pair figcaption { padding: 12px 16px; font-size: 14px; color: var(--color-text-secondary); }
.code-head, .code-row { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
.code-head > *, .code-row > * { min-width: 0; margin: 0; padding: 12px 16px; }
.code-head { font-size: 14px; font-weight: 700; }
.code-row + .code-row { border-top: 1px solid var(--color-border); }
.source { display: grid; grid-template-columns: 3ch minmax(0, 1fr); gap: 12px;
  background: var(--color-bg-code); color: #CDD6F4; }
.line-no { color: var(--code-comment); user-select: none; font: 14px/1.6 var(--font-mono); }
pre { min-width: 0; margin: 0; white-space: pre-wrap; overflow-wrap: anywhere; tab-size: 2; }
code { font: 14px/1.6 var(--font-mono); }
.explanation { background: var(--color-surface-warm); font-size: 16px; }
.kw { color: var(--code-keyword); } .str { color: var(--code-string); }
.fn { color: var(--code-function); } .comment { color: var(--code-comment); }
.num { color: var(--code-number); } .prop { color: var(--code-property); }
.op { color: var(--code-operator); } .tag { color: var(--code-tag); }
.attr { color: var(--code-attr); } .value { color: var(--code-value); }
.diagram { max-width: 100%; overflow: auto; }
.diagram svg { display: block; max-width: 100%; height: auto; }
@media (max-width: 768px) {
  h2 { font-size: 30px; } h1 { font-size: 36px; }
  .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .code-head { display: none; } .code-row { grid-template-columns: minmax(0, 1fr); }
}
@media (max-width: 480px) {
  h2 { font-size: 24px; } .chapter { padding: 32px 16px; }
  .cards { grid-template-columns: minmax(0, 1fr); }
  .card, .aha { padding: 16px; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
  button:hover { transform: none; }
}
```

## index.html: sections and paired lines

**Each `.code-row` contains one source line and its explanation.** Desktop places them side by side; at ≤768px each line stacks code before explanation. Preserve source whitespace, actual line numbers, and file references. Escape `& < >` when inserting HTML; highlighting adds markup without changing source text. Replace this demo with project evidence; give new sections unique IDs.

```html
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project concepts</title>
<link rel="stylesheet" href="styles.css">
<script src="main.js" defer></script>
<nav class="chapter-nav" aria-label="Chapters">
  <div class="nav-links"><a href="#purpose">Purpose</a><a href="#implementation">Implementation</a></div>
</nav>
<progress class="reading-progress" max="100" value="0" aria-label="Reading position"></progress>
<main>
  <section class="chapter" id="purpose"><div class="content">
    <h1>Project concepts</h1><h2>What problem does it solve?</h2>
    <p>Explain its purpose through one concrete project scenario.</p>
    <details class="aha"><summary>Aha: why remember state?</summary>
      <p>Like a shopping list remembering selected items, state lets the next action continue from earlier results.</p>
    </details>
  </div></section>
  <section class="chapter" id="implementation"><div class="content wide">
    <h2>How the design becomes code</h2><p>Check one action against its implementation, line by line.</p>
    <figure class="code-pair" aria-labelledby="source-caption">
      <figcaption id="source-caption">Demo code; replace with the project file path, symbol, and actual line numbers before delivery.</figcaption>
      <div class="code-head" aria-hidden="true"><span>Code</span><span>Plain explanation</span></div>
      <div class="code-row">
        <div class="source"><span class="line-no" aria-hidden="true">1</span><pre><code><span class="kw">const</span> count = items.length;</code></pre></div>
        <p class="explanation">Count the items in the list and name that number count.</p>
      </div>
      <div class="code-row">
        <div class="source"><span class="line-no" aria-hidden="true">2</span><pre><code><span class="kw">return</span> count;</code></pre></div>
        <p class="explanation">Give that number back to the caller.</p>
      </div>
    </figure>
  </div></section>
</main>
</html>
```

## main.js: navigation and reading position

Track scroll position and reached sections; **reading progress does not measure understanding**. Native anchors preserve Tab, Enter, and browser history. This code does not intercept arrow keys, hide content, or force scrolling.

```js
const nav = document.querySelector('.chapter-nav');
const progress = document.querySelector('.reading-progress');
const links = [...document.querySelectorAll('.nav-links a[href^="#"]')];
const entries = links.map(link => ({ link, section: document.getElementById(link.hash.slice(1)) }))
  .filter(entry => entry.section);
let scheduled = false;
function updateReading() {
  scheduled = false;
  const page = document.documentElement;
  const distance = page.scrollHeight - page.clientHeight;
  const percent = distance > 0 ? Math.min(100, Math.max(0, page.scrollTop / distance * 100)) : 0;
  if (progress) progress.value = percent;
  const offset = (nav?.getBoundingClientRect().height ?? 0) + 24;
  let current = entries[0];
  for (const entry of entries) {
    if (entry.section.getBoundingClientRect().top <= offset) {
      current = entry;
      entry.link.dataset.visited = '';
    }
  }
  for (const entry of entries) {
    if (entry === current) entry.link.setAttribute('aria-current', 'location');
    else entry.link.removeAttribute('aria-current');
  }
}
function scheduleReading() {
  if (!scheduled) { scheduled = true; requestAnimationFrame(updateReading); }
}
addEventListener('scroll', scheduleReading, { passive: true });
addEventListener('resize', scheduleReading);
addEventListener('load', scheduleReading);
updateReading();
```

## Content-specific rules

- **Separate actor and status:** `.card.actor[data-actor="1"]` keeps a stable actor identity; include its name. Use `.status[data-status="success|error|info"]` for outcomes, with the words “Success / Error / Info.” Reserve `--color-text-muted` for decoration; essential labels use body or secondary text.
- **Reflow diagrams:** give SVG a `viewBox`; below 480px use vertical coordinates and reorient arrows. When a wide diagram must remain wide, wrap it in `<div class="diagram" role="region" aria-label="Diagram name" tabindex="0">` with an adjacent text explanation. Restore selection using the same concept ID after redraw.
- **Make interactions checkable:** label buttons “Next step / Reset.” Each action updates the diagram, state values, and explanation together; announce results through `aria-live="polite"`. Reset restores demo initial values. Default to no automatic entrance animation; when transitions are needed, reuse the 150/300/500ms tokens and respect reduced motion.
- **Verify:** open `index.html` offline; at 1000/768/480/320px check no page-wide horizontal overflow and correct line pairing. Operate with Tab/Enter; read all content with JS disabled. Non-scrollable pages report 0 progress. Require ≥4.5:1 body contrast and ≥3:1 large-text and control-boundary contrast.
