#!/usr/bin/env python3
"""
Qodra Systems — Official GitHub Organization Profile Generator (qodrasystems/.github)
Generates dual-theme (dark + light) animated vector SVG assets for github.com/qodrasystems.
"""
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "profile" / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

FONT_SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"


def save_svg(path: Path, svg_text: str):
    ET.fromstring(svg_text)
    path.write_text(svg_text, encoding="utf-8")


def hex_points(cx, cy, r, flat_top=True):
    pts = []
    for i in range(6):
        angle_deg = 60 * i if flat_top else 60 * i - 30
        rad = math.radians(angle_deg)
        pts.append(f"{cx + r * math.cos(rad):.2f},{cy + r * math.sin(rad):.2f}")
    return " ".join(pts)


def pill_width(label: str, min_w=54, char_w=7.4, pad=24):
    return max(min_w, int(round(len(label) * char_w + pad)))


def qodra_logo_group(tx, ty, scale, mode="dark", uid="q"):
    if mode == "dark":
        c0a, c0b = "#3B82F6", "#2563EB"
        c1a, c1b = "#818CF8", "#4F46E5"
        c2a, c2b = "#60A5FA", "#3B82F6"
    else:
        c0a, c0b = "#2563EB", "#1D4ED8"
        c1a, c1b = "#4F46E5", "#3730A3"
        c2a, c2b = "#3B82F6", "#2563EB"

    defs = f"""
    <linearGradient id="{uid}_b0" gradientUnits="userSpaceOnUse" x1="69.92" y1="-136.42" x2="134.28" y2="73.96">
      <stop offset="0" stop-color="{c0a}"/><stop offset="1" stop-color="{c0b}"/>
    </linearGradient>
    <linearGradient id="{uid}_b1" gradientUnits="userSpaceOnUse" x1="83.19" y1="128.76" x2="-131.19" y2="79.31">
      <stop offset="0" stop-color="{c1a}"/><stop offset="1" stop-color="{c1b}"/>
    </linearGradient>
    <linearGradient id="{uid}_b2" gradientUnits="userSpaceOnUse" x1="-153.11" y1="7.66" x2="-3.09" y2="-153.27">
      <stop offset="0" stop-color="{c2a}"/><stop offset="1" stop-color="{c2b}"/>
    </linearGradient>
    """
    paths = f"""
    <g transform="translate({tx},{ty}) scale({scale})">
      <path d="M 178.00 0.00 L 123.50 94.40 L 60.00 57.74 L 60.00 -154.15 L 89.00 -154.15 Z" fill="url(#{uid}_b0)" stroke="url(#{uid}_b0)" stroke-width="10" stroke-linejoin="round"/>
      <path d="M 103.50 129.04 L 89.00 154.15 L -89.00 154.15 L -143.50 59.76 L -80.00 23.09 Z" fill="url(#{uid}_b1)" stroke="url(#{uid}_b1)" stroke-width="10" stroke-linejoin="round"/>
      <path d="M -163.50 25.11 L -178.00 0.00 L -89.00 -154.15 L 20.00 -154.15 L 20.00 -80.83 Z" fill="url(#{uid}_b2)" stroke="url(#{uid}_b2)" stroke-width="10" stroke-linejoin="round"/>
    </g>
    """
    return defs, paths


