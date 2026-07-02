"""Generate simple dark-neon PowerPoint illustration assets.

This script is a starter, not a full design system. Copy and adapt it in the
target project when a deck needs Canva-safe PNG teaching diagrams.
"""

from pathlib import Path
from math import cos, sin, pi

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1120, 430
BG1 = (4, 16, 32, 255)
BG2 = (7, 28, 48, 255)
PANEL = (13, 39, 64, 238)
WHITE = (248, 250, 252, 255)
TEAL = (5, 214, 164, 255)
BLUE = (56, 189, 248, 255)
PURPLE = (167, 139, 250, 255)
AMBER = (251, 191, 36, 255)
GREEN = (52, 211, 153, 255)


def font(size, bold=False):
    for name in (("arialbd.ttf", "Arial Bold.ttf") if bold else ("arial.ttf", "Arial.ttf")):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def background():
    image = Image.new("RGBA", (W, H), BG1)
    pixels = image.load()
    for y in range(H):
        for x in range(W):
            dx = (x - W * 0.6) / W
            dy = (y - H * 0.45) / H
            glow = max(0, 1 - (dx * dx * 5.5 + dy * dy * 7))
            pixels[x, y] = tuple(int(BG1[i] * (1 - glow) + BG2[i] * glow) for i in range(3)) + (255,)
    return image


def glow_circle(image, x, y, r, color):
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((x - r, y - r, x + r, y + r), outline=color[:3] + (180,), width=8)
    image.alpha_composite(glow.filter(ImageFilter.GaussianBlur(13)))
    draw = ImageDraw.Draw(image)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=PANEL, outline=color, width=3)


def center_text(draw, box, value, size=22):
    fnt = font(size, True)
    lines = value.split("\n")
    boxes = [draw.textbbox((0, 0), line, font=fnt) for line in lines]
    heights = [b[3] - b[1] for b in boxes]
    total_h = sum(heights) + (len(lines) - 1) * 6
    y = box[1] + (box[3] - box[1] - total_h) / 2
    for line, b, h in zip(lines, boxes, heights):
        w = b[2] - b[0]
        draw.text((box[0] + (box[2] - box[0] - w) / 2, y), line, font=fnt, fill=WHITE)
        y += h + 6


def hub_and_spoke(output, center_label, nodes):
    image = background()
    draw = ImageDraw.Draw(image)
    cx, cy = W // 2, H // 2
    glow_circle(image, cx, cy, 82, TEAL)
    center_text(draw, (cx - 85, cy - 35, cx + 85, cy + 35), center_label, 24)
    for i, (label, color) in enumerate(nodes):
        angle = -pi / 2 + i * 2 * pi / len(nodes)
        x = int(cx + 320 * cos(angle))
        y = int(cy + 150 * sin(angle))
        line = Image.new("RGBA", image.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(line)
        ld.line((cx, cy, x, y), fill=TEAL, width=3)
        image.alpha_composite(line.filter(ImageFilter.GaussianBlur(8)))
        draw.line((cx, cy, x, y), fill=TEAL, width=2)
        glow_circle(image, x, y, 58, color)
        center_text(draw, (x - 75, y - 25, x + 75, y + 25), label, 18)
    image.save(output)


def main():
    out = Path("illustration-output")
    out.mkdir(exist_ok=True)
    hub_and_spoke(
        out / "hub-and-spoke.png",
        "AGENT",
        [("Goal", TEAL), ("Context", BLUE), ("Tools", GREEN), ("Actions", AMBER), ("Memory", PURPLE)],
    )
    print(out)


if __name__ == "__main__":
    main()
