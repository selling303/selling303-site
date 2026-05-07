#!/usr/bin/env python3
"""
generate-gbp-phone-mockup.py — Phone-mockup-style GBP image generator.

Renders a 1200x1200 PNG of a stylized iPhone-shaped frame containing a
brand-faithful rendering of the post's hero widget. Same visual language
as the live site but without depending on a browser screenshot — fast,
reliable, brand-cohesive.

Usage:
    python3 generate-gbp-phone-mockup.py \\
        --output /path/to/out.png \\
        --eyebrow "ARAPAHOE / DOUGLAS / JEFFERSON · 2026 NOV" \\
        --title "Should you protest? Run the numbers." \\
        --countdown-label "until June 1" \\
        --countdown-value "26d 9h" \\
        --above-phone "Try the new 2026 NOV calculator" \\
        --url "selling303.com/blog/2026-notice-of-valuation-protest-playbook-south-denver"
"""

import argparse
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

NAVY = (0, 42, 58)
NAVY_DARK = (0, 60, 82)
NAVY_DARKER = (0, 32, 45)
GOLD = (200, 150, 90)
GOLD_LIGHT = (240, 200, 154)
GREEN = (74, 124, 89)
GREEN_LIGHT = (240, 244, 240)
LIGHT_BG = (249, 251, 252)
WHITE = (255, 255, 255)
WHITE_DIM = (200, 215, 220)
GRAY_BORDER = (214, 224, 230)
TEXT_GRAY = (85, 85, 85)
PHONE_FRAME = (24, 30, 38)
PHONE_BEZEL = (8, 12, 16)

FONT_HEAVY = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def vertical_gradient(size, top_color, bottom_color):
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


def draw_centered(draw, text, font, y, color, canvas_w, x_offset=0):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (canvas_w - w) // 2 - bbox[0] + x_offset
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]


