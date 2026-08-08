# AGENTS.md

This repository contains **宋瓷 (Songci)** — a reusable skill pack that turns Song Dynasty porcelain aesthetics into AI image/video-generation prompts and a Tianqing (天青) UI design language — plus self-contained HTML cover templates for Xiaohongshu / WeChat / WeChat Official Accounts.

## What's inside

| Path | What it is |
|---|---|
| `skills/宋瓷/` | The skill in standard SKILL.md format (`name` + `description` frontmatter). Load `SKILL.md`; supporting assets in `assets/` |
| `templates/*.html` | Self-contained cover templates — single-file, html2canvas inlined, no network/build needed. Open in any browser. Chinese filenames |
| `docs/` | Full documentation — design specs (PDF/MD), prompt guides, WeChat publishing kit (`wechat_publish.py`), covers. Chinese filenames |
| `README.md` / `README_en.md` | Bilingual overview (Chinese primary / English) |

## For agents

The skill lives at `skills/宋瓷/SKILL.md` and follows the standard SKILL.md convention, so any agent that supports it (Claude Code, CodeBuddy, Cursor, Codex, etc.) can use it directly.

- **When the user asks for 宋瓷-style prompts, Song porcelain aesthetics, 新中式 design, or Tianqing UI design** → read `skills/宋瓷/SKILL.md`, then use `assets/prompt-guide.md` (prompt cheatsheet) and `assets/design-language.md` (UI design language) as needed.
- **Install into a local agent:**
  - Any SKILL.md-compatible agent: `npx skills add ilps2/songci-skill`
  - Claude Code: `mkdir -p ~/.claude/skills && cp -r skills/宋瓷 ~/.claude/skills/`
  - CodeBuddy: `cp -r skills/宋瓷 ~/.codebuddy/skills/`
- **Trigger keywords:** 宋瓷, 宋代美学, 宋韵, 汝窑, 官窑, 哥窑, 钧窑, 龙泉, 建窑, 天青, 粉青, 梅子青, 开片, 金丝铁线, 窑变, 兔毫, 曜变, 新中式, Song porcelain, Ru ware, Jian ware, celadon.

## Notes

- HTML templates: open `templates/宋瓷风·通用主题版模板.html` in a browser → click any text to edit → click bottom glaze dots to switch themes → export PNG. No server, no build.
- `docs/wechat_publish.py` reads `WECHAT_APPID` / `WECHAT_SECRET` from env vars — placeholders only, no real secrets in this repo.
- Docs filenames are Chinese; README provides the bilingual index.
