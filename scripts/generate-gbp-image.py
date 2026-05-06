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
    hero_color=GOLD,
    footer_line="JACOB STARK · 8z REAL ESTATE · 303-997-0634",
    canvas_size=1200,
):
    W = H = canvas_size

    # 1. Background — vertical gradient navy → slightly lighter navy
    img = vertical_gradient((W, H), NAVY, NAVY_DARK)
    draw = ImageDraw.Draw(img)

    # 2. Top-right corner mark — small gold "303" accent (subtle brand cue,
    #    won't compete with the corner wordmark).
    f_corner = ImageFont.truetype(FONT_HEAVY, 22)
    draw.text((W - 95, 42), "303", font=f_corner, fill=hero_color)

    # 3. Hero number — auto-fit font size up to ~560px so very long numbers still fit
    font_size = 560
    while font_size > 200:
        f_hero = ImageFont.truetype(FONT_HEAVY, font_size)
        bbox = draw.textbbox((0, 0), hero_number, font=f_hero)
        if bbox[2] - bbox[0] <= int(W * 0.85):
            break
        font_size -= 20
    hero_y = 230
    bbox = draw.textbbox((0, 0), hero_number, font=f_hero)
    hero_w = bbox[2] - bbox[0]
    hero_h = bbox[3] - bbox[1]
    hero_x = (W - hero_w) // 2 - bbox[0]
    draw.text((hero_x, hero_y - bbox[1]), hero_number, font=f_hero, fill=hero_color)

    # 4. Hero label — small uppercase letter-spaced under the hero number
    f_label = ImageFont.truetype(FONT_BOLD, 38)
    label_y = hero_y + hero_h + 30
    spaced = "  ".join(list(hero_label))  # letter-space by inserting spaces between chars
    # Use light spacing instead of full-letter for readability
    spaced = " ".join(hero_label.split())  # collapse multi-space to single
    spaced = spaced.upper()
    # Manual letter-spacing via tracking
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

    # 5. Gold accent line below label
    rule_y = label_y + 70
    rule_w = 220
    draw.rectangle([((W - rule_w) // 2, rule_y),
                    ((W + rule_w) // 2, rule_y + 5)], fill=hero_color)

    # 6. Headline — wrapped, white, large bold
    f_head = ImageFont.truetype(FONT_BOLD, 62)
    head_max_w = int(W * 0.84)
    lines = wrap_text_to_width(draw, headline, f_head, head_max_w)
    head_y = rule_y + 60
    line_height = 78
    for line in lines:
        draw_centered_text(draw, line, f_head, head_y, WHITE, W)
        head_y += line_height

    # 7. Footer band — slightly darker rectangle at bottom
    footer_h = 100
    draw.rectangle([(0, H - footer_h), (W, H)], fill=NAVY_DARK)
    # subtle gold rule above footer
    draw.rectangle([(0, H - footer_h - 2), (W, H - footer_h)], fill=hero_color)

    f_foot = ImageFont.truetype(FONT_BOLD, 26)
    foot_y = H - footer_h + (footer_h - 26) // 2 - 4
    draw_centered_text(draw, footer_line.upper(), f_foot, foot_y, WHITE, W)

    # 8. Top wordmark — small "selling303.com" top-left corner
    f_brand = ImageFont.truetype(FONT_BOLD, 26)
    draw.text((50, 38), "selling303.com", font=f_brand, fill=WHITE)
    # gold dot accent
    draw.ellipse([(50 + 200, 50), (50 + 212, 62)], fill=hero_color)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    p = argparse.ArgumentParser(description="Generate a selling303 GBP hero card.")
    p.add_argument("--output", required=True)
    p.add_argument("--hero-number", required=True)
    p.add_argument("--hero-label", required=True)
    p.add_argument("--headline", required=True)
    p.add_argument("--hero-color", default="#c8965a")
    p.add_argument("--footer-line",
                   default="JACOB STARK · 8z REAL ESTATE · 303-997-0634")
    p.add_argument("--canvas-size", type=int, default=1200)
    args = p.parse_args()

    hc = args.hero_color.lstrip("#")
    hero_color_rgb = tuple(int(hc[i:i + 2], 16) for i in (0, 2, 4))

    out = generate_hero_card(
        hero_number=args.hero_number,
        hero_label=args.hero_label,
        headline=args.headline,
        output_path=args.output,
        hero_color=hero_color_rgb,
        footer_line=args.footer_line,
        canvas_size=args.canvas_size,
    )
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