# ---------------------------------------------------------------------------
# 1. ORGANIZATION HERO BANNER (840 x 276)
# ---------------------------------------------------------------------------
def build_org_hero(mode="dark"):
    W, H = 840, 276
    if mode == "dark":
        bg1, bg2 = "#100F24", "#181634"
        border = "#2F2C52"
        sheen_op = "0.14"
        ink = "#F6F4FF"
        sub_accent = "#A296FA"
        muted = "#BCB8D4"
        pill_bg = "#1D1B38"
        pill_border = "#35315E"
        badge_bg = "#201D40"
        badge_border = "#3E3972"
        hex_stroke = "#3A3666"
        center_hex_fill = "#111024"
        center_hex_stroke = "#655DF0"
        glow_color = "#5A52EA"
        glow_opacity = "0.34"
        dot_color = "#4FBF92"
        chip_text = "#DCD7FF"
        grid_dot = "#9A8DF8"
        grid_op = "0.10"
        pulse_color = "#A5B4FC"
    else:
        bg1, bg2 = "#FCFBF8", "#F3F0E8"
        border = "#DDD8CE"
        sheen_op = "0.90"
        ink = "#17162B"
        sub_accent = "#4338CA"
        muted = "#4D4A61"
        pill_bg = "#FFFFFF"
        pill_border = "#DDD8CE"
        badge_bg = "#EBE9FE"
        badge_border = "#C7C2FA"
        hex_stroke = "#CFC9E6"
        center_hex_fill = "#1B1A33"
        center_hex_stroke = "#4F46E5"
        glow_color = "#4F46E5"
        glow_opacity = "0.14"
        dot_color = "#166549"
        chip_text = "#312E81"
        grid_dot = "#4F46E5"
        grid_op = "0.09"
        pulse_color = "#4F46E5"

    cx, cy = 694, 138
    r_center = 42
    ring_dist = 78
    r_sat = 29

    satellites = [
        (0, "AI", "#5A52EA" if mode == "dark" else "#4338CA", "3.6s", "0s"),
        (60, "ERP", "#2E7564" if mode == "dark" else "#166549", "4.2s", "0.7s"),
        (120, "POS", "#9C5B82" if mode == "dark" else "#8A4570", "3.9s", "1.4s"),
        (180, "NAV", "#8B5CF6" if mode == "dark" else "#6D28D9", "4.5s", "2.1s"),
        (240, "CLOUD", "#3B82F6" if mode == "dark" else "#1D4ED8", "3.8s", "2.8s"),
        (300, "HR", "#C89B3C" if mode == "dark" else "#9A6B16", "4.4s", "3.5s"),
    ]

    sat_svgs = [
        f'<circle cx="{cx}" cy="{cy}" r="{ring_dist}" fill="none" stroke="{hex_stroke}" stroke-opacity="0.40" stroke-width="1" stroke-dasharray="3 5"/>'
    ]
    for deg in range(30, 360, 60):
        rad = math.radians(deg)
        ox = cx + 140 * math.cos(rad)
        oy = cy + 140 * math.sin(rad)
        sat_svgs.append(
            f'<polygon points="{hex_points(ox, oy, 26, True)}" fill="none" stroke="{hex_stroke}" stroke-opacity="0.28" stroke-width="1"/>'
        )

    for deg, label, tint, dur, begin in satellites:
        rad = math.radians(deg - 30)
        sx = cx + ring_dist * math.cos(rad)
        sy = cy + ring_dist * math.sin(rad)
        x1 = cx + (r_center + 2) * math.cos(rad)
        y1 = cy + (r_center + 2) * math.sin(rad)
        x2 = sx - (r_sat + 1) * math.cos(rad)
        y2 = sy - (r_sat + 1) * math.sin(rad)
        sat_svgs.append(
            f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="{hex_stroke}" stroke-opacity="0.65" stroke-width="1.1"/>'
        )
        sat_svgs.append(f"""
        <circle r="2.2" fill="{pulse_color}" opacity="0">
          <animateMotion dur="{dur}" begin="{begin}" repeatCount="indefinite" path="M {x1:.1f} {y1:.1f} L {x2:.1f} {y2:.1f}"/>
          <animate attributeName="opacity" values="0;0.95;0.95;0" keyTimes="0;0.18;0.82;1" dur="{dur}" begin="{begin}" repeatCount="indefinite"/>
        </circle>
        """)
        fill_op = "0.22" if mode == "dark" else "0.10"
        stroke_op = "0.58" if mode == "dark" else "0.38"
        sat_svgs.append(
            f'<polygon points="{hex_points(sx, sy, r_sat, True)}" fill="{tint}" fill-opacity="{fill_op}" stroke="{tint}" stroke-opacity="{stroke_op}" stroke-width="1.2"/>'
        )
        sat_svgs.append(
            f'<text x="{sx:.1f}" y="{sy + 3.8:.1f}" text-anchor="middle" font-family="{FONT_MONO}" font-size="9.5" font-weight="700" letter-spacing="0.6" fill="{ink if mode == "dark" else tint}" fill-opacity="0.94">{escape(label)}</text>'
        )

    logo_defs, logo_paths = qodra_logo_group(cx, cy, 0.14, mode="dark", uid=f"org_hero_{mode}")

    chips = [
        ("Amman, Jordan", 34, 140, '<path d="M6 11s3.5-3.1 3.5-5.8a3.5 3.5 0 1 0-7 0C2.5 7.9 6 11 6 11z"/><circle cx="6" cy="5.2" r="1.2"/>'),
        ("qodrasystems.com", 184, 160, '<circle cx="6" cy="6" r="4.6"/><path d="M1.4 6h9.2M6 1.4a7 7 0 0 1 0 9.2 7 7 0 0 1 0-9.2z"/>'),
        ("info@qodrasystems.com", 354, 188, '<rect x="1.2" y="2.2" width="9.6" height="7.6" rx="1.4"/><path d="M1.6 3.2l4.4 3.1 4.4-3.1"/>'),
    ]
    chip_svgs = []
    for text, x, w, icon in chips:
        chip_svgs.append(f"""
        <rect x="{x}" y="210" width="{w}" height="30" rx="8" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
        <g transform="translate({x + 11}, 219)" fill="none" stroke="{sub_accent}" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
        <text x="{x + 29}" y="229.2" font-family="{FONT_SANS}" font-size="11.6" font-weight="500" fill="{chip_text}">{escape(text)}</text>
        """)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Qodra Systems — Enterprise Operating Systems, AI Agents and Custom Software">
  <defs>
    <style>
      .beacon-ring {{
        transform-box: fill-box;
        transform-origin: center;
        animation: beacon 2.8s cubic-bezier(0.2, 0.7, 0.3, 1) infinite;
      }}
      .core-glow {{ animation: breathe 4.6s ease-in-out infinite; }}
      @keyframes beacon {{
        0% {{ transform: scale(1); opacity: 0.72; }}
        70% {{ transform: scale(2.4); opacity: 0; }}
        100% {{ transform: scale(2.4); opacity: 0; }}
      }}
      @keyframes breathe {{
        0%, 100% {{ opacity: 0.78; }}
        50% {{ opacity: 1; }}
      }}
      @media (prefers-reduced-motion: reduce) {{ .beacon-ring, .core-glow {{ animation: none !important; }} }}
    </style>
    <linearGradient id="obg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <radialGradient id="oglow_{mode}" cx="82%" cy="50%" r="42%">
      <stop offset="0%" stop-color="{glow_color}" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="{glow_color}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="osheen_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="30%" stop-color="#FFFFFF" stop-opacity="{sheen_op}"/>
      <stop offset="70%" stop-color="#FFFFFF" stop-opacity="{sheen_op}"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="otop_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5" stop-opacity="0"/>
      <stop offset="26%" stop-color="#6366F1" stop-opacity="0.92"/>
      <stop offset="74%" stop-color="#A5B4FC" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="#4F46E5" stop-opacity="0"/>
    </linearGradient>
    <pattern id="odots_{mode}" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{grid_dot}" fill-opacity="{grid_op}"/>
    </pattern>
    <linearGradient id="odfade_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="40%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="78%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.6"/>
    </linearGradient>
    <mask id="odmask_{mode}">
      <rect width="{W}" height="{H}" fill="url(#odfade_{mode})"/>
    </mask>
    <clipPath id="oclip_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16"/>
    </clipPath>
    {logo_defs}
  </defs>

  <g clip-path="url(#oclip_{mode})">
    <rect width="{W}" height="{H}" fill="url(#obg_{mode})"/>
    <rect width="{W}" height="{H}" fill="url(#odots_{mode})" mask="url(#odmask_{mode})"/>
    <rect width="{W}" height="{H}" fill="url(#oglow_{mode})" class="core-glow"/>
    <rect x="0" y="0" width="{W}" height="2.5" fill="url(#otop_{mode})"/>
    <rect x="0" y="2.5" width="{W}" height="1" fill="url(#osheen_{mode})"/>

    {''.join(sat_svgs)}
    <polygon points="{hex_points(cx, cy, r_center + 6, True)}" fill="none" stroke="{center_hex_stroke}" stroke-opacity="0.32" stroke-width="1"/>
    <polygon points="{hex_points(cx, cy, r_center, True)}" fill="{center_hex_fill}" stroke="{center_hex_stroke}" stroke-width="1.8"/>
    {logo_paths}

    <rect x="34" y="34" width="298" height="28" rx="14" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1"/>
    <circle cx="50" cy="48" r="4" fill="{dot_color}" class="beacon-ring"/>
    <circle cx="50" cy="48" r="3.8" fill="{dot_color}"/>
    <text x="63" y="52.2" font-family="{FONT_MONO}" font-size="10.8" font-weight="700" letter-spacing="0.9" fill="{sub_accent}">ENTERPRISE SYSTEMS &amp; AI · JORDAN</text>

    <text x="34" y="106" font-family="{FONT_SANS}" font-size="36" font-weight="700" letter-spacing="-0.8" fill="{ink}">Qodra Systems</text>

    <text x="34" y="133" font-family="{FONT_SANS}" font-size="14.5" font-weight="600" fill="{sub_accent}">Unified Business OS  ·  Governed AI Agents  ·  Custom Platforms</text>

    <text x="34" y="163" font-family="{FONT_SANS}" font-size="13.5" font-weight="400" fill="{muted}">We engineer business management systems, permission-aware AI agents,</text>
    <text x="34" y="184" font-family="{FONT_SANS}" font-size="13.5" font-weight="400" fill="{muted}">GPS-free indoor navigation platforms, and bespoke enterprise software.</text>

    {''.join(chip_svgs)}
  </g>

  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"org-hero-{mode}.svg", svg)


