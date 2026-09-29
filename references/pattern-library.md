# Pattern Library: research notes behind the bearing skill

Field notes on the reference systems the skill draws from. Each entry records
what the design actually does, not what its marketing claims, plus the
transferable move and what not to steal.

Cite by slug: `bearing:linear`, `bearing:vignelli-nyc`. Every entry was checked
on the date in the index; sites change, so re-check before leaning on one.

## Index

| slug | source | medium | temp | density | risk |
| --- | --- | --- | --- | --- | --- |
| `carbon` | Carbon (IBM) | web | clinical | dense | low |
| `atlassian` | Atlassian Design System | web | neutral | dense | low |
| `shadcn` | shadcn/ui | web | clinical | mid | medium |
| `tailwind-plus` | Tailwind Plus | web | neutral | airy | high |
| `untitled-ui` | Untitled UI | web | clinical | mid | high |
| `wise` | Wise | web | warm | airy | medium |
| `radix` | Radix Primitives | web | neutral | mid | low |
| `base` | Base (Uber) | web | clinical | dense | medium |
| `linear` | linear.app | web | clinical | dense | high |
| `cursor` | cursor.com | web | clinical | mid | medium |
| `autumn` | useautumn.com | web | warm | airy | medium |
| `morphic` | morphic.com | web | neutral | dense | medium |
| `vercel` | vercel.com/home | web | clinical | dense | high |
| `jib-jamt` | jib.design / ja.mt | web | neutral | airy | medium |
| `interfere` | interfere.com | web | clinical | dense | medium |
| `aside` | aside.com | web | neutral | dense | medium |
| `family` | family.co | web | warm | airy | high |
| `xai` | x.ai | web | clinical | airy | high |
| `stripe` | stripe.com | web | neutral | dense | high |
| `new-industrials` | thenewindustrials.com | web | neutral | airy | low |
| `sapphic-index` | sapphicindex.com | web | neutral | airy | low |
| `neue-montreal` | neuemontreal.com | web | warm | airy | medium |
| `monolog` | bymonolog.com | web | neutral | airy | medium |
| `khroma` | khroma.co | web | clinical | mid | low |
| `re-do-newvalley` | re-do.studio / newvalleylabs.com | web | warm | airy | low |
| `vignelli-nyc` | Vignelli / NYC Transit standard | print | clinical | dense | low |
| `rams-braun` | Dieter Rams / Braun | industrial | clinical | airy | medium |
| `swiss-grid` | Muller-Brockmann, grid systems | print | clinical | dense | low |
| `tui` | lazygit, btop, htop | terminal | clinical | dense | low |
| `teenage-engineering` | Teenage Engineering | industrial | neutral | airy | medium |

Risk is how likely the move is to read as a clone. `high` means take
the move and change at least one other variable.

---

Field notes on the reference systems and sites the skill draws from. Each entry
records what the design actually does (not marketing claims) and the transferable
move. Use this file to ground direction choices in specifics; cite entries when
explaining a direction to the user.

---

## Part 1: Design systems

### Carbon (IBM): preview.carbondesignsystem.com {#carbon}
`clinical / dense` · medium: web · risk: low · checked: 2026-09-29

- The most rigorous token system in the list: everything derives from a 2x grid.
  Spacing steps are literal multiples; components snap to column grids.
- Type: IBM Plex family with a fixed modular scale; display sizes stay modest ,
  hierarchy comes from weight and position, not size explosions.
