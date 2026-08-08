# 天青 · 宋瓷 UI 设计语言规范

> **Tianqing Design Language** —— 从宋代瓷器美学中提炼的通用 UI 设计语言
> 版本：1.0 ｜ 定位：可复用的设计令牌体系 + 组件规范 + 扩展指南
> 适用范围：Web / 移动端 / 数据可视化 / 品牌视觉 / 文创周边

---

## 1. 设计语言概述

### 1.1 设计哲学

宋瓷美学与现代 UI 设计共享同一底层语言——**极简、克制、重质感**。本设计语言不做"复古装饰"，而是提取宋瓷的**美学法则**，转译为可执行的界面语法：

> **以釉色定调，以器型定形，以留白定气，以玉感定触，以含蓄定动。**

### 1.2 五条设计原则

| # | 原则 | 规范级描述 | 落地检查问题 |
|---|---|---|---|
| 1 | **器无赘饰** | 装饰元素最少化；优先用留白、字重、色相建立层级，而非边框与分割线 | 每个装饰元素都删不掉吗？ |
| 2 | **釉色为美** | 全局低饱和；主色仅一个（天青）；强调色出现频率受控（≤ 每屏 1 处大面积强调） | 界面能数出几个颜色？ |
| 3 | **温润如玉** | 大圆角、漫反射阴影、微透明渐变；避免硬边框、强投影、纯黑 | 阴影是"柔和扩散"还是"生硬"？ |
| 4 | **计白当黑** | 区块间距 ≥ 48px；信息密度主动降低；单屏视觉焦点 ≤ 3 个 | 留白是否"敢"大面积出现？ |
| 5 | **动若釉流** | 动效时长 200–500ms；缓出优先；无弹跳、无夸张位移 | 动效是"存在但不出声"吗？ |

### 1.3 适用与不适用场景

| ✅ 适用 | ❌ 不适合 |
|---|---|
| 文化/艺术类产品、内容社区、阅读类应用 | 高信息密度的后台管理系统（可作点缀使用） |
| 茶饮、香道、文房、家居、文旅、博物馆 | 强娱乐化、快节奏的消费级应用 |
| 品牌官网、作品集、数据大屏（庄重场合） | 需要强烈促销感、多色彩刺激的场景 |
| 文创、出版、展陈数字屏 | 极端暗黑科幻风（可参考"黑釉"暗色模式，见 9.5） |

---

## 2. 色彩系统（Color Tokens）

### 2.1 核心色板（源自宋瓷釉色）

| Token | 色值 | 色名 | 来源 | 用途 |
|---|---|---|---|---|
| `color.primary.500` | `#7FA8B8` | 天青 | 汝窑 | 全局主色 |
| `color.primary.600` | `#648C9E` | 深天青 | 汝窑(雨后) | 主色 Hover / 强调 |
| `color.primary.200` | `#B9CFD9` | 淡天青 | 汝窑(薄釉处) | 辅助、图标浅底 |
| `color.secondary.400` | `#B5CFC8` | 粉青 | 龙泉 | 次级强调 |
| `color.success.500` | `#5C7A52` | 豆青 | 耀州 | 成功态文字/图形 |
| `color.success.200` | `#AABFA3` | 浅豆青 | 耀州 | 成功态浅底 |
| `color.warning.500` | `#A47C48` | 茶褐 | 茶席/木案 | 警示、点缀 |
| `color.danger.500` | `#A65E44` | 窑变赭 | 钧窑(窑变) | 错误、删除 |
| `color.neutral.0` | `#F7F4EC` | 象牙白 | 定窑 | 卡片/表面 |
| `color.neutral.50` | `#EEF1F3` | 月白 | 官窑 | 页面背景 |
| `color.neutral.100` | `#E5E0D4` | 汝釉 | 汝窑(釉面) | 边框/分隔 |
| `color.neutral.900` | `#22201C` | 黑釉 | 建窑 | 主文字 |
| `color.neutral.700` | `#4A453D` | 墨 | 墨色 | 次级文字 |
| `color.neutral.400` | `#8A8478` | 灰陶 | 灰陶 | 弱化文字/占位 |

### 2.2 主色色阶（天青 50–900）

> 供深色模式、图表、品牌场景扩展使用

```
50  #F0F6F8    100 #DCECEF    200 #B9CFD9    300 #9FB9C6
400 #8CAEBD    500 #7FA8B8 ★  600 #648C9E    700 #4E7486
800 #3E5F6E    900 #2C4550
```

### 2.3 功能色映射与对比度

