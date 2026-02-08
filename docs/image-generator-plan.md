# BTC102 Split - Image Generation Plan

> **⚠️ DEPRECATED - This document has been moved to a separate repository.**
>
> The image generator tool is being built in its own repo. This file is kept for reference only.
>
> ---
>
> ~~Master document for generating images across all 7 courses~~
>
> ~~Total images needed: ~220 | Current: 75 | Gap: ~145~~
>
> Last updated: 2026-01-21

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Overview](#overview)
3. [Style Guide](#style-guide)
4. [AI Tool Recommendations](#ai-tool-recommendations)
5. [Prompt Templates](#prompt-templates)
6. [Image Specifications by Course](#image-specifications-by-course)
   - [BTC102v2 - Hub Course](#btc102v2---your-first-bitcoin-journey-hub)
   - [BTC103 - Why Bitcoin Matters](#btc103---why-bitcoin-matters)
   - [BIZ102 - Bitcoin Industry Overview](#biz102---bitcoin-industry-overview)
   - [SOV102 - Bitcoin Inheritance Planning](#sov102---bitcoin-inheritance-planning)
   - [BTC104 - How to Secure Bitcoin](#btc104---how-to-secure-bitcoin)
   - [BTC105 - How to Acquire Bitcoin](#btc105---how-to-acquire-bitcoin)
   - [SCU102 - Financial Fraud & Security](#scu102---financial-fraud-scams--online-security)
7. [Web Interface (HTML)](#web-interface-html)
8. [Progress Tracking](#progress-tracking)

---

## Quick Start

### Workflow for Creating Images

1. **Choose a course** from the specifications below
2. **Find an image spec** that matches your target
3. **Copy the AI-ready prompt** (provided for each image)
4. **Generate** using your preferred AI tool (DALL-E 3, Midjourney, etc.)
5. **Convert** to WebP format (max 1920x1080, under 500KB)
6. **Name** the file following the convention: `###.webp` (e.g., `005.webp`)
7. **Place** in the correct folder: `courses/[code]/assets/en/`
8. **Mark as complete** in the tracking section

### File Placement Guide

| Course | Folder | Assets Location |
|--------|--------|-----------------|
| BTC102v2 | `courses/btc102v2/` | `courses/btc102v2/assets/en/` |
| BTC103 | `courses/btc103-new/` | `courses/btc103-new/assets/en/` |
| BIZ102 | `courses/biz102-new/` | `courses/biz102-new/assets/en/` |
| SOV102 | `courses/sov102/` | `courses/sov102/assets/en/` |
| BTC104 | `courses/btc104/` | `courses/btc104/assets/en/` |
| BTC105 | `courses/btc105/` | `courses/btc105/assets/en/` |
| SCU102 | `courses/scu102-new/` | `courses/scu102-new/assets/en/` |

---

## Overview

### Image Gap Summary

| Course | Code | Current | Target | Gap | Priority |
|--------|------|---------|--------|-----|----------|
| BTC102v2 | Hub | 4 | 4-12 | **0-8** | Low (hub course) |
| BTC103 | Why Bitcoin | 24 | 25-30 | **1-6** | Low (nearly complete) |
| BIZ102 | Industry | 11 | 30-38 | **19-27** | Medium |
| SOV102 | Inheritance | 4 | 22-27 | **18-23** | Medium |
| BTC104 | Security | 3 | 37-47 | **34-44** | High |
| BTC105 | Acquisition | 4 | 56-70 | **52-66** | High |
| SCU102 | Fraud/Security | 25 | 88-95 | **63-70** | High |
| **TOTAL** | | **75** | **262-329** | **~190** | |

### Recommended Processing Order

1. **BTC103** (1-6 images) - Quick win, nearly complete
2. **BTC102v2** (0-8 images) - Hub course, optional images
3. **BIZ102** (19-27 images) - Medium scope
4. **SOV102** (18-23 images) - Medium scope
5. **BTC104** (34-44 images) - Large scope, security focus
6. **BTC105** (52-66 images) - Largest acquisition course
7. **SCU102** (63-70 images) - Most comprehensive course

---

## Style Guide

### Technical Requirements

| Property | Requirement |
|----------|-------------|
| **Format** | WebP only |
| **Max Dimensions** | 1920 x 1080 px |
| **Recommended** | 1280 x 720 px (16:9) or 1080 x 1080 px (1:1) |
| **Max File Size** | 500 KB |
| **Naming** | `###.webp` (zero-padded, e.g., 001, 012, 099) |
| **Background** | White `#FFFFFF` or light gray `#F5F5F5` (no pure black `#000000`) |
| **Corners** | No rounded corners or baked-in shapes |

### Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Bitcoin Orange** | `#F7931A` | Primary accent, highlights |
| **Dark Gray** | `#4D4D4D` | Text, secondary elements |
| **Teal** | `#00D4AA` | Positive indicators, success |
| **Red** | `#E53935` | Warnings, errors, dangers |
| **White** | `#FFFFFF` | Backgrounds |
| **Light Gray** | `#F5F5F5` | Alternative backgrounds |

### Visual Style Guidelines

**DO:**
- Use flat design with clean lines
- Use isometric perspective for 3D elements
- Include relevant icons and simple illustrations
- Keep text minimal (labels only if essential)
- Use consistent stroke widths (2-3px)
- Maintain visual hierarchy through size/color

**DON'T:**
- Use photorealistic imagery
- Include text that needs translation (use visual language)
- Add watermarks or signatures
- Use complex gradients or shadows
- Include rounded corners (system applies these)
- Use pure black backgrounds

### Image Types and Targets

| Image Type | Target per Chapter | Best Tools |
|------------|-------------------|------------|
| **Diagrams/Flowcharts** | 1-2 | Claude Artifacts, NanoBanana |
| **Infographics** | 1-2 | DALL-E 3, Gemini |
| **Illustrations** | 1-2 | Midjourney, DALL-E 3 |
| **Comparison Tables** | 0-1 | Manual, Figma |
| **Warning Graphics** | 0-1 | DALL-E 3 |
| **Icons/Thumbnails** | As needed | DALL-E 3, Stable Diffusion |

### Chapter Type Guidelines

| Chapter Type | Image Count | Notes |
|--------------|-------------|-------|
| Introduction/Welcome | 0-1 | Optional overview graphic |
| Substantive Content | 4-5 | Full visual support |
| Going Further | 1-2 | Resource summary |
| Conclusion | 0 | No images needed |

---

## AI Tool Recommendations

### Tool Selection by Image Type

| Image Type | Primary | Secondary | Notes |
|------------|---------|-----------|-------|
| **Flowcharts/Process Diagrams** | Claude Artifacts | NanoBanana | Best for structured, logical layouts |
| **Comparison Diagrams** | DALL-E 3 | Gemini | Good at side-by-side visuals |
| **Infographics** | DALL-E 3 | NanoBanana | Data visualization |
| **Conceptual Illustrations** | Midjourney | DALL-E 3 | Best artistic quality |
| **Warning/Alert Graphics** | DALL-E 3 | Stable Diffusion | Clear, simple warnings |
| **Icons and Thumbnails** | DALL-E 3 | Stable Diffusion | Consistent style |
| **Technical Diagrams** | Manual/Figma | Claude Artifacts | Precision needed |
| **Screenshots/Mockups** | Manual | - | Do NOT use real app screenshots |

### Tool-Specific Tips

#### DALL-E 3
- Best for: Illustrations, infographics, conceptual images
- Prompt tip: Be explicit about style ("flat design", "minimal", "educational")
- Limitation: May add unwanted text - specify "no text" in prompt

#### Midjourney
- Best for: High-quality artistic illustrations
- Prompt tip: Use `--style raw` for cleaner educational look
- Parameters: `--ar 16:9` for landscape, `--v 6` for latest version

#### Claude Artifacts (SVG)
- Best for: Flowcharts, process diagrams, structured layouts
- Prompt tip: Ask for SVG code that can be exported
- Limitation: Export and convert to WebP manually

#### Gemini
- Best for: Data visualizations, charts, infographics
- Prompt tip: Provide specific data points if applicable

#### NanoBanana
- Best for: Diagrams, flowcharts, structured visuals
- Tip: Use for consistent diagram style across courses

#### Stable Diffusion / Flux
- Best for: Batch generation, consistent style
- Prompt tip: Use negative prompts to avoid photorealism

---

## Prompt Templates

### Base Template (All Images)

```
Create an educational [TYPE] for a Bitcoin course.

Topic: [TOPIC]
Description: [DESCRIPTION]

Style Requirements:
- Flat design, clean and minimal
- Color palette: Bitcoin orange (#F7931A), dark gray (#4D4D4D), white background
- Professional, educational appearance
- No text embedded in the image (or minimal labels only)
- Resolution: 1280x720 minimum

Must Include:
[LIST OF REQUIRED ELEMENTS]

Must Avoid:
- Photorealistic imagery
- Complex backgrounds
- Watermarks or signatures
- Text that would need translation
```

### Diagram Template

```
Create a clean educational diagram showing [CONCEPT].

Layout: [flowchart/process/comparison/matrix]
Elements:
- [Element 1]
- [Element 2]
- [Element 3]

Style: Flat design with Bitcoin orange (#F7931A) accents, dark gray (#4D4D4D) lines, white background.
Flow direction: [left-to-right/top-to-bottom]
Connectors: Simple arrows with consistent 2px stroke

No text labels (or minimal single-word labels only).
```

### Illustration Template

```
Create a flat-design illustration for Bitcoin education.

Concept: [CONCEPT]
Scene: [DESCRIBE THE SCENE]

Visual elements:
- [Element 1]
- [Element 2]
- [Element 3]

Style: Flat/isometric design, Bitcoin orange (#F7931A) as accent color, friendly and approachable, suitable for beginners.

Avoid: Photorealistic rendering, complex textures, dark backgrounds.
```

### Infographic Template

```
Create an educational infographic about [TOPIC].

Information to visualize:
- [Point 1]
- [Point 2]
- [Point 3]

Layout: [vertical list/grid/comparison]
Icons: Simple, outlined style
Color coding: Use orange for emphasis, gray for secondary

Style: Clean data visualization, easy to scan, professional appearance.
```

### Warning/Alert Template

```
Create a warning graphic for Bitcoin education.

Warning topic: [TOPIC]
Key message: [MESSAGE]

Visual approach:
- [Symbol or icon]
- [Color treatment - use red #E53935 for danger]
- [Layout suggestion]

Style: Clear, unambiguous warning that communicates risk without being alarming.
Avoid text - rely on visual symbols.
```

---

## Image Specifications by Course

---

## BTC102v2 - Your First Bitcoin Journey (Hub)

**Status:** 4 existing images | Gap: 0-8 images | Priority: Low

**Note:** BTC102v2 is a hub course that directs learners to other courses. Images are optional but helpful for user profiles and learning paths.

### Existing Images
- `001.webp` - Ch 2: Course Overview
- `002.webp` - Ch 2: Course Overview
- `003.webp` - Ch 2: Course Overview
- `004.webp` - Ch 2: Course Overview

### Chapter 3: Understanding Your Profile (needs 4-5 images)

#### IMG-BTC102v2-CH03-001: User Profiles Quadrant
| Field | Value |
|-------|-------|
| **Name** | `user-profiles-overview` |
| **Output** | `005.webp` |
| **Style** | Diagram/Infographic |
| **Priority** | High |
| **Description** | Quadrant diagram showing four Bitcoin user profiles (Hodler, Stacker, Active User, Privacy-Focused) with key characteristics of each |

**AI-Ready Prompt:**
```
Create an educational quadrant diagram for a Bitcoin course.

Topic: Bitcoin User Profiles
Layout: 2x2 grid/quadrant with four distinct user types

Quadrants:
1. TOP-LEFT: "Hodler" - Icon of person with locked vault, long-term focus symbol
2. TOP-RIGHT: "Stacker" - Icon of person with stacking blocks/coins, DCA symbol
3. BOTTOM-LEFT: "Active User" - Icon of person with mobile phone, Lightning bolt
4. BOTTOM-RIGHT: "Privacy-Focused" - Icon of person with shield/mask, privacy symbol

Style: Flat design, Bitcoin orange (#F7931A) accents, white background, clean icons.
Each quadrant should be visually distinct but harmonious.
No text labels in the image.
```

#### IMG-BTC102v2-CH03-002: Hodler Profile Icon
| Field | Value |
|-------|-------|
| **Name** | `hodler-profile` |
| **Output** | `006.webp` |
| **Style** | Illustration |
| **Priority** | Medium |
| **Description** | Icon/illustration representing the Hodler profile - person with locked vault/safe, long-term focus, minimal activity |

**AI-Ready Prompt:**
```
Create a flat-design illustration for Bitcoin education.

Concept: The "Hodler" Bitcoin user profile
Scene: A calm figure standing next to a secure vault/safe, with a clock showing long-term (years), minimal transaction activity

Visual elements:
- Person figure (simple, friendly)
- Secure vault or safe (prominent)
- Time indicator showing "long-term" (calendar pages, growing tree)
- Bitcoin symbol subtly integrated

Style: Flat design, Bitcoin orange accents, white background, approachable and simple.
Convey: Security, patience, long-term thinking
```

#### IMG-BTC102v2-CH03-003: Stacker Profile Icon
| Field | Value |
|-------|-------|
| **Name** | `stacker-profile` |
| **Output** | `007.webp` |
| **Style** | Illustration |
| **Priority** | Medium |
| **Description** | Icon/illustration representing the Stacker profile - person with recurring purchases, DCA concept, building blocks |

**AI-Ready Prompt:**
```
Create a flat-design illustration for Bitcoin education.

Concept: The "Stacker" Bitcoin user profile (Dollar Cost Averaging)
Scene: A figure regularly adding blocks/coins to a growing stack, with recurring schedule indicator

Visual elements:
- Person figure adding to a stack
- Growing stack of blocks or coins
- Calendar/recurring symbol (weekly/monthly)
- Upward growth trajectory

Style: Flat design, Bitcoin orange accents, white background.
Convey: Consistency, discipline, gradual accumulation
```

#### IMG-BTC102v2-CH03-004: Active User Profile Icon
| Field | Value |
|-------|-------|
| **Name** | `active-user-profile` |
| **Output** | `008.webp` |
| **Style** | Illustration |
| **Priority** | Medium |
| **Description** | Icon/illustration representing the Active User - person making transactions, Lightning symbol, mobile wallet |

**AI-Ready Prompt:**
```
Create a flat-design illustration for Bitcoin education.

Concept: The "Active User" Bitcoin profile
Scene: A person actively using Bitcoin for transactions, mobile-first, Lightning-enabled

Visual elements:
- Person with mobile phone/device
- Lightning bolt symbol (for Lightning Network)
- Transaction indicators (sending/receiving)
- Active/dynamic pose

Style: Flat design, Bitcoin orange accents, teal (#00D4AA) for Lightning, white background.
Convey: Activity, everyday use, modern technology
```

#### IMG-BTC102v2-CH03-005: Privacy-Focused Profile Icon
| Field | Value |
|-------|-------|
| **Name** | `privacy-focused-profile` |
| **Output** | `009.webp` |
| **Style** | Illustration |
| **Priority** | Medium |
| **Description** | Icon/illustration representing Privacy-Focused user - person with shield/mask, no-KYC symbol, privacy tools |

**AI-Ready Prompt:**
```
Create a flat-design illustration for Bitcoin education.

Concept: The "Privacy-Focused" Bitcoin user profile
Scene: A figure with privacy shields, avoiding surveillance, using privacy tools

Visual elements:
- Person with privacy shield or subtle mask
- No-KYC indicator (crossed out ID card)
- Privacy tools symbols (Tor onion, lock)
- Protective barrier between user and external eyes

Style: Flat design, Bitcoin orange accents, darker gray for privacy elements, white background.
Convey: Privacy, autonomy, protection from surveillance
```

### Chapter 4: Recommended Course Sequences (needs 4-5 images)

#### IMG-BTC102v2-CH04-001: Path A - Cautious Beginner
| Field | Value |
|-------|-------|
| **Name** | `path-a-cautious-beginner` |
| **Output** | `010.webp` |
| **Style** | Flowchart/Diagram |
| **Priority** | High |
| **Description** | Flowchart showing Path A sequence: SCU102 -> BTC103 -> BTC105 -> BTC104 -> SOV102 |

**AI-Ready Prompt:**
```
Create an educational flowchart for a Bitcoin learning path.

Topic: "Path A: Cautious Beginner" - Recommended course sequence
Layout: Horizontal flow from left to right

Sequence (5 boxes connected by arrows):
1. SCU102 (Security first) - Shield icon
2. BTC103 (Why Bitcoin) - Question mark/lightbulb icon
3. BTC105 (Acquire) - Plus/add icon
4. BTC104 (Secure) - Lock icon
5. SOV102 (Inheritance) - Family/document icon

Style: Clean flowchart, each box a different shade, arrows connecting them.
Color: Use Bitcoin orange for the path arrows, gray boxes with icons.
Convey: Progressive learning journey, security-first approach.
```

#### IMG-BTC102v2-CH04-002: Path B - Eager Acquirer
| Field | Value |
|-------|-------|
| **Name** | `path-b-eager-acquirer` |
| **Output** | `011.webp` |
| **Style** | Flowchart/Diagram |
| **Priority** | High |
| **Description** | Flowchart showing Path B sequence: BTC105 -> BTC104 -> SCU102 -> BTC103 -> SOV102 |

**AI-Ready Prompt:**
```
Create an educational flowchart for a Bitcoin learning path.

Topic: "Path B: Eager Acquirer" - Recommended course sequence
Layout: Horizontal flow from left to right

Sequence (5 boxes connected by arrows):
1. BTC105 (Acquire first) - Plus/add icon, emphasized
2. BTC104 (Secure) - Lock icon
3. SCU102 (Security) - Shield icon
4. BTC103 (Why Bitcoin) - Lightbulb icon
5. SOV102 (Inheritance) - Document icon

Style: Clean flowchart, first box highlighted (eager to start).
Color: Bitcoin orange for path arrows, highlight first step.
Convey: Action-oriented approach, learn by doing.
```

#### IMG-BTC102v2-CH04-003: Course Map Complete
| Field | Value |
|-------|-------|
| **Name** | `course-map-complete` |
| **Output** | `012.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Master diagram showing all courses with interconnections and recommended flows |

**AI-Ready Prompt:**
```
Create a comprehensive course map diagram for Bitcoin education.

Topic: Complete Bitcoin Learning Ecosystem
Layout: Central hub with connected courses around it

Structure:
- CENTER: BTC102v2 (Hub) - Orange, prominent
- Connected courses in a circular arrangement:
  - SCU102 (Security) - Shield icon
  - BTC103 (Why Bitcoin) - Lightbulb
  - BIZ102 (Industry) - Building/business
  - BTC104 (Secure wallets) - Lock
  - BTC105 (Acquire) - Plus sign
  - SOV102 (Inheritance) - Family/document

Connections: Lines showing common paths between courses
Arrows indicate typical progression directions

Style: Clean hub-and-spoke diagram, Bitcoin orange center, gray spokes.
Convey: Flexible learning paths, interconnected knowledge.
```

### Chapter 8: Your First Steps (needs 2-3 images)

#### IMG-BTC102v2-CH08-001: Four Steps Checklist
| Field | Value |
|-------|-------|
| **Name** | `four-steps-checklist` |
| **Output** | `013.webp` |
| **Style** | Infographic |
| **Priority** | Medium |
| **Description** | Visual checklist showing the 4 steps: Choose Path -> Start Course -> Practice -> Continue Learning |

**AI-Ready Prompt:**
```
Create an educational infographic showing four action steps.

Topic: Your First Steps with Bitcoin Learning
Layout: Horizontal or numbered vertical steps

Steps:
1. Choose Your Path - Path/road icon
2. Start Your First Course - Play button/book icon
3. Practice What You Learn - Hands/practice icon
4. Continue Your Journey - Forward arrow/growth icon

Style: Clean checklist design, numbered steps, progress indication.
Color: Bitcoin orange for step numbers/icons, gray text areas.
Convey: Clear action sequence, achievable steps.
```

---

## BTC103 - Why Bitcoin Matters

**Status:** 24 existing images | Gap: 1-6 images | Priority: Low (nearly complete!)

**Note:** This course has the smallest gap. Focus on the missing chapters only.

### Chapter 4: Monetary Properties & Transparency (needs 2-3 images)

#### IMG-BTC103-CH04-001: Bitcoin Supply Curve
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-supply-curve` |
| **Output** | `025.webp` (next available after existing 24) |
| **Style** | Chart/Diagram |
| **Priority** | High |
| **Description** | Chart showing Bitcoin's issuance schedule from 2009-2140, with halving events marked and cumulative supply approaching 21M |

**AI-Ready Prompt:**
```
Create an educational chart for Bitcoin monetary policy.

Topic: Bitcoin Supply Schedule (2009-2140)
Type: Line/area chart with milestones

Elements:
- X-axis: Years from 2009 to 2140
- Y-axis: Total Bitcoin supply (0 to 21 million)
- Curve showing diminishing issuance (asymptotic approach to 21M)
- Halving events marked (2012, 2016, 2020, 2024, 2028, etc.)
- Current point highlighted
- 21 million cap line at top

Style: Clean data visualization, Bitcoin orange for the supply curve.
Emphasize: Predictability, scarcity, halving events.
No detailed numbers needed - visual concept is key.
```

#### IMG-BTC103-CH04-002: Open Source Transparency
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-open-source` |
| **Output** | `026.webp` |
| **Style** | Illustration |
| **Priority** | Medium |
| **Description** | Illustration showing the open-source nature of Bitcoin Core - multiple developers reviewing code, global collaboration |

**AI-Ready Prompt:**
```
Create a flat-design illustration about open-source development.

Concept: Bitcoin's transparent, open-source development
Scene: Global collaboration on code review

Visual elements:
- Multiple developer figures around a central code repository
- Globe or connected world map
- Code symbols (brackets, version control)
- Transparency/visibility symbols (magnifying glass, open book)

Style: Flat design, Bitcoin orange accents, white background.
Convey: Transparency, global collaboration, anyone can audit.
```

### Chapter 5: Use Cases (needs 3-4 images)

#### IMG-BTC103-CH05-001: Cross-Border Payments
| Field | Value |
|-------|-------|
| **Name** | `cross-border-payments` |
| **Output** | `027.webp` |
| **Style** | Illustration/Map |
| **Priority** | High |
| **Description** | World map showing Bitcoin transactions crossing borders 24/7, contrasting with traditional banking limitations |

**AI-Ready Prompt:**
```
Create an educational illustration about global payments.

Concept: Bitcoin enables borderless transactions 24/7
Scene: World map with Bitcoin transactions flowing across borders

Visual elements:
- Simplified world map
- Orange lightning/arrows crossing borders freely
- 24/7 clock indicator
- Contrast: traditional banks with "closed" or limited hours (optional)

Style: Flat design, Bitcoin orange for transaction lines, white/gray map.
Convey: No borders, no banking hours, instant global transfer.
```

#### IMG-BTC103-CH05-002: Store of Value Growth
| Field | Value |
|-------|-------|
| **Name** | `store-of-value-growth` |
| **Output** | `028.webp` |
| **Style** | Chart |
| **Priority** | High |
| **Description** | Chart showing Bitcoin's long-term appreciation despite short-term volatility, compared to gold and fiat |

**AI-Ready Prompt:**
```
Create a comparison chart for store of value.

Topic: Long-term value preservation comparison
Type: Simplified trend lines over time

Elements:
- Three trend lines over a long time period:
  1. Bitcoin (orange) - volatile but upward trending
  2. Gold (yellow/gold) - stable, slight upward
  3. Fiat/Dollar (gray) - declining purchasing power
- Time axis showing "years" (no specific numbers needed)
- Value axis showing relative purchasing power

Style: Clean line chart, emphasize Bitcoin's long-term growth despite volatility.
Convey: Bitcoin as emerging store of value, fiat losing purchasing power.
```

### Going Further Chapter (TO BE CREATED - needs 1-2 images)

#### IMG-BTC103-GF-001: Learning Path Next Steps
| Field | Value |
|-------|-------|
| **Name** | `learning-path-next-steps` |
| **Output** | `029.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Visual roadmap showing progression from BTC103 to practical courses |

**AI-Ready Prompt:**
```
Create a learning path roadmap diagram.

Topic: What to learn next after understanding Why Bitcoin Matters
Layout: Current course leading to multiple next options

Structure:
- START: BTC103 "Why Bitcoin" (completed, checkmark)
- BRANCHES TO:
  - BTC105 (How to Acquire) - "Get Bitcoin"
  - BTC104 (How to Secure) - "Secure it"
  - BTC101 (Deep Philosophy) - "Go deeper"

Style: Clean roadmap with branching paths, Bitcoin orange for current course.
Convey: Multiple valid next steps, continued learning journey.
```

---

## BIZ102 - Bitcoin Industry Overview

**Status:** 11 existing images | Gap: 19-27 images | Priority: Medium

### Chapter 2: A Radical Innovation (needs 3-4 images)

#### IMG-BIZ102-CH02-001: Bitcoin Timeline
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-timeline` |
| **Output** | `012.webp` |
| **Style** | Timeline/Infographic |
| **Priority** | High |
| **Description** | Timeline showing Bitcoin's growth from 2009 to present: key milestones like first exchange, price milestones, institutional adoption |

**AI-Ready Prompt:**
```
Create an educational timeline for Bitcoin history.

Topic: Bitcoin Industry Growth (2009-Present)
Layout: Horizontal timeline with key milestones

Milestones (simplified icons, no text):
- 2009: Genesis block (origin point)
- 2010: First exchange (trading icon)
- 2013: $1,000 milestone (price up)
- 2017: $20,000 peak (chart peak)
- 2020: Institutional adoption (building/corporate)
- 2021: El Salvador (flag/country)
- 2024: ETF approval (certificate/document)

Style: Clean timeline, Bitcoin orange markers, growth trajectory implied.
Convey: Rapid growth, increasing legitimacy.
```

#### IMG-BIZ102-CH02-002: Industry Growth Visualization
| Field | Value |
|-------|-------|
| **Name** | `industry-growth` |
| **Output** | `013.webp` |
| **Style** | Chart/Diagram |
| **Priority** | High |
| **Description** | Visualization showing exponential growth of Bitcoin ecosystem: companies, developers, market cap |

**AI-Ready Prompt:**
```
Create an exponential growth visualization.

Topic: Bitcoin Ecosystem Expansion
Type: Multiple growth curves or expanding circles

Elements to show growth in:
- Number of companies/businesses
- Developer activity
- Market capitalization
- User adoption

Style: Clean growth chart, multiple metrics rising exponentially.
Color: Bitcoin orange for main curve, grays for supporting metrics.
Convey: Explosive growth across all metrics.
```

### Chapter 3: The Proliferation of Altcoins (needs 4-5 images)

#### IMG-BIZ102-CH03-001: Altcoin Explosion
| Field | Value |
|-------|-------|
| **Name** | `altcoin-explosion` |
| **Output** | `014.webp` |
| **Style** | Chart/Diagram |
| **Priority** | High |
| **Description** | Visualization showing explosion from 5,000 (2019) to millions (2025) of cryptocurrencies, most being scams |

**AI-Ready Prompt:**
```
Create a dramatic growth/explosion visualization.

Topic: Cryptocurrency Token Explosion
Concept: From thousands to millions of tokens, most worthless

Visual approach:
- Small cluster (2019): ~5,000 tokens
- Massive explosion (2025): Millions of tokens
- Most shown as faded/gray (worthless)
- Bitcoin stands out in orange (legitimate)

Style: Explosion or scatter diagram, contrast between Bitcoin and altcoins.
Convey: Overwhelming number of tokens, most are noise/scams, Bitcoin stands apart.
```

#### IMG-BIZ102-CH03-002: Bitcoin vs Altcoins Comparison
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-vs-altcoins-table` |
| **Output** | `015.webp` |
| **Style** | Comparison/Infographic |
| **Priority** | High |
| **Description** | Visual comparison: Bitcoin (liquidity, adoption, decentralization, security) vs typical altcoins |

**AI-Ready Prompt:**
```
Create a comparison infographic.

Topic: Bitcoin vs Altcoins Key Differences
Layout: Side-by-side comparison with icons

Bitcoin (Left, Orange):
- High liquidity (wave icon, full)
- Global adoption (globe, filled)
- True decentralization (distributed nodes)
- Proven security (shield, solid)

Altcoins (Right, Gray):
- Low liquidity (wave, empty)
- Limited adoption (globe, partial)
- Centralized control (single node)
- Questionable security (shield, broken)

Style: Clear comparison, Bitcoin winning on all metrics.
Convey: Fundamental differences, not just branding.
```

### Chapter 4: Institutional Adoption (needs 3-4 images)

#### IMG-BIZ102-CH04-001: CBDC World Map
| Field | Value |
|-------|-------|
| **Name** | `cbdc-map` |
| **Output** | `016.webp` |
| **Style** | Map/Infographic |
| **Priority** | High |
| **Description** | World map showing countries exploring or implementing CBDCs (China, EU, etc.) |

**AI-Ready Prompt:**
```
Create a world map infographic.

Topic: Central Bank Digital Currencies (CBDCs) Global Status
Type: World map with regional indicators

Regions to highlight:
- China: Active (dark shade)
- EU: Exploring (medium shade)
- US: Researching (light shade)
- Other countries with varying status

Style: Clean world map, different shades indicating CBDC status.
Color: Use a separate color from Bitcoin orange (perhaps blue/purple for government).
Convey: Global interest in digital currencies, government response to Bitcoin.
```

#### IMG-BIZ102-CH04-002: Bitcoin vs CBDC
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-vs-cbdc-table` |
| **Output** | `017.webp` |
| **Style** | Comparison/Infographic |
| **Priority** | High |
| **Description** | Comparison: Bitcoin (public, open, borderless, neutral, censorship-resistant) vs CBDC |

**AI-Ready Prompt:**
```
Create a comparison diagram.

Topic: Bitcoin vs Central Bank Digital Currencies
Layout: Two columns with property comparisons

Bitcoin (Left, Orange):
- Public/Open (open eye)
- Borderless (globe with no borders)
- Neutral (balanced scale)
- Censorship-resistant (broken chain)
- Fixed supply (21M cap)

CBDC (Right, Blue/Gray):
- Government controlled (building)
- National borders (flag)
- Policy tool (gears)
- Censorable (controlled access)
- Unlimited supply (infinity)

Style: Clear side-by-side, icons for each property.
Convey: Fundamental philosophical differences.
```

### Chapter 5: Regulation (needs 2-3 images)

#### IMG-BIZ102-CH05-001: Regulatory Spectrum
| Field | Value |
|-------|-------|
| **Name** | `regulatory-spectrum` |
| **Output** | `018.webp` |
| **Style** | Spectrum/Diagram |
| **Priority** | High |
| **Description** | Spectrum showing government approaches from restrictive (China) to welcoming (El Salvador) |

**AI-Ready Prompt:**
```
Create a spectrum diagram.

Topic: Global Bitcoin Regulatory Approaches
Layout: Horizontal spectrum from restrictive to welcoming

Spectrum (Left to Right):
- RESTRICTIVE: Ban icons, X marks (China example)
- CAUTIOUS: Warning signs (some countries)
- NEUTRAL: Balance scales (many countries)
- FAVORABLE: Checkmarks (Switzerland, Singapore)
- WELCOMING: Full embrace (El Salvador)

Style: Clean spectrum with gradient from red to green.
Place country indicators along the spectrum without flags.
Convey: Wide range of regulatory approaches globally.
```

### Chapter 6: Banks' Stance (needs 4-5 images)

#### IMG-BIZ102-CH06-001: Bank Threat Perception
| Field | Value |
|-------|-------|
| **Name** | `bank-threat-perception` |
| **Output** | `019.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Illustration showing how banks view Bitcoin as threat to their intermediation model |

**AI-Ready Prompt:**
```
Create a conceptual illustration.

Concept: Banks viewing Bitcoin as a threat
Scene: Traditional bank building looking worried at Bitcoin disrupting their model

Visual elements:
- Traditional bank building (pillars, institutional)
- Bitcoin symbol approaching/bypassing the bank
- Direct connection between people (peer-to-peer) bypassing bank
- Bank's intermediary role being questioned

Style: Flat design, subtle humor, contrast between old (bank) and new (Bitcoin).
Convey: Disintermediation threat to traditional banking model.
```

#### IMG-BIZ102-CH06-002: Bank Restrictions
| Field | Value |
|-------|-------|
| **Name** | `bank-restrictions` |
| **Output** | `020.webp` |
| **Style** | Infographic |
| **Priority** | High |
| **Description** | Examples of bank restrictions on crypto: account closures, service limitations |

**AI-Ready Prompt:**
```
Create an infographic about bank restrictions.

Topic: How Banks Restrict Bitcoin Access
Layout: List or grid of restriction types

Restrictions to visualize:
- Account closures (door closing)
- Wire transfer blocks (X on money transfer)
- Service denial (access denied)
- Suspicious activity flags (warning triangle)

Style: Clean icons with indication of restriction/denial.
Color: Red/gray for restrictions, contrast with Bitcoin orange.
Convey: Friction that banks create for Bitcoin users.
```

### Chapter 7: Exchanges & Custody (needs 3-4 images)

#### IMG-BIZ102-CH07-001: Exchange Types
| Field | Value |
|-------|-------|
| **Name** | `exchange-types` |
| **Output** | `021.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Diagram showing different types: P2P, Bitcoin-only, general trading platforms |

**AI-Ready Prompt:**
```
Create a classification diagram.

Topic: Types of Bitcoin Exchanges
Layout: Categories with icons

Categories:
1. Peer-to-Peer (P2P): Two people exchanging directly
2. Bitcoin-Only Exchanges: Bitcoin symbol only
3. General Crypto Exchanges: Multiple coins
4. Traditional Brokers: Suit/professional icon

Style: Clean category boxes with representative icons.
Color: Bitcoin orange for Bitcoin-focused, gray for others.
Convey: Different options for acquiring Bitcoin.
```

#### IMG-BIZ102-CH07-002: Exchange Risks
| Field | Value |
|-------|-------|
| **Name** | `exchange-risks` |
| **Output** | `022.webp` |
| **Style** | Infographic |
| **Priority** | High |
| **Description** | Risks of leaving Bitcoin on exchanges: hacking, seizure, bankruptcy (Mt.Gox, FTX examples) |

**AI-Ready Prompt:**
```
Create a risk visualization infographic.

Topic: Risks of Leaving Bitcoin on Exchanges
Layout: Warning-style infographic

Risks to visualize:
- Hacking (broken lock/skull)
- Bankruptcy (falling building)
- Account seizure (frozen/locked)
- Insider theft (hand taking)

Historical examples (abstract, no logos):
- Exchange collapse symbols (2014, 2022)

Style: Warning colors (red accents), clear danger indication.
Convey: "Not your keys, not your coins" - exchange risks.
```

### Chapter 8: Wallets, Mining, Development (needs 2-3 images)

#### IMG-BIZ102-CH08-001: Wallet Types Overview
| Field | Value |
|-------|-------|
| **Name** | `wallet-types` |
| **Output** | `023.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Comprehensive diagram: hardware, software, DIY wallet options |

**AI-Ready Prompt:**
```
Create a wallet types overview diagram.

Topic: Bitcoin Wallet Categories
Layout: Three main categories with examples

Categories:
1. Hardware Wallets: Physical device icons (USB-like)
2. Software Wallets: Mobile/desktop app icons
3. DIY/Advanced: Raspberry Pi, air-gapped computer

Security gradient: Hardware (most secure) -> Software -> DIY (depends)

Style: Clean icons for each wallet type, security indicators.
Color: Green for high security, yellow for medium.
Convey: Multiple wallet options for different needs.
```

#### IMG-BIZ102-CH08-002: Mining Ecosystem
| Field | Value |
|-------|-------|
| **Name** | `mining-ecosystem` |
| **Output** | `024.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Mining ecosystem: hardware manufacturers, pools, individual miners |

**AI-Ready Prompt:**
```
Create a mining ecosystem diagram.

Topic: Bitcoin Mining Industry Structure
Layout: Connected ecosystem diagram

Components:
- Hardware Manufacturers (factory icon)
- Mining Pools (connected computers)
- Individual Miners (single computer/ASIC)
- Bitcoin Network (center, receiving hash power)

Connections: Arrows showing relationships
- Manufacturers -> Miners
- Miners -> Pools
- Pools -> Network

Style: Clean ecosystem diagram, industrial feel.
Convey: Complex industry supporting network security.
```

### Chapter 9: Extension Layers (needs 1-2 images)

#### IMG-BIZ102-CH09-001: Sidechain Concept
| Field | Value |
|-------|-------|
| **Name** | `sidechain-concept` |
| **Output** | `025.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | How sidechains connect to Bitcoin main chain via two-way peg |

**AI-Ready Prompt:**
```
Create a technical diagram.

Topic: Bitcoin Sidechains - Two-Way Peg
Layout: Main chain with connected sidechain

Structure:
- MAIN CHAIN: Bitcoin blockchain (orange, prominent)
- SIDECHAIN: Parallel chain (gray, connected)
- TWO-WAY PEG: Bidirectional arrows showing BTC moving between chains
- LOCK/UNLOCK: Indicators showing BTC locked on main chain while active on sidechain

Style: Clean blockchain visualization, clear connection points.
Convey: Sidechains extend Bitcoin functionality while anchoring to main chain.
```

### Chapter 10: Merchant Tools (needs 4-5 images)

#### IMG-BIZ102-CH10-001: Merchant Solutions Spectrum
| Field | Value |
|-------|-------|
| **Name** | `merchant-solutions-spectrum` |
| **Output** | `026.webp` |
| **Style** | Spectrum/Diagram |
| **Priority** | High |
| **Description** | Spectrum from simple (hot wallet) to advanced (BTCPay Server) |

**AI-Ready Prompt:**
```
Create a complexity spectrum diagram.

Topic: Bitcoin Merchant Payment Solutions
Layout: Horizontal spectrum from simple to advanced

Spectrum (Left to Right):
- SIMPLE: Personal wallet QR code (phone icon)
- BASIC: Payment processor (service icon)
- INTERMEDIATE: Hosted BTCPay (cloud icon)
- ADVANCED: Self-hosted BTCPay Server (server icon)

Indicators for each:
- Setup difficulty
- Control level
- Fee structure

Style: Clean spectrum, gradient from easy (green) to advanced (orange).
Convey: Options for every merchant's technical level.
```

#### IMG-BIZ102-CH10-002: Bitcoin Payment Benefits
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-payment-benefits` |
| **Output** | `027.webp` |
| **Style** | Infographic |
| **Priority** | High |
| **Description** | Benefits: no chargebacks, lower fees, no bank required, global |

**AI-Ready Prompt:**
```
Create a benefits infographic.

Topic: Why Merchants Accept Bitcoin
Layout: Icon grid or list of benefits

Benefits:
- No Chargebacks (checkmark, no reversal)
- Lower Fees (percentage down arrow)
- No Bank Required (bank with X)
- Global Reach (globe)
- Instant Settlement (clock/lightning)
- Self-Custody Option (key)

Style: Clean icons with positive indicators (checkmarks, green).
Convey: Clear advantages over traditional payment processing.
```

---

## SOV102 - Bitcoin Inheritance Planning

**Status:** 4 existing images | Gap: 18-23 images | Priority: Medium

### Chapter 2: Why Inheritance Matters (needs 3-4 images)

#### IMG-SOV102-CH02-001: Lost Bitcoin Scenario
| Field | Value |
|-------|-------|
| **Name** | `lost-bitcoin-scenario` |
| **Output** | `005.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Grieving family unable to access bitcoin - locked wallet with question marks |

**AI-Ready Prompt:**
```
Create an emotional illustration about inheritance.

Concept: Family unable to access deceased person's Bitcoin
Scene: Sad family members looking at a locked/inaccessible wallet

Visual elements:
- Family figures (2-3 people, sad/confused expressions)
- Locked wallet or safe with Bitcoin symbol
- Question marks around the lock
- No key visible

Style: Flat design, subdued colors, emotional but not morbid.
Convey: The problem of Bitcoin being lost forever without planning.
```

#### IMG-SOV102-CH02-002: Bank vs Bitcoin Recovery
| Field | Value |
|-------|-------|
| **Name** | `bank-vs-bitcoin` |
| **Output** | `006.webp` |
| **Style** | Comparison Diagram |
| **Priority** | High |
| **Description** | Comparison: bank with "forgot password" recovery vs Bitcoin with no recovery option |

**AI-Ready Prompt:**
```
Create a comparison diagram.

Topic: Recovery Options - Traditional Bank vs Bitcoin
Layout: Side-by-side comparison

LEFT (Bank):
- Password forgotten
- "Reset password" option available
- Customer support
- Recovery possible (checkmark)

RIGHT (Bitcoin):
- Seed phrase lost
- No reset option (X)
- No customer support
- Recovery impossible (X)

Style: Clear contrast, bank side shows safety net, Bitcoin side shows responsibility.
Convey: Bitcoin's irreversibility requires planning.
```

### Chapter 3: Common Misconceptions (needs 4-5 images)

#### IMG-SOV102-CH03-001: Myth - Need a Lawyer
| Field | Value |
|-------|-------|
| **Name** | `myth-lawyer` |
| **Output** | `007.webp` |
| **Style** | Myth-Busting Illustration |
| **Priority** | High |
| **Description** | Myth vs Reality: "I need a lawyer" - crossed-out lawyer with checkmark on DIY plan |

**AI-Ready Prompt:**
```
Create a myth-busting illustration.

Concept: Myth: "I need a lawyer for Bitcoin inheritance"
Layout: Myth (crossed out) vs Reality (checkmark)

MYTH side:
- Lawyer figure with expensive/complex vibe
- Red X overlay

REALITY side:
- Simple paper/pen inheritance plan
- Green checkmark
- "DIY possible" indicator

Style: Clear myth-busting format, red X on myth, green check on reality.
Convey: You can create a basic plan yourself.
```

#### IMG-SOV102-CH03-002: Myth - Heirs Will Figure It Out
| Field | Value |
|-------|-------|
| **Name** | `myth-heirs` |
| **Output** | `008.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Myth: "My heirs will figure it out" - confused heir vs guided heir |

**AI-Ready Prompt:**
```
Create a comparison illustration.

Concept: Myth: "My heirs will figure it out"
Layout: Two scenarios side by side

SCENARIO 1 (No Plan):
- Confused heir with question marks
- Locked wallet, no instructions
- Frustrated expression

SCENARIO 2 (With Plan):
- Confident heir with clear instructions
- Step-by-step guide visible
- Successful access

Style: Clear contrast between outcomes.
Convey: Planning makes the difference between success and failure.
```

### Chapter 6: Trusted Assistants (needs 4-5 images)

#### IMG-SOV102-CH06-001: Trusted Assistant Roles
| Field | Value |
|-------|-------|
| **Name** | `trusted-assistant-roles` |
| **Output** | `009.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Two roles: trusted relative + experienced Bitcoin user |

**AI-Ready Prompt:**
```
Create a role diagram.

Topic: Two Key Roles for Bitcoin Inheritance Assistants
Layout: Two distinct roles with descriptions

Role 1 - Trusted Relative:
- Family member icon
- Heart/trust symbol
- "Knows your wishes" indicator

Role 2 - Bitcoin Expert:
- Technical person icon
- Bitcoin knowledge symbol
- "Knows how to help" indicator

Connection: Both roles work together to help heirs

Style: Clean role diagram, two complementary figures.
Convey: Different skills needed, often different people.
```

#### IMG-SOV102-CH06-002: Trust-Knowledge Matrix
| Field | Value |
|-------|-------|
| **Name** | `trust-knowledge-matrix` |
| **Output** | `010.webp` |
| **Style** | Matrix Diagram |
| **Priority** | High |
| **Description** | 2x2 matrix: trust level vs Bitcoin knowledge for evaluating candidates |

**AI-Ready Prompt:**
```
Create a 2x2 matrix diagram.

Topic: Evaluating Potential Assistants
Axes:
- X-axis: Bitcoin Knowledge (Low to High)
- Y-axis: Trust Level (Low to High)

Quadrants:
- High Trust + High Knowledge: IDEAL (green, star)
- High Trust + Low Knowledge: Good Trusted Relative (yellow)
- Low Trust + High Knowledge: Potential Expert Helper (yellow)
- Low Trust + Low Knowledge: Not Suitable (red, X)

Style: Clean matrix, color-coded quadrants.
Convey: Evaluate assistants on both dimensions.
```

### Chapter 7: Create Your Inventory (needs 4-5 images)

#### IMG-SOV102-CH07-001: Inventory Categories
| Field | Value |
|-------|-------|
| **Name** | `inventory-categories` |
| **Output** | `011.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Categories: exchanges, hot wallets, hardware wallets, other assets |

**AI-Ready Prompt:**
```
Create a categorization diagram.

Topic: Bitcoin Asset Inventory Categories
Layout: Four distinct categories with icons

Categories:
1. Exchange Accounts: Building/platform icon
2. Hot Wallets: Mobile phone icon
3. Hardware Wallets: USB device icon
4. Other: Lightning, multi-sig, etc.

Each category shows:
- Icon representation
- Example items to document

Style: Clean category grid, organized structure.
Convey: Comprehensive inventory covers all Bitcoin locations.
```

### Chapter 8: Write the Letter (needs 4-5 images)

#### IMG-SOV102-CH08-001: Letter Components
| Field | Value |
|-------|-------|
| **Name** | `letter-components` |
| **Output** | `012.webp` |
| **Style** | Infographic |
| **Priority** | High |
| **Description** | Letter sections: intro, contacts, inventory, safety instructions, final message |

**AI-Ready Prompt:**
```
Create a document structure infographic.

Topic: Inheritance Letter Components
Layout: Sections of a letter document

Sections (top to bottom):
1. Introduction: Who you are, why this letter
2. Contacts: Trusted assistants to call
3. Inventory: Where your Bitcoin is
4. Safety Instructions: What NOT to do
5. Final Message: Personal words to heirs

Style: Clean document outline, numbered sections.
Convey: Complete letter has all necessary information.
```

#### IMG-SOV102-CH08-002: Security-Accessibility Balance
| Field | Value |
|-------|-------|
| **Name** | `security-accessibility-balance` |
| **Output** | `013.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Balance scale: too little info (can't access) vs too much info (theft risk) |

**AI-Ready Prompt:**
```
Create a balance scale diagram.

Topic: Finding the Right Balance in Inheritance Letters
Layout: Scale with two extremes

LEFT (Too Little Info):
- Locked out symbol
- Heirs can't access
- Scale tips down (bad)

CENTER (Balanced):
- Checkmark
- Just enough info
- Scale balanced (good)

RIGHT (Too Much Info):
- Theft risk symbol
- Anyone could steal
- Scale tips down (bad)

Style: Classic balance scale metaphor.
Convey: The letter needs the right amount of detail.
```

### Chapter 9: Review and Store (needs 3-4 images)

#### IMG-SOV102-CH09-001: Storage Locations
| Field | Value |
|-------|-------|
| **Name** | `storage-locations` |
| **Output** | `014.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Multiple secure locations: home safe, trusted person, bank vault |

**AI-Ready Prompt:**
```
Create a multi-location storage illustration.

Topic: Where to Store Your Inheritance Plan
Layout: Three secure storage options

Locations:
1. Home Safe: Fireproof safe in home
2. Trusted Person: Sealed envelope with trusted family member
3. Bank Vault: Safe deposit box at bank (optional)

Each location shows:
- Secure storage icon
- Different geographic location implied

Style: Clean icons for each storage option.
Convey: Multiple copies in different locations for redundancy.
```

---

## BTC104 - How to Secure Bitcoin

**Status:** 3 existing images | Gap: 34-44 images | Priority: High

### Chapter 2: Why You Need Your Own Wallet (needs 3-4 images)

#### IMG-BTC104-CH02-001: Exchange Risks Timeline
| Field | Value |
|-------|-------|
| **Name** | `exchange-risks-timeline` |
| **Output** | `004.webp` |
| **Style** | Timeline |
| **Priority** | High |
| **Description** | Timeline of exchange failures: Mt. Gox (2014), FTX (2022), with icons for hacks, bankruptcies |

**AI-Ready Prompt:**
```
Create a historical timeline diagram.

Topic: History of Exchange Failures
Layout: Horizontal timeline with incidents

Events (with icons, no specific names):
- 2014: Major exchange hack (broken lock)
- 2019: Exchange exit scam (running figure)
- 2022: Exchange bankruptcy (falling building)
- Various: Account freezes (ice/freeze symbol)

Style: Timeline with warning indicators, red accents for danger.
Convey: Exchange custody has repeatedly failed users.
```

#### IMG-BTC104-CH02-002: Keys Concept
| Field | Value |
|-------|-------|
| **Name** | `keys-concept` |
| **Output** | `005.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | "Not your keys, not your coins" - exchange holding keys vs user holding keys |

**AI-Ready Prompt:**
```
Create a comparison illustration.

Concept: "Not Your Keys, Not Your Coins"
Layout: Split screen comparison

LEFT (Exchange Custody):
- Exchange building holding the key
- User has no key
- Bitcoin behind exchange's lock
- User has IOU/receipt only

RIGHT (Self-Custody):
- User holding their own key
- Bitcoin directly accessible
- No intermediary
- Full control

Style: Clear visual contrast between custody models.
Convey: Fundamental difference in who controls the Bitcoin.
```

### Chapter 3: What Is a Bitcoin Wallet? (needs 4-5 images)

#### IMG-BTC104-CH03-001: Wallet Not Storage
| Field | Value |
|-------|-------|
| **Name** | `wallet-not-storage` |
| **Output** | `006.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Wallet as key holder, not storage - bitcoin lives on the network |

**AI-Ready Prompt:**
```
Create an educational illustration.

Concept: Bitcoin Wallet = Key Holder, NOT Storage
Scene: Dispelling the common misconception

Visual approach:
- WRONG: Wallet containing Bitcoin (crossed out)
- RIGHT: Wallet holding keys that access Bitcoin on the network

Show:
- Keys inside the wallet
- Bitcoin existing on the distributed network
- Keys "pointing to" Bitcoin on network

Style: Clear myth-busting visual.
Convey: Your wallet holds keys, not actual Bitcoin.
```

#### IMG-BTC104-CH03-002: Public/Private Keys
| Field | Value |
|-------|-------|
| **Name** | `public-private-keys` |
| **Output** | `007.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Public key (shareable address) vs private key (secret), mailbox analogy |

**AI-Ready Prompt:**
```
Create an educational diagram.

Topic: Public Key vs Private Key
Layout: Mailbox analogy with two key types

PUBLIC KEY (Address):
- Mailbox number/address
- Shareable (anyone can send mail to it)
- Like your email address
- Green/open indicator

PRIVATE KEY:
- Key to open the mailbox
- Never share (only you can access)
- Like your email password
- Red/secret indicator

Style: Clear mailbox analogy, two distinct key types.
Convey: Public = share freely, Private = guard carefully.
```

#### IMG-BTC104-CH03-003: Seed Phrase Generation
| Field | Value |
|-------|-------|
| **Name** | `seed-phrase-generation` |
| **Output** | `008.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Seed phrase (12/24 words) generating all keys |

**AI-Ready Prompt:**
```
Create a hierarchical diagram.

Topic: Seed Phrase -> Keys Generation
Layout: Tree structure from seed to keys

Structure:
- TOP: Seed Phrase (12/24 words) - Master
- MIDDLE: Generates multiple Private Keys
- BOTTOM: Each Private Key -> Public Key -> Address

Flow: One seed creates unlimited keys/addresses

Style: Clean hierarchy diagram, branching structure.
Convey: Seed phrase is the master backup for everything.
```

### Chapter 4: Types of Wallets (needs 3-4 images)

#### IMG-BTC104-CH04-001: Hot vs Cold Comparison
| Field | Value |
|-------|-------|
| **Name** | `hot-vs-cold-comparison` |
| **Output** | `009.webp` |
| **Style** | Comparison Chart |
| **Priority** | High |
| **Description** | Side-by-side: hot wallet (pros/cons) vs hardware wallet (pros/cons) |

**AI-Ready Prompt:**
```
Create a comparison chart.

Topic: Hot Wallets vs Hardware Wallets
Layout: Side-by-side with pros and cons

HOT WALLETS:
Pros: Free, convenient, always available
Cons: Connected to internet, vulnerable to hacks

HARDWARE WALLETS:
Pros: Keys never online, high security
Cons: Cost money, less convenient

Style: Clean comparison table with icons.
Convey: Different tools for different amounts and uses.
```

### Chapter 5: Custodial vs Self-Custody (needs 4-5 images)

#### IMG-BTC104-CH05-001: Custodial Diagram
| Field | Value |
|-------|-------|
| **Name** | `custodial-diagram` |
| **Output** | `010.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Custodial: user -> exchange holds keys -> bitcoin |

**AI-Ready Prompt:**
```
Create a flow diagram.

Topic: How Custodial Services Work
Layout: Flow from user to Bitcoin

Flow:
USER -> EXCHANGE (holds keys) -> BITCOIN

Show:
- User has account only
- Exchange has the actual keys
- Bitcoin controlled by exchange
- User must ask exchange for access

Style: Clear flow diagram with intermediary highlighted.
Convey: Third party controls your Bitcoin.
```

#### IMG-BTC104-CH05-002: Self-Custody Diagram
| Field | Value |
|-------|-------|
| **Name** | `self-custody-diagram` |
| **Output** | `011.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Self-custody: user holds keys -> direct bitcoin control |

**AI-Ready Prompt:**
```
Create a flow diagram.

Topic: How Self-Custody Works
Layout: Direct flow from user to Bitcoin

Flow:
USER (holds keys) -> BITCOIN

Show:
- User holds their own keys
- No intermediary
- Direct access to Bitcoin
- Full control and responsibility

Style: Clean flow diagram, simpler than custodial.
Convey: You control your own Bitcoin directly.
```

### Chapter 6: Choosing Your First Wallet (needs 4-5 images)

#### IMG-BTC104-CH06-001: Fake App Warning
| Field | Value |
|-------|-------|
| **Name** | `fake-app-warning` |
| **Output** | `012.webp` |
| **Style** | Warning Illustration |
| **Priority** | High |
| **Description** | Warning about fake apps in app stores with red flags |

**AI-Ready Prompt:**
```
Create a warning infographic.

Topic: Fake Wallet Apps in App Stores
Layout: Warning with red flags to look for

Red Flags:
- Misspelled app names
- Wrong developer name
- Low review count/new app
- Asking for seed phrase import immediately
- Too many permissions requested

Style: Warning format, red accents, clear danger indicators.
Convey: Always verify before downloading wallet apps.
```

### Chapter 7: Creating Your Wallet (needs 4-5 images)

#### IMG-BTC104-CH07-001: Seed Phrase Display
| Field | Value |
|-------|-------|
| **Name** | `seed-phrase-display` |
| **Output** | `013.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Example seed phrase display with warning: never share - use fake words |

**AI-Ready Prompt:**
```
Create an educational illustration.

Topic: Seed Phrase Display (Example)
Scene: What you see when creating a wallet

Visual elements:
- Screen showing 12 numbered word boxes (use placeholder words like "word1", "word2" or random innocuous words)
- WARNING indicator: "Never share these words"
- Clean, official-looking interface
- Write-down indicator

Style: Clean wallet interface mockup.
Important: Use FAKE/EXAMPLE words, not real seed phrase.
Convey: This is what the seed phrase looks like.
```

#### IMG-BTC104-CH07-002: Writing Seed Phrase
| Field | Value |
|-------|-------|
| **Name** | `writing-seed-phrase` |
| **Output** | `014.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Proper way to write seed phrase - pen, paper, numbered words |

**AI-Ready Prompt:**
```
Create an instructional illustration.

Topic: How to Properly Record Your Seed Phrase
Scene: Correct backup method

Visual elements:
- Hand with pen writing on paper
- Numbered list (1-12 or 1-24)
- Clean, legible handwriting
- No digital devices in scene
- Secure/private setting implied

Style: Clean instructional illustration.
Convey: Write it down by hand, on paper, numbered.
```

### Chapter 8: Securing Your Seed Phrase (needs 4-5 images)

#### IMG-BTC104-CH08-001: Seed Loss Consequences
| Field | Value |
|-------|-------|
| **Name** | `seed-loss-consequences` |
| **Output** | `015.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Phone breaks + no seed = bitcoin lost forever |

**AI-Ready Prompt:**
```
Create a consequence diagram.

Topic: What Happens If You Lose Your Seed Phrase
Layout: Cause and effect

Scenario:
- Phone breaks/lost (broken phone icon)
- PLUS no seed phrase backup (X on paper)
- EQUALS Bitcoin lost forever (locked/inaccessible Bitcoin)

Style: Clear cause-effect diagram, serious tone.
Convey: Without backup, device loss = permanent Bitcoin loss.
```

#### IMG-BTC104-CH08-002: Don't Store Digitally
| Field | Value |
|-------|-------|
| **Name** | `dont-store-digitally` |
| **Output** | `016.webp` |
| **Style** | Warning Illustration |
| **Priority** | High |
| **Description** | Icons with X: no computer, no phone, no cloud, no email, no photos |

**AI-Ready Prompt:**
```
Create a "don't do this" warning graphic.

Topic: Where NOT to Store Your Seed Phrase
Layout: Grid of prohibited storage methods

Prohibited (all with red X):
- Computer/laptop
- Phone/notes app
- Cloud storage
- Email/messaging
- Screenshots/photos
- Password managers (for seed phrase)

Style: Clear prohibition icons, red X on each.
Convey: Never store seed phrase digitally anywhere.
```

#### IMG-BTC104-CH08-003: Safe Storage Options
| Field | Value |
|-------|-------|
| **Name** | `safe-storage-options` |
| **Output** | `017.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Good options: fireproof safe, locked drawer, backup in different location |

**AI-Ready Prompt:**
```
Create a "do this" illustration.

Topic: Safe Seed Phrase Storage Options
Layout: Grid of recommended storage methods

Recommended (all with green checkmark):
- Fireproof safe at home
- Locked drawer/cabinet
- Metal backup plate
- Second copy at different location
- Sealed envelope with trusted person

Style: Clear recommendation icons, green checkmarks.
Convey: Physical, secure, redundant storage.
```

### Chapter 9: Receiving Bitcoin (needs 4-5 images)

#### IMG-BTC104-CH09-001: Receive Address QR
| Field | Value |
|-------|-------|
| **Name** | `receive-address-qr` |
| **Output** | `018.webp` |
| **Style** | Screenshot Mockup |
| **Priority** | High |
| **Description** | Example wallet screen showing QR code and address |

**AI-Ready Prompt:**
```
Create a wallet interface mockup.

Topic: Receiving Bitcoin - QR Code Display
Scene: What you see when requesting to receive

Visual elements:
- QR code (generic pattern)
- Long alphanumeric address below
- "Receive" or "Your Address" label
- Copy button indicator
- Clean mobile interface

Style: Clean wallet app mockup, generic design.
Convey: This is how you share your receiving address.
```

### Chapter 10: Security Best Practices (needs 4-5 images)

#### IMG-BTC104-CH10-001: Never Share Seed
| Field | Value |
|-------|-------|
| **Name** | `never-share-seed` |
| **Output** | `019.webp` |
| **Style** | Warning Illustration |
| **Priority** | High |
| **Description** | Warning: who NOT to share seed with - fake support, "experts" |

**AI-Ready Prompt:**
```
Create a strong warning illustration.

Topic: Never Share Your Seed Phrase With Anyone
Layout: List of people who might ask (all are scammers)

DO NOT SHARE WITH:
- "Support" representatives (headset icon + X)
- Bitcoin "experts" offering help (X)
- Anyone online (X)
- Even friends or family (X) - unless inheritance plan

Style: Strong warning format, red accents.
Convey: NO ONE legitimate will EVER ask for your seed.
```

#### IMG-BTC104-CH10-002: Scam Examples
| Field | Value |
|-------|-------|
| **Name** | `scam-examples` |
| **Output** | `020.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Common scams: fake support, "send to double", verify wallet emails |

**AI-Ready Prompt:**
```
Create a scam awareness infographic.

Topic: Common Bitcoin Scams to Avoid
Layout: Examples of scam tactics

Scam Types:
- Fake support messages asking for seed (chat bubble with warning)
- "Send 1 BTC, get 2 back" schemes (doubling arrow with X)
- Phishing emails about wallet "verification" (email with warning)
- Fake giveaways (gift with X)

Style: Warning infographic, clear scam indicators.
Convey: Recognize these common scam patterns.
```

### Chapter 11: When to Upgrade (needs 3-4 images)

#### IMG-BTC104-CH11-001: Upgrade Threshold
| Field | Value |
|-------|-------|
| **Name** | `upgrade-threshold` |
| **Output** | `021.webp` |
| **Style** | Decision Diagram |
| **Priority** | High |
| **Description** | When to get hardware wallet: amount > device cost, hundreds+, long-term |

**AI-Ready Prompt:**
```
Create a decision flow diagram.

Topic: When to Upgrade to Hardware Wallet
Layout: Decision tree or threshold diagram

Upgrade triggers:
- Amount exceeds device cost (value comparison)
- Holding hundreds of dollars or more
- Planning to hold long-term
- Want better security for any amount

Style: Clean decision flow, clear trigger points.
Convey: At certain points, hardware wallet becomes worth it.
```

### Chapter 12: Common Mistakes (needs 4-5 images)

#### IMG-BTC104-CH12-001: Mistake - Exchange Storage
| Field | Value |
|-------|-------|
| **Name** | `mistake-exchange` |
| **Output** | `022.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Bitcoin sitting on exchange vs own wallet |

**AI-Ready Prompt:**
```
Create a comparison illustration.

Topic: Common Mistake - Leaving Bitcoin on Exchanges
Layout: Wrong vs Right comparison

WRONG:
- Bitcoin sitting on exchange
- Exchange building with your Bitcoin inside
- Risk indicators (cracks, warning signs)

RIGHT:
- Bitcoin in your own wallet
- You holding the keys
- Security indicators (solid, protected)

Style: Clear wrong/right comparison.
Convey: Move your Bitcoin to your own wallet.
```

---

## BTC105 - How to Acquire Bitcoin

**Status:** 4 existing images | Gap: 52-66 images | Priority: High (largest course)

### Chapter 2: Prerequisites (needs 4-5 images)

#### IMG-BTC105-CH02-001: Not Your Keys Concept
| Field | Value |
|-------|-------|
| **Name** | `not-your-keys-concept` |
| **Output** | `005.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Visual of "Not your keys, not your coins" - exchange vs self-custody |

**AI-Ready Prompt:**
```
Create an educational illustration.

Concept: "Not Your Keys, Not Your Coins"
Scene: Visual explanation of custody difference

Visual approach:
- Split screen showing two scenarios
- LEFT: Exchange holds keys, user has claim only
- RIGHT: User holds keys, Bitcoin is truly theirs

Style: Clear comparison, educational tone.
Convey: Custody type fundamentally changes ownership.
```

#### IMG-BTC105-CH02-002: Hot vs Hardware Wallet
| Field | Value |
|-------|-------|
| **Name** | `hot-vs-hardware-wallet` |
| **Output** | `006.webp` |
| **Style** | Comparison Diagram |
| **Priority** | High |
| **Description** | Phone with hot wallet app vs physical hardware wallet device |

**AI-Ready Prompt:**
```
Create a comparison diagram.

Topic: Hot Wallet vs Hardware Wallet
Layout: Side-by-side comparison

LEFT (Hot Wallet):
- Mobile phone with wallet app
- Connected to internet indicator
- Good for: small amounts, spending
- Risk: online vulnerabilities

RIGHT (Hardware Wallet):
- Physical device (USB-like)
- Offline indicator
- Good for: larger amounts, savings
- Benefit: keys never online

Style: Clean side-by-side, clear differences.
Convey: Different tools for different purposes.
```

### Chapter 3: Key Questions (needs 4-5 images)

#### IMG-BTC105-CH03-001: Investment Types Comparison
| Field | Value |
|-------|-------|
| **Name** | `investment-types-comparison` |
| **Output** | `007.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Lump sum (single arrow) vs DCA (multiple small arrows over time) |

**AI-Ready Prompt:**
```
Create a comparison diagram.

Topic: Lump Sum vs Dollar Cost Averaging (DCA)
Layout: Two investment approaches visualized

LUMP SUM:
- Single large arrow/purchase
- All at once
- One price point

DCA:
- Multiple smaller arrows over time
- Regular intervals (weekly/monthly)
- Multiple price points, averaging out

Style: Clean visual comparison, time axis shown.
Convey: Two valid approaches to buying Bitcoin.
```

#### IMG-BTC105-CH03-002: Privacy Spectrum
| Field | Value |
|-------|-------|
| **Name** | `privacy-spectrum` |
| **Output** | `008.webp` |
| **Style** | Spectrum Diagram |
| **Priority** | High |
| **Description** | Spectrum from "Full KYC" to "Full Privacy" with methods placed along it |

**AI-Ready Prompt:**
```
Create a spectrum diagram.

Topic: Privacy Spectrum for Bitcoin Acquisition
Layout: Horizontal spectrum with methods placed

LEFT (Full KYC/Low Privacy):
- Major exchanges (most convenient)
- Full identity verification

CENTER (Partial Privacy):
- Some P2P platforms
- Limited KYC

RIGHT (High Privacy):
- No-KYC P2P trades
- Cash purchases
- Mining

Style: Gradient spectrum, methods placed along it.
Convey: Trade-off between convenience and privacy.
```

### Chapter 4: Understanding Trade-offs (needs 3-4 images)

#### IMG-BTC105-CH04-001: KYC Privacy Risk
| Field | Value |
|-------|-------|
| **Name** | `kyc-privacy-risk` |
| **Output** | `009.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | How KYC links identity to bitcoin addresses, enabling tracking |

**AI-Ready Prompt:**
```
Create a risk visualization diagram.

Topic: How KYC Creates Privacy Risk
Layout: Flow showing identity linkage

Flow:
- ID submitted to exchange
- ID linked to Bitcoin addresses
- Future transactions potentially trackable
- Blockchain analysis connecting activity

Style: Flow diagram showing linkage chain.
Convey: KYC creates permanent identity connection.
```

#### IMG-BTC105-CH04-002: Fees Comparison Table
| Field | Value |
|-------|-------|
| **Name** | `fees-comparison-table` |
| **Output** | `010.webp` |
| **Style** | Chart/Table |
| **Priority** | High |
| **Description** | Fee comparison: KYC Exchange (0.1-1%), DCA (1-2%), P2P (3-10%), ATM (5-15%) |

**AI-Ready Prompt:**
```
Create a fee comparison chart.

Topic: Acquisition Method Fee Comparison
Layout: Bar chart or table

Methods (Low to High Fees):
- KYC Exchange: 0.1-1% (lowest)
- DCA Service: 1-2%
- P2P Platforms: 3-10%
- Bitcoin ATM: 5-15% (highest)
- Earning: 0% (if applicable)

Style: Clean comparison, fee ranges clear.
Convey: Lower fees = more Bitcoin for your money.
```

### Chapter 5: Lump Sum KYC (needs 4-5 images)

#### IMG-BTC105-CH05-001: KYC Exchange Workflow
| Field | Value |
|-------|-------|
| **Name** | `kyc-exchange-workflow` |
| **Output** | `011.webp` |
| **Style** | Flowchart |
| **Priority** | High |
| **Description** | Steps: Create account > KYC > Deposit fiat > Buy > Withdraw to wallet |

**AI-Ready Prompt:**
```
Create a step-by-step flowchart.

Topic: Buying Bitcoin on a KYC Exchange
Layout: Horizontal flow with 5 steps

Steps:
1. Create Account (user icon)
2. Complete KYC (ID icon)
3. Deposit Fiat (bank transfer icon)
4. Buy Bitcoin (exchange icon)
5. Withdraw to Wallet (wallet icon, emphasized)

Style: Clean numbered flowchart, final step highlighted.
Convey: Don't forget step 5 - withdraw to your own wallet!
```

### Chapter 6: Lump Sum No-KYC (needs 4-5 images)

#### IMG-BTC105-CH06-001: P2P Escrow Flow
| Field | Value |
|-------|-------|
| **Name** | `p2p-escrow-flow` |
| **Output** | `012.webp` |
| **Style** | Flowchart |
| **Priority** | High |
| **Description** | P2P trade: Seller deposits > Buyer sends fiat > Seller confirms > BTC released |

**AI-Ready Prompt:**
```
Create a P2P trade flow diagram.

Topic: How P2P Escrow Trading Works
Layout: Circular or linear flow with 4 steps

Flow:
1. Seller locks BTC in escrow (lock icon)
2. Buyer sends fiat payment (money transfer)
3. Seller confirms receipt (checkmark)
4. BTC released to buyer (unlock icon)

Show escrow as central holding mechanism.

Style: Clean flow diagram, escrow role clear.
Convey: Escrow protects both buyer and seller.
```

### Chapter 7: DCA KYC (needs 2-3 images)

#### IMG-BTC105-CH07-001: DCA Volatility Smoothing
| Field | Value |
|-------|-------|
| **Name** | `dca-volatility-smoothing` |
| **Output** | `013.webp` |
| **Style** | Chart |
| **Priority** | High |
| **Description** | How DCA smooths out price volatility over time |

**AI-Ready Prompt:**
```
Create an educational chart.

Topic: How DCA Smooths Volatility
Layout: Price chart with DCA purchases marked

Show:
- Volatile price line (ups and downs)
- Regular DCA purchase points (dots at various prices)
- Average cost line (smooth, between highs and lows)
- Result: Cost basis smoothed out

Style: Clean price chart with DCA overlay.
Convey: Regular buying averages out the highs and lows.
```

### Chapter 9: Bitcoin ETFs (needs 4-5 images)

#### IMG-BTC105-CH09-001: ETF Concept Explained
| Field | Value |
|-------|-------|
| **Name** | `etf-concept-explained` |
| **Output** | `014.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | How ETF works: Investor buys shares > Fund holds bitcoin > Price tracking |

**AI-Ready Prompt:**
```
Create an educational diagram.

Topic: How Bitcoin ETFs Work
Layout: Flow diagram

Structure:
- INVESTOR: Buys ETF shares (stock certificate icon)
- ETF FUND: Holds actual Bitcoin (fund icon with BTC)
- TRACKING: Share price tracks Bitcoin price

Show the separation:
- Investor owns shares (paper)
- Fund owns Bitcoin (actual BTC)

Style: Clean institutional diagram.
Convey: ETFs are indirect Bitcoin exposure.
```

#### IMG-BTC105-CH09-002: ETF Not Bitcoin Warning
| Field | Value |
|-------|-------|
| **Name** | `etf-not-bitcoin-warning` |
| **Output** | `015.webp` |
| **Style** | Warning Illustration |
| **Priority** | High |
| **Description** | "ETFs are NOT Bitcoin" - paper exposure vs actual ownership |

**AI-Ready Prompt:**
```
Create a warning/clarification illustration.

Topic: ETFs Are NOT Bitcoin
Layout: Side-by-side comparison

ETF OWNERSHIP:
- Paper/certificate icon
- You own shares
- Fund controls Bitcoin
- Counterparty risk exists

BITCOIN OWNERSHIP:
- Bitcoin in your wallet
- You hold keys
- Direct ownership
- Self-custody

Style: Clear distinction, warning tone for ETF side.
Convey: ETFs give exposure, not actual Bitcoin ownership.
```

### Chapter 14: Securing Your Bitcoin (needs 4-5 images)

#### IMG-BTC105-CH14-001: Exchange to Wallet Flow
| Field | Value |
|-------|-------|
| **Name** | `exchange-to-wallet-flow` |
| **Output** | `016.webp` |
| **Style** | Flowchart |
| **Priority** | High |
| **Description** | Steps: Have wallet > Get address > Exchange withdraw > Verify > Confirm |

**AI-Ready Prompt:**
```
Create a withdrawal process flowchart.

Topic: Moving Bitcoin from Exchange to Your Wallet
Layout: Step-by-step flow

Steps:
1. Set up your wallet first (wallet icon)
2. Get your receiving address (QR/address)
3. Go to exchange withdrawal (exchange icon)
4. Paste address carefully (paste/verify icon)
5. Confirm and wait for confirmations (checkmark/clock)

Style: Clear numbered steps, emphasis on verification.
Convey: Careful, deliberate process for self-custody.
```

### Chapter 15: Taxes & Compliance (needs 4-5 images)

#### IMG-BTC105-CH15-001: Tax Events Diagram
| Field | Value |
|-------|-------|
| **Name** | `tax-events-diagram` |
| **Output** | `017.webp` |
| **Style** | Split Diagram |
| **Priority** | High |
| **Description** | Taxable: Selling/Trading/Spending vs Non-taxable: Buying/Transferring |

**AI-Ready Prompt:**
```
Create a tax event classification diagram.

Topic: What Creates a Taxable Event?
Layout: Two columns - Taxable vs Usually Not Taxable

TAXABLE EVENTS:
- Selling Bitcoin for fiat (cash out)
- Trading Bitcoin for other crypto
- Spending Bitcoin on goods/services
- Earning Bitcoin as income

USUALLY NOT TAXABLE:
- Buying Bitcoin
- Transferring between your own wallets
- Gifting (varies by amount/jurisdiction)
- Holding

Style: Clear two-column classification.
Note: Add disclaimer that tax rules vary by jurisdiction.
Convey: Know which actions trigger tax obligations.
```

### Chapter 17: Personal Strategy (needs 4-5 images)

#### IMG-BTC105-CH17-001: Decision Tree Full
| Field | Value |
|-------|-------|
| **Name** | `decision-tree-full` |
| **Output** | `018.webp` |
| **Style** | Flowchart |
| **Priority** | High |
| **Description** | Complete decision tree: Privacy? > Lump sum? > Hands-off? > Tech comfort? |

**AI-Ready Prompt:**
```
Create a decision tree flowchart.

Topic: Choosing Your Bitcoin Acquisition Strategy
Layout: Branching decision tree

Questions (in order):
1. Is privacy important? (Yes/No branches)
2. Do you prefer lump sum or DCA?
3. Want hands-off automation?
4. Technical comfort level?

Each branch leads to recommended methods.

Style: Clear decision tree, multiple paths to outcomes.
Convey: Answer these questions to find your best method.
```

---

## SCU102 - Financial Fraud, Scams & Online Security

**Status:** 25 existing images | Gap: 63-70 images | Priority: High (most comprehensive)

### Chapter 2: Understanding Financial Fraud (needs 2-3 images)

#### IMG-SCU102-CH02-001: Fraud Landscape
| Field | Value |
|-------|-------|
| **Name** | `fraud-landscape` |
| **Output** | `026.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Overview of fraud types in crypto ecosystem |

**AI-Ready Prompt:**
```
Create an overview diagram.

Topic: Types of Fraud in the Crypto Space
Layout: Central hub with connected fraud types

Categories radiating from center:
- Ponzi/Pyramid Schemes
- Pump & Dump
- Fake Giveaways
- Shitcoins/Airdrops
- Phishing
- Dishonest Influencers
- Fake Exchanges

Style: Hub and spoke diagram, warning colors.
Convey: Many fraud types exist - awareness is key.
```

### Chapter 3: Pyramid & Ponzi Schemes (needs 3-4 images)

#### IMG-SCU102-CH03-001: Ponzi Mechanics
| Field | Value |
|-------|-------|
| **Name** | `ponzi-mechanics` |
| **Output** | `027.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | How Ponzi works: new investor money paying old investors |

**AI-Ready Prompt:**
```
Create a Ponzi scheme mechanics diagram.

Topic: How Ponzi Schemes Actually Work
Layout: Flow showing money movement

Structure:
- New investors put money in
- Their money goes to earlier investors as "returns"
- No actual investment/profit
- Eventually collapses when new money stops

Visual: Money flowing from bottom (new) to top (old), not from legitimate source.

Style: Clear expose of the fraud mechanism.
Convey: "Returns" come from other victims, not profits.
```

### Chapter 6: Shitcoins & Airdrops (needs 4-5 images)

#### IMG-SCU102-CH06-001: Airdrop Scam Flow
| Field | Value |
|-------|-------|
| **Name** | `airdrop-scam-flow` |
| **Output** | `028.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | How malicious airdrops work to steal funds |

**AI-Ready Prompt:**
```
Create a scam flow diagram.

Topic: How Malicious Airdrops Work
Layout: Step-by-step trap

Flow:
1. Random tokens appear in your wallet
2. You're curious, try to "claim" or sell them
3. Malicious contract asks for permissions
4. If you approve, your real assets get drained

Style: Warning diagram, danger progression shown.
Convey: Unsolicited tokens are often traps.
```

### Chapter 7: Phishing & Identity Theft (needs 4-5 images)

#### IMG-SCU102-CH07-001: Phishing Attack Types
| Field | Value |
|-------|-------|
| **Name** | `phishing-attack-types` |
| **Output** | `029.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Different phishing vectors: email, social media, phone, mail |

**AI-Ready Prompt:**
```
Create a phishing vectors diagram.

Topic: Ways Phishing Attacks Reach You
Layout: Central target (victim) with attack vectors

Attack Vectors:
- Email phishing (envelope icon)
- Social media messages (chat icon)
- Phone calls (vishing) (phone icon)
- SMS/text (smishing) (message icon)
- Fake websites (browser icon)

Style: Threat diagram, vectors pointing at victim.
Convey: Phishing comes through many channels.
```

#### IMG-SCU102-CH07-002: Private Key Warning
| Field | Value |
|-------|-------|
| **Name** | `private-key-warning` |
| **Output** | `030.webp` |
| **Style** | Warning Graphic |
| **Priority** | High |
| **Description** | Strong warning: never share private keys/seed phrases |

**AI-Ready Prompt:**
```
Create a strong warning graphic.

Topic: NEVER Share Your Private Keys or Seed Phrase
Layout: Prominent warning message

Elements:
- Large warning symbol
- "NEVER SHARE" message (visual, not text)
- Icons for what not to share: key icon, word list icon
- Red/danger coloring

Style: Maximum impact warning graphic.
Convey: This is the #1 rule - never share these.
```

### Chapter 10: Red Flags & Verification (needs 4-5 images)

#### IMG-SCU102-CH10-001: Master Red Flags
| Field | Value |
|-------|-------|
| **Name** | `master-red-flags` |
| **Output** | `031.webp` |
| **Style** | Infographic |
| **Priority** | High |
| **Description** | Comprehensive summary of all red flags from the course |

**AI-Ready Prompt:**
```
Create a comprehensive red flags infographic.

Topic: Master List of Crypto Scam Red Flags
Layout: Organized checklist with icons

Red Flags Categories:

PROMISES:
- Guaranteed returns
- "Risk-free" investment
- "Get rich quick"

PRESSURE:
- Limited time offers
- FOMO inducement
- "Act now" urgency

REQUESTS:
- Asking for seed phrase
- "Send to verify"
- Upfront fees

SOURCES:
- Unsolicited contact
- Celebrity endorsements
- Anonymous teams

Style: Clean, scannable checklist format.
Convey: Recognize these patterns to stay safe.
```

### Chapter 11: Why Cybersecurity Matters (needs 4-5 images)

#### IMG-SCU102-CH11-001: You Are Your Own Bank
| Field | Value |
|-------|-------|
| **Name** | `bitcoin-self-custody` |
| **Output** | `032.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | "You are your own bank" concept and responsibilities |

**AI-Ready Prompt:**
```
Create a conceptual illustration.

Concept: "You Are Your Own Bank"
Scene: Individual taking on bank responsibilities

Visual elements:
- Person standing confidently
- Bank vault/safe they control
- Key in their hand
- Responsibility indicators: security, backups, access control

Style: Empowering but serious illustration.
Convey: Self-custody means self-responsibility.
```

### Chapter 13: Password Security (needs 3-4 images)

#### IMG-SCU102-CH13-001: Password Reuse Danger
| Field | Value |
|-------|-------|
| **Name** | `password-reuse-danger` |
| **Output** | `033.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Domino effect when one reused password is compromised |

**AI-Ready Prompt:**
```
Create a domino effect diagram.

Topic: The Danger of Password Reuse
Layout: Domino chain falling

Scenario:
- One site gets breached (first domino falls)
- Same password used everywhere
- All accounts become compromised (dominoes falling)
- Bank, email, crypto, social - all down

Style: Clear cause-and-effect visualization.
Convey: One compromised password can compromise everything.
```

### Chapter 16: Security Progression (needs 4-5 images)

#### IMG-SCU102-CH16-001: Security Progression Ladder
| Field | Value |
|-------|-------|
| **Name** | `security-progression-ladder` |
| **Output** | `034.webp` |
| **Style** | Diagram |
| **Priority** | High |
| **Description** | Visual ladder from beginner to advanced security |

**AI-Ready Prompt:**
```
Create a security progression diagram.

Topic: Security Improvement Steps (Beginner to Advanced)
Layout: Ladder or staircase climbing up

Levels (bottom to top):
1. BASICS: Strong passwords, password manager
2. ESSENTIAL: 2FA on all accounts, software updates
3. INTERMEDIATE: Hardware wallet, encrypted backups
4. ADVANCED: Hardware 2FA keys, air-gapped devices
5. EXPERT: Multi-sig, distributed backups

Style: Climbing progression, each step builds on previous.
Convey: Security is a journey, start simple and improve.
```

### Chapter 21: Confidentiality & Discretion (needs 4-5 images)

#### IMG-SCU102-CH21-001: Discretion Importance
| Field | Value |
|-------|-------|
| **Name** | `discretion-importance` |
| **Output** | `035.webp` |
| **Style** | Illustration |
| **Priority** | High |
| **Description** | Why keeping Bitcoin holdings private matters |

**AI-Ready Prompt:**
```
Create an educational illustration.

Topic: The Importance of Discretion About Bitcoin Holdings
Scene: Contrast between discrete and indiscrete behavior

Visual approach:
- WRONG: Person announcing their Bitcoin (megaphone, social media)
- RIGHT: Person keeping holdings private (quiet, secure)

Show risks of disclosure: target on back, unwanted attention.

Style: Clear contrast illustration.
Convey: Privacy is part of security.
```

### Chapter 23: Trading vs Investing vs Holding (needs 4-5 images)

#### IMG-SCU102-CH23-001: Trading Warning
| Field | Value |
|-------|-------|
| **Name** | `trading-warning` |
| **Output** | `036.webp` |
| **Style** | Warning Graphic |
| **Priority** | High |
| **Description** | Strong warning that most traders lose money |

**AI-Ready Prompt:**
```
Create a warning infographic.

Topic: Most Traders Lose Money
Layout: Strong warning with statistics concept

Visual elements:
- Large warning indicator
- Statistic visualization (90%+ lose)
- Trader stress/loss imagery
- Contrast with long-term holder (calm)

Style: Serious warning format.
Convey: Trading is extremely difficult; most people lose.
```

---

## Web Interface (HTML)

The following HTML code can be used to create a simple web interface for browsing and tracking image generation progress. Save as a standalone HTML file and open in any browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BTC102 Split - Image Generator</title>
    <style>
        :root {
            --btc-orange: #F7931A;
            --dark-gray: #4D4D4D;
            --light-gray: #F5F5F5;
            --teal: #00D4AA;
            --red: #E53935;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--light-gray);
            color: var(--dark-gray);
            line-height: 1.6;
        }

        header {
            background: var(--btc-orange);
            color: white;
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        header h1 {
            font-size: 1.5rem;
            font-weight: 600;
        }

        .controls {
            display: flex;
            gap: 1rem;
            padding: 1rem 2rem;
            background: white;
            border-bottom: 1px solid #ddd;
            flex-wrap: wrap;
            align-items: center;
        }

        .controls select, .controls input {
            padding: 0.5rem 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .progress-bar {
            flex: 1;
            min-width: 200px;
            background: #eee;
            border-radius: 4px;
            height: 24px;
            overflow: hidden;
            position: relative;
        }

        .progress-bar .fill {
            background: var(--teal);
            height: 100%;
            transition: width 0.3s;
        }

        .progress-bar .text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 0.8rem;
            font-weight: 600;
        }

        main {
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 1.5rem;
        }

        .card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .card-header {
            background: var(--dark-gray);
            color: white;
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
        }

        .card-header .course {
            font-weight: 600;
            color: var(--btc-orange);
        }

        .card-body {
            padding: 1rem;
        }

        .card-body h3 {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: var(--dark-gray);
        }

        .meta {
            display: flex;
            gap: 1rem;
            margin-bottom: 0.75rem;
            font-size: 0.85rem;
        }

        .meta span {
            background: var(--light-gray);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
        }

        .meta .priority-high { background: #ffebee; color: var(--red); }
        .meta .priority-medium { background: #fff8e1; color: #f57c00; }
        .meta .priority-low { background: #e8f5e9; color: #388e3c; }

        .description {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }

        .card-actions {
            display: flex;
            gap: 0.5rem;
            padding: 1rem;
            border-top: 1px solid #eee;
            flex-wrap: wrap;
        }

        button {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: background 0.2s;
        }

        .btn-primary {
            background: var(--btc-orange);
            color: white;
        }

        .btn-primary:hover {
            background: #e8851a;
        }

        .btn-secondary {
            background: var(--light-gray);
            color: var(--dark-gray);
        }

        .btn-secondary:hover {
            background: #e0e0e0;
        }

        .btn-success {
            background: var(--teal);
            color: white;
        }

        .btn-success:hover {
            background: #00b894;
        }

        .completed .card-body {
            opacity: 0.6;
        }

        .completed .card-header {
            background: var(--teal);
        }

        /* Modal for prompt */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 200;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            border-radius: 8px;
            max-width: 700px;
            width: 90%;
            max-height: 80vh;
            overflow: auto;
        }

        .modal-header {
            background: var(--btc-orange);
            color: white;
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .modal-body {
            padding: 1.5rem;
        }

        .modal-body pre {
            background: var(--light-gray);
            padding: 1rem;
            border-radius: 4px;
            overflow-x: auto;
            font-size: 0.85rem;
            line-height: 1.5;
            white-space: pre-wrap;
        }

        .modal-footer {
            padding: 1rem;
            border-top: 1px solid #eee;
            display: flex;
            gap: 0.5rem;
            justify-content: flex-end;
        }

        .close-btn {
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
        }

        .output-info {
            background: #e3f2fd;
            padding: 0.75rem 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .output-info code {
            background: white;
            padding: 0.25rem 0.5rem;
            border-radius: 3px;
            font-family: monospace;
        }

        @media (max-width: 768px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .controls {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>BTC102 Split - Image Generator</h1>
    </header>

    <div class="controls">
        <select id="courseFilter">
            <option value="all">All Courses</option>
            <option value="btc102v2">BTC102v2 - Hub</option>
            <option value="btc103">BTC103 - Why Bitcoin</option>
            <option value="biz102">BIZ102 - Industry</option>
            <option value="sov102">SOV102 - Inheritance</option>
            <option value="btc104">BTC104 - Security</option>
            <option value="btc105">BTC105 - Acquisition</option>
            <option value="scu102">SCU102 - Fraud</option>
        </select>

        <select id="statusFilter">
            <option value="all">All Status</option>
            <option value="pending">Pending</option>
            <option value="completed">Completed</option>
        </select>

        <select id="priorityFilter">
            <option value="all">All Priorities</option>
            <option value="high">High Priority</option>
            <option value="medium">Medium Priority</option>
            <option value="low">Low Priority</option>
        </select>

        <div class="progress-bar">
            <div class="fill" id="progressFill" style="width: 0%"></div>
            <span class="text" id="progressText">0/0 (0%)</span>
        </div>
    </div>

    <main>
        <div class="cards" id="cardContainer">
            <!-- Cards will be dynamically inserted here -->
        </div>
    </main>

    <!-- Prompt Modal -->
    <div class="modal" id="promptModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalTitle">Prompt</h3>
                <button class="close-btn" onclick="closeModal()">&times;</button>
            </div>
            <div class="modal-body">
                <div class="output-info" id="outputInfo"></div>
                <pre id="promptContent"></pre>
            </div>
            <div class="modal-footer">
                <button class="btn-secondary" onclick="closeModal()">Close</button>
                <button class="btn-primary" onclick="copyPrompt()">Copy to Clipboard</button>
            </div>
        </div>
    </div>

    <script>
        // Image specifications data (sample - in production, load from JSON)
        const imageSpecs = [
            // BTC102v2
            {
                id: 'btc102v2-ch03-001',
                course: 'btc102v2',
                chapter: 'Ch 3: Understanding Your Profile',
                name: 'user-profiles-overview',
                output: '005.webp',
                style: 'Diagram',
                priority: 'high',
                description: 'Quadrant diagram showing four Bitcoin user profiles (Hodler, Stacker, Active User, Privacy-Focused)',
                prompt: `Create an educational quadrant diagram for a Bitcoin course.

Topic: Bitcoin User Profiles
Layout: 2x2 grid/quadrant with four distinct user types

Quadrants:
1. TOP-LEFT: "Hodler" - Icon of person with locked vault, long-term focus symbol
2. TOP-RIGHT: "Stacker" - Icon of person with stacking blocks/coins, DCA symbol
3. BOTTOM-LEFT: "Active User" - Icon of person with mobile phone, Lightning bolt
4. BOTTOM-RIGHT: "Privacy-Focused" - Icon of person with shield/mask, privacy symbol

Style: Flat design, Bitcoin orange (#F7931A) accents, white background, clean icons.
Each quadrant should be visually distinct but harmonious.
No text labels in the image.`,
                status: 'pending'
            },
            {
                id: 'btc102v2-ch04-001',
                course: 'btc102v2',
                chapter: 'Ch 4: Recommended Course Sequences',
                name: 'path-a-cautious-beginner',
                output: '010.webp',
                style: 'Flowchart',
                priority: 'high',
                description: 'Flowchart showing Path A: SCU102 -> BTC103 -> BTC105 -> BTC104 -> SOV102',
                prompt: `Create an educational flowchart for a Bitcoin learning path.

Topic: "Path A: Cautious Beginner" - Recommended course sequence
Layout: Horizontal flow from left to right

Sequence (5 boxes connected by arrows):
1. SCU102 (Security first) - Shield icon
2. BTC103 (Why Bitcoin) - Question mark/lightbulb icon
3. BTC105 (Acquire) - Plus/add icon
4. BTC104 (Secure) - Lock icon
5. SOV102 (Inheritance) - Family/document icon

Style: Clean flowchart, each box a different shade, arrows connecting them.
Color: Use Bitcoin orange for the path arrows, gray boxes with icons.`,
                status: 'pending'
            },
            // BTC103
            {
                id: 'btc103-ch04-001',
                course: 'btc103',
                chapter: 'Ch 4: Monetary Properties',
                name: 'bitcoin-supply-curve',
                output: '025.webp',
                style: 'Chart',
                priority: 'high',
                description: 'Bitcoin supply schedule from 2009-2140 with halving events',
                prompt: `Create an educational chart for Bitcoin monetary policy.

Topic: Bitcoin Supply Schedule (2009-2140)
Type: Line/area chart with milestones

Elements:
- X-axis: Years from 2009 to 2140
- Y-axis: Total Bitcoin supply (0 to 21 million)
- Curve showing diminishing issuance (asymptotic approach to 21M)
- Halving events marked (2012, 2016, 2020, 2024, 2028, etc.)
- 21 million cap line at top

Style: Clean data visualization, Bitcoin orange for the supply curve.
Emphasize: Predictability, scarcity, halving events.`,
                status: 'pending'
            },
            // Add more specs here...
        ];

        // Load status from localStorage
        function loadStatus() {
            const saved = localStorage.getItem('imageGenStatus');
            if (saved) {
                const statuses = JSON.parse(saved);
                imageSpecs.forEach(spec => {
                    if (statuses[spec.id]) {
                        spec.status = statuses[spec.id];
                    }
                });
            }
        }

        // Save status to localStorage
        function saveStatus() {
            const statuses = {};
            imageSpecs.forEach(spec => {
                statuses[spec.id] = spec.status;
            });
            localStorage.setItem('imageGenStatus', JSON.stringify(statuses));
        }

        // Render cards
        function renderCards() {
            const container = document.getElementById('cardContainer');
            const courseFilter = document.getElementById('courseFilter').value;
            const statusFilter = document.getElementById('statusFilter').value;
            const priorityFilter = document.getElementById('priorityFilter').value;

            const filtered = imageSpecs.filter(spec => {
                if (courseFilter !== 'all' && spec.course !== courseFilter) return false;
                if (statusFilter !== 'all' && spec.status !== statusFilter) return false;
                if (priorityFilter !== 'all' && spec.priority !== priorityFilter) return false;
                return true;
            });

            container.innerHTML = filtered.map(spec => `
                <div class="card ${spec.status === 'completed' ? 'completed' : ''}" data-id="${spec.id}">
                    <div class="card-header">
                        <span class="course">${spec.course.toUpperCase()}</span> > ${spec.chapter}
                    </div>
                    <div class="card-body">
                        <h3>${spec.name}</h3>
                        <div class="meta">
                            <span>${spec.style}</span>
                            <span class="priority-${spec.priority}">${spec.priority.charAt(0).toUpperCase() + spec.priority.slice(1)} Priority</span>
                            <span>${spec.output}</span>
                        </div>
                        <p class="description">${spec.description}</p>
                    </div>
                    <div class="card-actions">
                        <button class="btn-primary" onclick="showPrompt('${spec.id}')">View Prompt</button>
                        <button class="btn-${spec.status === 'completed' ? 'secondary' : 'success'}" onclick="toggleStatus('${spec.id}')">
                            ${spec.status === 'completed' ? 'Mark Pending' : 'Mark Complete'}
                        </button>
                    </div>
                </div>
            `).join('');

            updateProgress();
        }

        // Update progress bar
        function updateProgress() {
            const total = imageSpecs.length;
            const completed = imageSpecs.filter(s => s.status === 'completed').length;
            const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

            document.getElementById('progressFill').style.width = percent + '%';
            document.getElementById('progressText').textContent = `${completed}/${total} (${percent}%)`;
        }

        // Show prompt modal
        function showPrompt(id) {
            const spec = imageSpecs.find(s => s.id === id);
            if (!spec) return;

            document.getElementById('modalTitle').textContent = spec.name;
            document.getElementById('outputInfo').innerHTML = `
                <strong>Output:</strong> <code>${spec.output}</code> in
                <code>courses/${spec.course}/assets/en/</code>
            `;
            document.getElementById('promptContent').textContent = spec.prompt;
            document.getElementById('promptModal').classList.add('active');
        }

        // Close modal
        function closeModal() {
            document.getElementById('promptModal').classList.remove('active');
        }

        // Copy prompt to clipboard
        function copyPrompt() {
            const prompt = document.getElementById('promptContent').textContent;
            navigator.clipboard.writeText(prompt).then(() => {
                alert('Prompt copied to clipboard!');
            });
        }

        // Toggle completion status
        function toggleStatus(id) {
            const spec = imageSpecs.find(s => s.id === id);
            if (!spec) return;

            spec.status = spec.status === 'completed' ? 'pending' : 'completed';
            saveStatus();
            renderCards();
        }

        // Initialize
        loadStatus();
        renderCards();

        // Event listeners for filters
        document.getElementById('courseFilter').addEventListener('change', renderCards);
        document.getElementById('statusFilter').addEventListener('change', renderCards);
        document.getElementById('priorityFilter').addEventListener('change', renderCards);

        // Close modal on outside click
        document.getElementById('promptModal').addEventListener('click', function(e) {
            if (e.target === this) closeModal();
        });
    </script>
</body>
</html>
```

---

## Progress Tracking

### Overall Progress

| Course | Total Specs | Completed | Remaining |
|--------|-------------|-----------|-----------|
| BTC102v2 | 8 | 0 | 8 |
| BTC103 | 6 | 0 | 6 |
| BIZ102 | 24 | 0 | 24 |
| SOV102 | 21 | 0 | 21 |
| BTC104 | 39 | 0 | 39 |
| BTC105 | 59 | 0 | 59 |
| SCU102 | 67 | 0 | 67 |
| **TOTAL** | **~220** | **0** | **~220** |

### Session Log

| Date | Course | Images Created | Notes |
|------|--------|----------------|-------|
| | | | |

---

## Appendix: Quick Reference

### File Naming Convention
- Format: `###.webp` (e.g., `001.webp`, `025.webp`)
- Sequence continues from existing images in each course

### Folder Paths
```
courses/btc102v2/assets/en/###.webp
courses/btc103-new/assets/en/###.webp
courses/biz102-new/assets/en/###.webp
courses/sov102/assets/en/###.webp
courses/btc104/assets/en/###.webp
courses/btc105/assets/en/###.webp
courses/scu102-new/assets/en/###.webp
```

### WebP Conversion
If your AI tool outputs PNG/JPG, convert to WebP:
- Online: squoosh.app, cloudconvert.com
- CLI: `cwebp input.png -o output.webp -q 85`
- Python: Use Pillow library

### Quality Checklist
Before adding an image:
- [ ] Format is WebP
- [ ] Dimensions under 1920x1080
- [ ] File size under 500KB
- [ ] No text that needs translation
- [ ] Follows color palette
- [ ] Matches flat/educational style
- [ ] Named correctly (###.webp)
- [ ] Placed in correct course folder