# ---------------------------------------------------------------------------
# 2. CTA BUTTONS (height=40)
# ---------------------------------------------------------------------------
def build_action_button(filename, label, icon_markup, icon_mode="stroke", variant="secondary", width=184, mode="dark"):
    H = 40
    if variant == "primary":
        bg1 = "#625AF2" if mode == "dark" else "#4F46E5"
        bg2 = "#4D45DC" if mode == "dark" else "#4338CA"
        border = "#837CF8" if mode == "dark" else "#3730A3"
        fg = "#FFFFFF"
        icon_color = "#FFFFFF"
        sheen_op = "0.24"
    elif variant == "whatsapp":
        bg1 = "#112E24" if mode == "dark" else "#E8F8F0"
        bg2 = "#0E251D" if mode == "dark" else "#DCF4E8"
        border = "#24664D" if mode == "dark" else "#9CDAB9"
        fg = "#6EE7B7" if mode == "dark" else "#166549"
        icon_color = "#25D366" if mode == "dark" else "#16A34A"
        sheen_op = "0.10"
    else:
        bg1 = "#191830" if mode == "dark" else "#FDFCFA"
        bg2 = "#141326" if mode == "dark" else "#F4F1EA"
        border = "#322E56" if mode == "dark" else "#DDD8CE"
        fg = "#EEEBFF" if mode == "dark" else "#17162B"
        icon_color = "#A296FA" if mode == "dark" else "#4338CA"
        sheen_op = "0.10" if mode == "dark" else "0.80"

    text_w = len(label) * 7.4
    group_w = 17 + 9 + text_w
    start_x = max(14, (width - group_w) / 2.0)

    if icon_mode == "custom":
        icon_group = f'<g transform="translate({start_x:.1f}, 11.5) scale(0.71)">{icon_markup.format(color=icon_color)}</g>'
    else:
        icon_group = f'<g transform="translate({start_x:.1f}, 11.5) scale(0.71)" fill="none" stroke="{icon_color}" stroke-width="1.95" stroke-linecap="round" stroke-linejoin="round">{icon_markup}</g>'

    shimmer_css = ""
    shimmer_rect = ""
    if variant == "primary":
        shimmer_css = """
        <style>
          .shimmer { animation: sweep 6.5s ease-in-out infinite; }
          @keyframes sweep {
            0%, 62% { transform: translateX(-120px); opacity: 0; }
            72% { opacity: 0.24; }
            96% { transform: translateX(260px); opacity: 0; }
            100% { transform: translateX(260px); opacity: 0; }
          }
          @media (prefers-reduced-motion: reduce) { .shimmer { animation: none !important; opacity: 0; } }
        </style>
        """
        shimmer_rect = f'<polygon class="shimmer" points="0,0 38,0 18,{H} -20,{H}" fill="#FFFFFF" opacity="0"/>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" role="img" aria-label="{escape(label)}">
  <defs>
    {shimmer_css}
    <linearGradient id="obtn_{filename}_{mode}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="obsheen_{filename}_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="{sheen_op}"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="obclip_{filename}_{mode}">
      <rect x="0.5" y="0.5" width="{width-1}" height="{H-1}" rx="10"/>
    </clipPath>
  </defs>
  <g clip-path="url(#obclip_{filename}_{mode})">
    <rect width="{width}" height="{H}" fill="url(#obtn_{filename}_{mode})"/>
    <rect x="0" y="1" width="{width}" height="1" fill="url(#obsheen_{filename}_{mode})"/>
    {shimmer_rect}
    {icon_group}
    <text x="{start_x + 25:.1f}" y="24.5" font-family="{FONT_SANS}" font-size="13" font-weight="600" fill="{fg}">{escape(label)}</text>
  </g>
  <rect x="0.5" y="0.5" width="{width-1}" height="{H-1}" rx="10" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"{filename}-{mode}.svg", svg)


