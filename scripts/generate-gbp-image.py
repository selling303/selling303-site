#!/usr/bin/env python3
"""
generate-gbp-image.py — Numeric Hero Card generator for selling303.com GBP posts.

Reusable image generator for Google Business Profile post images. Produces a
1200×1200 PNG branded for selling303.com — single dominant hero number,
question-led headline, brand wordmark, and Jacob Stark contact line.

Usage:
    python3 generate-gbp-image.py \\
        --output /path/to/output.png \\
        --hero-number "26" \\
        --hero-label "DAYS UNTIL JUNE 1" \\
        --headline "Should you protest your 2026 Notice of Valuation?"

Optional:
    --hero-color "#c8965a"     # default gold accent
    --footer-line "JACOB STARK · 8z REAL ESTATE · 303-997-0634"

Brand palette (selling303.com):
    Navy #002a3a / Dark navy #003c52 / Gold #c8965a / Green #4a7c59 / Light #f4f7f9
"""

import argparse
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

# Brand palette
NAVY = (0, 42, 58)
NAVY_DARK = (0, 60, 82)
GOLD = (200, 150, 90)
GOLD_LIGHT = (240, 200, 154)
GREEN = (74, 124, 89)
WHITE = (255, 255, 255)
LIGHT = (244, 247, 249)

# Font paths (Ubuntu sandbox defaults)
FONT_HEAVY = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def vertical_gradient(size, top_color, bottom_color):
    """Build a vertical-gradient RGB image."""
    w, h = size
    img = Image.new("RGB", size)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * t)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * t)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def wrap_text_to_width(draw, text, font, max_width):
    """Wrap text to fit max_width pixels using the given font."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for w in words[1:]:
        test = cur + " " + w
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def draw_centered_text(draw, text, font, y, color, canvas_w):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (canvas_w - w) // 2 - bbox[0]
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]  # height returned


def generate_hero_card(
    hero_number,
    hero_label,
    headline,
    output_path,
    subline="",
    hero_color=GOLD,
    footer_line="JACOB STARK · 8z REAL ESTATE · 303-997-0634",
    canvas_width=1200,
    canvas_height=900,
):
    """Render a 4:3 hero card. 1200x900 fits GBP feed-card thumbnails fully."""
    W = canvas_width
    H = canvas_height

    # 1. Background — vertical gradient navy → slightly lighter navy
    img = vertical_gradient((W, H), NAVY, NAVY_DARK)
    draw = ImageDraw.Draw(img)

    # 2. Top wordmark — small "selling303.com" top-left (no decorative dot)
    f_brand = ImageFont.truetype(FONT_BOLD, 24)
    draw.text((40, 28), "selling303.com", font=f_brand, fill=WHITE)

    # 3. Hero number — smaller to make room for bigger headline + vertical centering
    font_size = 280
    while font_size > 140:
        f_hero = ImageFont.truetype(FONT_HEAVY, font_size)
        bbox = draw.textbbox((0, 0), hero_number, font=f_hero)
        if bbox[2] - bbox[0] <= int(W * 0.78):
            break
        font_size -= 20

    # Pre-measure all elements so we can vertically center the stack
    f_label = ImageFont.truetype(FONT_BOLD, 26)
    f_head = ImageFont.truetype(FONT_BOLD, 84)  # match Option 2
    head_max_w = int(W * 0.78)  # narrower margins for tighter centered framing
    lines = wrap_text_to_width(draw, headline, f_head, head_max_w)
    line_height = 100

    bbox_h = draw.textbbox((0, 0), hero_number, font=f_hero)
    hero_h = bbox_h[3] - bbox_h[1]

    spaced = " ".join(hero_label.split()).upper()
    label_h = draw.textbbox((0, 0), spaced, font=f_label)[3]

    sub_h = 0
    sub_lines = []
    if subline:
        f_sub = ImageFont.truetype(FONT_BOLD, 26)
        sub_max_w = int(W * 0.78)
        sub_lines = wrap_text_to_width(draw, subline, f_sub, sub_max_w)
        sub_h = len(sub_lines) * 34

    head_total_h = len(lines) * line_height
    gap_hero_label = 14
    gap_label_rule = 50
    gap_rule_head = 36
    gap_head_sub = 22

    stack_h = (hero_h + gap_hero_label + label_h + gap_label_rule + 4
               + gap_rule_head + head_total_h)
    if subline:
        stack_h += gap_head_sub + sub_h

    # Center vertically
    top_y = (H - stack_h) // 2

    # Render hero
    hero_y = top_y
    hero_x = (W - (bbox_h[2] - bbox_h[0])) // 2 - bbox_h[0]
    draw.text((hero_x, hero_y - bbox_h[1]), hero_number, font=f_hero, fill=hero_color)

    # Label
    label_y = hero_y + hero_h + gap_hero_label
    total_w = 0
    for ch in spaced:
        bb = draw.textbbox((0, 0), ch, font=f_label)
        total_w += (bb[2] - bb[0]) + 4
    total_w -= 4
    cx = (W - total_w) // 2
    for ch in spaced:
        bb = draw.textbbox((0, 0), ch, font=f_label)
        draw.text((cx, label_y), ch, font=f_label, fill=hero_color)
        cx += (bb[2] - bb[0]) + 4

    # Gold rule
    rule_y = label_y + gap_label_rule
    rule_w = 160
    draw.rectangle([((W - rule_w) // 2, rule_y),
                    ((W + rule_w) // 2, rule_y + 4)], fill=hero_color)

    # Headline
    head_y = rule_y + gap_rule_head
    for line in lines:
        draw_centered_text(draw, line, f_head, head_y, WHITE, W)
        head_y += line_height

    # Subline
    if subline:
        sub_y = head_y + gap_head_sub
        for line in sub_lines:
            draw_centered_text(draw, line, f_sub, sub_y, GOLD_LIGHT, W)
            sub_y += 34

    # 8. (No footer band — wordmark up top carries identity. Cleaner image.)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    p = argparse.ArgumentParser(description="Generate a selling303 GBP hero card.")
    p.add_argument("--output", required=True)
    p.add_argument("--hero-number", required=True)
    p.add_argument("--hero-label", required=True)
    p.add_argument("--headline", required=True)
    p.add_argument("--subline", default="")
    p.add_argument("--hero-color", default="#c8965a")
    p.add_argument("--footer-line",
                   default="JACOB STARK · 8z REAL ESTATE · 303-997-0634")
    p.add_argument("--canvas-width", type=int, default=1200)
    p.add_argument("--canvas-height", type=int, default=900)
    args = p.parse_args()

    hc = args.hero_color.lstrip("#")
    hero_color_rgb = tuple(int(hc[i:i + 2], 16) for i in (0, 2, 4))

    out = generate_hero_card(
        hero_number=args.hero_number,
        hero_label=args.hero_label,
        headline=args.headline,
        output_path=args.output,
        subline=args.subline,
        hero_color=hero_color_rgb,
        footer_line=args.footer_line,
        canvas_width=args.canvas_width,
        canvas_height=args.canvas_height,
    )
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
