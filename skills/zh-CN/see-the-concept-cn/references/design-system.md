# 设计语言：直接复用代码

**先复制下面的 CSS、HTML 和 JS，再替换项目内容。** 配色、字号、间距和断点以代码为准；全站只维护一份 `styles.css` 和 `main.js`。保留项目术语，字体使用本机回退或 `assets/` 中的本地文件。

## styles.css：变量与布局

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

## index.html：章节与逐行对照

**每个 `.code-row` 放一行源码和对应解释。** 桌面左右并排；≤768px 时每行先代码、后解释。保留源码空格、真实行号与文件定位；插入 HTML 时转义 `& < >`，高亮只加标签，不改源码。下面是演示内容，交付时换成项目证据；新章节沿用结构并使用唯一 ID。

```html
<!doctype html>
<html lang="zh-CN">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>项目概念图解</title>
<link rel="stylesheet" href="styles.css">
<script src="main.js" defer></script>
<nav class="chapter-nav" aria-label="章节">
  <div class="nav-links"><a href="#purpose">用途</a><a href="#implementation">实现</a></div>
</nav>
<progress class="reading-progress" max="100" value="0" aria-label="阅读位置"></progress>
<main>
  <section class="chapter" id="purpose"><div class="content">
    <h1>项目概念图解</h1><h2>它解决什么问题</h2>
    <p>用一个项目中的具体场景说明用途。</p>
    <details class="aha"><summary>啊哈：为什么要记住状态？</summary>
      <p>像购物清单记住已选物品，状态让下一步操作接着已有结果继续。</p>
    </details>
  </div></section>
  <section class="chapter" id="implementation"><div class="content wide">
    <h2>设计怎样落到代码里</h2><p>逐行核对一个动作的实现。</p>
    <figure class="code-pair" aria-labelledby="source-caption">
      <figcaption id="source-caption">演示代码；交付时换成项目文件路径、符号及真实行号。</figcaption>
      <div class="code-head" aria-hidden="true"><span>代码</span><span>逐行解释</span></div>
      <div class="code-row">
        <div class="source"><span class="line-no" aria-hidden="true">1</span><pre><code><span class="kw">const</span> count = items.length;</code></pre></div>
        <p class="explanation">数出清单里有多少项，把数量记为 count。</p>
      </div>
      <div class="code-row">
        <div class="source"><span class="line-no" aria-hidden="true">2</span><pre><code><span class="kw">return</span> count;</code></pre></div>
        <p class="explanation">把这个数量交给调用它的地方。</p>
      </div>
    </figure>
  </div></section>
</main>
</html>
```

## main.js：导航与阅读位置

只标记滚动位置与已到达章节，**不把阅读进度当作理解程度**。原生锚点保留 Tab、Enter 和浏览器历史行为；代码不接管方向键，不自动隐藏正文，不强制滚动。

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

## 按内容替换的规则

- **角色与状态分开：** `.card.actor[data-actor="1"]` 表示固定角色，卡片内写角色名；结果用 `.status[data-status="success|error|info"]`，同时写“成功／失败／提示”。`--color-text-muted` 只作装饰；必要标签用正文或次级文字色。
- **图随屏幕重排：** SVG 用 `viewBox`；480px 以下改为竖向坐标并同步调整箭头。必须保留宽图时，包进 `<div class="diagram" role="region" aria-label="图名" tabindex="0">`，在图旁提供文字说明。重绘后用同一概念 ID 恢复选择。
- **交互可核对：** 按钮明确写“下一步／重置”；每次操作同时更新图、状态值与解释，用 `aria-live="polite"` 宣布结果。重置恢复演示初值。默认无自动入场动画；需要转场时复用 150/300/500ms 变量，遵循减少动态效果设置。
- **验收：** 断网打开 `index.html`；在 1000/768/480/320px 检查无页面横向溢出、代码与解释逐行配对；Tab/Enter 能操作；禁用 JS 仍能读全部正文；页面不能滚动时进度为 0；正文对比度≥4.5:1，大字和控件边界≥3:1。
