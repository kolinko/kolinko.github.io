# Parrot Assistant — BOM v2 (solder-free redesign)

**Apr 18 2026** • budget target 800 PLN • ship-to Twarda 4 m 274, 00-127 Warsaw

**User constraint:** "very very basic assembly, preferably no soldering." v1.2 claimed solder-free but required makerspace soldering (XIAO 14-pin header, MAX98357A 6-pin header, TPS61023 4-pin header, 1N5819 diode leads). v2 eliminates all but **one** 6-pin solder joint that cannot be avoided with any commercially available MAX98357A breakout (industry-wide reality — verified Apr 2026 against Adafruit 3006, SparkFun BOB-14809, Kamami 1182935, plus M5Stack / Waveshare / DFRobot audio-amp catalogs).

## Summary

| # | Item | Supplier SKU | Qty | PLN | Solder-free? |
|---|------|----|----:|----:|---|
| 1 | Kamami XIAOML Kit (pre-soldered XIAO ESP32-S3 Sense) | Kamami 1202930 | 1 | 229.63 | **yes** |
| 2 | MAX98357A I2S amp | Kamami 1182935 | 1 | 25.98 | **no — 1 joint (6 pins)** |
| 3 | Mini metal speaker 28mm 8Ω 1W pre-wired | Kamami 234920 | 1 | 11.25 | yes |
| 4 | JST-PH 2.0 2-pin 10cm pigtail | Kamami 1181279 | 3 | 5.61 | yes |
| 5 | Blow PB12 6000mAh USB power bank | Botland 6846 | 1 | 45.00 | yes (with risk note) |
| 6 | USB-A → USB-C 1m Lanberg cable | Botland 14829 | 2 | 21.80 | yes |
| 7 | justPi F-F jumper ribbon 20cm 40 pcs | Botland 19620 | 1 | 14.00 | yes |
| 8 | Neodymium disc magnet 10×1.5 mm, pack of 10 | Kamami 1186978 | 1 | 5.25 | yes |
| 9 | PVC electrical insulation tape 19mm × 10m | Botland 532 | 1 | 5.00 | yes |
| **Total** | | | | **363.52 PLN** | 8/9 active lines = 89% solder-free; one flagged joint is unavoidable industry-wide |

**Budget status:** 363.52 PLN / 800 PLN target (54% headroom); 4.8% of the 7500 PLN project budget.

Retired from v1.2 (qty=0 / status=replaced in Redis): Pimoroni 500mAh LiPo, Pimoroni LiPo Amigo Pro, Adafruit TPS61023 MiniBoost, Schottky 1N5819. Eliminates **14 pins** of XIAO header solder + **4 pins** of TPS61023 solder + **2 lead tails** of 1N5819 solder + removes the 5 V backfeed failure mode that crippled v1.

---

## Solder-free status per item

### 1. XIAO ESP32-S3 Sense — pre-soldered (via Kamami XIAOML Kit)

- **SKU**: Kamami `1202930` (XIAOML Kit – AI Development Kit with Camera and ESP32-S3).
- **Contents**: XIAO ESP32-S3 Sense with **factory-soldered 7+7 pin headers**, OV3660 camera (pre-attached), digital PDM microphone, microSD reader. Bundled extras we won't use: IMU+OLED module, 2.4 GHz FPC antenna, 2× heatsinks, 32 GB microSD + USB adapters.
- **Price**: 229.63 PLN (gross), 24 h PL stock.
- **Why not cheaper**: The standalone `102010635` pre-soldered variant is **not stocked at Botland, Kamami, or TME** (Apr 2026). Mouser EU returns "Restricted Availability — does not presently sell this product in your region" for 102010635. Mouser US has 164 in stock at $14.99 but 40% EU customs flag + cross-Atlantic shipping raises total to ~180 PLN with multi-week delivery. Kiwi Electronics NL is OOS. The XIAOML Kit from Kamami (PL warehouse, 24 h) is the most reliable pre-soldered path verified Apr 2026.
- **Saves**: 14 pins of solder vs the stock `113991115` (loose headers).

### 2. MAX98357A I2S amp — the one unavoidable solder joint

- **SKU**: Kamami `1182935` (Class-D 2.5 W I2S amp, PH2.0 speaker socket pre-installed).
- **Price**: 25.98 PLN.
- **Solder-free? NO — 6 gold-pin through-holes on the I2S/power side must be soldered.**
- **Why unavoidable** (triple-verified: Kamami + Adafruit + SparkFun product pages, plus Gemini 2.5 Pro second-opinion):
  - Adafruit `3006`, SparkFun `BOB-14809`, and Kamami `1182935` **all** ship with male headers **loose** in the bag. Adafruit product page quotes: *"Comes as an assembled and tested breakout board with pre-soldered terminal block, with a small piece of optional header. Some soldering is required to attach the header."*
  - No MAX98357A breakout **in the industry** (M5Stack, Waveshare, DFRobot, Pimoroni, Adafruit, SparkFun, Kamami, AliExpress clones) ships with male headers factory-installed as of Apr 2026.
  - The ESP32-S3 has **no Classic Bluetooth / A2DP** (BLE only), so switching to a wireless Bluetooth speaker to sidestep I2S wiring **is architecturally impossible**.
  - Pressure-fit female header would be unreliable under shoulder-mount vibration.
  - **M5Stack Atomic Echo Base A149** is the only true-solder-free audio option but would force a switch to the AtomS3R ecosystem, invalidating the XIAO-based CAD body already in Phase 1.
