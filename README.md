# 天青 Design Language

**把宋代美学做成 UI 设计系统。** 9 座宋代窑口，每个颜色都有出处——一色一窑，每个决策皆有依据。

- 10 阶天青色阶 + 8 组语义色 + 明暗双模式
- 五原则：器无赘饰 · 釉色为美 · 温润如玉 · 计白当黑 · 动若釉流
- 完整 Design Tokens（CSS / JSON，Style Dictionary 与 Figma Tokens 兼容）
- 可运行参考实现 + AI 速查卡

## 快速开始

```bash
# 打开参考实现（浏览器直接预览）
open demo/index.html

# 引入设计令牌
<link rel="stylesheet" href="assets/tokens.css">
```

## 核心色（一色一窑）

| 色值 | 名字 | 出处 |
|---|---|---|
| `#7FA8B8` | 天青 | 汝窑 · 全局主色 |
| `#B5CFC8` | 粉青 | 龙泉 · 次级强调 |
| `#EEF1F3` | 月白 | 官窑 · 背景 |
| `#F7F4EC` | 象牙白 | 定窑 · 表面 |
| `#22201C` | 黑釉 | 建窑 · 主文字 |
| `#5C7A52` | 豆青 | 耀州 · 成功态 |
| `#A47C48` | 茶褐 | 茶席 · 警示点缀 |
| `#A65E44` | 窑变赭 | 钧窑 · 错误态 |

## 五原则

1. **器无赘饰** —— 极简。装饰若有若无，用留白和字重分层
2. **釉色为美** —— 低饱和，单主色，天青占比 <15%
3. **温润如玉** —— 圆角 ≥6px，漫反射阴影，禁纯黑投影
4. **计白当黑** —— 区块间距 ≥40px，单屏视觉焦点 ≤3
5. **动若釉流** —— 动效 200–500ms 缓出，禁弹跳

## 目录

```
SKILL.md                   技能入口（Skill 用法）
assets/
  design-language-ai.md    AI 速查卡（AI 使用前必读）
  design-language.md       完整规范速查
  tokens.css               可引入的 CSS 设计令牌（含暗色模式）
  tokens.json              Design Tokens JSON（Figma 兼容）
  palette.png              宋瓷釉色板参考图
  prompt-guide.md          宋瓷生图提示词速查（附带功能）
demo/
  index.html               可运行参考实现（品牌官网，明暗双模式）
  out/                     demo 截图与发布文案
```

## 验证

参考实现经过实测：双模式渲染、组件态、对比度（WCAG AA）、响应式。验证中发现的缺陷（按钮对比度 2.05→4.93:1、暗色纯黑阴影）已修复。

## License

MIT
