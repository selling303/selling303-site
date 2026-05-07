#!/usr/bin/env python3
"""
generate-gbp-data-viz.py — Live Data Snapshot generator for selling303.com GBP posts.

For data-driven blog posts where the visual itself communicates the post's value.
Currently supports the "deadline-spine" template — horizontal timeline with
milestones, today's marker, and urgency anchor. Future templates can be added
(price-bar, market-trend, etc.) under the same script with --template flag.

Usage (deadline-spine):
    python3 generate-gbp-data-viz.py \\
        --output /path/to/output.png \\
        --template deadline-spine \\
        --headline "South Denver 2026 NOV protest closes in" \\
        --hero-number "26" \\
        --hero-unit "days" \\
        --milestones "MAY 1:NOV mailed:past:170,TODAY:May 6:today:350,JUNE 1:Protest deadline:urgent:600,JULY 20:Abatement:future:850,AUG 15:CBOE review:future:1030" \\
        --footer "selling303.com/blog/2026-notice-of-valuation-protest-playbook-south-denver"
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
GRAY_TRACK = (90, 110, 122)
GRAY_PAST = (153, 173, 184)
WHITE = (255, 255, 255)
WHITE_DIM = (200, 215, 220)

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


def draw_centered(draw, text, font, y, color, canvas_w):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (canvas_w - w) // 2 - bbox[0]
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]


def draw_glow_circle(img, center, radius, color, glow_radius=20):
    """Draw a circle with a soft outer glow for the today-marker."""
    cx, cy = center
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for i in range(glow_radius, 0, -2):
        alpha = int(140 * (1 - i / glow_radius) ** 2)
        gd.ellipse(
            [(cx - radius - i, cy - radius - i),
             (cx + radius + i, cy + radius + i)],
            fill=(color[0], color[1], color[2], alpha),
        )
    glow = glow.filter(ImageFilter.GaussianBlur(4))
    base = img.convert("RGBA")
    base = Image.alpha_composite(base, glow)
    d = ImageDraw.Draw(base)
    d.ellipse([(cx - radius, cy - radius), (cx + radius, cy + radius)], fill=color)
    d.ellipse([(cx - 6, cy - 6), (cx + 6, cy + 6)], fill=WHITE)
    return base.convert("RGB")


def parse_milestones(spec):
    """Parse 'LABEL:desc:state:x,...' into list of dicts."""
    out = []
    for chunk in spec.split(","):
        parts = chunk.split(":")
        if len(parts) != 4:
            continue
        out.append({
            "label": parts[0].strip(),
            "desc": parts[1].strip(),
            "state": parts[2].strip(),
            "x": int(parts[3].strip()),
        })
    return out


def render_deadline_spine(
    output_path,
    headline,
    hero_number,
    hero_unit,
    milestones,
    footer,
    question="",
    canvas_width=1200,
    canvas_height=900,
):
    """4:3 deadline spine — minimal layout: wordmark, timeline (visual interest),
    big question (click hook). No top header band, no URL footer."""
    W = canvas_width
    H = canvas_height
    img = vertical_gradient((W, H), NAVY, NAVY_DARK)
    draw = ImageDraw.Draw(img)

    # Top wordmark
    f_brand = ImageFont.truetype(FONT_BOLD, 24)
    draw.text((40, 28), "selling303.com", font=f_brand, fill=WHITE)

    # === Compute vertically centered stack ===
    # Pre-measure question wrapping so we can size everything together
    q_text = question if question else "Should you protest your 2026 property tax?"
    f_q = ImageFont.truetype(FONT_BOLD, 84)
    q_max_w = int(W * 0.86)
    q_words = q_text.split()
    q_lines = []
    cur = q_words[0]
    for w in q_words[1:]:
        test = cur + " " + w
        bb = draw.textbbox((0, 0), test, font=f_q)
        if bb[2] - bb[0] <= q_max_w:
            cur = test
        else:
            q_lines.append(cur)
            cur = w
    q_lines.append(cur)
    q_lines = q_lines[:3]
    line_h = 100

    # Stack components (top→bottom):
    #   timeline labels above (~24)  +  gap (12)  +  dot row (~24)  +
    #   gap (12)  +  timeline labels below (~24)  +  gap (75)  +
    #   question (N × 100)  +  gap (12)  +  rule (4)  +  gap (28)  +  sub (24)
    timeline_block_h = 24 + 12 + 24 + 12 + 24
    gap_timeline_question = 75
    q_block_h = len(q_lines) * line_h
    sub_block_h = 12 + 4 + 28 + 24
    stack_h = timeline_block_h + gap_timeline_question + q_block_h + sub_block_h

    stack_top = (H - stack_h) // 2
    # Timeline dot row sits ~60px below stack_top (after labels-above)
    timeline_y = stack_top + 60

    # Track baseline (gray)
    draw.line([(120, timeline_y), (1080, timeline_y)],
              fill=GRAY_TRACK, width=6)

    # Find today index for the past-portion fill
    today_idx = next((i for i, m in enumerate(milestones)
                      if m["state"] == "today"), None)
    if today_idx is not None:
        today_x = milestones[today_idx]["x"]
        # Past-portion fill in lighter gray
        draw.line([(120, timeline_y), (today_x, timeline_y)],
                  fill=GRAY_PAST, width=6)

    # Now draw each milestone — past first, then future, then today on top
    state_colors = {
        "past": GRAY_PAST,
        "future": GRAY_TRACK,
        "urgent": NAVY_DARKER,
        "today": GOLD,
    }
    f_m_label = ImageFont.truetype(FONT_BOLD, 26)
    f_m_desc = ImageFont.truetype(FONT_REG, 20)

    # Save today for last to render glow on top
    for m in milestones:
        if m["state"] == "today":
            continue
        cx = m["x"]
        if m["state"] == "urgent":
            # Urgent (June 1): navy block badge with "!"
            badge_w, badge_h = 50, 36
            draw.rectangle(
                [(cx - badge_w // 2, timeline_y - badge_h // 2),
                 (cx + badge_w // 2, timeline_y + badge_h // 2)],
                fill=NAVY_DARKER,
            )
            f_bang = ImageFont.truetype(FONT_HEAVY, 26)
            bb = draw.textbbox((0, 0), "!", font=f_bang)
            draw.text(
                (cx - (bb[2] - bb[0]) // 2 - bb[0],
                 timeline_y - (bb[3] - bb[1]) // 2 - bb[1]),
                "!", font=f_bang, fill=GOLD,
            )
        else:
            r = 14 if m["state"] == "future" else 12
            color = state_colors[m["state"]]
            draw.ellipse([(cx - r, timeline_y - r), (cx + r, timeline_y + r)],
                         fill=color)

        # Date label above (gold or white per state)
        label_color = GOLD if m["state"] == "urgent" else WHITE
        bb = draw.textbbox((0, 0), m["label"], font=f_m_label)
        draw.text(
            (cx - (bb[2] - bb[0]) // 2 - bb[0], timeline_y - 80),
            m["label"], font=f_m_label, fill=label_color,
        )
        # Description below
        desc_color = WHITE_DIM if m["state"] in ("past", "future") else WHITE
        if m["state"] == "urgent":
            desc_color = GOLD_LIGHT
        bb = draw.textbbox((0, 0), m["desc"], font=f_m_desc)
        draw.text(
            (cx - (bb[2] - bb[0]) // 2 - bb[0], timeline_y + 36),
            m["desc"], font=f_m_desc, fill=desc_color,
        )

    # Today milestone with glow on top of everything
    if today_idx is not None:
        today = milestones[today_idx]
        img = draw_glow_circle(img, (today["x"], timeline_y), 18, GOLD,
                               glow_radius=25)
        draw = ImageDraw.Draw(img)
        bb = draw.textbbox((0, 0), today["label"], font=f_m_label)
        draw.text(
            (today["x"] - (bb[2] - bb[0]) // 2 - bb[0], timeline_y - 80),
            today["label"], font=f_m_label, fill=GOLD,
        )
        bb = draw.textbbox((0, 0), today["desc"], font=f_m_desc)
        draw.text(
            (today["x"] - (bb[2] - bb[0]) // 2 - bb[0], timeline_y + 36),
            today["desc"], font=f_m_desc, fill=WHITE,
        )

    # === BIG QUESTION below the timeline (the click hook) ===
    # Position computed from the stack-centered timeline_y above.
    # Question starts after timeline labels-below + gap.
    f_sub = ImageFont.truetype(FONT_BOLD, 24)
    q_y = timeline_y + 56 + gap_timeline_question  # 56 = labels-below offset
    for line in q_lines:
        draw_centered(draw, line, f_q, q_y, WHITE, W)
        q_y += line_h

    # Small gold accent rule + sub-CTA below the question
    rule_w = 120
    rule_y = q_y + 12
    draw.rectangle([((W - rule_w) // 2, rule_y),
                    ((W + rule_w) // 2, rule_y + 4)], fill=GOLD)
    draw_centered(draw, "Free calculator · 30 seconds",
                  f_sub, rule_y + 28, GOLD_LIGHT, W)

    # (No footer band — wordmark up top carries identity. Cleaner image.)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    return output_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", required=True)
    p.add_argument("--template", default="deadline-spine",
                   choices=["deadline-spine"])
    p.add_argument("--headline", required=True)
    p.add_argument("--hero-number", required=True)
    p.add_argument("--hero-unit", default="days")
    p.add_argument("--milestones", required=True)
    p.add_argument("--footer", default="")
    p.add_argument("--question", default="")
    p.add_argument("--canvas-width", type=int, default=1200)
    p.add_argument("--canvas-height", type=int, default=900)
    args = p.parse_args()

    if args.template == "deadline-spine":
        out = render_deadline_spine(
            output_path=args.output,
            headline=args.headline,
            hero_number=args.hero_number,
            hero_unit=args.hero_unit,
            milestones=parse_milestones(args.milestones),
            footer=args.footer,
            question=args.question,
            canvas_width=args.canvas_width,
            canvas_height=args.canvas_height,
        )
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
