---
name: songci
description: 宋瓷美学应用技能 —— 用于①宋瓷风格的 AI 生图/生视频提示词写作（汝窑天青、哥窑开片、钧窑窑变、建窑兔毫/曜变、龙泉粉青等）；②宋瓷美学转译的 UI 设计语言（天青 Design Language）应用于界面、品牌、可视化设计；③宋瓷风小红书封面设计与批量生产（9 种布局 × 20 场景 × 6 釉色主题 × 4 尺寸的封面生成器，覆盖语录/图文/清单/教程/对比/拼图/测评/海报等主流封面类型）。触发关键词：宋瓷、宋代美学、宋韵、汝窑、官窑、哥窑、钧窑、定窑、龙泉、建窑、耀州、磁州、天青釉、天青、粉青、梅子青、开片、金丝铁线、窑变、兔毫、油滴、曜变、茶盏、梅瓶、青瓷、白瓷、黑釉、新中式、国风 UI、宋瓷风提示词、天青设计语言、小红书封面、XHS 封面、封面图、封面模板、封面设计、笔记封面、Song porcelain、Ru ware、Jian ware、celadon、cover。
version: "2.0.0"
author: "CodeBuddy"
created: "2026-08-07"
updated: "2026-08-13"
allowed-tools: Read, Write, Edit, Bash, WebSearch, ImageGen
---

# 宋瓷 · 美学应用技能

> 目标：把宋代瓷器美学的完整知识体系，转化为可执行的「生图/生视频提示词」与「UI 设计语言」，供任何设计类任务直接调用。
> `<skill-directory>` 指本 Skill 所在目录。详细资产见 `<skill-directory>/assets/`。

## When to Use

- 用户要求生成 **宋瓷风格 / 宋代美学 / 宋韵 / 新中式** 的图片或视频提示词。
- 用户要求做 **宋瓷风的 UI、网站、App、品牌、海报、数据可视化** 设计。
- 用户要求做 **小红书封面 / 笔记封面 / 封面图**：语录、好物、家居、穿搭、美食、教程、测评、对比、拼图、海报、旅行攻略等。
- 用户提到窑口名（汝窑/官窑/哥窑/钧窑/定窑/龙泉/建窑/耀州/磁州）、釉色词（天青/粉青/梅子青/月白/豆青/黑釉）、工艺词（开片/金丝铁线/窑变/兔毫/油滴/曜变）、器型词（梅瓶/茶盏/弦纹瓶…）。
- 用户 @ 提到「宋瓷」「天青」「宋瓷 skill」「song porcelain」。

## 核心公式（必须遵守）

> **生图提示词** = 窑口釉色 + 器型 + 釉面特征 + 展示场景 + 光线 + 摄影质感
> **UI 设计** = 天青定主调 + 月白铺底 + 象牙白承内容 + 黑釉立文字 + 茶褐点睛；衬线题标题，无衬走正文；圆角皆过 6px；阴影不带纯黑；间距敢留白；动效缓如釉。

---

## A. 宋瓷生图 / 生视频提示词

### A1. 窑口速查（核心关键词，直接写入提示词）

| 窑口 | 英文关键词 | 釉色/特征 | 典型器型 |
|---|---|---|---|
| 汝窑 | `ru ware` | sky-blue glaze 天青、jade-like、subtle hairline crackle、muted pale blue | meiping、vase with raised bow-string lines、tripod brush washer |
| 官窑 | `guan ware` | thick powder-blue glaze、large ice-crackle、purple mouth & iron-brown foot | vase with tubular handles |
| 哥窑 | `ge ware` | crackled glaze、golden thread & iron-wire crackle、fish-roe crazing | jar、brush washer |
| 钧窑 | `jun ware` | kiln transmutation、rose-purple & sky-blue mottled、crimson splash | flower pot、zun |
| 定窑 | `ding ware` | ivory-white porcelain、incised lotus decoration、unglazed rim | meiping、bowl |
| 龙泉 | `longquan celadon` | powder-blue / plum-green glaze、thick jade-like surface | meiping、phoenix-handled vase、li-style censer |
| 建窑 | `jian ware` | black glaze、hare's fur streaks、oil spot、yohen(曜变) | tea bowl (conical) |
| 磁州 | `cizhou ware` | white slip with black painted decoration | jar、pillow |
| 耀州 | `yaozhou ware` | carved celadon、olive-green glaze、sharp incised relief | bowl、vase |