def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Wrapper for rounded_rectangle that handles older Pillow."""
    draw.rounded_rectangle(xy, radius=radius, fill=fill,
                           outline=outline, width=width)


def shadow_layer(size, x, y, w, h, radius, blur, color=(0, 0, 0, 180)):
    """Drop-shadow helper."""
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle([(x, y), (x + w, y + h)], radius=radius, fill=color)
    return layer.filter(ImageFilter.GaussianBlur(blur))


def render_phone_mockup(
    output_path,
    eyebrow,
    title,
    countdown_label,
    countdown_value,
    above_phone,
    url,
    canvas_width=1200,
    canvas_height=900,
):
    """4:3 side-by-side: phone left, big headline right. Optimized for GBP
    feed-card thumbnails — full image visible, headline readable at small size."""
    W = canvas_width
    H = canvas_height

    # Background — navy gradient
    img = vertical_gradient((W, H), NAVY, NAVY_DARK).convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Top wordmark (small)
    f_brand = ImageFont.truetype(FONT_BOLD, 22)
    draw.text((40, 28), "selling303.com", font=f_brand, fill=WHITE)
    draw.ellipse([(216, 38), (228, 50)], fill=GOLD)

    # === BIG HEADLINE — top-centered, dominant element for thumbnail ===
    f_head = ImageFont.truetype(FONT_BOLD, 78)
    head_max_w = int(W * 0.88)
    words = above_phone.split()
    head_lines = []
    cur = words[0]
    for w in words[1:]:
        test = cur + " " + w
        bb = draw.textbbox((0, 0), test, font=f_head)
        if bb[2] - bb[0] <= head_max_w:
            cur = test
        else:
            head_lines.append(cur)
            cur = w
    head_lines.append(cur)
    head_y = 90
    for line in head_lines[:3]:
        draw_centered(draw, line, f_head, head_y, WHITE, W)
        head_y += 92
    head_bottom_y = head_y

    # Gold rule under headline
    rule_w = 140
    rule_y = head_bottom_y + 12
    draw.rectangle([((W - rule_w) // 2, rule_y),
                    ((W + rule_w) // 2, rule_y + 4)], fill=GOLD)

    # Sub-CTA below the rule
    f_sub_cta = ImageFont.truetype(FONT_BOLD, 26)
    draw_centered(draw, "Free interactive calculator · 30 seconds",
                  f_sub_cta, rule_y + 22, GOLD_LIGHT, W)

    # === PHONE FRAME — smaller, centered below the headline ===
    phone_w, phone_h = 320, 380
    phone_x = (W - phone_w) // 2
    phone_y = rule_y + 70
    phone_radius = 36

    # Drop shadow under the phone
    shadow = shadow_layer((W, H), phone_x + 18, phone_y + 28,
                          phone_w, phone_h, phone_radius, 30,
                          color=(0, 0, 0, 160))
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)

    # Outer dark frame
    rounded_rect(draw, [(phone_x, phone_y),
                        (phone_x + phone_w, phone_y + phone_h)],
                 phone_radius, fill=PHONE_FRAME)
    # Inner bezel highlight
    rounded_rect(draw, [(phone_x + 4, phone_y + 4),
                        (phone_x + phone_w - 4, phone_y + phone_h - 4)],
                 phone_radius - 4, fill=PHONE_BEZEL)

    # Screen area
    screen_inset = 14
    sx = phone_x + screen_inset
    sy = phone_y + screen_inset
    sw = phone_w - screen_inset * 2
    sh = phone_h - screen_inset * 2
    screen_radius = phone_radius - 12
    rounded_rect(draw, [(sx, sy), (sx + sw, sy + sh)],
                 screen_radius, fill=LIGHT_BG)

    # Notch / dynamic-island
    notch_w = 130
    notch_h = 30
    notch_x = phone_x + (phone_w - notch_w) // 2
    notch_y = phone_y + 22
    rounded_rect(draw, [(notch_x, notch_y),
                        (notch_x + notch_w, notch_y + notch_h)],
                 14, fill=PHONE_BEZEL)

    # === SCREEN CONTENT — render a brand-faithful Gap Calculator hero ===

    # Browser-bar URL strip at top of screen
    bar_y = sy + 8
    bar_h = 36
    rounded_rect(draw, [(sx + 16, bar_y), (sx + sw - 16, bar_y + bar_h)],
                 8, fill=(232, 238, 242))
    f_url = ImageFont.truetype(FONT_REG, 14)
    short_url = url.replace("https://", "").replace("http://", "")
    if len(short_url) > 38:
        short_url = short_url[:36] + "…"
    draw.text((sx + 30, bar_y + 10), short_url, font=f_url, fill=TEXT_GRAY)
    # Lock icon (small dot)
    draw.ellipse([(sx + 20, bar_y + 14), (sx + 28, bar_y + 22)], fill=GREEN)

    # Widget container starts below browser bar — extends to fill screen
    wx = sx + 22
    wy = bar_y + bar_h + 22
    ww = sw - 44
    wh = sh - (bar_y + bar_h + 22 - sy) - 22
    # Widget shadow
    wshadow = shadow_layer((W, H), wx + 4, wy + 6, ww, wh, 14, 12,
                           color=(0, 42, 58, 60))
    img = Image.alpha_composite(img, wshadow)
    draw = ImageDraw.Draw(img)

    rounded_rect(draw, [(wx, wy), (wx + ww, wy + wh)], 14,
                 fill=WHITE, outline=GRAY_BORDER, width=1)

    # Widget header — navy gradient band
    header_h = 130
    header_layer = Image.new("RGBA", (ww, header_h), (0, 0, 0, 0))
    px = header_layer.load()
    for y in range(header_h):
        t = y / max(header_h - 1, 1)
        r = int(NAVY[0] + (NAVY_DARK[0] - NAVY[0]) * t)
        g = int(NAVY[1] + (NAVY_DARK[1] - NAVY[1]) * t)
        b = int(NAVY[2] + (NAVY_DARK[2] - NAVY[2]) * t)
        for x in range(ww):
            px[x, y] = (r, g, b, 255)

    # Mask the header to round the top corners
    mask = Image.new("L", (ww, header_h), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([(0, 0), (ww, header_h)],
                            radius=14, fill=255)
    # Force bottom of header to be square
    mdraw.rectangle([(0, header_h // 2), (ww, header_h)], fill=255)
    img.paste(header_layer, (wx, wy), mask)
    draw = ImageDraw.Draw(img)

    # Eyebrow
    f_eyebrow = ImageFont.truetype(FONT_BOLD, 11)
    eyebrow_upper = eyebrow.upper()
    draw.text((wx + 18, wy + 16), eyebrow_upper, font=f_eyebrow,
              fill=(220, 230, 235))

    # Title (no badge inside — countdown is in the headline above)
    f_title = ImageFont.truetype(FONT_BOLD, 20)
    words = title.split()
    lines = []
    cur = words[0]
    for w in words[1:]:
        test = cur + " " + w
        bb = draw.textbbox((0, 0), test, font=f_title)
        if bb[2] - bb[0] <= ww - 36:
            cur = test
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    ty = wy + 40
    for line in lines[:2]:
        draw.text((wx + 18, ty), line, font=f_title, fill=WHITE)
        ty += 26

    # Body — simplified preview (3 county chips + a tap-CTA, fits the small phone)
    body_y = wy + header_h + 16
    f_lbl = ImageFont.truetype(FONT_BOLD, 10)
    draw.text((wx + 14, body_y), "PICK YOUR COUNTY", font=f_lbl, fill=GREEN)
    chip_y = body_y + 18
    counties = ["Arapahoe", "Douglas", "Jefferson"]
    f_chip = ImageFont.truetype(FONT_BOLD, 11)
    chip_x = wx + 14
    for c in counties:
        bb = draw.textbbox((0, 0), c, font=f_chip)
        cw = bb[2] - bb[0] + 16
        rounded_rect(draw, [(chip_x, chip_y), (chip_x + cw, chip_y + 26)], 4,
                     fill=WHITE, outline=GRAY_BORDER, width=1)
        draw.text((chip_x + 8, chip_y + 7), c, font=f_chip, fill=NAVY)
        chip_x += cw + 6

    # Big tap CTA — centered, fills remaining screen vertically
    cta_y = chip_y + 50
    cta_h = 60
    cta_w = ww - 28
    cta_x = wx + 14
    rounded_rect(draw, [(cta_x, cta_y), (cta_x + cta_w, cta_y + cta_h)], 8,
                 fill=NAVY, outline=GOLD, width=2)
    f_cta = ImageFont.truetype(FONT_BOLD, 18)
    cta_text = "Run the numbers →"
    bb = draw.textbbox((0, 0), cta_text, font=f_cta)
    draw.text((cta_x + (cta_w - (bb[2] - bb[0])) // 2,
               cta_y + (cta_h - (bb[3] - bb[1])) // 2 - 2),
              cta_text, font=f_cta, fill=GOLD_LIGHT)

    # Skip the legacy body sections by short-circuiting (deceptively named to
    # preserve the path-cards code below being skipped — uses an early-return
    # pattern in the simplified phone preview)
    if True:
        # === Right side: anchor for footer alignment, then continue to footer ===
        cards_section_y = cta_y + cta_h + 9999  # off-canvas; legacy code below is dead

    # 3 path cards stacked vertically (more readable in narrow phone width)
    cards_top = cards_section_y + 22
    card_h = 70
    card_gap = 8
    paths = [
        ("PATH 1", "Protest", "File by June 1", GREEN, GREEN_LIGHT),
        ("PATH 2", "Skip", "No filing this cycle", (153, 173, 184), (244, 247, 249)),
        ("PATH 3", "Abate", "File by July 20", NAVY, (244, 247, 249)),
    ]
    f_pc_label = ImageFont.truetype(FONT_BOLD, 10)
    f_pc_name = ImageFont.truetype(FONT_BOLD, 18)
    f_pc_chip = ImageFont.truetype(FONT_BOLD, 11)
    for i, (label, name, chip, accent, chip_bg) in enumerate(paths):
        cy = cards_top + i * (card_h + card_gap)
        rounded_rect(draw, [(wx + 18, cy), (wx + ww - 18, cy + card_h)], 8,
                     fill=WHITE, outline=GRAY_BORDER, width=1)
        # Top accent stripe
        draw.rectangle([(wx + 18, cy), (wx + ww - 18, cy + 4)], fill=accent)
        # Path label + name (left)
        draw.text((wx + 30, cy + 14), label, font=f_pc_label, fill=accent)
        draw.text((wx + 30, cy + 28), name, font=f_pc_name, fill=NAVY)
        # Chip (right)
        chip_bb = draw.textbbox((0, 0), chip, font=f_pc_chip)
        cw = chip_bb[2] - chip_bb[0] + 18
        cx = wx + ww - cw - 30
        cy_chip = cy + (card_h - 24) // 2
        rounded_rect(draw, [(cx, cy_chip), (cx + cw, cy_chip + 24)], 12,
                     fill=chip_bg, outline=accent, width=1)
        draw.text((cx + 9, cy_chip + 6), chip, font=f_pc_chip, fill=NAVY)

    # === Footer band ===
    footer_h = 70
    draw.rectangle([(0, H - footer_h), (W, H)], fill=NAVY_DARK)
    draw.rectangle([(0, H - footer_h - 2), (W, H - footer_h)], fill=GOLD)
    f_foot = ImageFont.truetype(FONT_BOLD, 22)
    foot_y = H - footer_h + (footer_h - 22) // 2 - 3
    draw_centered(draw, "JACOB STARK · 8Z REAL ESTATE · 303-997-0634",
                  f_foot, foot_y, WHITE, W)

    out = img.convert("RGB")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    out.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", required=True)
    p.add_argument("--eyebrow", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--countdown-label", required=True)
    p.add_argument("--countdown-value", required=True)
    p.add_argument("--above-phone", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--canvas-width", type=int, default=1200)
    p.add_argument("--canvas-height", type=int, default=900)
    args = p.parse_args()
    out = render_phone_mockup(
        output_path=args.output,
        eyebrow=args.eyebrow,
        title=args.title,
        countdown_label=args.countdown_label,
        countdown_value=args.countdown_value,
        above_phone=args.above_phone,
        url=args.url,
        canvas_width=args.canvas_width,
        canvas_height=args.canvas_height,
    )
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
