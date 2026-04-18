# Parrot Assistant — recommended print settings

Profile tested mentally against Prusa MK4 / Bambu P1S / Ender 3 V3 KE class
hobby FDM printers. PLA is the recommended material — easiest to print, best
surface finish, widest matte colour selection. PETG is acceptable if the
upper shell will see sustained sun exposure, but for indoor shoulder use PLA
is plenty (cavity heat load is minimal with off-body power).

## Files

| Part | STL | Layer | Infill | Supports | Orientation |
|------|-----|-------|--------|----------|-------------|
| Body top | `body_top.stl` | 0.20 mm | 15 % gyroid | tree, auto 50° | belly opening UP (seam DOWN on bed) |
| Belly plate | `belly_plate.stl` | 0.20 mm | 20 % gyroid | none | floor DOWN, tongue UP |
| **Feet plate (v4)** | `feet.stl` | 0.20 mm | 20 % gyroid | none | pad-bottom DOWN, pegs UP |

## Slicer settings (one slicer-agnostic recipe)

- **Material**: PLA matte, vanilla grey or stone grey (e.g. Bambu PLA Matte
  "Ash Gray", Prusament PLA "Galaxy Silver", or any local matte grey ~25 PLN/kg).
  For a darker "stealth" look, matte charcoal works equally well.
- **Layer height**: 0.20 mm (default). Drop to 0.15 mm for the body top if
  beak/eye-socket detail looks rough on the test print.
- **Perimeters / walls**: 3. The cavity needs to be sealed against rattling
  electronics and a 3-perimeter wall hits ~1.2 mm of solid plastic which is
  the right strength/weight balance.
- **Top / bottom layers**: 4 / 4.
- **Infill**: 15 % gyroid for body_top (rigid + lightweight, gyroid is also
  acoustically dead which helps the speaker chamber). 20 % for the belly
  plate so the magnet pockets sit in solid plastic.
- **Supports**: tree (organic), 50° auto-detect angle. Body_top needs them
  for the under-beak overhang, the back of the head, and inside the eye
  socket. Belly plate needs none.
- **Brim**: 5 mm brim on body_top to avoid corner lift on the tail and head
  contact patches. Belly plate is flat-bottomed so no brim needed.
- **Print speed**: stock profile (60–120 mm/s outer, 200+ for infill on
  modern machines). The whole job is well under 12 h on a 0.4 mm nozzle.
- **Seam position**: aligned to the rear centre-line so it hides in the tail
  crease.
- **Cooling**: full part cooling for PLA. The beak is a tiny overhang
  feature and benefits from max fan on layers > layer 30.

## Orientation notes

### body_top — print SEAM-DOWN (cut face on the bed)

Orient the part with the **cut seam plane (the open belly face) flat on
the print bed**, head pointing UP. The bed-contact face is the seam ring
itself, so the first layer is a clean closed loop. The body silhouette
curves UPWARD from there, narrowing toward the head and crown.

This puts:

- The whole body silhouette above the bed at angles ≤ 50° from vertical
  → no tree supports needed on the visible chest, back, or flanks
- The beak (forward overhang) → needs a small tree-support cluster under
  it (auto-detected by the slicer at 50°)
- The eye socket → punches sideways through the head wall; tree supports
  inside the socket bore (auto-detected)
- The speaker grille → on the front of the chest, holes face forward at
  ~−10° → tiny bridges per hole, prints cleanly without per-hole support

**Why this beats head-down:** seam-down keeps the bed-contact area on a
flat closed ring (best first-layer adhesion + zero support scars on the
visible silhouette). Total support volume ≈ 5 g of branched tree under
the beak only.

In your slicer, this is "Z up" with no rotation needed if you exported
the STL with body_top in its native CAD orientation (which `parrot_body.scad`
does).

### belly_plate — print floor down

Lay the plate **floor side DOWN** (registration tongue pointing UP). The
floor becomes the bed-contact surface (no support, perfect first layer);
the tongue extrudes upward as a clean ring. Magnet pockets are cut into
the floor from below, so they print as a downward-facing recess that the
slicer handles automatically with a bridge layer.

## Estimated print times + filament usage

Estimated on a Prusa MK4 with the stock 0.4 mm nozzle and the 0.20 mm
SPEED PLA profile:

| Part                 | Time        | Filament    |
|----------------------|-------------|-------------|
| body_top             | ~6.5 h      | ~75 g       |
| belly_plate          | ~1.5 h      | ~22 g       |
| feet (2 on 1 plate)  | ~0.4 h      | ~4 g        |
| **Total (v4)**       | **~8.4 h**  | **~101 g**  |

At ~80 PLN/kg matte PLA, that's **~8 PLN of material**. The feet plate
adds <5 PLN to service pricing. Most of the print-budget envelope (under
500 PLN) still goes to the print-service mark-up, not the plastic.

## Post-processing

- Pop the brim off both parts.
- Lightly sand the seam where the brim attached (220 → 400 grit, 60 s).
- **Paint accents** (optional, ~15 min):
  - Beak and lower mandible: matte black acrylic / Posca black
  - Tail stub: crimson red Posca or acrylic
  - Face mask ring around the eyes: matte white Posca for the African
    Grey "white face" signature
- Glue 1–2 of the 10 × 1.5 mm neodymium magnets into the belly plate
  pocket using cyanoacrylate (CA) glue. Magnet pole orientation: north
  side facing UP (toward the body cavity) on both magnets — keeps them
  from interfering with each other or with shirt-side magnets.

### feet.stl (v4) — print pad-bottom DOWN

Two stylized 3-toe feet on one plate (~22 mm apart, centered). The
**pad underside is bed-contact**; pegs point UP (away from bed). No
supports needed — toes taper gradually and the pegs are vertical
cylinders. Use 0.20 mm layers and 20 % infill (solid-ish pegs resist
peg shear during friction-fit insertion). Print alongside the belly
plate on the same bed if the service combines small prints.

## Post-print assembly notes (v4)

After printing all three STLs:

1. **Friction-fit the feet**: Align each foot's 2 pegs with the 2 holes
   under the belly plate at (x=+5) and (x=−20). Press up firmly — should
   seat with ~4 mm of peg engagement, visible foot pad flush (±0.5 mm)
   against the belly exterior. Test-pull: foot should hold ~0.5 kg of
   vertical shear before popping free. If too loose → dab CA into the
   hole and re-insert.

2. **Glue the bar pin**: Drop a standard 38 mm bar-pin brooch finding
   (pad-style, the kind used on fabric brooches) into the 40 × 3.2 × 2.2 mm
   recess between the two feet. Pad side DOWN into the recess, pin bar
   protruding UP so fabric can thread through it. Run a bead of CA
   cyanoacrylate along the pad edges and cure 10 min.

3. **Wear test**: Pin the parrot onto a shoulder T-shirt seam. The feet
   provide the visual "grip" stance; the pin is invisible from outside.
   Should hold through normal arm motion; doesn't tolerate jumping/running
   (remove before exercising).

## Print-service notes

If sending to a service, send **all three STLs together** in the same job
to share the bed and minimize per-part fees. Specify:
- Material: **PLA matte** (any colour from light grey through charcoal)
- Layer height: **0.20 mm**
- Infill: **15 %**
- Supports: **tree, auto**
- Single colour (don't pay for multi-material — the red tail accent and
  black beak are post-paint Posca work)

Quotes from Polish print-on-demand services live in `print-quotes.md`.