### A2. 釉面特征词典

`hairline crackle`(蝉翼纹) / `ice-crackle`(冰裂纹) / `golden thread & iron-wire`(金丝铁线) / `kiln transmutation`(窑变) / `hare's fur`(兔毫) / `oil spot`(油滴) / `yohen`(曜变) / `sesame-seed spur marks`(支钉痕) / `jade-like`(玉感) / `muted`(低饱和) / `thick glaze`(厚釉)

### A3. 展示场景三套语法

- **博物馆级**（研究还原）：`museum display, soft spotlight, dark backdrop, product photography, photorealistic, 8k`
- **文人氛围**（美学创作）：`literati study, tea ceremony, wooden table, warm side light, wabi-sabi, film still, cinematic`
- **细节微距**（纹理研究）：`macro photography, extreme close-up on glaze, raking light, fine art photography`

### A4. 完整示例（可直接输出给用户）

```
ru ware porcelain vase, meiping form, sky-blue glaze, jade-like muted tone,
subtle cicada-wing crackle, dim museum display, soft top spotlight,
dark backdrop, product photography, photorealistic, 8k
```

### A5. 通用负面词（必须附带）

```
negative: vivid colors, painted floral decoration, glossy plastic look,
busy background, cluttered scene, watermark, text, modern style
```

### A6. 生视频运镜（宋瓷动态表达）

`camera orbits 360° around the vase`(旋转鉴赏) / `slowly dollies in on the glaze surface`(微距推镜) / `hot tea poured into the jian bowl, steam rising`(茶叙) / `soft light moving across the celadon`(光影流动) / 时长 200–500ms 原则仅用于 UI 动效，视频运镜用 slowly/smooth 修饰。

### A7. 防翻车要点

天青易艳蓝→加 muted/pale；易变明清彩瓷→强调 monochrome glaze, no painted decoration；开片易过密→subtle/hairline；兔毫易花→单一特征。

---

## B. 天青 UI 设计语言（宋瓷 → 界面）

### B1. 五原则

器无赘饰(极简) · 釉色为美(低饱和单主色) · 温润如玉(大圆角+漫反射阴影) · 计白当黑(大留白) · 动若釉流(动效克制)

### B2. 核心色彩令牌（UI/品牌/图表通用）

| Token | 色值 | 用途 |
|---|---|---|
| `--color-primary-500` | `#7FA8B8` | 天青·全局主色（汝窑） |
| `--color-primary-600` | `#648C9E` | 深天青·Hover/强调 |
| `--color-secondary-400` | `#B5CFC8` | 粉青·次级强调（龙泉） |
| `--color-success-500` | `#5C7A52` | 豆青·成功（耀州） |
| `--color-warning-500` | `#A47C48` | 茶褐·警示/点缀 |
| `--color-danger-500` | `#A65E44` | 窑变赭·错误（钧窑） |
| `--color-neutral-0` | `#F7F4EC` | 象牙白·表面（定窑） |
| `--color-neutral-50` | `#EEF1F3` | 月白·背景（官窑） |
| `--color-neutral-100` | `#E5E0D4` | 汝釉·边框 |
| `--color-neutral-900` | `#22201C` | 黑釉·主文字（建窑） |

### B3. 字体 / 圆角 / 阴影 / 间距 / 动效

- 字体：标题衬线 `Noto Serif SC`，正文无衬线 `Noto Sans SC`；正文行高 ≥1.7
- 圆角：sm 8 / md 14 / lg 22 / full 999（**禁用 <6px 直角**）
- 阴影：漫反射玉感，带天青冷灰，禁纯黑；`0 8px 24px rgba(34,32,28,.07)`
- 间距：4/8/16/24/40/64/96px；区块留白 ≥40px；单屏视觉焦点 ≤3
- 动效：fast 200 / base 350 / slow 500ms，缓出，禁弹跳；位移 ≤16px
- 规则：**禁纯黑 #000 与纯白 #FFF**