# ---------------------------------------------------------------------------
# 3. PRODUCT BENTO CARDS (414 x 192)
# ---------------------------------------------------------------------------
def build_product_card(filename, title, subtitle, line1, line2, tags, accent_dark, accent_light, icon_svg, micro_visual, mode="dark"):
    W, H = 414, 192
    if mode == "dark":
        bg1, bg2 = "#131227", "#181632"
        border = "#2E2B50"
        sheen_op = "0.10"
        ink = "#F6F4FF"
        muted = "#B7B3CE"
        tag_bg = "#1E1C3A"
        tag_border = "#35315E"
        tag_fg = "#D6D1FF"
        accent = accent_dark
        icon_bg_op = "0.16"
        arrow_bg = "#1E1C3A"
        arrow_border = "#35315E"
        arrow_fg = "#B7B3CE"
    else:
        bg1, bg2 = "#FCFBF8", "#F4F1EA"
        border = "#DDD8CE"
        sheen_op = "0.85"
        ink = "#17162B"
        muted = "#524F66"
        tag_bg = "#FFFFFF"
        tag_border = "#DDD8CE"
        tag_fg = "#35324A"
        accent = accent_light
        icon_bg_op = "0.11"
        arrow_bg = "#FFFFFF"
        arrow_border = "#DDD8CE"
        arrow_fg = "#524F66"

    tag_svgs = []
    tx = 22
    for t in tags:
        tw = pill_width(t, min_w=46, char_w=6.8, pad=18)
        tag_svgs.append(f"""
        <rect x="{tx}" y="146" width="{tw}" height="26" rx="7" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
        <text x="{tx + tw/2:.1f}" y="163" text-anchor="middle" font-family="{FONT_SANS}" font-size="11" font-weight="500" fill="{tag_fg}">{escape(t)}</text>
        """)
        tx += tw + 7

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="ocbg_{filename}_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="octop_{filename}_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="22%" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="78%" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="ocglow_{filename}_{mode}" cx="11%" cy="22%" r="36%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="{0.22 if mode == 'dark' else 0.11}"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="occlip_{filename}_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
  </defs>

  <g clip-path="url(#occlip_{filename}_{mode})">
    <rect width="{W}" height="{H}" fill="url(#ocbg_{filename}_{mode})"/>
    <rect width="{W}" height="{H}" fill="url(#ocglow_{filename}_{mode})"/>
    <rect x="0" y="0" width="{W}" height="2.5" fill="url(#octop_{filename}_{mode})"/>
    <line x1="16" y1="2.5" x2="{W-16}" y2="2.5" stroke="#FFFFFF" stroke-opacity="{sheen_op}" stroke-width="1"/>

    {micro_visual(accent, mode)}

    <polygon points="{hex_points(42, 44, 20, True)}" fill="{accent}" fill-opacity="{icon_bg_op}" stroke="{accent}" stroke-opacity="0.5" stroke-width="1.2"/>
    <g transform="translate(33, 35)" fill="none" stroke="{accent}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
      {icon_svg}
    </g>

    <text x="74" y="40" font-family="{FONT_SANS}" font-size="16" font-weight="700" fill="{ink}">{escape(title)}</text>
    <text x="74" y="58" font-family="{FONT_MONO}" font-size="10.2" font-weight="700" letter-spacing="0.5" fill="{accent}">{escape(subtitle)}</text>

    <rect x="{W - 44}" y="22" width="24" height="24" rx="7" fill="{arrow_bg}" stroke="{arrow_border}" stroke-width="1"/>
    <g transform="translate({W - 40}, 26)" fill="none" stroke="{arrow_fg}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 11L11 5M6 5h5v5"/>
    </g>

    <text x="22" y="98" font-family="{FONT_SANS}" font-size="12.6" fill="{muted}">{escape(line1)}</text>
    <text x="22" y="118" font-family="{FONT_SANS}" font-size="12.6" fill="{muted}">{escape(line2)}</text>

    {''.join(tag_svgs)}
  </g>

  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"{filename}-{mode}.svg", svg)


