# bearing

The captain of your design skill.

A design-direction skill for coding agents. It reads the brief, states an
explicit direction with named coordinates, grounds it in a researched pattern
library, and outputs a `DIRECTION.md` that any medium can execute: React,
SwiftUI, a terminal UI, print, slides, game UI.

It decides what to aim at. `frontend-design` helps you shoot, `no-slop` checks
you did not hit the clichés instead.

## Why

Agents do not fail at design because they cannot write CSS. They fail because
nothing decided what the design is for before the first component got written.
By the time the layout exists, the direction has already been chosen by default.
Bearing moves that choice to the front and makes it sayable, so it can be
rejected before it is built.

## The contract

Never generate anything non-trivial before stating this and showing it:

```
PURPOSE:     <one sentence>
AUDIENCE:    <who, and how fluent>
MEDIUM:      <web app / landing page / iOS / CLI / deck / print / ...>
COORDINATES: temperature clinical<->warm = X, density airy<->dense = Y
VIBE:        <3 adjectives, at least one from the user's own words>
REFERENCES:  <ref> -> taking <specific move>, not <surface look>
ASSETS:      <what exists, what's missing>
DIRECTION:   <named direction + one-sentence pitch>
```

The contract is a veto window, so it has to be vetoable. Every contract carries
at least one falsifiable claim, a sentence the user could disagree with, and one
named rejected alternative. A contract made only of adjectives cannot be argued
with, which turns the review step into theatre.

If the user corrects a line, re-issue the contract before continuing.

## Coordinates first

Two axes explain most of the design space.

- **Temperature:** clinical <-> warm
- **Density:** airy editorial <-> dense operational

Plot the project on both before choosing anything. Then filter the pattern
library's index by those coordinates instead of browsing it, and remix at most
two directions, naming what you take from each.

## The pattern library

`references/pattern-library.md` holds field notes on 30 references, sourced from
real systems and sites rather than from taste. Each entry records what the design
actually does, the transferable move, and what not to steal.

An index at the top carries the coordinates, the signature device and a clone
risk for every entry:

| slug | source | medium | temp | density | risk |
| --- | --- | --- | --- | --- | --- |
| `carbon` | Carbon (IBM) | web | clinical | dense | low |
| `linear` | linear.app | web | clinical | dense | high |
| `wise` | Wise | web | warm | airy | medium |
| `vignelli-nyc` | Vignelli / NYC Transit standard | print | clinical | dense | low |

Cite by slug in the direction and in review: `bearing:linear`,
`bearing:vignelli-nyc`. Risk is how likely the move is to read as a clone;
`high` means take the move and change at least one other variable.

Rule 4 claims a direction survives a change of medium, so five entries are
deliberately not screens: the Vignelli transit standard, Rams-era Braun, Swiss
grid systems, terminal interfaces, and Teenage Engineering. A direction that
only works as `className="..."` is not a direction.

## Order of operations

```
brief -> Rule 0 questions -> interpretation contract
      -> coordinates + remixed direction (cite the library)
      -> delight budget
      -> DIRECTION.md -> user veto window -> implement
      -> audit with no-slop
```

Two notes on the handoff, learned the hard way:

- Run `no-slop`'s scanner early, not only at the end. Several of its rules ban
  things a direction may have just chosen, a gradient as the signature device or
  a purple accent among them, and finding that out after building means rework.
- The delight budget needs a number. "Tune it later" is not a budget. State it in
  the contract, on a scale, with what changes at each step.

## Files

```
SKILL.md                        the rules
references/pattern-library.md   the 30 references, indexed and cited by slug
scripts/check_library.py        validates the library against its own index
```

## Install

Drop the directory into whatever reads skills:

```
~/.claude/skills/bearing/
~/.pi/agent/skills/bearing/
```

## Verify

```bash
python3 scripts/check_library.py
```

Checks that every entry has an index row and every row has an entry, that slugs
are unique, that each entry carries a check date, a transferable move and a
do-not-take line, and that coordinates and risk come from the allowed sets. A
library that drifts from its own index cannot be cited reliably, which is the
whole point of having an index.

## Contributing

New references are welcome if they come with all five fields: coordinates, a
signature device, a clone risk, a check date, and the do-not-take line. An entry
without an anti-take is a recommendation to clone, which is the opposite of the
point.

## License

MIT. See `LICENSE`.
