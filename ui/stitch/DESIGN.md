---
name: Atelier Workspace
colors:
  surface: '#121316'
  surface-dim: '#121316'
  surface-bright: '#38393c'
  surface-container-lowest: '#0d0e11'
  surface-container-low: '#1b1b1f'
  surface-container: '#1f1f23'
  surface-container-high: '#292a2d'
  surface-container-highest: '#343538'
  on-surface: '#e3e2e6'
  on-surface-variant: '#dbc2b0'
  inverse-surface: '#e3e2e6'
  inverse-on-surface: '#2f3034'
  outline: '#a38c7c'
  outline-variant: '#554336'
  surface-tint: '#ffb77d'
  primary: '#ffb77d'
  on-primary: '#4d2600'
  primary-container: '#d97707'
  on-primary-container: '#432100'
  inverse-primary: '#904d00'
  secondary: '#80d5cb'
  on-secondary: '#003733'
  secondary-container: '#007068'
  on-secondary-container: '#9af0e5'
  tertiary: '#cec5bf'
  on-tertiary: '#342f2b'
  tertiary-container: '#978f8a'
  on-tertiary-container: '#2e2925'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc3'
  primary-fixed-dim: '#ffb77d'
  on-primary-fixed: '#2f1500'
  on-primary-fixed-variant: '#6e3900'
  secondary-fixed: '#9cf2e8'
  secondary-fixed-dim: '#80d5cb'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#00504a'
  tertiary-fixed: '#eae1da'
  tertiary-fixed-dim: '#cec5bf'
  on-tertiary-fixed: '#1f1b17'
  on-tertiary-fixed-variant: '#4b4641'
  background: '#121316'
  on-background: '#e3e2e6'
  surface-variant: '#343538'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.025em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 17px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: -0.005em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.005em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.03em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: -0.005em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-desktop: 2rem
  space-2xs: 0.125rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 2rem
  space-2xl: 3rem
---

## Brand & Style

This design system establishes an architectural, tool-grade environment for engineering leads, product designers, and technical thinkers. It intentionally rejects the prevailing tropes of generic AI products—over-saturated cyan-purple gradients, aggressive glassmorphism, and synthetic neon glows—in favor of physical precision, editorial clarity, and monastic focus.

The aesthetic fuses **Modern Minimalism** with **Warm Tactile Precision**:
- **Utilitarian Elegance:** Visual rhythm driven by precise layout alignment, consistent baseline geometry, and disciplined typographic scale.
- **Physical Groundedness:** Surfaces evoke honed obsidian, volcanic slate, raw stone, and fine-grain cast metal, counterpointed by a restrained warm amber bronze accent that signals purpose and execution rather than decoration.
- **Cognitive Quiet:** High functional density without sensory friction. Chrome elements recede into background layers, elevating customer content and code artifact clarity.

## Colors

The color architecture is built around warm, earthy obsidian foundations, deliberately stepping away from clinical pure blacks (`#000000`) or cool navy-tinted corporate slates.

### Dark Mode (Default)
- **Canvas Base:** `#121316` (Deep obsidian espresso)
- **Surface Level 1 (Panels / Sidebars):** `#16171b`
- **Surface Level 2 (Cards / Modals / Menus):** `#1e1f24`
- **Surface Level 3 (Inputs / Active states):** `#27282e`
- **Borders & Dividers:**
  - Subtle: `rgba(255, 255, 255, 0.06)` or `#23242a`
  - Crisp / Interactive: `#2e3038`
  - Active / Focus: `#d97706`
- **Text & Content:**
  - Primary: `#f4f4f5`
  - Secondary: `#a1a1aa`
  - Muted / Disabled: `#52525b`
- **Accent Primary (Amber / Bronze):** `#d97706` (Hover: `#f59e0b`, Pressed: `#b45309`)
- **Accent Secondary (Sage Teal):** `#0f766e` (Subtle metadata, badges, and positive diff states)

### Light Mode
- **Canvas Base:** `#fcfbf9` (Warm alabaster stone)
- **Surface Level 1:** `#f4f2ee`
- **Surface Level 2:** `#ffffff`
- **Surface Level 3:** `#eae6df`
- **Borders & Dividers:**
  - Subtle: `rgba(24, 24, 27, 0.08)` or `#e5e2dc`
  - Crisp / Interactive: `#d6d1c8`
- **Text & Content:**
  - Primary: `#18181b`
  - Secondary: `#57534e`
  - Muted: `#a8a29e`
- **Accent Primary:** `#b45309` (Active: `#92400e`)
- **Accent Secondary:** `#115e59`

## Typography

The typographic hierarchy balances structural precision with effortless readability.

- **Headlines (Plus Jakarta Sans):** Imparts human warmth and contemporary architectural structure with tight tracking and balanced ascenders.
- **Body & Controls (Inter):** Pure utilitarian legibility. Rendered with calibrated letter spacing to ensure scannability across dense data grids, issue matrices, and documentation.
- **Technical & Metadata (JetBrains Mono):** Dedicated role for commit SHAs, keyboard shortcuts, inline terminal output, and technical IDs.

Numerical data in tables and status trackers must use `font-variant-numeric: tabular-nums` to preserve vertical optical alignment.

## Layout & Spacing

The layout is grounded in a continuous 4px/8px incremental rhythm configured for workspace productivity:

- **Desktop (1280px+):** Fluid multi-pane workspace. Fixed left navigation rail (56px collapsed, 240px expanded), secondary tree sidebar (280px), and an elastic primary canvas with a maximum comfortable reading measure of 840px for documents, or 100% fluid for kanban/spreadsheet surfaces.
- **Tablet (768px - 1279px):** Auto-collapsing sidebars into slide-over panels; workspace canvas retains 1.5rem margins with compact column grids.
- **Mobile (< 768px):** Single-column stacked stack. Margins collapse to 1rem. Modals convert to bottom sheets. Dense toolbars collapse into floating action menus.

All components adhere strictly to fixed vertical intervals: row items, inputs, and button components standardize around heights of 28px (compact/table), 32px (standard workspace default), and 40px (prominent actions).

## Elevation & Depth

Visual hierarchy is maintained primarily through **tonal step surfaces** and **hairline edge definition**, completely avoiding heavy diffuse drop shadows or artificial colored blurs.

1. **Layer 0 (Canvas):** Base background tone (`#121316`).
2. **Layer 1 (Recessed/Divided):** Sinks or grouped containers using a 1px border (`rgba(255, 255, 255, 0.07)`) and subtle dark tint (`#16171b`).
3. **Layer 2 (Resting Cards & Panes):** Surface `#1e1f24` edged with a 1px perimeter border `#27282e`. No drop shadow.
4. **Layer 3 (Floating Menus, Command Palettes, Popovers):** Surface `#23242a`, bounded by a crisp 1px border (`#34363f`), accompanied by an ultra-subtle directional ambient shadow:
   `box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05) inset`.
5. **Layer 4 (Modals & Focus Dialogs):** `#23242a` seated atop a subdued obsidian scrim (`rgba(10, 11, 13, 0.75)` with `backdrop-filter: blur(4px)`).

Highlighting is achieved via subtle inner top highlights: a 1px top border gradient (`linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 100%)`) mimicking an overhead raking light source.

## Shapes

The design system embraces a **Soft (Level 1)** geometric silhouette. It uses clean, calibrated corners that echo machined hardware tools rather than bubbly consumer apps.

- **Base Components (Buttons, Badges, Inputs):** `0.25rem` (4px) or `0.375rem` (6px) depending on target size.
- **Cards, Panes, and Popovers (`rounded-lg`):** `0.5rem` (8px).
- **Large Modals & Command Palettes (`rounded-xl`):** `0.75rem` (12px).
- **Status Indicators & Avatars:** Fully circular (`rounded-full`).

Corners remain consistently proportional to the bounding dimension of the element to prevent visual dissonance across nested containers.

## Components

### Buttons
- **Primary:** Solid warm bronze accent (`#d97706`), text in high-contrast deep ink (`#121316` or `#ffffff` depending on WCAG AAA criteria), subtle 1px top highlight inset. Hover shifts to `#f59e0b`.
- **Secondary (Default Workspace Action):** Charcoal surface (`#1e1f24`), crisp border (`#2e3038`), text `#f4f4f5`. Hover initiates border brightening to `#3f424d` and background to `#27282e`.
- **Ghost:** Transparent canvas, text `#a1a1aa`. Hover background `#1a1b20`, text `#ffffff`.
- **Sizes:** Compact (28px height, 11px font), Default (32px height, 13px font), Prominent (40px height, 14px font).

### Input Fields
- Dark surface `#16171b` with a hairline `#27282e` border.
- Text `#f4f4f5` with `#52525b` placeholder.
- Focus state eliminates standard browser rings; instead transitions border to `#d97706` with an inner hairline highlight glow `0 0 0 1px #d97706`.
- Integrated monospace indicators for prefix/suffix metadata (e.g., branch names, URL protocols).

### Cards & Grouped Containers
- Background `#1e1f24`, hairline border `#27282d`.
- Zero box-shadow when resting; interactive cards shift border to `#3f424e` with an imperceptible 1px Y-axis lift on hover.
- Header partitions use subtle horizontal hairline dividers (`rgba(255, 255, 255, 0.05)`).

### Command Palette (Raycast / Linear-style)
- Centered overlay, width 640px, surface `#1c1d22`, border `#32343c`.
- Top persistent search input with an understated amber search glyph.
- Results categorized under uppercase `label-sm` category headers (`#71717a`).
- Active list row marked by `#27282e` background, `#f4f4f5` bolded label, and a subtle amber vertical left accent pipe (2px wide).
- Keyboard shortcut caps rendered in JetBrains Mono with raised borders (`#2e3038`), background `#16171a`, and text `#a1a1aa`.

### Chips & Status Badges
- Pill-shaped or 4px soft radius badges.
- Neutral variant: Background `rgba(255, 255, 255, 0.05)`, border `rgba(255, 255, 255, 0.08)`, text `#a1a1aa`.
- Active / Status variant: Dark muted background tinted with secondary forest sage (`rgba(15, 118, 110, 0.15)`), border `rgba(15, 118, 110, 0.3)`, text `#2dd4bf`.

### Checkboxes & Radios
- 16px square/circle with a solid `#16171b` base and `#2e3038` border.
- Checked state fills with `#d97706`, presenting a razor-sharp `#121316` geometric checkmark icon.