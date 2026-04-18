# Parrot CAD v4 — feet + bar-pin brooch shoulder mount

> Apr 18 2026. Supersedes `cad-brief-final.md` (v3). v4's central change:
> **real shoulder mount** — 2× printed stylized 3-toe feet (cosmetic perching
> stance) + a hidden bar-pin brooch (jewelry finding) glued into a recess on
> the belly plate. The user pins the parrot through their shirt shoulder seam
> via the brooch; the feet hide the pin and form the visual grip. Existing
> belly-plate magnets are retained as a fallback mount (shirt-magnet variant).

## Files (all in `parrot/cad/` and mirrored to `static/parrot/cad/`)

| File | Purpose |
|------|---------|
| `parrot_body.scad` | Parametric OpenSCAD source — 20 tunable parameters |
| `body_top.stl` | Upper shell (~75 g printed) — unchanged vs v3 |
| `belly_plate.stl` | Lower shell (~22 g printed) — NOW with 4 foot peg-holes + 40×3.2×2.2 mm bar-pin recess |
| `feet.stl` | NEW — 2 stylized 3-toe feet on one print plate (~4 g combined) |
| `assembly_preview.png` | 3/4 hero render — perching stance, both feet visible |
| `assembly_exploded.png` | Exploded: body_top / belly_plate / feet separated |
| `view_front.png`, `view_side.png`, `view_rear.png`, `view_top.png` | Ortho views |
| `dimensions.svg` | Labeled dimension drawing |
| `print_settings.md` | Slicer profile, now covering feet plate |
| `print-quotes.md` | Polish print-on-demand service quotes |
| `cad-brief-v4.md` | This document |

## v4 additions (the mount system)

### Feet — separate `feet.stl` print plate

Each foot is a stylized 3-toe parrot foot:
- Footprint: ~18 × 12 mm (including toes); pad disc ~14 × 7 mm, 3 mm thick
- Two forward toes splayed ±35° from +X, one shorter rear toe (tripod stance)
- Two 2.5 mm Ø × 4 mm pegs on the upper surface, spaced 6 mm apart (Y axis)
- Prints flat-on-bed: pad underside is bed-contact, pegs point UP (no supports)

The feet plate lays both feet on one bed with ~8 mm gap between them. The
user slides each foot's pegs into matching holes on the belly plate underside.
**Friction fit only** — no glue required during test fitting. If either foot
shakes loose in daily wear, the user can reintroduce a dab of CA into the
peg holes for a permanent bond.

### Belly plate modifications

The belly plate now has FIVE new features cut into its exterior (the
shirt-facing side when worn):

1. **4× foot peg holes** — 2.75 mm Ø × 5 mm deep, at:
   - (x=+5, y=±3): front foot (under chest, forward of chest low point)
   - (x=-20, y=±3): rear foot (under belly, aft of seam center)
   - The 0.25 mm clearance vs. the 2.5 mm peg gives a firm press-fit
     (initial insertion needs light thumb pressure; retention shear ~0.5–1 kg).

2. **1× bar-pin brooch recess** — 40 mm (Y) × 3.2 mm (X) × 2.2 mm (Z),
   centered at (x=-8, y=0). Y-aligned (pin bar runs wing-to-wing when parrot
   is upright on the shoulder). Fits a standard 38 mm bar-pin jewelry
   finding. Pin is glued in with CA (super glue); depth is tuned so the
   pin sits flush with the belly exterior surface.

### How the mount works

```
   shirt-facing belly (parrot is upside-down in this diagram)
   --------------------------------------------------------
   |                                                      |
   |     [foot]             [pin bar]           [foot]    |
   |     ○○                 ═══════════           ○○      |
   |                     (hidden glued)                   |
   |   (toes curl in,                                     |
   |    visible from                                      |
   |    outside)                                          |
   --------------------------------------------------------
```

To wear: lift a pinch of shirt fabric at the shoulder seam; unhook the bar
pin; thread the fabric pinch through the bar's channel; re-hook the pin.
The parrot now hangs from that fabric anchor, with the feet visually
"perched" on top of the shoulder.

Because the feet surround the pin recess, the brooch is invisible from any
viewing angle except straight-on-belly. From the street, the parrot looks
like it's gripping the user's shoulder with its own feet.

### Why the pin-bar is Y-aligned

With the pin bar running wing-to-wing (Y axis), the fabric pinch runs
parallel to the bar. That means the parrot is anchored against **front-back
tilt** (the most common failure mode — bird wants to tip forward off the
shoulder), while side-to-side it's held by the feet resting on the shirt
surface. The two mount points together create a stable 2-axis anchor.

## Assembly sequence (post-print)

1. Print all three STLs (body_top, belly_plate, feet — see print_settings.md).
2. Install electronics through the belly opening (see cad-brief-final.md v3
   for electronic layout — unchanged).