- Color is role-based, not decorative: `interactive`, `focus`, `danger`,
  `success`, `warning` tokens. Accent color appears almost exclusively on
  interactive elements. Blue (#0f62fe) is a control, not a mood.
- Layer vocabulary: explicit surface tokens (`layer-01/02/03`) for nesting depth,
  so elevation is expressed as background shifts, not shadows.
- Transferable move: **color = state, structure = depth.** If your accent shows
  up on non-interactive elements, you're decorating, not designing.
- **Do not take:** the blue as decoration. take the role tokens, not the IBM look.

### Atlassian Design System {#atlassian}
`neutral / dense` · medium: web · risk: low · checked: 2026-09-29

- Three stated pillars: clarity, depth, personality, personality delivered
  through illustration and microcopy, never through noisy layout.
- Dense-product discipline: tight 8px-ish spacing scale, small type ramp, borders
  before shadows. Feels "busy" only because information density is high, not
  because ornament is.
- Illustration system has one hand (consistent line weight, palette-limited) so
  dozens of images still read as one brand.
- Transferable move: **personality lives in illustration + voice**, freeing the
  layout chrome to stay quiet and predictable.
- **Do not take:** the product chrome. take the discipline, not the blue.

### shadcn/ui {#shadcn}
`clinical / mid` · medium: web · risk: medium · checked: 2026-09-29

- Not a component library, copy-paste ownership. Styling is semantic tokens
  (`--background`, `--muted-foreground`, `--primary`) over Radix primitives.
- Near-monochrome by default: grays carry hierarchy, one accent max. Radius and
  border width do most of the stylistic work; swap radius → new personality.
- Transferable move: **design tokens as the entire brand surface.** A whole
  product's look can legitimately be "gray scale + radius choice + one accent."
- **Do not take:** the default tokens unmodified. everyone already has them.

### Tailwind Plus (formerly Tailwind UI) {#tailwind-plus}
`neutral / airy` · medium: web · risk: high · checked: 2026-09-29

- The commercial standard for "tasteful SaaS": generous whitespace, 3-column
  features done well, sticky translucent navs, subtle gradients behind heroes.
- Its sections work because of consistent internal padding rhythm and strict
  type ramp, the templates all share bones even when skins differ.
- Risk: it IS the default SaaS look now. Steal its spacing discipline, not its
  section inventory.
- Transferable move: **vertical rhythm consistency**, identical block padding
  per band makes even long pages feel calm.
- **Do not take:** the section inventory. it is the default SaaS grammar now.

### Untitled UI {#untitled-ui}
`clinical / mid` · medium: web · risk: high · checked: 2026-09-29

- The most "perfect default" of the list: Inter, gray-900-on-white, rounded-lg,
  blue primary. Immaculate and anonymous in equal measure.
- Useful for its component anatomy: form field proportions, button height steps,
  icon sizing (20px inside 40px controls).
- Transferable move: **component metrics** (control heights in 4px steps, icon
  inset ratios). Do not inherit its aesthetic wholesale, that's the slop baseline.
- **Do not take:** the palette and type. that combination is the slop baseline.

### Wise design direction (wise.design) {#wise}
`warm / airy` · medium: web · risk: medium · checked: 2026-09-29

- Bright flat color fields as section backgrounds, whole bands of saturated
  green/yellow, no gradients, no glass.
- Chunky humanist type at very large sizes; numbers and currency are hero
  content. Currency symbols get typographic celebration.
- Illustration is flat, diverse, and slightly awkward on purpose, anti-corporate.
- Transferable move: **color fields as architecture.** A background can be a
  solid brand color spanning full viewport height; contrast does the separating.
- **Do not take:** the green. the move is the field, not the hue.

### Radix Primitives (+ Radix Themes) {#radix}
`neutral / mid` · medium: web · risk: low · checked: 2026-09-29

- Headless accessibility-first primitives: focus management, aria wiring, unstyled
  cores. Proof that behavior and style are separable layers.
- Transferable move: **interaction correctness as an aesthetic value.** Keyboard
  focus rings, escape-to-close, and announced states are part of visual taste.
- **Do not take:** nothing visual. it is a behaviour reference.

### Base (Uber) {#base}
`clinical / dense` · medium: web · risk: medium · checked: 2026-09-29

- Motion and data-viz heavyweights: standardized duration/easing curves across
  every animated element; charting grammar with semantic ramps.
- Strict type and spacing scales tuned for dense operational products (maps,
  dashboards).
- Transferable move: **one motion vocabulary**, same easing curve everywhere,
  durations binned into 2–3 tiers, nothing springs arbitrarily.
- **Do not take:** the data-table weight without the density to justify it.

---

## Part 2: Product/company sites

### linear.app {#linear}
`clinical / dense` · medium: web · risk: high · checked: 2026-09-29

- Dark neutral canvas (#08090a-ish) where surfaces step by tiny luminance deltas;
  hairline borders (`1px rgba(255,255,255,.08)`); almost no pure black or white.
- Single restrained accent (violet) used at <5% coverage; status colors do the
  rest. Glow used only on the product hero image, light representing the screen.
- Signature content pattern: **the product's own UI as the hero asset**, rendered
  pixel-perfect with real data. Numbered exhibits ("FIG 0.2", "1.0 Intake") give
  the page documentary authority.
- Typography: tight-tracking grotesque, mid-size headings, dense but airy lists.
- Transferable moves: luminance-stepped dark surfaces; numbered figure captions;
  screenshots-with-real-data instead of illustrations.
- **Do not take:** the violet. it is the most-copied accent in the category.

### cursor.com {#cursor}
`clinical / mid` · medium: web · risk: medium · checked: 2026-09-29

- Monochrome, near-brutalist restraint: white/black, mono accents for code, big
  plain statements. The editor itself (with AI interaction moments) carries all
  color.
- Copy does persuasion ("Built to make you extraordinarily productive"), design
  stays out of the way.
- Transferable move: **let the tool's output (code/diffs) be the visual.**
- **Do not take:** monochrome brutalism as a costume for a non-technical product.

### useautumn.com {#autumn}
`warm / airy` · medium: web · risk: medium · checked: 2026-09-29

- Warm cream paper background, burnt-orange accent, serif-leaning headings on a
  dev-infrastructure product, deliberately anti-"dark developer tool".
- Playful diagrams and honest docs-like content blocks; pricing explained like a
  friend, not a matrix.
- Transferable move: **warmth as differentiation in a cold category.** A devtool
  doesn't have to be near-black.
- **Do not take:** cream plus serif plus burnt orange as a kit. it is a decision.

### morphic.com {#morphic}
`neutral / dense` · medium: web · risk: medium · checked: 2026-09-29

- Dark cinematic canvas, media-first: generated video/images ARE the layout.
  Minimal chrome, huge media cards, workflow cards with thumbnail + verb.
- Transferable move: **content-is-interface**, when the product makes media,
  the page is a gallery of the media.
- **Do not take:** huge media cards with no media. empty frames read as unfinished.

### vercel.com/home {#vercel}
`clinical / dense` · medium: web · risk: high · checked: 2026-09-29

- Black/white extremity with the occasional spectral gradient reserved for the
  triangle/logo moment. Grid lines and technical annotations (deployment URLs,
  timestamps) as decoration-that-informs.
- Transferable move: **one branded gradient moment per page**, spent exactly
  once, plus engineering-metadata-as-texture.
- **Do not take:** the triangle gradient. it is spent, and it works once.

### jib.design / ja.mt (Jace) {#jib-jamt}
`neutral / airy` · medium: web · risk: medium · checked: 2026-09-29

- Designer-portfolio minimalism: single column, huge index lists, monospace
  metadata, custom icons as the only imagery. Personality via writing voice.
- Transferable move: **the index list as hero**, a plain `<ul>` set in good type
  beats any card grid for showing work.
- **Do not take:** huge type with nothing behind it. the list has to be real work.

### interfere.com {#interfere}
`clinical / dense` · medium: web · risk: medium · checked: 2026-09-29

- Linear-school dark precision applied to observability: dense fake-product UI
  panels with plausible incident data, timelines, code diffs. Every claim paired
  with an artifact.
- Numbered 01/02/03 narrative where each number owns a full-width band with
  alternating artifact placement.
- Transferable move: **evidence-per-claim**, no feature statement without an
  adjacent concrete artifact (log line, timeline, diff).
- **Do not take:** fabricated incident data. plausible is the requirement.

### aside.com {#aside}
`neutral / dense` · medium: web · risk: medium · checked: 2026-09-29

- Soft dark UI with warm highlights; browser-window mockups showing agent tasks
  mid-progress ("Working for 3m 46s"). Benchmark tables presented as plain bars.
- Transferable move: **process visible**, show the agent/product working, not
  just results; live-status textures create credibility.
- **Do not take:** fake progress states. if it is not live, do not fake it.

### family.co {#family}
`warm / airy` · medium: web · risk: high · checked: 2026-09-29

- The delight benchmark: enormous rounded forms, friendly gradients, emoji as
  iconography, springy microinteractions on everything (chart scrubbing, card
  tilts, count-ups).
- Sections titled with single adjectives ("Easy", "Fun", "Seamless"), one-word
  headers, short proofs under each.
- Crypto made approachable through toy-like warmth: the opposite strategy of
  every fintech peer.
- Transferable moves: adjective-as-section-title; **delight budget**, many tiny
  springy interactions instead of one big animation.
- **Do not take:** gradient blobs and emoji without the interaction craft underneath.

### x.ai {#xai}
`clinical / airy` · medium: web · risk: high · checked: 2026-09-29

- Severe monochrome, monumental type, almost no imagery. Brand confidence via
  emptiness.
- Transferable move: **scale contrast**, one gigantic statement vs. tiny
  metadata, nothing in between.
- **Do not take:** emptiness as a substitute for a message. there has to be a statement.

### stripe.com {#stripe}
`neutral / dense` · medium: web · risk: high · checked: 2026-09-29

- The canonical developer-trust aesthetic: crisp multi-column docs-grade layout,
  code samples front and center, signature diagonal gradient used sparingly and
  always anchored to the logo mark.
- Density done warmly: lots on screen, nothing shouting.
- Transferable move: **gradient as signature, not wallpaper**, one ownable
  gradient device, reused identically everywhere.
- **Do not take:** the diagonal gradient itself. it belongs to them.

### thenewindustrials.com (Raw Materials essay) {#new-industrials}
`neutral / airy` · medium: web · risk: low · checked: 2026-09-29

- Long-form editorial layout for a design argument: single measure column, pull
  quotes, generous leading. Content about industrials styled like an industrial
  broadsheet.
- Thesis worth stealing: "The opposite of by design is by accident."
- Transferable move: **medium-matching**, an essay looks like an essay; don't
  force landing-page grammar onto long-form content.
- **Do not take:** broadsheet pastiche on content that is not long-form.

### sapphicindex.com {#sapphic-index}
`neutral / airy` · medium: web · risk: low · checked: 2026-09-29

- Ultra-minimal directory: title, list, done. One accent, no imagery. Proves a
  useful page can be nearly bare if typography and naming are right.
- Transferable move: **subtract to the function**, especially for directories/
  indexes/resources.
- **Do not take:** bareness on a page that has something to explain.

### neuemontreal.com {#neue-montreal}
`warm / airy` · medium: web · risk: medium · checked: 2026-09-29

- Agency showcase built on kinetic oversized type, image reveal on hover,
  horizontal scroll moments. Type IS the interface.
- Transferable move: **type-driven navigation**, menu items at display size act
  as both nav and art.
- **Do not take:** kinetic type with no reading order. motion is not hierarchy.

### bymonolog.com {#monolog}
`neutral / airy` · medium: web · risk: medium · checked: 2026-09-29

- Studio site with editorial confidence: giant statement headlines broken across
  lines, numbered stats (0#/03), parenthetical micro-labels ("(SOON)",
  "(STUDIO DETAILS)"), marquee client strips, case-study metric callouts (21%,
  $100K+).
- Transferable move: **parenthetical metadata voice**, small bracketed labels
  feel handmade compared to all-caps eyebrows.
- **Do not take:** bracketed labels as a costume with no editorial confidence behind them.

### khroma.co {#khroma}
`clinical / mid` · medium: web · risk: low · checked: 2026-09-29

- Tool that generates personalized palettes; the site itself is neutral so the
  colors (its output) star.
- Transferable move: **neutral frame, vivid payload**, when the product's
  output is colorful, chrome goes grayscale.
- **Do not take:** grayscale chrome on a product whose output is not the star.

### re-do.studio / newvalleylabs.com {#re-do-newvalley}
`warm / airy` · medium: web · risk: low · checked: 2026-09-29

- Small-studio sites: strong single accent, straightforward grids, confident
  copy, portfolio-first. Proof that one good accent + one good typeface + honest
  work samples is a complete identity.
- Transferable move: **identity minimum viable**: accent + face + work. Nothing
  else required.
- **Do not take:** small-studio minimalism with no work samples to carry it.

---

## Part 4: Non-screen references

Rule 4 claims a direction survives a change of medium. These are the entries that test it.

### Vignelli / NYC Transit Authority Graphics Standards Manual (1970) {#vignelli-nyc}
`clinical / dense` · medium: print · risk: low · checked: 2026-09-29

- A standard survives because it removes choices, not because it looks of its time. The manual fixes the grid, the type, the sign geometry and the handful of permitted exceptions; nothing else is allowed in.
- **Signature:** grid, type, sign geometry, permitted exceptions, nothing else.
- **Transferable move:** Make the standard the design: specify grid, type and permitted exceptions, then refuse everything else.
- **Do not take:** nostalgic Helvetica cosplay. the point is the constraint system.

---

### Dieter Rams / Braun {#rams-braun}
`clinical / airy` · medium: industrial · risk: medium · checked: 2026-09-29

- The ten principles are a removal procedure. Keep removing until removing again would break the function. Materials are shown rather than concealed, and nothing is added for appearance alone.
- **Signature:** remove until removing breaks the function.
- **Transferable move:** Order by function, then remove. Keep subtracting until the next removal breaks something the object must do.
- **Do not take:** beige 1960s skin. the lesson is subtractive, not retro.

---

### Josef Muller-Brockmann / grid systems {#swiss-grid}
`clinical / dense` · medium: print · risk: low · checked: 2026-09-29

- Choose the grid before the type, then let asymmetry inside it do the composing. A grid is what lets a layout change completely every issue while the publication stays recognisable.
- **Signature:** asymmetry composed inside a fixed grid.
- **Transferable move:** Choose the grid before the type, then compose asymmetry inside it.
- **Do not take:** flush-left Helvetica with no grid underneath. that is a look.

---

### Terminal interfaces: lazygit, btop, htop {#tui}
`clinical / dense` · medium: terminal · risk: low · checked: 2026-09-29

- One cell of resolution, keyboard-only states, colour as a legend. The medium forces the restraint that screen design has to choose deliberately, which makes it a useful calibration reference.
- **Signature:** legibility at one cell, keyboard-only states.
- **Transferable move:** Design at the resolution of the medium: one cell, keyboard-only, colour as a legend.
- **Do not take:** amber or green for atmosphere. palette is a state legend, not a mood.

---

### Teenage Engineering {#teenage-engineering}
`neutral / airy` · medium: industrial · risk: medium · checked: 2026-09-29

- Diegetic labelling: the instruction lives on the object rather than in a legend beside it. Affordances are physical before they are visual, and the control count is the interface count.
- **Signature:** the instruction is printed on the thing.
- **Transferable move:** Label the object, not the manual. Put the instruction on the thing and let the controls be the interface.
- **Do not take:** the aluminium and tiny type without the control logic.

---

## Cross-cutting observations

1. Every reference spends its special-effect budget in exactly one place: Linear
   on product shots, Vercel on the gradient triangle, Stripe on the diagonal,
   Family on microinteractions, x.ai on emptiness. Pages that spend everywhere
   read cheap; pages that spend nowhere read unfinished.
2. Evidence beats assertion everywhere: real UI, real numbers, real diffs, real
   names. This agrees with no-slop Rule 6 from the opposite direction.
3. Dark themes in this list are never black plus neon. They are stepped neutrals
   with hairlines and one disciplined accent.
4. Micro-copy is a design material. Parentheticals, numbered figures, adjective
   titles and timestamp textures all do branding work without pixels.
5. The non-screen entries exist to test Rule 4. A direction that only makes sense
   as `className="..."` is not a direction, and the print and industrial
   references are where that becomes obvious.