### B4. 暗色模式（黑釉主题）

背景 `#17150F`、表面 `#221F18`、边框 `#3A352B`、文字 `#EDE8DC`；主色提亮为 `primary.300 #9FB9C6`。

### B5. 组件要点

- 按钮 Primary：天青底+白字+full 圆角+天青柔影；Ghost：透明+天青描边；禁用：汝釉底+灰陶字
- 卡片：象牙白底+22px 圆角+soft 阴影，悬停 lift+上浮 4px
- 标签：语义色 14% 透明度底 + 500/600 号文字，full 圆角
- 输入框：`#FFFDF7` 底+汝釉边框+14px 圆角，聚焦天青边+4px 光晕
- 图表：主序列天青/深天青，次序列粉青/豆青，第三序列茶褐/窑变赭，网格极淡

---

## C. 小红书封面体系（宋瓷 → 封面）

> 工具：`<skill-directory>/templates/宋瓷风小红书封面生成器.html`（单文件、免构建、可导出 PNG）
> 完整手册：`<skill-directory>/assets/xhs-cover-guide.md`（平台规范 / 类型学 / 文案公式 / 批量流程 / 避坑）

### C1. 平台硬规范（必守）

| 项 | 规范 |
|---|---|
| 首选尺寸 | 3:4 竖版 1080×1440（信息流展示面积最大） |
| 其他尺寸 | 1:1 方图（干货合集）、9:16（视频封面）；慎用 4:3 横版 |
| 安全区 | 四边留 6%–10%；底部 15% 是点赞/标题盲区，不放关键信息 |
| 文字 | 标题 ≤15 字；文字占比 ≤30%；禁二维码/联系方式/极限词 |

### C2. 类型 → 布局映射（覆盖主流封面需求）

| 需求 | 布局 | 适用 |
|---|---|---|
| 金句/观点/读书/情感 | `quote` 大字语录 | 一行大标题撑场 |
| 好物/家居/穿搭/美食 | `photo` 图文卡 | 图占 60% + 标题 2 行 |
| 设计分享/人物故事 | `magazine` 杂志分栏 | 左图右文、竖排标签 |
| 干货/攻略/科普 | `list` 清单攻略 | 序号徽章 3–6 条 |
| 教程/健身/食谱 | `steps` 步骤教程 | 步骤章 + 小图 |
| 横评/二选一 | `compare` 对比 PK | 双栏 + VS 章 |
| 年度图集/多图种草 | `collage` 拼图九宫 | 3×3 网格 |
| 测评/美妆/数码 | `score` 测评评分 | 大分数 + 维度条 |
| 风景/活动/招募 | `poster` 全图海报 | 全图 + 渐变遮罩 |

### C3. 封面设计规范（宋瓷转译）

- **色板**：与 B2 令牌同源；`--primary` 主色、`--accent` 茶褐点缀、`--bg` 月白渐变、`--ink` 黑釉文字。禁纯黑/纯白/高饱和。
- **字号阶梯**（3:4、画布宽 1080px）：大标题 ≈136px / 中标题 ≈95px / 小标题 ≈70px / 正文 ≈38px / 标签 ≈31px。标题宋体，正文黑体。
- **装饰**：开片纹（透明度 ≤.06）、双线框+四角菱点、单字印章、釉色带；同时出现 ≤2 类。
- **主题 × 品类**：天青→知识/职场；象牙→家居/手作；粉青→风景/旅行；窑变→美妆/时尚；黑釉→数码/高冷；月白→通用。
- **文案公式**：数字型「3步泡一盏好茶」/ 悬念型「汝窑还是龙泉」/ 人群型「学生党必看」/ 场景型「把家装成宋代书房」。

### C4. 工作流