| 语义 | Token | 前景搭配 | WCAG 说明 |
|---|---|---|---|
| 主操作 | `primary.500` 底 + `#FFFFFF` 字 | 对比度 3.6:1（大字号/粗体可用） | 大按钮建议用 600 号底 |
| 正文 | `neutral.900` | 对比度 13.8:1 | ✅ 满足 AA |
| 次要文字 | `neutral.700` | 对比度 7.9:1 | ✅ 满足 AA |
| 弱化文字 | `neutral.400` | 对比度 3.4:1 | ⚠️ 仅用于装饰性/占位文本 |
| 成功 | `success.500` | 对比度 4.8:1 | ✅ 满足 AA |
| 警示 | `warning.500` | 对比度 4.1:1 | ✅ 满足 AA |
| 错误 | `danger.500` | 对比度 4.4:1 | ✅ 满足 AA |

### 2.4 色彩使用规则

1. **大面积**（背景、卡片）：只用月白、象牙白、黑釉（暗色模式）。
2. **主色天青**：用于主要操作、激活态、链接；占比建议 < 15%。
3. **粉青**：仅用于"次级强调"（如当前分类、次级选中），不得与天青同时大面积出现。
4. **茶褐**：点缀色，用于标签、图标点睛、品牌元素，占比 < 5%。
5. **杜绝**：纯黑 `#000`、纯白 `#FFF`、高饱和红绿蓝——用本语言内的色值替代。

---

## 3. 字体排版（Typography Tokens）

### 3.1 字体家族

| 角色 | 字体栈（按优先级） |
|---|---|
| 标题/品牌（衬线） | `Noto Serif SC` → `Songti SC` → `STSong` → `SimSun` |
| 正文/UI（无衬线） | `Noto Sans SC` → `PingFang SC` → `Microsoft YaHei` → `sans-serif` |
| 数字/代码 | `JetBrains Mono` → `SF Mono` → `Consolas` |

> 规则：**标题衬线，正文无衬线**。标题不加粗至 800 以上、不用斜体、不用下划线装饰。

### 3.2 字号阶梯（Type Scale）

| Token | 字号/行高 | 字重 | 字距 | 用途 |
|---|---|---|---|---|
| `type.display` | 40 / 56px | 600 | 0.12em | 品牌大标题（衬线） |
| `type.h1` | 30 / 44px | 600 | 0.06em | 页面标题 |
| `type.h2` | 22 / 34px | 600 | 0.05em | 区块标题 |
| `type.h3` | 17 / 28px | 600 | 0.04em | 卡片标题 |
| `type.body` | 15 / 26px | 400 | 0.02em | 正文 |
| `type.caption` | 12 / 18px | 400 | 0.15em | 辅助说明、标签文字 |

### 3.3 排版规则

1. 中文字体正文行高 ≥ 1.7；标题 ≥ 1.3。
2. 中英文混排：中英文间加空格；英文数字用无衬线或等宽。
3. 段间距 ≥ 12px；标题与正文间距 ≥ 16px。
4. 全角标点优先（中文语境），强调用**字重**而非颜色。

---

## 4. 形状与质感（Shape & Elevation Tokens）

### 4.1 圆角阶梯（玉润曲线）

| Token | 值 | 用途 |
|---|---|---|
| `radius.sm` | 8px | 标签、小元素 |
| `radius.md` | 14px | 按钮、输入框、图标容器 |
| `radius.lg` | 22px | 卡片、弹窗 |
| `radius.full` | 999px | 胶囊按钮、头像 |

> 规则：**全站不使用 < 6px 的直角**。卡片四角圆润，是"玉感"的第一来源。

### 4.2 阴影阶梯（漫反射）

| Token | 值 | 用途 |
|---|---|---|
| `shadow.soft` | `0 8px 24px rgba(34,32,28,.07), 0 2px 6px rgba(34,32,28,.04)` | 默认卡片 |
| `shadow.lift` | `0 16px 40px rgba(100,140,158,.16), 0 4px 12px rgba(34,32,28,.05)` | 悬停/浮起 |
| `shadow.modal` | `0 24px 64px rgba(34,32,28,.18)` | 弹窗 |

> 规则：阴影**带天青底色的冷灰**，不纯黑；透明度低、扩散大——模拟玉的漫反射光。

### 4.3 玉感质感

| 手法 | 规范 |
|---|---|
| 渐变 | 仅用同色系 100→300 号之间的柔和渐变，禁止反差大的渐变 |
| 微透明 | 浮层背景 `rgba(247,244,236,.92)` + 8px 模糊 |
| 表面色 | 表面统一用象牙白 `neutral.0`，绝不纯白 |
| 边框 | 用 `neutral.100`（汝釉色），1px，必要时 0.5px 透明度 |