def micro_erp(accent, mode):
    op = "0.28" if mode == "dark" else "0.18"
    return f"""
    <g transform="translate(332, 130)" opacity="0.88">
      <rect x="0" y="22" width="9" height="18" rx="2.5" fill="{accent}" fill-opacity="{op}"><animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" begin="0s" repeatCount="indefinite"/></rect>
      <rect x="14" y="14" width="9" height="26" rx="2.5" fill="{accent}" fill-opacity="{op}"><animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" begin="0.6s" repeatCount="indefinite"/></rect>
      <rect x="28" y="18" width="9" height="22" rx="2.5" fill="{accent}" fill-opacity="{op}"><animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" begin="1.2s" repeatCount="indefinite"/></rect>
      <rect x="42" y="4" width="9" height="36" rx="2.5" fill="{accent}" fill-opacity="0.58"><animate attributeName="opacity" values="0.65;1;0.65" dur="3.2s" begin="1.8s" repeatCount="indefinite"/></rect>
    </g>"""


def micro_ai(accent, mode):
    op = "0.42" if mode == "dark" else "0.28"
    return f"""
    <g transform="translate(338, 132)">
      <path d="M6 34 L28 6 L50 34 Z" fill="none" stroke="{accent}" stroke-opacity="{op}" stroke-width="1.2"/>
      <circle cx="6" cy="34" r="3.2" fill="{accent}" fill-opacity="0.55"/>
      <circle cx="28" cy="6" r="3.8" fill="{accent}" fill-opacity="0.88"/>
      <circle cx="50" cy="34" r="3.2" fill="{accent}" fill-opacity="0.55"/>
      <circle r="2.2" fill="{accent}"><animateMotion dur="3.8s" repeatCount="indefinite" path="M 6 34 L 28 6 L 50 34 L 6 34"/></circle>
    </g>"""


def micro_nav(accent, mode):
    op = "0.35" if mode == "dark" else "0.24"
    return f"""
    <g transform="translate(320, 128)">
      <rect x="0" y="4" width="72" height="40" rx="6" fill="none" stroke="{accent}" stroke-opacity="{op}" stroke-width="1"/>
      <path d="M10 34 L26 34 L26 16 L50 16 L50 26 L62 26" fill="none" stroke="{accent}" stroke-opacity="0.65" stroke-width="1.5" stroke-dasharray="3 2.5"/>
      <circle cx="10" cy="34" r="2.6" fill="{accent}" fill-opacity="0.5"/>
      <circle cx="62" cy="26" r="3.0" fill="{accent}"/>
      <circle r="2.4" fill="{accent}"><animateMotion dur="4.2s" repeatCount="indefinite" path="M 10 34 L 26 34 L 26 16 L 50 16 L 50 26 L 62 26"/></circle>
    </g>"""


def micro_custom(accent, mode):
    op = "0.38" if mode == "dark" else "0.25"
    return f"""
    <g transform="translate(328, 138)">
      <rect x="0" y="10" width="14" height="14" rx="3.5" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-opacity="{op}" stroke-width="1.1"/>
      <rect x="24" y="10" width="14" height="14" rx="3.5" fill="{accent}" fill-opacity="0.22" stroke="{accent}" stroke-opacity="0.6" stroke-width="1.1"/>
      <rect x="48" y="10" width="14" height="14" rx="3.5" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-opacity="{op}" stroke-width="1.1"/>
      <line x1="14" y1="17" x2="24" y2="17" stroke="{accent}" stroke-opacity="{op}" stroke-width="1.2"/>
      <line x1="38" y1="17" x2="48" y2="17" stroke="{accent}" stroke-opacity="{op}" stroke-width="1.2"/>
      <circle r="2.1" fill="{accent}"><animateMotion dur="3.4s" repeatCount="indefinite" path="M 14 17 L 48 17"/></circle>
    </g>"""


