---
name: bearing
description: The captain of your design skill. Design-direction skill and creative
  partner to no-slop. Interprets the brief (purpose, audience, references, assets, vibe), states an explicit design direction with named coordinates, picks tactics from a researched pattern library of real design systems and sites (Linear, Stripe, Carbon, Wise, Family, shadcn, Vercel, etc.), and outputs a medium-agnostic DIRECTION.md that any implementation, React, Swift, terminal TUI, print, slides, game UI, can execute. Use when starting any new design/brand/UI work, when the user asks "what direction should this take", or before running no-slop/frontend-design so execution has something to aim at.
---

# Bearing

Choose the direction before touching pixels. no-slop stops you from sounding
generic; frontend-design helps you execute; this skill decides what you're
making in the first place, and says it out loud so the user can veto it early.

Works for any medium. Nothing here assumes React, web, or screens: a direction
is expressed as relationships (hierarchy, temperature, density, motion
character) that translate to markup, native UI, terminals, print, or slides.

## Rule 0: Read the room first

Before proposing anything, answer these from the brief, the user's words, and
available assets. If a question can't be answered from the brief, ask, or state
your assumption explicitly in the interpretation (Step 1) so it can be corrected.

1. **What is it for?** A page? An app? A pitch deck? A CLI tool? A physical
   object? What single action or understanding should the audience leave with?
2. **Who is the audience?** Their fluency matters more than their demographics:
   developers tolerate density; consumers don't; procurement wants trust cues.
3. **What references did they give?** Each named reference is a clue. Extract
   *what specifically* they likely want from it ("like Linear" usually means
   dark precision + product-as-hero, not "copy Linear's nav").
4. **What assets exist?** Logo, brand colors, photography, an existing design
   system, real data, real screenshots. Real assets outrank invented decoration;
   if none exist, note that illustration/imagery must be commissioned or omitted.
5. **What vibe words did they use?** Take them literally. "Playful" is a spec,
   not a suggestion. If they gave none, infer from category and audience.
6. **What are the constraints?** Serious/compliance context (corporate, medical,
   legal) caps playfulness. Legacy brand elements cap reinvention.

## Rule 1: State your interpretation before designing

Write a short interpretation block and show it to the user before generating
anything non-trivial:

```
PURPOSE:     <one sentence>
AUDIENCE:    <who, and how fluent>
MEDIUM:      <web app / landing page / iOS / CLI / deck / print / ...>
COORDINATES: temperature clinical↔warm = X, density airy↔dense = Y
VIBE:        <3 adjectives, at least one from the user's own words>
REFERENCES:  <ref> → taking <specific move>, not <surface look>
ASSETS:      <what exists, what's missing>
DIRECTION:   <named direction + one-sentence pitch>  (see Rule 2)
```

This is a contract, not a formality: every later design decision should be
traceable to a line in it. If the user corrects a line, re-issue the contract
before continuing.

It is also a veto window, so it has to be vetoable. Every contract must carry at
least one falsifiable claim, a sentence the user could disagree with, and one
named rejected alternative. A contract made only of adjectives cannot be argued
with, which turns the review step into theatre.

## Rule 2: Pick coordinates, then remix a direction

Two axes explain most of design space: **temperature** (clinical ↔ warm) and
**density** (airy editorial ↔ dense operational). Plot the project on both
first; tactics follow from the plot, not from habit.

Then choose a direction from the pattern library (`references/pattern-library.md`).
Filter the index by your coordinates first, then read only the entries that fit;
citation slugs are in the index. Thirty references, notes on Carbon, Atlassian,
shadcn/ui, Tailwind Plus, Untitled UI, Wise, Radix, Base, Linear, Cursor, Autumn,
Morphic, Vercel, jib/ja.mt, Interfere, Aside, Family, x.ai, Stripe, The New
Industrials, Sapphic Index, Neue Montreal, Monolog, Khroma, Re-do, New Valley
Labs, plus five non-screen references: the Vignelli transit standard, Rams-era
Braun, Swiss grid systems, terminal interfaces and Teenage Engineering.

Directions are ingredients, not costumes. Three laws:

1. **Remix, don't clone.** Combine two directions at most, and name what you're
   taking from each: "Linear's luminance-stepped dark surfaces + Family's
   microinteraction delight." A pure clone of any named site is a failed choice ,
   including cloning the defaults (Untitled-UI-gray-on-white is the slop baseline).
2. **One special effect.** Every strong reference spends its signature budget in
   exactly one place (Linear: pixel-perfect product shots; Stripe: the diagonal
   gradient; Family: springy microinteractions; x.ai: monumental emptiness).
   Pick ONE signature device for the project and spend the entire effects budget
   there. A page that spends everywhere reads cheap; nowhere reads unfinished.
3. **Evidence beats assertion.** Prefer real screenshots, real numbers, real
   diffs, real names over illustrations-of-concepts. If no real artifacts exist,
   say so rather than faking stock-y ones.

## Rule 3: Delight budget

Microinteractions are encouraged by default even in clean, formal directions ,
hover reveals, springy transitions, count-ups, cursor-aware elements, drag
physics, satisfying toggles. They signal craft the way good kerning does.

Cap by seriousness: corporate/compliance/legal/medical contexts get *restrained*
delight (focus states, subtle easing consistency) rather than playful springs ,
unless the user explicitly asks for fun there anyway. When unsure, put the
delight budget line in the interpretation contract and let the user tune it.

Motion discipline (durations, easings, reduced-motion, nothing hidden behind JS
on web) is delegated to no-slop / platform conventions at build time; here you
only decide *character*: snappy vs springy vs cinematic.

## Rule 4: Universality check

Express the direction as medium-independent decisions before implementing:

- **Hierarchy**: what wins, what whispers (works in CSS, SwiftUI, ncurses, ink).
- **Color roles**: surface / text / interactive / status / accent, never raw
  hex as identity. Accent color is a control (Carbon), not wallpaper.
- **Type character**: face class + ramp shape + tracking mood, not just a font
  name. (A direction that only works with one Google Font is fragile.)
- **Density & rhythm**: spacing scale, measure widths, row heights.
- **Motion character**: one easing family, 2–3 duration tiers (Base's rule).
- **Voice**: parentheticals, numbered figures, adjective titles, copy patterns
  are design materials too.

Sanity test: could a designer implement this direction in a different framework
or medium using only your DIRECTION.md? If a decision only makes sense as
`className="..."`, rewrite it as a relationship.

## Rule 5: Output a DIRECTION.md

For any non-trivial work, write `DIRECTION.md` next to the project (or into the
plan) containing: the interpretation contract, chosen direction + remix sources,
the signature device, color roles, type character, density/rhythm rules, motion
character, delight budget, and 3–5 concrete reference citations from the pattern
library with what's borrowed from each. Implementation skills consume this file;
reviewers compare output against it.

## Workflow summary

```
brief → Rule 0 questions → interpretation contract (Rule 1)
     → coordinates + remixed direction (Rule 2, cite library)
     → delight budget set (Rule 3)
     → DIRECTION.md (Rule 5) → user veto window → implement
     → audit with no-slop final pass
```

bearing decides where to aim; no-slop checks you didn't hit the clichés instead;
frontend-design helps you shoot. Run them in that order.

## References

- `references/pattern-library.md`, per-source research notes: what each system
  and site actually does, and the transferable move extracted from it. Read the
  relevant entries before citing a direction.
