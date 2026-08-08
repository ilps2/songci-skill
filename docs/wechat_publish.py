#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号 · 官方 API 自动发布脚本
====================================
把 Markdown 文章排版成公众号图文，创建草稿（默认）或直接发布。

【前提】
- 公众号已认证（服务号或认证订阅号），且拥有"草稿箱 / 发布能力"接口权限
- 运行本脚本的机器出口 IP 已加入公众号后台"IP 白名单"

【用法】
  WECHAT_APPID=你的AppID WECHAT_SECRET=你的AppSecret python3 wechat_publish.py \
      --md "从雨过天青到一张会变色的封面·公众号文章.md" \
      --cover "cover_示例.png" \
      --title "从雨过天青到一张会变色的封面" \
      --author "你的名字"

  只创建草稿（默认，推荐）：不加任何参数
  创建草稿后直接发布：加 --publish
  正文追加配图：--images "cover_美食.png,cover_黑釉.png"

【注意】
- AppSecret 只在生成时显示一次，请妥善保管，勿提交到代码仓库
- 沙箱/动态出口 IP 会变化，若报 40164 请在公众号后台更新 IP 白名单
"""
import argparse
import json
import os
import re
import sys
import time
import requests

API = "https://api.weixin.qq.com/cgi-bin"


def get_token(appid: str, secret: str, cache_file="/tmp/wx_token.json") -> str:
    """获取 access_token（带本地缓存，有效期 7200 秒）"""
    now = time.time()
    try:
        with open(cache_file, encoding="utf-8") as f:
            c = json.load(f)
        if c.get("expire_at", 0) > now + 300:
            return c["access_token"]
    except Exception:
        pass
    r = requests.get(f"{API}/token", params={
        "grant_type": "client_credential", "appid": appid, "secret": secret
    }, timeout=15).json()
    if "access_token" not in r:
        die(r, "获取 access_token 失败")
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump({"access_token": r["access_token"], "expire_at": now + r["expires_in"]}, f)
    return r["access_token"]


def die(resp: dict, ctx: str):
    """打印错误码并给出常见提示"""
    errcode = resp.get("errcode")
    tips = {
        40001: "access_token 无效或过期，删除缓存文件 /tmp/wx_token.json 后重试",
        40164: "请求来源 IP 不在白名单：请把本机出口 IP 加入公众号后台 → 设置与开发 → 基本配置 → IP 白名单",
        40013: "AppID 无效，请检查",
        40125: "AppSecret 无效，请重新生成",
        48001: "接口无权限：需要公众号已认证且开通「草稿箱/发布」能力",
        45009: "接口调用超限额，请稍后再试",
        40007: "media_id 无效，请重新上传封面",
        41001: "缺少 access_token",
        53010: "文章内容包含违规/敏感内容，请检查",
    }
    print(f"\n❌ {ctx}")
    print(f"   errcode={errcode}  errmsg={resp.get('errmsg')}")
    if errcode in tips:
        print(f"   提示：{tips[errcode]}")
    sys.exit(1)


def upload_thumb(token: str, cover_path: str) -> str:
    """上传封面图（永久素材，作为 thumb_media_id）"""
    if not os.path.exists(cover_path):
        print(f"⚠ 封面文件不存在：{cover_path}，跳过封面")
        return ""
    with open(cover_path, "rb") as f:
        r = requests.post(f"{API}/material/add_material", params={
            "access_token": token, "type": "image"
        }, files={"media": (os.path.basename(cover_path), f,
                            "image/png" if cover_path.endswith(".png") else "image/jpeg")},
            timeout=30).json()
    if "media_id" not in r:
        die(r, "上传封面失败")
    print(f"✓ 封面已上传 media_id={r['media_id']}")
    return r["media_id"]


def upload_content_image(token: str, img_path: str) -> str:
    """上传正文配图，返回可插入正文的 URL"""
    with open(img_path, "rb") as f:
        r = requests.post(f"{API}/media/uploadimg", params={
            "access_token": token
        }, files={"media": (os.path.basename(img_path), f,
                            "image/png" if img_path.endswith(".png") else "image/jpeg")},
            timeout=30).json()
    if "url" not in r:
        die(r, f"上传正文图片失败：{img_path}")
    return r["url"]


def md_to_content(md_path: str, token: str, extra_images=None) -> str:
    """Markdown → 公众号 HTML；本地图片自动上传替换；可选追加配图"""
    import markdown
    md = open(md_path, encoding="utf-8").read()
    html = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])

    # 1) 把正文里的本地图片 ![](path) 上传替换
    def _replace_img(m):
        p = m.group(1)
        if p.startswith("http"):
            return m.group(0)
        url = upload_content_image(token, p)
        return f'<img src="{url}" style="width:100%;border-radius:8px;"/>'
    html = re.sub(r"!\[[^\]]*\]\(([^)]+)\)", _replace_img, html)

    # 2) 追加配图（作为文末插图）
    if extra_images:
        imgs = []
        for p in extra_images:
            if os.path.exists(p):
                url = upload_content_image(token, p)
                imgs.append(f'<p style="text-align:center;"><img src="{url}" '
                            f'style="width:100%;border-radius:8px;"/></p>')
        if imgs:
            html += '<p></p>' + "".join(imgs)

    # 3) 公众号正文样式增强：段落行距、标题颜色（内联样式，兼容性优先）
    html = html.replace("<h1>", '<h1 style="font-size:20px;color:#1a1a2e;">')
    html = html.replace("<h2>", '<h2 style="font-size:17px;color:#1a1a2e;border-left:4px solid #7FA8B8;padding-left:8px;">')
    html = html.replace("<h3>", '<h3 style="font-size:15px;color:#333;">')
    html = html.replace("<blockquote>",
        '<blockquote style="background:#f0f6f8;border-left:4px solid #7FA8B8;padding:10px 14px;color:#2c4550;border-radius:0 6px 6px 0;">')
    html = html.replace("<table>",
        '<table style="border-collapse:collapse;width:100%;font-size:13px;margin:12px 0;">')
    html = html.replace("<th>", '<th style="background:#7FA8B8;color:#fff;padding:6px 8px;text-align:left;">')
    html = html.replace("<td>", '<td style="border:1px solid #d8dee9;padding:5px 8px;">')
    return html


def create_draft(token: str, title: str, content: str, thumb_media_id: str,
                 author: str = "", digest: str = "") -> str:
    r = requests.post(f"{API}/draft/add", params={"access_token": token},
                      data=json.dumps({
                          "articles": [{
                              "title": title,
                              "author": author,
                              "digest": digest,
                              "content": content,
                              "content_source_url": "",
                              "thumb_media_id": thumb_media_id,
                              "need_open_comment": 1,
                              "only_fans_can_comment": 0,
                          }]
                      }, ensure_ascii=False).encode("utf-8"),
                      headers={"Content-Type": "application/json"}, timeout=20).json()
    if "media_id" not in r:
        die(r, "创建草稿失败")
    print(f"✓ 草稿已创建 media_id={r['media_id']}")
    return r["media_id"]


def publish(token: str, draft_media_id: str):
    r = requests.post(f"{API}/freepublish/submit", params={"access_token": token},
                      data=json.dumps({"media_id": draft_media_id}).encode("utf-8"),
                      headers={"Content-Type": "application/json"}, timeout=20).json()
    if "publish_id" not in r:
        die(r, "提交发布失败")
    print(f"✓ 已提交发布 publish_id={r['publish_id']}")
    print("  可在公众号后台 → 内容与互动 → 发布记录 查看状态")


def main():
    ap = argparse.ArgumentParser(description="微信公众号 API 自动发布")
    ap.add_argument("--md", required=True, help="Markdown 文章路径")
    ap.add_argument("--cover", default="", help="封面图路径（建议 900x383 或 1:1）")
    ap.add_argument("--title", required=True, help="文章标题")
    ap.add_argument("--author", default="", help="作者")
    ap.add_argument("--digest", default="", help="摘要（留空则取正文前 54 字）")
    ap.add_argument("--images", default="", help="追加正文配图，逗号分隔")
    ap.add_argument("--publish", action="store_true", help="创建草稿后直接发布")
    args = ap.parse_args()

    appid = os.environ.get("WECHAT_APPID")
    secret = os.environ.get("WECHAT_SECRET")
    if not appid or not secret:
        print("❌ 缺少凭据：请设置环境变量 WECHAT_APPID 和 WECHAT_SECRET")
        sys.exit(1)

    token = get_token(appid, secret)
    print(f"✓ access_token 获取成功（{token[:12]}...）")

    thumb = upload_thumb(token, args.cover) if args.cover else ""
    extra = [p.strip() for p in args.images.split(",") if p.strip()] if args.images else None
    content = md_to_content(args.md, token, extra)
    digest = args.digest or re.sub(r"<[^>]+>", "", content)[:54]

    media_id = create_draft(token, args.title, content, thumb, args.author, digest)
    print("\n完成！请在公众号后台「草稿箱」确认后发布。")
    if args.publish:
        publish(token, media_id)


if __name__ == "__main__":
    main()
