# Skill: UI/UX Design Implementation

> **Skill ID**: `SKILL_DESIGN`
> **Tags**: `ui-ux`, `design-gate`, `ue-ux-standard`
> **Version**: 1.0
> **Related Knowledge**: `KNOWLEDGE_DESIGN.md`

## 1. The Design Gate (Mandatory Protocol)

**Trigger**: Every time a UI-related request is made (Creating pages, components, or entire apps).

### 1.1 Design Audit (Pre-Execution)

Before writing any UI code, the AI must perform an internal audit:

- **Visual Hierarchy Check**: Is the "Primary Action" the most prominent?
- **Cognitive Load Check**: Are there too many choices? (Apply Hick's Law).
- **Premium Check**: Does the design use modern palettes and effects (Glassmorphism/Shadows)?

### 1.2 Implementation Rules

- **Rule 1**: ALWAYS use a consistent spacing system (4px grid). Ad-hoc pixel values are FORBIDDEN.
- **Rule 2**: ALWAYS implement a Dark Mode strategy (even if not requested, use CSS Variables).
- **Rule 3**: ALWAYS add micro-interactions (hover states, subtle transitions `transition: all 0.2s ease`).
- **Rule 4**: Use professional SVGs (Lucide style) for all icons. No emojis in pro-UI unless specified for a "playful" brand.

## 2. Advanced Aesthetics Protocol

### 2.1 Glassmorphism & Depth

When the user asks for a "Premium" or "Modern" feel, the AI SHOULD:

1. Apply `backdrop-filter: blur`.
2. Use multiple layered shadows to simulate depth.
3. Use high-quality gradients over flat colors.

### 2.2 Typography & Alignment

- Use responsive font sizes (rem/em).
- Maintain line-height of 1.5 - 1.6 for body text.
- Ensure 4.5:1 contrast ratio for accessibility.

## 3. Interaction Design (UE)

- **Feedback**: Every interaction MUST have visual feedback (Button clicks = active state).
- **Skeleton Screens**: For data-heavy pages, implement skeleton loaders to reduce perceived latency.
- **Error States**: UI must transition gracefully into error states with clear recovery actions.