1. **定布局**：按内容类型选 C2 布局（默认 3:4 尺寸）。
2. **定场景**：20 个内置场景（金句/读书/好物/家居/穿搭/探店/攻略/教程/测评…）直接套用，改文案即用。
3. **定釉色**：按品类选主题；同账号系列固定主题+尺寸，形成品牌辨识度。
4. **生产**：打开生成器 → 点画布文字直接编辑 → 图片槽导入本地照片 → 导出 PNG（1080 宽输出，3:4 → 1080×1440 合规）。
5. **批量**：URL hash 直连场景：`宋瓷风小红书封面生成器.html#layout=list&scene=gonglue&theme=ru&size=34`。
6. **生成器不可用时**：按 C1/C3 规范手写 HTML/CSS 实现同款封面（参考 B 章令牌）。

---

## 应用流程（Step-by-Step）

### 场景 1：用户要宋瓷风生图/生视频提示词

1. 确认用户目标：器物还原（博物馆级）/ 氛围创作（文人向）/ 细节研究（微距）？
2. 按「窑口 → 器型 → 釉面特征 → 场景 → 光线 → 质感」组装提示词。
3. 必带负面词（A5）；提示生图模型用「景别+角度+焦段」、生视频用「运镜+速度」。
4. 若用户需要实测：告知可用 ImageGen 生成验证（消耗积分），再执行。

### 场景 2：用户要宋瓷风 UI / 品牌 / 可视化设计

1. 用 B2 色彩令牌定色；大面积只用月白/象牙白/黑釉，天青占比 <15%，茶褐 <5%。
2. 字体按 B3；组件按 B5；暗色模式按 B4。
3. 可直接引用 `<skill-directory>/assets/tokens.css` 与 `tokens.json`。
4. 交付 HTML demo 时，遵循五原则并保持「装饰若有若无」。

### 场景 3：用户要小红书封面 / 笔记封面

1. 判断内容类型 → C2 选布局；问清是否有照片（有图用 photo/poster/collage，无图用 quote/list/steps）。
2. 选釉色主题（C3 品类映射）与尺寸（默认 3:4）。
3. 用 C4 工作流生产：内置场景套文案 → 画布编辑 → 导入图片 → 导出 PNG（1080/1620）。
4. 交付要点：告知布局/主题/尺寸选择依据；同账号批量出图时建议固定主题统一风格；提醒底部 15% 盲区与文字 ≤15 字。

---

## 输出规范

- 提示词输出：中英对照（英文核心词可复制），附 1 条完整示例 + 1 条负面词。
- UI 输出：优先产出可运行的 HTML/CSS demo 或 tokens 文件；说明色值来源（窑口/釉色），让用户理解每个决策的依据。
- 封面输出：优先用封面生成器产出 PNG；批量时用 hash 直连；说明布局/主题/尺寸选择依据。
- 所有输出保持宋瓷审美的克制：信息密度低、装饰少、留白足。

## 参考资产

| 文件 | 内容 |
|---|---|
| `assets/design-language-ai.md` | 天青设计语言 **AI 速查卡**（AI 使用前必读：数值规范、占比、对比度坑、禁止清单） |
| `assets/prompt-guide.md` | 生图/生视频提示词完整速查（窑口×器型×特征×场景组合表） |
| `assets/design-language.md` | 天青 UI 设计语言完整规范速查 |
| `assets/xhs-cover-guide.md` | 小红书封面设计手册（平台规范、类型学、宋瓷规范、文案公式、批量流程、避坑） |
| `assets/tokens.css` | 可直接引入的 CSS 设计令牌（含暗色模式与组件类） |
| `assets/tokens.json` | 标准设计令牌 JSON（Style Dictionary / Figma Tokens 兼容） |
| `assets/palette.png` | 宋瓷釉色板参考图（生图配色参考） |
| `demo/index.html` | 天青设计语言可运行参考实现（品牌官网，明暗双模式、组件与图表） |
| `templates/宋瓷风小红书封面生成器.html`（skill 目录内） | **封面主工具**：9 布局 × 20 场景 × 6 釉色 × 4 尺寸，可编辑+导入图片+导出 PNG（1080/1620） |
| `templates/宋瓷风小红书通用模板.html` | 通用图文卡单版式模板（旧版，含 5 场景预设） |