- **Work required**: 6 solder joints, ~2 min at an electronics hackspace. Beginner-friendly 2.54 mm through-holes.
- **Preferred remediation — at Kamami checkout**: add a note on the order: *"prosze o zamontowanie listwy goldpin 1×6 do modulu 1182935 (usluga odplatna)"*. Kamami offers paid header-install services; this moves the joint entirely off the user's bench.
- **Fallback — makerspace**: Warsaw options include [Hackerspace Warszawa](https://hackerspace.pl/) and [Fab Lab Warsaw](https://fablab.waw.pl/). A basic 25 W iron + rosin-core solder; no fine-pitch skill required.

### 3. Speaker — pre-wired, no solder

Kamami `234920`, 28 mm 8 Ω 1 W with factory-soldered bare-end lead wires. Connects to a JST-PH pigtail via twist-and-tape (no iron, no crimper, no heat gun — just insulation tape and fingers).

### 4. JST-PH 2.0 pigtail — factory-crimped

Kamami `1181279`, factory-crimped 2-pin JST-PH 2.0 female plug on one end, bare tinned leads on the other. 3 pcs (2 in use + spare).

### 5. USB power bank — replaces the whole v1 power subsystem

- **SKU**: Botland `6846` (Blow PB12 6000 mAh, 2× USB-A output + microUSB/USB-C input).
- **Why**: replaces Pimoroni LiPo + Amigo Pro + TPS61023 + Schottky as one factory-sealed block. Charge via any USB-C wall plug.
- **⚠️ Risk flag**: many USB-A banks auto-off when load drops below ~50-100 mA. XIAO light-sleep drops lower. **Mitigations**:
  1. Force flashlight/keep-alive mode by double-pressing the Blow button (most Blow models support this; verify on arrival before final assembly).
  2. Keep the firmware in light-sleep not deep-sleep so current stays > 100 mA.
  3. If still triggers auto-off, swap for a power bank marketed for small IoT devices (Voltaic V15/V25 or any "Arduino/IoT" pack).
- **Runtime**: 6000 mAh × 3.7 V ≈ 22 Wh ÷ 0.75 W (XIAO 150 mA @ 5 V avg) ≈ **12 h**.
- **Tradeoff vs onboard LiPo**: externally worn (belt or pocket, cable under shirt). Upside: zero solder, zero onboard thermal concerns, universal recharge. Downside: one cable routed through the shirt.

### 6. USB-A → USB-C cable

Lanberg 1 m QC3.0, Botland `14829`, 10.90 PLN × 2 (one in use, one flashing spare).

### 7. Dupont F-F jumper ribbon (Gemini revision — saves 80 PLN vs v1 bulk kit)

justPi 40-pin F-F 20cm ribbon, Botland `19620`, 14 PLN. Peel off 6 ribbons for VIN, GND, SD, BCLK→D1, LRCLK→D3, DIN→D4. All contacts are standard 2.54 mm and mate with XIAO pre-soldered header and MAX98357A (post-maker-solder) header.

### 8. Magnet clip

Kamami `1186978`, neodymium disc magnet 10 × 1.5 mm, pack of 10 at 5.25 PLN. 12 packs in stock, 24 h PL delivery. Glue one or two discs into the printed belly-plate pocket; a mirror magnet or shirt safety-pin with a 10 × 1.5 disc glued to the head clips through the shirt fabric. If stronger hold needed, swap to a 10 × 3 mm variant in the same Kamami category.

### 9. PVC electrical insulation tape

Botland `532`, 19 mm × 10 m black PVC tape, 5 PLN. Used once to seal the twist-join between the 28 mm speaker leads and the JST-PH pigtail bare ends. Also serves general cable dressing inside the printed body.

---

## Wiring diagram

```
 Blow PB12 power bank (belt/pocket)
      │ USB-A output
      ▼
 USB-A ═══ USB-A→USB-C 1m Lanberg ═══ USB-C  (factory cable)
                                          │
                                          ▼
                                    XIAO ESP32-S3 Sense
                                    (pre-soldered 7+7 headers)
                                          │
                                          ├── GPIO2 (D1) BCLK ─┐
                                          ├── GPIO4 (D3) LRCLK ┤ 6× F-F
                                          ├── GPIO5 (D4) DIN   ┤ ribbon jumpers
                                          ├── 3V3        VIN   ┤ (no MCLK —
                                          ├── GND        GND   ┤  MAX98357A
                                          └── GND        SD    ┘  generates it
                                                              internally)
                                                ▼
                                   MAX98357A (6-pin solder HERE — ONE joint)
                                   │ PH2.0 socket is already factory-soldered
                                   │
                                   └── JST-PH pigtail
                                          │  (bare ends twist-
                                          │   joined to speaker,
                                          │   wrapped with tape)
                                          ▼
                                       28 mm 8 Ω speaker
```

## Assembly steps (user-facing)

1. **Before assembly** (at Kamami checkout note OR at a Warsaw makerspace): 6 pins soldered onto the MAX98357A gold-pin row. This is the only iron time in the entire build.
2. Join speaker leads to JST-PH pigtail bare ends: strip 5 mm of each lead, overlap and twist, wrap 3-4 turns of PVC tape.
3. Plug the JST-PH pigtail into the MAX98357A's pre-soldered PH2.0 speaker socket.
4. Plug 6 F-F jumper ribbons between XIAO and MAX98357A: VIN↔3V3, GND↔GND, SD↔GND, BCLK↔D1 (GPIO2), LRCLK↔D3 (GPIO4), DIN↔D4 (GPIO5).
5. Glue magnets into the belly-plate pocket of the printed body, seat XIAO + MAX98357A + speaker inside, close the shell.
6. Plug USB-A → USB-C cable between the Blow power bank (belt/pocket) and the XIAO's USB-C port.
7. Press the Blow's flashlight button twice to lock always-on → XIAO boots → parrot speaks.

## Total

- **Active BOM: 363.52 PLN** across 9 lines.
- Under the 800 PLN target by **436.48 PLN** headroom.
- Against the 7500 PLN project budget: **4.8%**.

## Second-opinion gate (completed)

Two independent reviewers ran over this BOM before lock.

**(a) Read-only red-team agent (verification subagent).** Flagged three concrete issues, all fixed before final lock:
- Heatshrink URL was a search page → swapped to Botland `532` PVC tape (concrete SKU, in stock).
- Magnet URL was an Allegro search → swapped to Kamami `1186978` (concrete SKU, 12 in stock).
- Power-bank auto-off risk was undocumented → added explicit risk flag + 3 mitigations.

**(b) Gemini 2.5 Pro second opinion.** Verdict: *"one revision"* — swap the 94 PLN 3×40pc dupont mixed kit for the 14 PLN 40pc F-F ribbon (Botland `19620`), since only 6 jumpers are actually used. **Applied, saves 80 PLN.** Gemini also confirmed: no residual solder hiding; MAX98357A MCLK is generated internally so 3-wire I2S is correct; I2S pin map (GPIO2/4/5) is valid and correctly avoids GPIO3 strapping; no cheaper MAX98357A path exists across M5Stack / Waveshare / DFRobot / Pimoroni / SparkFun / Adafruit catalogs.

## What was considered and rejected

| Option | Why rejected |
|--------|--------------|
| Seeed `102010635` standalone pre-soldered XIAO via Mouser EU | "Restricted Availability" for PL region Apr 2026. |
| Mouser US direct ship | 40% tariff flag + cross-Atlantic shipping → ~180 PLN + weeks delay. |
| Kiwi Electronics NL | OOS per project memory. |
| Adafruit PowerBoost 500 (1944) / 1000C (2465) | Listed "withdrawn" at Botland (Apr 2026); no PL stock at Kamami. Still ships with loose header strip regardless. |
| Bluetooth speaker via A2DP | ESP32-S3 has no Classic BT / A2DP stack — architecturally impossible. |
| Pressure-fit female header on MAX98357A | Unreliable under shoulder-mount vibration. |
| Waveshare Mini UPS 24760 onboard power | Takes 3× 10440 Li-ion cells → too large for shoulder body. |
| Wago 221-412 lever-nut for speaker joint | OOS at Kamami Apr 2026; Wago 2273-204 is solid-wire only, incompatible with stranded speaker leads. Fell back to twist + PVC tape, strictly tool-free. |
| Solder-sleeve heatshrink (Kamami 588800 / 588805) | Both OOS Apr 2026 with 4-week lead times. |
| M5Stack AtomS3R + Atomic Echo Base | Would invalidate XIAO-based CAD body (Phase 1 in progress). Reserve for v3 if ever needed. |

## Next action

User reviews this BOM at `https://kex7m.effort.ws/static/parrot/bom-v2.md`, clicks **Approve** on the `phase-2-order` milestone in the `/parrot` admin panel. Approval unlocks the Phase 2 order sub-issue to execute the Kamami + Botland carts.

---

*BOM v1.2 cargo-cult autopsy lives in `~/claude/varia/memory/parrot-bom-hardware-gotchas.md`. v2 research log in the `/parrot` activity feed. Red-team + Gemini transcripts are preserved in this sub-issue's timeline (source_issue_id da239d58).*