3. Glue the 4 magnets (CA, polarity as documented).
4. Close the belly plate — magnets latch.
5. Press fit each foot onto the belly plate:
   - Align 2 pegs with 2 holes; push UP firmly.
   - Should seat with 3–5 mm of peg engagement.
   - Test-pull: should not fall off under moderate shake.
6. Glue the 38 mm bar pin into the belly recess (CA, pin pad-side down so
   the pin bar sits proud ~1 mm above the recess floor).
7. Cure 10 min.

## Audit response (v4 self-audit)

See "Self-audit" section at bottom.

## Known limitations (inherited from v3)

- **Internal PCB mounts**: still VHB-taped (per v3). v3.1 can add mounting
  posts once XIAO board revision is confirmed.
- **Face mask**: still Posca-painted, not printed relief.
- **Tail red tip**: Posca paint.

## What's NOT in v4 (deferred to v4.1 if needed)

- **Foot articulation** — toes are rigid. Semi-flex filament not required
  for this use case since the foot pad rests on shirt fabric, not a perch.
- **Alt-mount: silicone tether** — a soft neck-strap option for users who
  don't want to pin through fabric. Can be added as `tether.stl` if desired.

## Print-order checklist

1. Send `body_top.stl` + `belly_plate.stl` + `feet.stl` together to a single
   print job (shares bed, shares shipping).
2. Material: PLA matte **light grey** (closest to African Grey body plumage).
3. Settings: 0.20 mm layer, 15 % infill (20 % for belly plate), 3 walls,
   tree supports auto.
4. Orientation:
   - body_top SEAM-DOWN
   - belly_plate FLOOR-DOWN (tongue up)
   - feet: pad-down, pegs up (no supports)
5. Estimated total print mass: **~99 g** (body 75 + belly 20 + feet 4).
6. Quote tier: **170–280 PLN delivered** (unchanged — feet add <5 PLN).
7. Lead time: 1–3 days.

## Self-audit (fresh-context subagent review) — v4.1 fixes

A fresh-context verification subagent red-teamed v4.0 and found 3 blockers
+ 2 majors. All blockers and the harder major were fixed in v4.1 (current):

### Applied fixes (v4.1)

| # | Severity | Finding | Fix |
|---|----------|---------|-----|
| 1 | BLOCKER | Pin recess 3.2 mm wide was sized for the PIN BAR, not the PAD (~7-8 mm wide). A real brooch pad would not fit. | **Widened to 9 mm × 34 mm × 1.5 mm deep** — fits a standard 38 mm bar-pin pad. Depth matches pad thickness so pad sits flush. |
| 2 | BLOCKER | Rear foot hole at (x=−20, y=±3) collided with the rear magnet pocket at (x=−25, Ø10.4 mm). Foot pegs would have broken into the magnet cavity. | **Moved rear foot to x=−33** (tail-base region, well past magnet at x=−25). |
| 3 | BLOCKER | Original 3 mm foot pad was taller than the pin bar protrusion (~1 mm). Feet would hit shirt fabric BEFORE the pin could thread through. | **Thinned foot pad to 1.6 mm**. With pad glued flush in the recess, the bar now protrudes ~2-3 mm below the foot pad bottom, giving fabric a clear threading channel. |
| 4 | MAJOR | 40 mm pin recess cut at constant Z breached the belly shell at Y extremes (where the shell curves up above the cutter). | Shortened to **34 mm** (Y) and widened to 9 mm (X), staying inside the belly silhouette. |
| 5 | MAJOR | 0.25 mm clearance became a loose sliding fit after FDM shrinkage + elephant's foot. Feet would fall off. | **INVERTED the fit: peg 2.7 mm, hole 2.5 mm** → 0.2 mm interference (firm press-fit, PLA gives slightly on insertion). |

### Accepted limitations (minor findings)

- **Foot pad geometry**: v4.1 pad is a `linear_extrude` from z=0, all geometry above the bed (fixing the audit's concern about old sphere hull dipping below z=0).
- **Peg shear strength at 0.4 mm nozzle**: 2.7 mm pegs are ~7 perimeters on a 0.4 nozzle. A sideways knock could still break pegs at the base — accepted risk; user can reprint feet cheaply.
- **Silhouette reads "generic plump bird" not specifically African Grey**: inherited from v3 — paint does the heavy lifting (matte black beak, red tail tip, white face ring around eyes with Posca markers per print_settings.md post-processing).

### Confirmed sound (audit)

- Pin-recess bridging: belly plate prints floor-down, recess is a downward-facing pocket bridged at the top — trivial for any hobby FDM.
- 2.5 mm hole printing: well within 0.4 mm nozzle resolution.
- Toe overhang geometry: toes rise at 30° above the pad surface, no unsupported drops.
- 2-peg spacing (6 mm): adequate to resist foot rotation once pressed in.
- Registration tongue + magnet latch: sound, unchanged from v3.
