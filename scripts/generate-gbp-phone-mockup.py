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

    # Top wordmark (small, no decorative dot — clean)
    f_brand = ImageFont.truetype(FONT_BOLD, 22)
    draw.text((40, 28), "selling303.com", font=f_brand, fill=WHITE)

    # === PHONE FRAME — left, narrow & tall (real iPhone-ish aspect ~9:20) ===
    phone_w, phone_h = 340, 720
    phone_x = 80
    phone_y = 100
    phone_radius = 42

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

    # Body — county chips
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

    # Two input fields side-by-side
    in_y = chip_y + 46
    in_h = 44
    in_w = (ww - 28 - 8) // 2
    for i, (lbl, val) in enumerate([
        ("YOUR NOV VALUE", "$ 0"),
        ("MARKET VALUE", "$ 0"),
    ]):
        ix = wx + 14 + i * (in_w + 8)
        draw.text((ix, in_y), lbl, font=f_lbl, fill=GREEN)
        rounded_rect(draw, [(ix, in_y + 18), (ix + in_w, in_y + 18 + in_h)],
                     5, fill=WHITE, outline=GRAY_BORDER, width=1)
        f_v = ImageFont.truetype(FONT_BOLD, 18)
        draw.text((ix + 10, in_y + 30), val, font=f_v, fill=NAVY)

    # Gap readout
    gap_y = in_y + 18 + in_h + 14
    gap_h = 46
    rounded_rect(draw, [(wx + 14, gap_y), (wx + ww - 14, gap_y + gap_h)],
                 5, fill=WHITE, outline=GRAY_BORDER, width=1)
    f_gap_lbl = ImageFont.truetype(FONT_BOLD, 9)
    draw.text((wx + 24, gap_y + 8), "GAP", font=f_gap_lbl, fill=TEXT_GRAY)
    f_gap_msg = ImageFont.truetype(FONT_REG, 10)
    draw.text((wx + 24, gap_y + 22),
              "Enter values to see gap.",
              font=f_gap_msg, fill=TEXT_GRAY)
    f_gap_pct = ImageFont.truetype(FONT_HEAVY, 22)
    draw.text((wx + ww - 70, gap_y + 12), "— %",
              font=f_gap_pct, fill=(153, 173, 184))

    # Section divider + path cards preview
    cards_section_y = gap_y + gap_h + 16
    f_sec = ImageFont.truetype(FONT_BOLD, 10)
    draw.text((wx + 14, cards_section_y), "YOUR POTENTIAL PATH",
              font=f_sec, fill=NAVY)

    # 3 path cards stacked vertically
    cards_top = cards_section_y + 18
    card_h = 50
    card_gap = 6
    paths = [
        ("PATH 1", "Protest", "By June 1", GREEN, GREEN_LIGHT),
        ("PATH 2", "Skip", "No filing", (153, 173, 184), (244, 247, 249)),
        ("PATH 3", "Abate", "By July 20", NAVY, (244, 247, 249)),
    ]
    f_pc_label = ImageFont.truetype(FONT_BOLD, 9)
    f_pc_name = ImageFont.truetype(FONT_BOLD, 15)
    f_pc_chip = ImageFont.truetype(FONT_BOLD, 10)
    for i, (label, name, chip, accent, chip_bg) in enumerate(paths):
        cy = cards_top + i * (card_h + card_gap)
        rounded_rect(draw, [(wx + 14, cy), (wx + ww - 14, cy + card_h)], 6,
                     fill=WHITE, outline=GRAY_BORDER, width=1)
        # Top accent stripe
        draw.rectangle([(wx + 14, cy), (wx + ww - 14, cy + 3)], fill=accent)
        # Path label + name (left)
        draw.text((wx + 22, cy + 9), label, font=f_pc_label, fill=accent)
        draw.text((wx + 22, cy + 22), name, font=f_pc_name, fill=NAVY)
        # Chip (right)
        chip_bb = draw.textbbox((0, 0), chip, font=f_pc_chip)
        cw = chip_bb[2] - chip_bb[0] + 14
        cx = wx + ww - cw - 22
        cy_chip = cy + (card_h - 20) // 2
        rounded_rect(draw, [(cx, cy_chip), (cx + cw, cy_chip + 20)], 10,
                     fill=chip_bg, outline=accent, width=1)
        draw.text((cx + 7, cy_chip + 5), chip, font=f_pc_chip, fill=NAVY)

    # === Right column — big headline + supporting copy ===
    rx = phone_x + phone_w + 60
    rx_max = W - 60
    rx_w = rx_max - rx

    # Eyebrow tag
    f_r_eye = ImageFont.truetype(FONT_BOLD, 18)
    draw.text((rx, 130), "INTERACTIVE TOOL", font=f_r_eye, fill=GOLD)
    draw.rectangle([(rx, 162), (rx + 50, 165)], fill=GOLD)

    # Big headline (3 lines max, ~72px so 3 lines fit comfortably)
    f_r_head = ImageFont.truetype(FONT_BOLD, 72)
    head_lines = []
    words = above_phone.split()
    cur = words[0]
    for w in words[1:]:
        test = cur + " " + w
        bb = draw.textbbox((0, 0), test, font=f_r_head)
        if bb[2] - bb[0] <= rx_w:
            cur = test
        else:
            head_lines.append(cur)
            cur = w
    head_lines.append(cur)
    head_y = 200
    for line in head_lines[:4]:
        draw.text((rx, head_y), line, font=f_r_head, fill=WHITE)
        head_y += 84

    # Gold accent rule under headline
    draw.rectangle([(rx, head_y + 16), (rx + 80, head_y + 20)], fill=GOLD)

    # Subline + URL
    f_r_sub = ImageFont.truetype(FONT_BOLD, 26)
    draw.text((rx, head_y + 38), "Free calculator · 30 seconds",
              font=f_r_sub, fill=GOLD_LIGHT)
    f_r_url = ImageFont.truetype(FONT_REG, 18)
    short_url = url.replace("https://", "").replace("http://", "")
    if len(short_url) > 56:
        short_url = short_url[:54] + "…"
    draw.text((rx, head_y + 84), short_url, font=f_r_url, fill=WHITE_DIM)

    # (No footer band — wordmark up top carries identity. Cleaner image.)

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