# ---------------------------------------------------------------------------
# 4. ENTERPRISE SECTORS MATRIX (840 x 192)
# ---------------------------------------------------------------------------
def build_sectors(mode="dark"):
    W, H = 840, 192
    if mode == "dark":
        bg1, bg2 = "#131227", "#181632"
        border = "#2E2B50"
        sheen_op = "0.10"
        header_fg = "#A296FA"
        ink = "#F4F2FC"
        muted = "#9B96B8"
        tile_bg = "#1B1934"
        tile_border = "#2E2B52"
    else:
        bg1, bg2 = "#FCFBF8", "#F4F1EA"
        border = "#DDD8CE"
        sheen_op = "0.85"
        header_fg = "#4338CA"
        ink = "#17162B"
        muted = "#5D5A73"
        tile_bg = "#FFFFFF"
        tile_border = "#E2DDD4"

    sectors = [
        ("Retail & Store Chains", "#4FBF92" if mode == "dark" else "#166549"),
        ("Wholesale & Distribution", "#60A5FA" if mode == "dark" else "#2563EB"),
        ("Manufacturing & Production", "#A296FA" if mode == "dark" else "#4338CA"),
        ("Contracting & Projects", "#F2A65A" if mode == "dark" else "#C2590C"),
        ("Real Estate & Properties", "#C084FC" if mode == "dark" else "#7E22CE"),
        ("Schools & Universities", "#38BDF8" if mode == "dark" else "#0284C7"),
        ("Clinics & Healthcare", "#34D399" if mode == "dark" else "#059669"),
        ("Jewellery & Luxury Retail", "#FBBF24" if mode == "dark" else "#B45309"),
        ("Malls, Airports & Venues", "#818CF8" if mode == "dark" else "#4F46E5"),
    ]

    tiles = []
    col_w = 256
    gap_x = 12
    row_h = 38
    gap_y = 10
    x0, y0 = 24, 48
    for idx, (name, dot) in enumerate(sectors):
        col = idx % 3
        row = idx // 3
        tx = x0 + col * (col_w + gap_x)
        ty = y0 + row * (row_h + gap_y)
        tiles.append(f"""
        <rect x="{tx}" y="{ty}" width="{col_w}" height="{row_h}" rx="9" fill="{tile_bg}" stroke="{tile_border}" stroke-width="1"/>
        <polygon points="{hex_points(tx + 20, ty + 19, 6.5, True)}" fill="{dot}" fill-opacity="0.22" stroke="{dot}" stroke-width="1.2"/>
        <circle cx="{tx + 20}" cy="{ty + 19}" r="2" fill="{dot}"/>
        <text x="{tx + 36}" y="{ty + 23.2}" font-family="{FONT_SANS}" font-size="12.5" font-weight="500" fill="{ink}">{escape(name)}</text>
        """)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Industries and Enterprise Sectors Served by Qodra Systems">
  <defs>
    <linearGradient id="sec_bg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <clipPath id="sec_clip_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
  </defs>
  <g clip-path="url(#sec_clip_{mode})">
    <rect width="{W}" height="{H}" fill="url(#sec_bg_{mode})"/>
    <line x1="20" y1="1.5" x2="{W-20}" y2="1.5" stroke="#FFFFFF" stroke-opacity="{sheen_op}" stroke-width="1"/>
    <text x="26" y="30" font-family="{FONT_MONO}" font-size="11" font-weight="700" letter-spacing="1.1" fill="{header_fg}">INDUSTRIES &amp; SECTOR SYSTEMS</text>
    <text x="{W - 26}" y="30" text-anchor="end" font-family="{FONT_MONO}" font-size="9.5" font-weight="600" letter-spacing="0.6" fill="{muted}">BUILT FOR MENA ENTERPRISES</text>
    {''.join(tiles)}
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"org-sectors-{mode}.svg", svg)