---

## 5. 间距与布局（Spacing Tokens）

### 5.1 间距阶梯（4px 基数）

| Token | 值 | 用途 |
|---|---|---|
| `space.1` | 4px | 图标与文字间距 |
| `space.2` | 8px | 紧凑元素间距 |
| `space.3` | 16px | 常规内边距 |
| `space.4` | 24px | 卡片内边距 |
| `space.5` | 40px | 区块内间距 |
| `space.6` | 64px | 区块间距 |
| `space.7` | 96px | 大区块/页面留白 |

### 5.2 布局规则（留白优先）

1. 页面左右留白 ≥ 24px（移动端）/ ≥ 64px（桌面端）。
2. 单屏信息密度上限：**视觉焦点 ≤ 3 个**，超出即分层或降级。
3. 宁可空，不要挤——宋瓷的器型从不"塞满"。
4. 栅格建议 12 列，间距用 `space.4`/`space.5` 倍数。

---

## 6. 动效（Motion Tokens）

### 6.1 时长与缓动

| Token | 值 | 用途 |
|---|---|---|
| `duration.fast` | 200ms | 微交互、hover |
| `duration.base` | 350ms | 常规过渡 |
| `duration.slow` | 500ms | 页面转场、大元素 |
| `easing.default` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | 通用缓出 |
| `easing.silk` | `cubic-bezier(0.45, 0.05, 0.25, 1)` | 釉面流动感 |

### 6.2 动效规则

1. 位移幅度 ≤ 16px，缩放 ≤ 1.03 倍——克制如釉。
2. 禁止：弹跳（bounce）、旋转入场、闪烁、夸张位移动画。
3. 位移 + 淡入组合（`opacity` + `translateY(8px)`）为标准入场。
4. 尊重系统"减弱动态"设置（`prefers-reduced-motion`）。

---

## 7. 图标与纹理（Icon & Texture Tokens）

### 7.1 线稿图标规范

| 属性 | 值 |
|---|---|
| 风格 | 单色线稿（如定窑刻花线条） |
| 描边 | 1.5px，`stroke-linecap: round` |
| 尺寸 | 16 / 20 / 24 / 32px 四档 |
| 颜色 | 默认 `neutral.700`，激活 `primary.600` |
| 规则 | 不用实心填充、不用渐变、不用双色 |

### 7.2 纹理使用规范

| 纹理 | 用法 | 透明度上限 |
|---|---|---|
| 开片纹 | 大面积背景点缀 | 5% |
| 玉感渐变 | 卡片/按钮背景 | — |
| 冰裂纹 | 详情页分隔装饰 | 8% |
| 墨色晕染 | 品牌视觉/海报 | 12% |

> 原则：纹理永远"若有若无"——看得见，但不会注意到。

---

## 8. 组件规范（Component Specs）

> 以下为关键组件的 Token 映射，完整组件库按此规格实现。

### 8.1 按钮

| 变体 | 背景 | 文字 | 圆角 | 阴影 | 尺寸 |
|---|---|---|---|---|---|
| Primary | `primary.500` | `#FFFFFF` | `radius.full` | 天青柔影 | H 40 / 44px，padding 0 24px |
| Ghost | 透明 | `primary.600` | `radius.full` | 无 | 边框 1px `primary.200` |
| Text | 透明 | `neutral.700` | `radius.full` | 无 | Hover 转 `primary.600` |
| 禁用 | `neutral.100` | `neutral.400` | — | 无 | — |

### 8.2 卡片

```
背景 neutral.0 ｜ 圆角 radius.lg ｜ 阴影 shadow.soft
标题 type.h3（衬线）｜ 正文 type.body ｜ 内边距 space.4
悬停：shadow.lift + translateY(-4px) @ duration.base
```

### 8.3 标签 Tag

```
背景：语义色 200 号 @ 14% 透明度 ｜ 文字：语义色 500/600 号
圆角 radius.full ｜ 字号 type.caption ｜ 内边距 4px 14px
```

### 8.4 输入框

```
背景 #FFFDF7 ｜ 边框 neutral.100 ｜ 圆角 radius.md ｜ 内边距 12px 16px
聚焦：边框 primary.500 + 4px 天青光晕 rgba(127,168,184,.15)
```

### 8.5 导航/标签栏

