# Knowledge: UI/UX Design Standards

> **Tags**: `design-tokens`, `glassmorphism`, `ux-laws`, `svg-assets`
> **Related Skill**: `SKILL_DESIGN.md`

## 1. Advanced UI Effects

### 1.1 Glassmorphism (Frosted Glass)

**Rationale**: Adds depth and a premium, modern feel.
**CSS implementation**:

```css
.glass-panel {
    background: rgba(255, 255, 255, 0.1); /* Semi-transparent */
    backdrop-filter: blur(10px);          /* Core effect */
    -webkit-backdrop-filter: blur(10px);  /* Safari support */
    border: 1px solid rgba(255, 255, 255, 0.2); /* Edge definition */
    border-radius: 16px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}
```

### 1.2 Bento UI (Grid Layout)

**Rationale**: Modular, clean organization of varied content.

- Use `display: grid` with `grid-template-areas`.
- Maintain consistent gaps (typically `1rem` or `1.5rem`).
- Use varying "box" sizes (1x1, 2x1, 1x2) to create visual interest.

### 1.3 Neumorphism (Soft UI)

**Rationale**: Tactile, soft, extruded look.
**CSS Implementation**:

```css
.neu-button {
    border-radius: 50px;
    background: #e0e0e0;
    box-shadow:  20px 20px 60px #bebebe,
                -20px -20px 60px #ffffff;
}
```

## 2. Professional SVG Assets

### 2.1 Recommended Libraries

- **Lucide**: (Preferred) Minimalist, consistent, 1500+ icons. [lucide.dev](https://lucide.dev)
- **Heroicons**: Optimized for Tailwind CSS. [heroicons.com](https://heroicons.com)
- **Iconsax**: Wide variety of styles (Linear, Bold, Two-tone). [iconsax.io](https://iconsax.io)

### 2.2 SVG Implementation Rules

1. **Never use `<img>` for icons**: Use inline SVG or component-based SVG (e.g., Lucide-React) for CSS styling (color/stroke).
2. **CurrentColor**: Set `fill="currentColor"` or `stroke="currentColor"` to allow inheritance from CSS text color.
3. **Accessibility**: Always add `aria-hidden="true"` for decorative icons or `<title>` for interactive ones.

## 3. Core UX/UE Principles (Designer Logic)

| Principle | Meaning for AI | Action |
| :--- | :--- | :--- |
| **Fitts's Law** | Target size matters | Important buttons must be larger and easier to reach. |
| **Hick's Law** | Decision time = choices | Simplify menus. Use "Batching" or "Steppers" for complex forms. |
| **Jakob's Law** | Familiarity | Stick to standard patterns (e.g., Search bar at top, Profile at right). |
| **Miller's Law** | Memory limit | Group information into "chunks" of 5-9 items max. |
| **Aesthetic-Usability** | Pretty = Works better | Spend time on transitions and alignment to build user trust. |

## 4. Design Tokens (The "Pro" Look)

- **Spacing**: Use a 4px grid (4, 8, 12, 16, 24, 32, 48, 64).
- **Typography**:
  - Sans-serif: Inter, Roboto, SF Pro (Premium feel).
  - Scale: ratio of 1.25 (16px -> 20px -> 25px -> 31px).
- **Color (Professional Palette)**:
  - **HSL System**: Use HSL for programmatic variations. `primary: hsl(220, 100%, 50%)`.
  - **Dark Mode Surface**: Avoid pure `#000`. Use deep Grays like `#0a0a0a` or `#0f172a`.
  - **Glass Borders**: Use `border: 1px solid rgba(255, 255, 255, 0.1)`.

## 5. Motion Design (The "Soul" of UI)

**Rationale**: Smooth transitions make an interface feel responsive and premium.

### 5.1 Easing & Timing

- **Standard**: `cubic-bezier(0.4, 0, 0.2, 1)` (Duration: 200ms-300ms).
- **Scale/Entrance**: `cubic-bezier(0.34, 1.56, 0.64, 1)` (Short Duration: 150ms).

### 5.2 Interactive States

- **Hover**: Subtle scaling (`scale(1.02)`) or brightness increase (`filter: brightness(1.1)`).
- **Active**: Immediate feedback (`scale(0.98)`).
- **Focus**: Distinct glow `box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5)`.

## 6. Artistic Lighting & Texture

- **Shadow Elevation**:
  - `Level 1`: `0 1px 2px 0 rgba(0, 0, 0, 0.05)` (Default buttons).
  - `Level 3`: `0 10px 15px -3px rgba(0, 0, 0, 0.1)` (Modals/Popups).
- **Grit & Texture**: For "Retro" or "Tactile" designs, use subtle noise overlays or gradients with `mix-blend-mode`.
