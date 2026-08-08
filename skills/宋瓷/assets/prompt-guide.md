# 宋瓷生图/生视频提示词 · 完整速查（Skill Asset）

## 公式

```
[窑口釉色] + [器型] + [釉面特征] + [展示场景] + [光线] + [摄影质感] + [画质词]
```

## 窑口 × 釉色 × 特征 × 器型 组合表

| 窑口 | 釉色关键词 | 釉面特征关键词 | 器型关键词 |
|---|---|---|---|
| 汝窑 | `ru ware, sky-blue glaze, pale blue` | `jade-like, subtle hairline crackle, sesame-seed spur marks` | `meiping, vase with raised bow-string lines, tripod brush washer` |
| 官窑 | `guan ware, thick powder-blue glaze, grey-blue` | `large ice-crackle pattern, purple mouth and iron-brown foot` | `vase with tubular handles, brush washer` |
| 哥窑 | `ge ware, warm grey or rice-yellow glaze` | `golden thread and iron-wire crackle lines, fish-roe crazing` | `jar, brush washer, small bottle` |
| 钧窑 | `jun ware, sky-blue, rose-purple, crabapple red` | `kiln transmutation, crimson splash, opalescent` | `flower pot, zun, brush washer` |
| 定窑 | `ding ware, ivory-white porcelain` | `incised lotus decoration, fine carved lines, unglazed rim` | `meiping, bowl, child-shaped pillow` |
| 龙泉 | `longquan celadon, powder-blue, plum-green` | `thick creamy jade-like surface, burnt-orange foot` | `meiping, phoenix-handled vase, li-style censer` |
| 建窑 | `jian ware, black glaze` | `hare's fur streaks, oil spot, yohen, metallic blue sheen` | `conical tea bowl, tea bowl` |
| 磁州 | `cizhou ware, white slip` | `black painted decoration, bold brushwork` | `jar, pillow, vase` |
| 耀州 | `yaozhou ware, olive-green` | `carved celadon, sharp incised relief` | `bowl, vase` |

## 三套场景语法

| 用途 | 场景词 |
|---|---|
| 博物馆级（还原） | `dim museum display, soft top spotlight, dark backdrop, product photography, photorealistic, 8k` |
| 文人氛围（创作） | `literati study, tea ceremony, wooden table, bamboo mat, warm side light, wabi-sabi, film still, cinematic` |
| 细节微距（研究） | `macro photography, extreme close-up on glaze surface, raking light, fine art photography` |

## 光线法则

- 侧光/侧逆光（`raking light` / `side light`）最能表现釉面与开片
- 柔光（`soft diffused light`）表现"温润如玉"
- 避免正面平光（画面发"平"，可用负面词排除）

## 通用负面词

```
negative: vivid colors, painted floral decoration, glossy plastic look,
busy background, cluttered scene, watermark, text, modern style
```

## 完整示例（复制即用）

**汝窑 · 天青弦纹瓶**
```
ru ware porcelain, sky-blue glaze, vase with raised bow-string lines,
jade-like muted tone, subtle cicada-wing crackle, dim museum display,
soft top spotlight, dark backdrop, product photography, photorealistic, 8k
```

**哥窑 · 金丝铁线开片洗**
```
ge ware brush washer, warm grey crackled glaze,
golden thread and iron-wire crackle lines, fish-roe crazing,
raking side light revealing crack texture, minimal composition,
still life photography, 8k
```

**建窑 · 曜变盏**
```
jian ware tea bowl, yohen kiln-change, iridescent blue and purple
galaxy-like spots on black glaze, rainbow oil-spot reflections,
dark museum spotlight, mystical atmosphere, macro photography
```

**龙泉 · 粉青梅瓶（文人向）**
```
longquan celadon meiping vase, powder-blue glaze,
thick creamy jade-like surface, plum-green tint,
literati study scene, warm side light, wabi-sabi atmosphere,
cinematic still, 8k
```

## 生视频运镜

| 表达 | 写法 |
|---|---|
| 旋转鉴赏 | `camera orbits 360° around the vase, slow smooth rotation` |
| 微距推镜 | `camera slowly dollies in on the glaze surface, macro detail` |
| 茶叙 | `hot tea being poured into the jian bowl, steam rising, camera tilts down` |
| 光影流动 | `soft light moving across the celadon surface, subtle reflections` |

## 防翻车清单

1. 天青易艳蓝 → 加 `muted, pale, jade-like`
2. 易变明清彩瓷 → 加 `monochrome glaze, no painted decoration`
3. 开片易密成网格 → `subtle, hairline, sparse`
4. 兔毫易花 → 单一特征 `delicate, fine`
5. 釉面易塑料感 → 必加 `jade-like, matte, glossy` 之一 + `ceramic texture`
6. 场景喧宾夺主 → `large object in frame`