# ---------------------------------------------------------------------------
# 5. COMPANY TECHNOLOGY STACK & ENGINEERING PILLARS (840 x 288)
# ---------------------------------------------------------------------------
def build_org_stack(mode="dark"):
    W, H = 840, 288
    if mode == "dark":
        bg1, bg2 = "#131227", "#181632"
        border = "#2E2B50"
        sheen_op = "0.10"
        header_fg = "#A296FA"
        label_fg = "#F4F2FC"
        muted = "#9B96B8"
        row_line = "#252242"
        pri_bg = "#221F44"
        pri_border = "#484284"
        pri_fg = "#F4F2FC"
        sec_bg = "#191730"
        sec_border = "#2D2A4E"
        sec_fg = "#B7B3CE"
        tenet_num = "#A296FA"
    else:
        bg1, bg2 = "#FCFBF8", "#F4F1EA"
        border = "#DDD8CE"
        sheen_op = "0.85"
        header_fg = "#4338CA"
        label_fg = "#17162B"
        muted = "#5D5A73"
        row_line = "#E6E1D8"
        pri_bg = "#FFFFFF"
        pri_border = "#B8B2EE"
        pri_fg = "#1E1B4B"
        sec_bg = "#F4F1EA"
        sec_border = "#DDD8CE"
        sec_fg = "#4D4A61"
        tenet_num = "#4338CA"

    rows = [
        ("Mobile & Web", "#60A5FA" if mode == "dark" else "#2563EB",
         [("Flutter", True), ("TypeScript", True), ("React", False), ("Next.js", False), ("Vue.js", False), ("Swift", False), ("Kotlin", False)]),
        ("Backend & Data", "#4FBF92" if mode == "dark" else "#166549",
         [("PostgreSQL", True), ("PL/pgSQL", True), ("Node.js", False), ("Python", False), ("Go", False), (".NET", False), ("Redis", False)]),
        ("Multi-Model AI", "#A296FA" if mode == "dark" else "#4338CA",
         [("Awni Agents", True), ("Arabic & Voice", True), ("OpenAI", False), ("Claude", False), ("Gemini", False), ("Llama", False)]),
        ("Cloud & Infra", "#F2A65A" if mode == "dark" else "#C2590C",
         [("AWS", True), ("Google Cloud", True), ("Azure", False), ("Supabase", False), ("Firebase", False), ("Docker", False)]),
    ]

    row_svgs = []
    y0 = 54
    row_h = 39
    for idx, (cat, dot, items) in enumerate(rows):
        y = y0 + idx * row_h
        if idx > 0:
            row_svgs.append(f'<line x1="24" y1="{y - 11}" x2="{W - 24}" y2="{y - 11}" stroke="{row_line}" stroke-width="1"/>')
        row_svgs.append(f'<circle cx="32" cy="{y + 8}" r="4" fill="{dot}"/>')
        row_svgs.append(f'<text x="46" y="{y + 12.2}" font-family="{FONT_SANS}" font-size="12.8" font-weight="600" fill="{label_fg}">{escape(cat)}</text>')

        cx = 178
        for label, is_pri in items:
            w = pill_width(label, min_w=54, char_w=7.4, pad=26 if is_pri else 22)
            p_bg = pri_bg if is_pri else sec_bg
            p_bd = pri_border if is_pri else sec_border
            p_fg = pri_fg if is_pri else sec_fg
            fw = "600" if is_pri else "500"
            dot_mark = f'<circle cx="{cx + 10}" cy="{y + 8}" r="2.3" fill="{dot}"/>' if is_pri else ""
            tx = cx + w / 2.0 + (4 if is_pri else 0)
            row_svgs.append(f"""
            <rect x="{cx}" y="{y - 5}" width="{w}" height="26" rx="7" fill="{p_bg}" stroke="{p_bd}" stroke-width="1"/>
            {dot_mark}
            <text x="{tx:.1f}" y="{y + 12}" text-anchor="middle" font-family="{FONT_SANS}" font-size="11.5" font-weight="{fw}" fill="{p_fg}">{escape(label)}</text>
            """)
            cx += w + 8

    tenets = [
        ("01 · SINGLE DATABASE CORE", "One POS sale updates stock, ledger,", "e-invoicing & dashboards in real time."),
        ("02 · GOVERNED ENTERPRISE AI", "Agents execute inside role permissions", "with audit trails & human approval."),
        ("03 · SECURITY & COMPLIANCE", "Regional e-invoicing, bank payroll", "files, and multi-branch governance."),
    ]
    tenet_svgs = [f'<line x1="24" y1="210" x2="{W - 24}" y2="210" stroke="{row_line}" stroke-width="1"/>']
    col_w = (W - 48) / 3.0
    for idx, (head, l1, l2) in enumerate(tenets):
        tx = 26 + idx * col_w
        if idx > 0:
            tenet_svgs.append(f'<line x1="{tx - 10:.1f}" y1="222" x2="{tx - 10:.1f}" y2="274" stroke="{row_line}" stroke-width="1"/>')
        tenet_svgs.append(f"""
        <text x="{tx:.1f}" y="233" font-family="{FONT_MONO}" font-size="10.2" font-weight="700" letter-spacing="0.8" fill="{tenet_num}">{escape(head)}</text>
        <text x="{tx:.1f}" y="252" font-family="{FONT_SANS}" font-size="11.6" fill="{muted}">{escape(l1)}</text>
        <text x="{tx:.1f}" y="268" font-family="{FONT_SANS}" font-size="11.6" fill="{muted}">{escape(l2)}</text>
        """)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Qodra Systems Technology Stack and Engineering Standards">
  <defs>
    <linearGradient id="ost_bg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <clipPath id="ost_clip_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
  </defs>
  <g clip-path="url(#ost_clip_{mode})">
    <rect width="{W}" height="{H}" fill="url(#ost_bg_{mode})"/>
    <line x1="20" y1="1.5" x2="{W-20}" y2="1.5" stroke="#FFFFFF" stroke-opacity="{sheen_op}" stroke-width="1"/>
    <text x="26" y="30" font-family="{FONT_MONO}" font-size="11" font-weight="700" letter-spacing="1.1" fill="{header_fg}">ENGINEERING STACK &amp; PLATFORM STANDARDS</text>
    <text x="{W - 26}" y="30" text-anchor="end" font-family="{FONT_MONO}" font-size="9.5" font-weight="600" letter-spacing="0.6" fill="{muted}">PRODUCTION ARCHITECTURE</text>
    {''.join(row_svgs)}
    {''.join(tenet_svgs)}
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"org-stack-{mode}.svg", svg)


