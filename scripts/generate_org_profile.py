#!/usr/bin/env python3
"""
Qodra Systems — Official GitHub Organization Profile Generator (v3)
- Harmonized Obsidian-Slate dark / Cool-White light surfaces with strict 2-accent discipline (Indigo + Emerald).
- Exclusively owns the iconic Qodra hexagonal constellation hero + 3-Layer Enterprise Architecture Diagram.
- >= 12px typography floor everywhere for crisp mobile & cross-OS legibility.
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
# 1. QODRA SYSTEMS SIGNATURE ORG HERO (840 x 264, >=54px text-to-hex gutter)
# ---------------------------------------------------------------------------
def build_org_hero(mode="dark"):
    W, H = 840, 264
    if mode == "dark":
        bg1, bg2 = "#0F131E", "#141A29"
        border = "#232B42"
        sheen_op = "0.10"
        ink = "#F8FAFC"
        accent = "#818CF8"
        muted = "#9BA6C0"
        pill_bg = "#141B2B"
        pill_border = "#242E48"
        pill_fg = "#CBD5E1"
        badge_bg = "#161D30"
        badge_border = "#2B3656"
        hex_stroke = "#2B3554"
        sat_fill = "#151C2E"
        sat_stroke = "#2E3A5E"
        sat_text = "#E2E8F0"
        center_hex_fill = "#0D111C"
        center_hex_stroke = "#6366F1"
        glow_color = "#6366F1"
        glow_op = "0.24"
        dot_live = "#34D399"
        grid_dot = "#818CF8"
        grid_op = "0.08"
    else:
        bg1, bg2 = "#FFFFFF", "#F8FAFC"
        border = "#E2E8F0"
        sheen_op = "0.90"
        ink = "#0F172A"
        accent = "#4F46E5"
        muted = "#475569"
        pill_bg = "#FFFFFF"
        pill_border = "#E2E8F0"
        pill_fg = "#334155"
        badge_bg = "#EEF2FF"
        badge_border = "#C7D2FE"
        hex_stroke = "#CBD5E1"
        sat_fill = "#FFFFFF"
        sat_stroke = "#CBD5E1"
        sat_text = "#1E293B"
        center_hex_fill = "#0F172A"
        center_hex_stroke = "#4F46E5"
        glow_color = "#4F46E5"
        glow_op = "0.10"
        dot_live = "#059669"
        grid_dot = "#4F46E5"
        grid_op = "0.07"

    # Positioned cleanly on the right (leftmost satellite edge = 702 - 64 - 28 = 610px; left text <= 515px -> 95px gutter!)
    cx, cy = 702, 132
    r_center = 40
    ring_dist = 74
    r_sat = 28

    satellites = [
        (0, "AI", True),
        (60, "ERP", True),
        (120, "POS", False),
        (180, "NAV", False),
        (240, "CLOUD", False),
        (300, "HR", False),
    ]

    sat_svgs = [
        f'<circle cx="{cx}" cy="{cy}" r="{ring_dist}" fill="none" stroke="{hex_stroke}" stroke-opacity="0.55" stroke-width="1" stroke-dasharray="3 5"/>'
    ]
    for deg, label, is_key in satellites:
        rad = math.radians(deg - 30)
        sx = cx + ring_dist * math.cos(rad)
        sy = cy + ring_dist * math.sin(rad)
        sat_svgs.append(
            f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="{hex_stroke}" stroke-opacity="0.7" stroke-width="1.1"/>'
        )
        stroke_col = accent if is_key else sat_stroke
        sat_svgs.append(
            f'<polygon points="{hex_points(sx, sy, r_sat, True)}" fill="{sat_fill}" stroke="{stroke_col}" stroke-opacity="{0.85 if is_key else 0.9}" stroke-width="1.2"/>'
        )
        sat_svgs.append(
            f'<text x="{sx:.1f}" y="{sy + 3.8:.1f}" text-anchor="middle" font-family="{FONT_MONO}" font-size="10" font-weight="700" letter-spacing="0.6" fill="{accent if is_key else sat_text}">{escape(label)}</text>'
        )

    logo_defs, logo_paths = qodra_logo_group(cx, cy, 0.135, mode="dark", uid=f"oh_{mode}")

    chips = [
        ("Amman, Jordan", 32, 138, '<path d="M6 11s3.5-3.1 3.5-5.8a3.5 3.5 0 1 0-7 0C2.5 7.9 6 11 6 11z"/><circle cx="6" cy="5.2" r="1.2"/>'),
        ("qodrasystems.com", 180, 158, '<circle cx="6" cy="6" r="4.6"/><path d="M1.4 6h9.2M6 1.4a7 7 0 0 1 0 9.2 7 7 0 0 1 0-9.2z"/>'),
        ("info@qodrasystems.com", 348, 184, '<rect x="1.2" y="2.2" width="9.6" height="7.6" rx="1.4"/><path d="M1.6 3.2l4.4 3.1 4.4-3.1"/>'),
    ]
    chip_svgs = []
    for text, x, w, icon in chips:
        chip_svgs.append(f"""
        <rect x="{x}" y="200" width="{w}" height="30" rx="8" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
        <g transform="translate({x + 11}, 209)" fill="none" stroke="{accent}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
        <text x="{x + 29}" y="219.2" font-family="{FONT_SANS}" font-size="11.8" font-weight="500" fill="{pill_fg}">{escape(text)}</text>
        """)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Qodra Systems — Enterprise Operating Systems, AI Agents, and Custom Software">
  <defs>
    <style>
      .beacon-ring {{
        transform-box: fill-box;
        transform-origin: center;
        animation: beacon 3s cubic-bezier(0.2, 0.7, 0.3, 1) infinite;
      }}
      @keyframes beacon {{
        0% {{ transform: scale(1); opacity: 0.7; }}
        72% {{ transform: scale(2.4); opacity: 0; }}
        100% {{ transform: scale(2.4); opacity: 0; }}
      }}
      @media (prefers-reduced-motion: reduce) {{ .beacon-ring {{ animation: none !important; }} }}
    </style>
    <linearGradient id="obg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <radialGradient id="oglow_{mode}" cx="83%" cy="50%" r="38%">
      <stop offset="0%" stop-color="{glow_color}" stop-opacity="{glow_op}"/>
      <stop offset="100%" stop-color="{glow_color}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="otop_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="30%" stop-color="{accent}" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="{accent}" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <pattern id="odots_{mode}" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{grid_dot}" fill-opacity="{grid_op}"/>
    </pattern>
    <linearGradient id="odfade_{mode}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="56%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="84%" stop-color="#FFFFFF" stop-opacity="1"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.7"/>
    </linearGradient>
    <mask id="odmask_{mode}">
      <rect width="{W}" height="{H}" fill="url(#odfade_{mode})"/>
    </mask>
    <clipPath id="oclip_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
    {logo_defs}
  </defs>

  <g clip-path="url(#oclip_{mode})">
    <rect width="{W}" height="{H}" fill="url(#obg_{mode})"/>
    <rect width="{W}" height="{H}" fill="url(#odots_{mode})" mask="url(#odmask_{mode})"/>
    <rect width="{W}" height="{H}" fill="url(#oglow_{mode})"/>
    <rect x="0" y="0" width="{W}" height="2" fill="url(#otop_{mode})"/>
    <line x1="20" y1="2.5" x2="{W-20}" y2="2.5" stroke="#FFFFFF" stroke-opacity="{sheen_op}" stroke-width="1"/>

    {''.join(sat_svgs)}
    <polygon points="{hex_points(cx, cy, r_center + 6, True)}" fill="none" stroke="{center_hex_stroke}" stroke-opacity="0.30" stroke-width="1"/>
    <polygon points="{hex_points(cx, cy, r_center, True)}" fill="{center_hex_fill}" stroke="{center_hex_stroke}" stroke-width="1.8"/>
    {logo_paths}

    <rect x="32" y="30" width="290" height="28" rx="14" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1"/>
    <circle cx="48" cy="44" r="4" fill="{dot_live}" class="beacon-ring"/>
    <circle cx="48" cy="44" r="3.6" fill="{dot_live}"/>
    <text x="61" y="48.2" font-family="{FONT_MONO}" font-size="10.8" font-weight="700" letter-spacing="0.9" fill="{accent}">ENTERPRISE SYSTEMS &amp; AI · JORDAN</text>

    <text x="32" y="102" font-family="{FONT_SANS}" font-size="36" font-weight="700" letter-spacing="-0.8" fill="{ink}">Qodra Systems</text>

    <text x="32" y="129" font-family="{FONT_SANS}" font-size="14.5" font-weight="600" fill="{accent}">Unified Business OS  ·  Governed AI Agents  ·  Custom Platforms</text>

    <text x="32" y="158" font-family="{FONT_SANS}" font-size="13.8" fill="{muted}">We build single-database business operating systems, Arabic &amp; voice</text>
    <text x="32" y="178" font-family="{FONT_SANS}" font-size="13.8" fill="{muted}">AI agents, indoor navigation platforms, and bespoke enterprise software.</text>

    {''.join(chip_svgs)}
  </g>

  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"org-hero-{mode}.svg", svg)


# ---------------------------------------------------------------------------
# 2. CLEAN CTA BUTTONS (height=38, calm, zero shimmer, uniform WhatsApp icon)
# ---------------------------------------------------------------------------
def build_action_button(filename, label, icon_markup, icon_mode="stroke", variant="secondary", width=176, mode="dark"):
    H = 38
    if variant == "primary":
        bg1 = "#5A52EA" if mode == "dark" else "#4F46E5"
        bg2 = "#4B43D6" if mode == "dark" else "#4338CA"
        border = "#7B74F5" if mode == "dark" else "#3730A3"
        fg = "#FFFFFF"
        icon_color = "#FFFFFF"
    elif variant == "whatsapp":
        bg1 = "#0F241D" if mode == "dark" else "#ECFDF5"
        bg2 = "#0C1D17" if mode == "dark" else "#D1FAE5"
        border = "#1E5240" if mode == "dark" else "#A7F3D0"
        fg = "#6EE7B7" if mode == "dark" else "#065F46"
        icon_color = "#25D366" if mode == "dark" else "#16A34A"
    else:
        bg1 = "#141928" if mode == "dark" else "#FFFFFF"
        bg2 = "#101420" if mode == "dark" else "#F8FAFC"
        border = "#252D46" if mode == "dark" else "#E2E8F0"
        fg = "#E2E8F0" if mode == "dark" else "#0F172A"
        icon_color = "#818CF8" if mode == "dark" else "#4F46E5"

    text_w = len(label) * 7.4
    group_w = 16 + 9 + text_w
    start_x = max(14, (width - group_w) / 2.0)

    if icon_mode == "custom":
        icon_group = f'<g transform="translate({start_x:.1f}, 10.5) scale(0.70)">{icon_markup.format(color=icon_color)}</g>'
    else:
        icon_group = f'<g transform="translate({start_x:.1f}, 10.5) scale(0.70)" fill="none" stroke="{icon_color}" stroke-width="1.95" stroke-linecap="round" stroke-linejoin="round">{icon_markup}</g>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" role="img" aria-label="{escape(label)}">
  <defs>
    <linearGradient id="ob_{filename}_{mode}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <clipPath id="obc_{filename}_{mode}">
      <rect x="0.5" y="0.5" width="{width-1}" height="{H-1}" rx="9"/>
    </clipPath>
  </defs>
  <g clip-path="url(#obc_{filename}_{mode})">
    <rect width="{width}" height="{H}" fill="url(#ob_{filename}_{mode})"/>
    {icon_group}
    <text x="{start_x + 24:.1f}" y="23.5" font-family="{FONT_SANS}" font-size="13" font-weight="600" fill="{fg}">{escape(label)}</text>
  </g>
  <rect x="0.5" y="0.5" width="{width-1}" height="{H-1}" rx="9" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"{filename}-{mode}.svg", svg)


# ---------------------------------------------------------------------------
# 3. 3-LAYER ENTERPRISE ARCHITECTURE DIAGRAM (840 x 332, >=12px type floor)
#    Replaces redundant 4 cards + rainbow 12-grid + 9-sectors with ONE clean diagram
# ---------------------------------------------------------------------------
def build_org_architecture(mode="dark"):
    W, H = 840, 344
    if mode == "dark":
        bg1, bg2 = "#0F131E", "#141928"
        border = "#232B42"
        sheen_op = "0.09"
        accent = "#818CF8"
        dot_live = "#34D399"
        ink = "#F8FAFC"
        muted = "#94A3B8"
        layer_bg = "#13192A"
        layer_border = "#232D47"
        tile_bg = "#171F34"
        tile_border = "#2A3656"
        core_bg = "#141B30"
        core_border = "#3E4A84"
        connector = "#334155"
    else:
        bg1, bg2 = "#FFFFFF", "#F8FAFC"
        border = "#E2E8F0"
        sheen_op = "0.90"
        accent = "#4F46E5"
        dot_live = "#059669"
        ink = "#0F172A"
        muted = "#475569"
        layer_bg = "#F8FAFC"
        layer_border = "#E2E8F0"
        tile_bg = "#FFFFFF"
        tile_border = "#CBD5E1"
        core_bg = "#EEF2FF"
        core_border = "#A5B4FC"
        connector = "#CBD5E1"

    # Layer 3: Industry Verticals (6 clean pills in 1 row or 3x2 — 3x2 gives big >=12.5px text!)
    verticals = [
        "Retail & Chains", "Wholesale & Distribution", "Manufacturing",
        "Contracting & Real Estate", "Clinics & Schools", "Jewellery & Venues",
    ]
    v_svgs = []
    vw = 248
    vg = 12
    for idx, label in enumerate(verticals):
        col = idx % 3
        row = idx // 3
        vx = 36 + col * (vw + vg)
        vy = 70 + row * 32
        v_svgs.append(f"""
        <rect x="{vx}" y="{vy}" width="{vw}" height="26" rx="6" fill="{tile_bg}" stroke="{tile_border}" stroke-width="1"/>
        <circle cx="{vx + 13}" cy="{vy + 13}" r="2.6" fill="{accent}"/>
        <text x="{vx + 25}" y="{vy + 17}" font-family="{FONT_SANS}" font-size="12" font-weight="500" fill="{ink}">{escape(label)}</text>
        """)

    # Layer 2: 6 Core Unified Qodra OS Modules (3x2 grid — spacious, zero collision!)
    modules = [
        ("ERP & Accounting", "Ledger · e-Invoice"),
        ("Sales & POS", "Cashier · Branches"),
        ("Inventory & WMS", "Stock · Batches"),
        ("Purchasing & SCM", "Suppliers · RFQs"),
        ("HR & Payroll", "Shifts · Bank WPS"),
        ("CRM & Store", "Loyalty · Online"),
    ]
    m_svgs = []
    for idx, (title, sub) in enumerate(modules):
        col = idx % 3
        row = idx // 3
        mx = 36 + col * (vw + vg)
        my = 172 + row * 32
        m_svgs.append(f"""
        <rect x="{mx}" y="{my}" width="{vw}" height="26" rx="6" fill="{tile_bg}" stroke="{tile_border}" stroke-width="1"/>
        <text x="{mx + 12}" y="{my + 17}" font-family="{FONT_SANS}" font-size="12" font-weight="700" fill="{ink}">{escape(title)}</text>
        <text x="{mx + vw - 10}" y="{my + 16.5}" text-anchor="end" font-family="{FONT_MONO}" font-size="9.2" fill="{muted}">{escape(sub)}</text>
        """)

    # Layer 1: 3 Foundational Engines (Core Database + Awni AI + Indoor Nav & Custom APIs)
    foundations = [
        ("Single PostgreSQL Core", "1 POS sale syncs stock, ledger & e-invoice", dot_live),
        ("Awni Governed AI Agents", "Arabic & voice · RBAC · human approval", accent),
        ("Indoor Nav & Custom APIs", "GPS-free wayfinding · Flutter · cloud", accent),
    ]
    f_svgs = []
    for idx, (title, sub, dot) in enumerate(foundations):
        fx = 36 + idx * (vw + vg)
        fy = 274
        f_svgs.append(f"""
        <rect x="{fx}" y="{fy}" width="{vw}" height="46" rx="8" fill="{core_bg}" stroke="{core_border}" stroke-width="1"/>
        <circle cx="{fx + 14}" cy="{fy + 17}" r="3.2" fill="{dot}"/>
        <text x="{fx + 25}" y="{fy + 21}" font-family="{FONT_SANS}" font-size="12.2" font-weight="700" fill="{ink}">{escape(title)}</text>
        <text x="{fx + 14}" y="{fy + 37}" font-family="{FONT_SANS}" font-size="10.8" fill="{muted}">{escape(sub)}</text>
        """)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Qodra Systems 3-Layer Enterprise Architecture">
  <defs>
    <linearGradient id="abg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
    <clipPath id="aclip_{mode}">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
  </defs>

  <g clip-path="url(#aclip_{mode})">
    <rect width="{W}" height="{H}" fill="url(#abg_{mode})"/>
    <line x1="20" y1="1.5" x2="{W-20}" y2="1.5" stroke="#FFFFFF" stroke-opacity="{sheen_op}" stroke-width="1"/>

    <text x="26" y="30" font-family="{FONT_MONO}" font-size="11" font-weight="700" letter-spacing="1.0" fill="{accent}">QODRA SYSTEMS  ·  3-LAYER ENTERPRISE ARCHITECTURE</text>
    <circle cx="628" cy="26.5" r="3.2" fill="{dot_live}"/>
    <text x="814" y="30" text-anchor="end" font-family="{FONT_MONO}" font-size="9.8" font-weight="600" letter-spacing="0.4" fill="{muted}">UNIFIED REAL-TIME PLATFORM</text>

    <!-- Layer 3 Container -->
    <rect x="24" y="46" width="{W-48}" height="90" rx="10" fill="{layer_bg}" stroke="{layer_border}" stroke-width="1"/>
    <text x="36" y="62" font-family="{FONT_MONO}" font-size="9.8" font-weight="700" letter-spacing="0.8" fill="{muted}">03 · INDUSTRY VERTICALS &amp; SPECIALIZED SECTORS</text>
    {''.join(v_svgs)}

    <!-- Vertical connectors L3 -> L2 -->
    <line x1="160" y1="136" x2="160" y2="148" stroke="{connector}" stroke-width="1.4" stroke-dasharray="2 2"/>
    <line x1="420" y1="136" x2="420" y2="148" stroke="{connector}" stroke-width="1.4" stroke-dasharray="2 2"/>
    <line x1="680" y1="136" x2="680" y2="148" stroke="{connector}" stroke-width="1.4" stroke-dasharray="2 2"/>

    <!-- Layer 2 Container -->
    <rect x="24" y="148" width="{W-48}" height="90" rx="10" fill="{layer_bg}" stroke="{layer_border}" stroke-width="1"/>
    <text x="36" y="164" font-family="{FONT_MONO}" font-size="9.8" font-weight="700" letter-spacing="0.8" fill="{muted}">02 · QODRA OS UNIFIED OPERATIONAL MODULES</text>
    {''.join(m_svgs)}

    <!-- Vertical connectors L2 -> L1 -->
    <line x1="160" y1="238" x2="160" y2="250" stroke="{accent}" stroke-opacity="0.65" stroke-width="1.4" stroke-dasharray="2 2"/>
    <line x1="420" y1="238" x2="420" y2="250" stroke="{accent}" stroke-opacity="0.65" stroke-width="1.4" stroke-dasharray="2 2"/>
    <line x1="680" y1="238" x2="680" y2="250" stroke="{accent}" stroke-opacity="0.65" stroke-width="1.4" stroke-dasharray="2 2"/>

    <!-- Layer 1 Container -->
    <rect x="24" y="250" width="{W-48}" height="80" rx="10" fill="{layer_bg}" stroke="{accent}" stroke-opacity="0.45" stroke-width="1"/>
    <text x="36" y="265.5" font-family="{FONT_MONO}" font-size="9.6" font-weight="700" letter-spacing="0.8" fill="{accent}">01 · FOUNDATION, REAL-TIME DATA &amp; AI RUNTIME</text>
    {''.join(f_svgs)}
  </g>

  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{border}" stroke-width="1"/>
</svg>
"""
    save_svg(ASSETS_DIR / f"org-architecture-{mode}.svg", svg)


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
        build_org_architecture(mode)
        build_action_button("btn-systems", "Explore Systems", ICON_LAYERS, variant="primary", width=180, mode=mode)
        build_action_button("btn-web", "qodrasystems.com", ICON_GLOBE, variant="secondary", width=188, mode=mode)
        build_action_button("btn-contact", "Contact Sales", ICON_EMAIL, variant="secondary", width=158, mode=mode)
        build_action_button("btn-whatsapp", "WhatsApp", ICON_WHATSAPP, icon_mode="custom", variant="whatsapp", width=148, mode=mode)

    print("v3 Qodra Systems Organization SVG assets generated & XML-validated!")


if __name__ == "__main__":
    main()
