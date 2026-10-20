# 📸 GUI Screenshots Directory

This directory stores visual assets and screenshots displayed in the root [`README.md`](../../README.md).

## 📁 Expected Screenshot Files

| File Name | Target Feature / View | Recommended Resolution | Description |
| :--- | :--- | :--- | :--- |
| **`pm-command-center-hero.png`** | PM Command Center Dashboard | 1920×1080 (16:9) | Hero banner showing the main workspace, sidebar skills & favorites, HUD, and Product Brain cards in Dark Mode. |
| **`deliverable-hub-mockup-sandbox.png`** | Deliverables & Artifacts Hub | 1920×1080 (16:9) | Dual-pane previewer showing an interactive prototype inside the responsive sandbox iframe (Desktop/Tablet/Mobile toggles). |
| **`skill-studio-socratic-gate.png`** | Skill Studio & Clarifying Gate | 1920×1080 (16:9) | Parameter selection form with framework lens and the Socratic clarifying questions modal. |
| **`product-brain-health.png`** | Product Brain Manager | 1920×1080 (16:9) | Detailed completeness cards for all `.context/` files with line/word counts and health statuses. |

---

## 🛠️ Image Optimization Guidelines

To keep the repository lightweight and ensure fast loading on GitHub:
- **Format**: PNG or WebP.
- **Max File Size**: Under **350 KB** per image.
- **Compression**: Use [`pngquant`](https://pngquant.org/) or [`squoosh`](https://squoosh.app/) before committing.
  ```bash
  # Example pngquant compression
  pngquant --quality=80-90 --ext .png --force assets/screenshots/*.png
  ```
- **Window Chrome**: Hide browser bookmarks and personal extensions; use clean localhost or full-viewport captures.