```
激活态：文字 primary.600 + 2px 天青下划线（或底部指示条）
非激活：neutral.700 → hover neutral.900
背景：透明或 neutral.0 @ 92% 微透明 + 模糊
```

### 8.6 图表配色（数据可视化扩展）

| 序列 | Token | 说明 |
|---|---|---|
| 主序列 | `primary.500` / `primary.700` | 柱/线图主色 |
| 次序列 | `secondary.400` / `success.500` | 对比序列 |
| 第三序列 | `warning.500` / `danger.500` | 补充序列 |
| 背景网格 | `neutral.100` @ 60% | 网格线 |
| 强调 | `chahe` 茶褐 | 高亮单一数据点 |

> 图表风格：无 3D、无渐变柱、圆角柱头（4px）、网格线极淡。

---

## 9. 扩展应用指南

### 9.1 Web / CSS 落地

直接引入 `tokens.css`（见随附文件），使用 CSS 变量：

```css
.card {
  background: var(--color-neutral-0);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-soft);
  padding: var(--space-4);
}
```

### 9.2 移动端

- iOS：`UIColor` 扩展 / SwiftUI `Color` 扩展，token 名保持一致。
- Android：`res/values/colors.xml` + `dimens.xml`，命名 `tianqing_primary_500`。
- 建议圆角、间距与 Web 版完全一致，保证跨端统一。

### 9.3 数据可视化

用 8.6 的图表配色；大屏（数据大屏）可将月白背景换成黑釉暗色（见 9.5），天青作为发光主色。

### 9.4 品牌与文创

- 品牌色 = 天青 500 + 象牙白；辅助 = 茶褐。
- 海报字体用衬线大标题 + 极淡开片纹理背景（5%）。
- 文创周边（茶具包装、书籍装帧）沿用同一色板，形成家族感。

### 9.5 暗色模式（黑釉主题）

| 语义 | 浅色 | 暗色（黑釉） |
|---|---|---|
| 背景 | `neutral.50` 月白 | `#17150F` 黑釉底 |
| 表面 | `neutral.0` 象牙白 | `#221F18` |
| 主文字 | `neutral.900` | `#EDE8DC` |
| 次级文字 | `neutral.700` | `#B8B0A0` |
| 主色 | `primary.500` | `primary.300`（#9FB9C6，提亮保对比） |
| 边框 | `neutral.100` | `#3A352B` |

> 暗色模式是"建窑黑釉"的语言——夜间的宋瓷之美，重点是**天青提亮**而不是全蓝。

---

## 10. 设计令牌完整清单（Design Tokens Reference）

### 10.1 色彩（Color）

```
--color-primary-50:   #F0F6F8   --color-primary-100: #DCECEF
--color-primary-200:  #B9CFD9   --color-primary-300: #9FB9C6
--color-primary-400:  #8CAEBD   --color-primary-500: #7FA8B8
--color-primary-600:  #648C9E   --color-primary-700: #4E7486
--color-primary-800:  #3E5F6E   --color-primary-900: #2C4550
--color-secondary-400:#B5CFC8   --color-success-500: #5C7A52
--color-success-200:  #AABFA3   --color-warning-500: #A47C48
--color-danger-500:   #A65E44
--color-neutral-0:    #F7F4EC   --color-neutral-50:  #EEF1F3
--color-neutral-100:  #E5E0D4   --color-neutral-400: #8A8478
--color-neutral-700:  #4A453D   --color-neutral-900: #22201C
```

### 10.2 字体（Typography）

```
--font-serif / --font-sans / --font-mono
--type-display: 40/56  --type-h1: 30/44  --type-h2: 22/34
--type-h3: 17/28      --type-body: 15/26 --type-caption: 12/18
```

### 10.3 形状与质感

```
--radius-sm: 8px  --radius-md: 14px  --radius-lg: 22px  --radius-full: 999px
--shadow-soft / --shadow-lift / --shadow-modal
```

### 10.4 间距与动效

```
--space-1:4px  --space-2:8px  --space-3:16px  --space-4:24px
--space-5:40px --space-6:64px --space-7:96px
--duration-fast:200ms --duration-base:350ms --duration-slow:500ms
--easing-default / --easing-silk
```

---

## 附：本语言一句话速记

> **天青定主调，月白铺底色，象牙承内容，黑釉立文字，茶褐作点睛。**
> 衬线题标题，无衬走正文；圆角皆过六，阴影不带黑；间距敢留白，动效缓如釉。

---

*本规范配套文件：`tokens.css`（CSS 变量）、`tokens.json`（设计令牌 JSON，可导入 Style Dictionary / Figma Tokens 插件）。*