ICON_LAYERS = '<path d="M12 2.5L2.5 7.5 12 12.5 21.5 7.5 12 2.5z"/><path d="M2.5 12.5L12 17.5 21.5 12.5"/><path d="M2.5 17.5L12 22.5 21.5 17.5"/>'
ICON_GLOBE = '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19"/><path d="M12 2.5a14.5 14.5 0 0 1 0 19 14.5 14.5 0 0 1 0-19Z"/>'
ICON_EMAIL = '<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="M3.2 6.2l7.6 5.4a2 2 0 0 0 2.4 0l7.6-5.4"/>'
ICON_WHATSAPP = (
    '<path d="M 3.92 15.46 A 9 9 0 1 1 6.72 18.79 L 2.8 20.6 Z" fill="none" stroke="{color}" stroke-width="2.05" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path fill="{color}" d="M 9.35 7.45 c -0.22 -0.49 -0.45 -0.50 -0.66 -0.51 c -0.17 -0.01 -0.37 -0.01 -0.56 -0.01 c -0.20 0 -0.51 0.07 -0.78 0.37 c -0.27 0.29 -1.03 1.00 -1.03 2.45 c 0 1.44 1.05 2.84 1.20 3.04 c 0.15 0.20 2.03 3.25 5.01 4.43 c 2.48 0.98 2.98 0.78 3.52 0.73 c 0.54 -0.05 1.74 -0.71 1.98 -1.40 c 0.24 -0.69 0.24 -1.27 0.17 -1.40 c -0.07 -0.12 -0.27 -0.20 -0.56 -0.34 c -0.29 -0.15 -1.74 -0.86 -2.01 -0.96 c -0.27 -0.10 -0.46 -0.15 -0.66 0.15 c -0.20 0.29 -0.76 0.96 -0.93 1.15 c -0.17 0.20 -0.34 0.22 -0.64 0.07 c -0.29 -0.15 -1.24 -0.46 -2.37 -1.46 c -0.88 -0.78 -1.47 -1.75 -1.64 -2.04 c -0.17 -0.29 -0.02 -0.45 0.13 -0.60 c 0.13 -0.13 0.29 -0.34 0.44 -0.51 c 0.15 -0.17 0.20 -0.29 0.29 -0.49 c 0.10 -0.20 0.05 -0.37 -0.02 -0.51 c -0.07 -0.15 -0.64 -1.59 -0.90 -2.17 Z" transform="translate(-0.35, -0.35) scale(0.95)"/>'
)


def main():
    for mode in ("dark", "light"):
        build_org_hero(mode)
        build_sectors(mode)
        build_org_stack(mode)

        build_action_button("btn-systems", "Explore Systems", ICON_LAYERS, variant="primary", width=184, mode=mode)
        build_action_button("btn-web", "qodrasystems.com", ICON_GLOBE, variant="secondary", width=192, mode=mode)
        build_action_button("btn-contact", "Contact Us", ICON_EMAIL, variant="secondary", width=152, mode=mode)
        build_action_button("btn-whatsapp", "WhatsApp", ICON_WHATSAPP, icon_mode="custom", variant="whatsapp", width=152, mode=mode)

        build_product_card(
            "card-erp", "Qodra OS", "UNIFIED ERP · E-INVOICING",
            "Accounting, POS, inventory, purchasing, HR & sector modules",
            "on a single real-time database with e-invoicing built in.",
            ["ERP", "Finance & POS", "Multi-Branch"],
            "#4FBF92", "#166549",
            '<path d="M9 1L2 5v8l7 4 7-4V5L9 1z"/><path d="M2 5l7 4 7-4M9 9v8"/>',
            micro_erp, mode=mode,
        )
        build_product_card(
            "card-ai", "Awni & AI Agents", "PERMISSION-AWARE AI",
            "Arabic & voice AI agents that work inside company systems",
            "within role permissions, audit trails, and team approval.",
            ["AI Agents", "Arabic & Voice", "Enterprise"],
            "#A296FA", "#4338CA",
            '<path d="M9 1.5l1.8 4.7 4.7 1.8-4.7 1.8L9 14.5l-1.8-4.7L2.5 8l4.7-1.8L9 1.5z"/>',
            micro_ai, mode=mode,
        )
        build_product_card(
            "card-nav", "Indoor Navigation", "GPS-FREE WAYFINDING",
            "Cross-floor visitor guidance app and live admin console",
            "built for malls, airports, hospitals, campuses & museums.",
            ["Cross-Floor", "Heatmaps", "Venues"],
            "#C084FC", "#6D28D9",
            '<path d="M9 16s5.5-4.8 5.5-9A5.5 5.5 0 1 0 3.5 7c0 4.2 5.5 9 5.5 9z"/><circle cx="9" cy="7" r="2"/>',
            micro_nav, mode=mode,
        )
        build_product_card(
            "card-custom", "Custom Systems & Apps", "BESPOKE PLATFORMS",
            "Tailored operational software, Flutter & web platforms,",
            "customer/supplier portals, and scalable cloud integrations.",
            ["Mobile & Web", "APIs & Cloud", "Custom"],
            "#60A5FA", "#1D4ED8",
            '<path d="M5.5 5L1.5 9l4 4M12.5 5l4 4-4 4M10.5 3l-3 12"/>',
            micro_custom, mode=mode,
        )

    print("Qodra Systems Organization SVG assets generated & validated in", ASSETS_DIR)


if __name__ == "__main__":
    main()
