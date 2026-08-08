# 宋瓷 · Songci Skill & Tianqing UI Templates

> Turn Song Dynasty porcelain aesthetics into **AI image-generation prompts** and a **UI design language**,
> plus a "color-shifting" Songci-style cover template (works for Xiaohongshu / WeChat / WeChat Official Accounts).

![Cover preview](docs-cover.png)

---

## 📦 Repository Structure

```
songci-skill/
├── AGENTS.md                 # Agent-facing repo guide (auto-read by Claude Code / Cursor / Codex, etc.)
├── docs-cover.png            # README cover image
├── skills/
│   └── 宋瓷/                 # Standard SKILL.md skill pack (works with any agent, copy & use)
│       ├── SKILL.md          # Main skill file (trigger words + instructions)
│       └── assets/           # Prompt cheatsheet / design language / design tokens / glaze palette
├── templates/                # HTML templates (self-contained single files, copy & use)
│   ├── 宋瓷风·通用主题版模板.html   # ★ Newest: 8-glaze one-click theme switcher + fully editable text
│   ├── 宋瓷风·通用文字版模板.html   # Generic text version
│   ├── 宋瓷风小红书通用模板.html     # 5-scenario preset version
│   ├── 宋瓷风小红书模板.html         # Fashion / outfit version
│   └── cover_*.png                 # 6 ready-made covers
└── docs/                     # Full documentation (filenames are in Chinese)
    ├── 天青·宋瓷UI设计语言规范        # Design spec PDF/MD + tokens.css/json + design system demo
    ├── 宋瓷美学·生图提示词研究手册    # Image-generation prompt guide
    ├── 电影运镜提示词速查手册         # Cinematography prompt cheatsheet
    ├── 宋瓷釉色·新中式女装配色方案    # Fashion colorways × 6 glazes
    ├── 宋瓷风广告背景·女装mockup     # Ad background mockup
    ├── 公众号文章 + 排版版 + 封面     # WeChat Official Account publishing kit
    ├── 公众号API发布说明 + wechat_publish.py  # Official API publishing script
    └── 宋瓷釉色板.png
```

---

## ✨ What the Songci Skill Can Do

### 1. Songci-style Image / Video Generation Prompts

**Core formula**: `kiln glaze + vessel form + glaze surface character + display scene + lighting + photographic texture`

- **9 kiln cheat-sheets**: Ru kiln sky-blue / Guan kiln crackle / Ge kiln golden-wire-iron-thread / Jun kiln kiln transmutation / Jian kiln hare's-fur & yohen / Longquan powder-green, and more
- **Three scene grammars**: museum-grade reproduction / literati ambiance creation / macro detail study
- **Anti-failure negative prompts**: prevents sky-blue from turning bright blue, prevents drifting into Ming/Qing polychrome styles

Example:

```
ru ware porcelain vase, meiping form, sky-blue glaze, jade-like muted tone,
subtle cicada-wing crackle, dim museum display, soft top spotlight,
dark backdrop, product photography, photorealistic, 8k
```

### 2. Tianqing UI Design Language (Songci → Interface)

- **Five principles**: form without adornment (器无赘饰) · glaze color is beauty (釉色为美) · warm and smooth as jade (温润如玉) · design with negative space (计白当黑) · motion like flowing glaze (动若釉流)
- **Color tokens**: Tianqing primary (<15%), moon-white base, ivory content, black-glaze text, tea-brown accents — a complete system with no borrowed colors
- Ships with `tokens.css` / `tokens.json`, ready to drop into a project or import into Figma

---

## 📱 HTML Template Features

| Feature | Description |
|---|---|
| Single-file self-contained | html2canvas inlined — double-click to use on any device, no internet needed |
| Fully editable text | Title / tag / seal / main copy / body / hashtags / brand — click to edit, placeholders when empty |
| 8-glaze one-click theme | Tianqing / powder-green / moon-white / pea-green / ivory / tea-brown / black glaze / kiln transmutation — text color auto-adjusts for contrast |
| Brand name sync | Bottom-left brand name follows the theme switch (黑釉 · HEIYOU) |
| Adaptive seal | Seal anchors to the right and extends leftward as text grows |
| One-click PNG export | Edit dashed border auto-hides on export, 2× resolution output |
| 5 scenario presets | Food / home / travel / products / knowledge — one-click copy fill |

**Use cases**: Xiaohongshu covers, WeChat Moments stickers, Official Account headers & cards, WeChat Channels covers, e-commerce ambience images, brand proposal mockups.

---

## 🚀 Installation & Usage

### Install the Skill (any agent)

The skill uses the standard `SKILL.md` format (`skills/宋瓷/SKILL.md`), compatible with Claude Code / CodeBuddy / Cursor / Codex and other mainstream agents:

```bash
# One-command install (any SKILL.md-compatible agent)
npx skills add ilps2/songci-skill

# Claude Code (Mac / Linux)
mkdir -p ~/.claude/skills && cp -r skills/宋瓷 ~/.claude/skills/

# CodeBuddy (Mac)
cp -r skills/宋瓷 ~/.codebuddy/skills/
# CodeBuddy (Windows)
# Copy skills/宋瓷 to %USERPROFILE%\.codebuddy\skills\
```

After restarting a session, mentioning 「汝窑 / 天青 / 宋瓷风 UI / 新中式」 or `@宋瓷` triggers the skill automatically.

### Use the Templates

Open `templates/宋瓷风·通用主题版模板.html` in a browser (Chrome / Safari / Edge):

1. Click any text area to edit the content
2. Click the glaze color dots at the bottom to switch themes
3. Click "导出 PNG 图片" (Export PNG) to download the finished cover

---

## 📄 License

MIT © 2026

---

*Inspired by the aesthetics of the five great Song Dynasty kilns (Ru / Guan / Ge / Jun / Ding) and the Jian & Longquan kilns.*
