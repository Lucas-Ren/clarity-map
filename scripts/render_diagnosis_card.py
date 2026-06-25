#!/usr/bin/env python3
"""Render a Clarity Map diagnosis card as deterministic SVG.

Input JSON schema:
{
  "title": "...",
  "diagnosis": "...",
  "assets": ["...", "..."],
  "candidates": ["...", "..."],
  "experiment": {"timebox": "14天", "core_action": "..."},
  "signals": {"pass": "...", "fail": "..."},
  "cta": "..."
}
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STYLE_PATH = ROOT / "assets" / "diagnosis_card_style.json"


def display_width(text: str) -> int:
    width = 0
    for ch in text:
        width += 2 if ord(ch) > 127 else 1
    return width


def clip(text: str, max_width: int) -> str:
    text = str(text).strip()
    if display_width(text) <= max_width:
        return text
    out = ""
    width = 0
    for ch in text:
        w = 2 if ord(ch) > 127 else 1
        if width + w > max_width - 2:
            break
        out += ch
        width += w
    return out.rstrip() + "..."


def wrap(text: str, max_width: int, max_lines: int) -> list[str]:
    text = str(text).strip()
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        if display_width(candidate) > max_width and current:
            lines.append(current)
            current = ch
            if len(lines) == max_lines:
                return [*lines[:-1], clip(lines[-1], max_width)]
        else:
            current = candidate
    if current and len(lines) < max_lines:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
    if lines and display_width(lines[-1]) > max_width:
        lines[-1] = clip(lines[-1], max_width)
    return lines


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def load_json(path_or_dash: str) -> dict[str, Any]:
    if path_or_dash == "-":
        import sys

        return json.load(sys.stdin)
    with open(path_or_dash, "r", encoding="utf-8") as f:
        return json.load(f)


def text_lines(
    lines: list[str],
    x: int,
    y: int,
    size: int,
    fill: str,
    family: str,
    weight: int = 400,
    line_gap: int = 1,
) -> str:
    parts = []
    line_height = int(size * 1.25) + line_gap
    for i, line in enumerate(lines):
        parts.append(
            f'<text x="{x}" y="{y + i * line_height}" '
            f'font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}">{esc(line)}</text>'
        )
    return "\n".join(parts)


def section(
    label: str,
    body_lines: list[str],
    y: int,
    style: dict[str, Any],
    accent_bar: bool = False,
) -> tuple[str, int]:
    pal = style["palette"]
    typ = style["type"]
    family = typ["font_family"]
    x = 92
    label_y = y + 22
    body_y = y + 60
    body_size = typ["body"]
    body_height = max(1, len(body_lines)) * 32
    height = 72 + body_height
    if accent_bar:
        height += 4
    items = [
        f'<line x1="88" y1="{y - 12}" x2="812" y2="{y - 12}" stroke="{pal["border"]}" stroke-width="2"/>',
        f'<text x="{x}" y="{label_y}" font-family="{family}" font-size="{typ["section_label"]}" font-weight="700" fill="{pal["accent"]}">{esc(label)}</text>',
        text_lines(body_lines, x, body_y, body_size, pal["ink"], family),
    ]
    if accent_bar:
        items.insert(
            1,
            f'<rect x="{x}" y="{y - 2}" width="64" height="5" rx="2.5" fill="{pal["secondary"]}"/>',
        )
    return "\n".join(items), y + height


def normalize_data(data: dict[str, Any], style: dict[str, Any]) -> dict[str, Any]:
    rules = style["rules"]
    assets = [clip(x, rules["asset_max_chars"] * 2) for x in data.get("assets", [])[:3]]
    candidates = [
        clip(x, rules["candidate_max_chars"] * 2) for x in data.get("candidates", [])[:3]
    ]
    exp = data.get("experiment", {})
    signals = data.get("signals", {})
    return {
        "title": clip(data.get("title", "Clarity Map 诊断图"), rules["title_max_chars"] * 2),
        "diagnosis": clip(data.get("diagnosis", ""), rules["diagnosis_max_chars"] * 2),
        "assets": assets,
        "candidates": candidates,
        "experiment": {
            "timebox": clip(exp.get("timebox", ""), 12),
            "core_action": clip(exp.get("core_action", ""), rules["experiment_max_chars"] * 2),
        },
        "signals": {
            "pass": clip(signals.get("pass", ""), rules["signal_max_chars"] * 2),
            "fail": clip(signals.get("fail", ""), rules["signal_max_chars"] * 2),
        },
        "cta": clip(data.get("cta", ""), rules["cta_max_chars"] * 2),
    }


def render_svg(data: dict[str, Any], style: dict[str, Any]) -> str:
    data = normalize_data(data, style)
    size = style["size"]
    pal = style["palette"]
    typ = style["type"]
    family = typ["font_family"]
    w = size["width"]
    h = size["height"]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="{pal["background"]}"/>',
        f'<rect x="42" y="38" width="{w - 84}" height="{h - 76}" rx="28" fill="{pal["surface"]}" stroke="{pal["border"]}" stroke-width="2"/>',
        f'<rect x="88" y="86" width="56" height="56" rx="14" fill="{pal["accent"]}"/>',
        f'<text x="116" y="122" text-anchor="middle" font-family="{family}" font-size="22" font-weight="800" fill="white">{esc(style["brand"]["mark"])}</text>',
        f'<text x="160" y="122" font-family="{family}" font-size="22" font-weight="700" fill="{pal["accent"]}">{esc(style["brand"]["text"])}</text>',
        f'<text x="88" y="205" font-family="{family}" font-size="{typ["title"]}" font-weight="800" fill="{pal["ink"]}">{esc(data["title"])}</text>',
    ]
    y = 285
    block, y = section("一句话诊断", wrap(data["diagnosis"], 32, 2), y, style, True)
    parts.append(block)

    asset_lines = [" / ".join(data["assets"]) if data["assets"] else "暂无足够证据"]
    block, y = section("已验证资产", wrap(asset_lines[0], 34, 2), y, style)
    parts.append(block)

    candidate_lines = [" / ".join(data["candidates"]) if data["candidates"] else "待验证方向"]
    block, y = section("候选方向", wrap(candidate_lines[0], 34, 2), y, style)
    parts.append(block)

    exp_line = f'{data["experiment"]["timebox"]}：{data["experiment"]["core_action"]}'.strip("：")
    block, y = section("最小实验", wrap(exp_line, 34, 2), y, style)
    parts.append(block)

    signal_lines = [
        f'通过：{data["signals"]["pass"]}',
        f'失败：{data["signals"]["fail"]}',
    ]
    block, y = section("验证信号", signal_lines, y, style)
    parts.append(block)

    cta_lines = wrap(data["cta"], 28, 1)
    block, y = section("下一步", cta_lines, y, style)
    parts.append(block)

    parts.extend(
        [
            f'<text x="{w / 2}" y="{h - 82}" text-anchor="middle" font-family="{family}" font-size="{typ["small"]}" fill="{pal["muted"]}">{esc(style["brand"].get("completion_mark", ""))}</text>',
            f'<text x="{w / 2}" y="{h - 52}" text-anchor="middle" font-family="{family}" font-size="{typ["footer"]}" fill="{pal["muted"]}">{esc(style["brand"]["footer"])}</text>',
            "</svg>",
        ]
    )
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="JSON data file, or '-' for stdin")
    parser.add_argument("--out", required=True, help="Output SVG path")
    parser.add_argument("--style", default=str(STYLE_PATH), help="Style JSON path")
    args = parser.parse_args()

    data = load_json(args.data)
    style = load_json(args.style)
    svg = render_svg(data, style)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
