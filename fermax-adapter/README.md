# Fermax CityMax Basic 4+N — Auto Door Opener Adapter

Research, recommendation, order plan, DIY fallback schematic and installation guide for
automatically opening the downstairs door when someone rings the apartment on a
**Fermax CityMax Basic 4+N (ref 80447)**.

Full write-up with diagrams: [index.html](index.html) · [kex7m mirror](https://kex7m.effort.ws/static/fermax-adapter/) · [public mirror](https://kolinko.eu/fermax-adapter/)

---

## Recommendation (TL;DR)

**Buy a Nuki Opener** — it's the only ready-to-install product that handles Fermax 4+N
cleanly, fits the budget, and ships to Warsaw in two days.

| | |
|-|-|
| Product | [Nuki Opener (white)](https://www.x-kom.pl/p/726238-inteligentny-zamek-nuki-opener-bialy.html) |
| Price | **399 PLN** / unit at x-kom.pl (free FedEx delivery) |
| Order quantity | 2 units = 798 PLN (per "order double" authorisation) |
| Compatibility | Fermax 80447 confirmed via [Nuki installer forum](https://developer.nuki.io/t/opener-installation-fermax/17423); profile "VDS BASIC LOFT TELEPHONE" |
| Feature | Built-in Ring-to-Open (auto-trigger door on ring) — exactly the spec requirement |

### Why not a custom PCB

80 minutes of research (Allegro, OLX, AliExpress, Amazon DE/PL, 5 Fermax distributors,
Tindie, Crowd Supply, GitHub, elektroda.pl, forbot.pl, Reddit) — no other finished
product exists for 4+N. ESPBell-MAX (€37, closest) requires Home Assistant, which the
user explicitly rejected. Designing + manufacturing + shipping a custom PCB via JLCPCB
PCBA adds ~$80 BOM + 2–3 weeks lead time vs Nuki's 2 days and 798 PLN total.

---

## Order status

| Field | Value |
|-------|-------|
| Seller | [x-kom.pl](https://www.x-kom.pl) (Polish retailer, 22y on market) |
| Cart built | 2 × Nuki Opener (Biały), 798,00 PLN |
| Delivery | FedEx courier, free, Wed 22.04.2026 |
| Ship to | Tomasz Kolinko · Twarda 4 m 274 · 00-127 Warszawa · +48 600 359 921 · kolinko@gmail.com |
| Payment method selected | Karta płatnicza online (card) |
| Card on file | 4165 98** **** 4661 (dedicated agent card, Revolut) |
| tpay txn ID | `TR-5VRG-T5M63GX` |
| Status | **Blocked on 3DS** — Revolut ACS timeout; requires approve-in-Revolut-app on the user's paired device, which a background agent cannot do |

**→ To finalise the order (≈30 seconds):** open the [x-kom product page](https://www.x-kom.pl/p/726238-inteligentny-zamek-nuki-opener-bialy.html),
click *Dodaj do koszyka* twice, *Koszyk* → *Kontynuuj bez logowania*, pick card or BLIK,
accept the ToS checkbox, *Kupuję i płacę*, confirm 3DS in the Revolut app.

Alternative payment methods on the same checkout that bypass 3DS:
- **Przelew tradycyjny** (bank transfer) — arrives 1–2 business days later
- **Przy odbiorze** (cash on delivery) — +5 PLN fee
- **BLIK** — instant, requires 6-digit code from bank app

---

## Installation — Nuki Opener on Fermax 80447

### Prerequisites

**Branch-point test first:** with the handset on the cradle, during an incoming ring,
press the blue *key* button. Does the door open?

- **YES** → simple install. Skip hook-switch workaround.
- **NO** → tape/wedge the handset up off the cradle to keep P1 open. Alternative
  solution to the same problem is the DIY board below with its optional second relay
  tapping P1 directly.

### Wiring (5 min)

Three wires from Nuki Opener into CN1 on the Fermax phone:

| Fermax pin | Function | Nuki lead |
|----|----|----|
| **1** | Door opener (Abrepuertas) | red (DOOR) |
| **3** | Common / ground | black (COMMON) |
| **4** | Electronic Call | blue (RING) |

No soldering on the Fermax PCB. Each wire tucks under the existing CN1 screw alongside
the wall wire and tightens down. Reversal is <5 min: loosen three screws, pull leads.

### Pairing

1. Insert 4×AAA batteries in Opener
2. `Add device → Opener` in Nuki app (iOS/Android)
3. Hold Opener button to enter pairing mode
4. Pick intercom: Fermax → **"VDS BASIC LOFT TELEPHONE"** profile (per forum; not CityMax Basic, despite the name mismatch — this is the one that works on 80447)
5. *Settings → Ring to Open → Enable*
6. Test from outdoor panel

---

## DIY fallback (if Nuki profile selection doesn't work)

Full schematic: [schematic.svg](schematic.svg)

Self-powered from the ring pulse (pin 4↔3 on CN1), galvanic isolation both sides:

- **Input protection:** 50 mA polyfuse + 18 V TVS clamp on the sense line
- **Sense:** PC817 optocoupler with 2.2 kΩ primary-side resistor
- **Power:** DB107 bridge rectifier + 470 µF bulk cap + LM2936Z-5 LDO → 5 V logic rail
- **Timing:** NE556 dual monostable — 1.5 s delay (clears off-hook settling window) + 1.5 s pulse (matches ESPBell-LITE tested value)
- **Output:** 5 V relay (Omron G5V-1) driven by 2N3904, dry contacts across pins 1↔3
- **UX:** 6 mm SPST toggle for enable/disable, red LED on ring detect
- **Optional:** second dry-contact relay + alligator-clip leads for tapping P1 hook-switch

### BOM (TME.eu — Łódź, next-day shipping within PL)

| Qty | Component | Example part | PLN |
|-----|-----------|--------------|-----|
| 1 | NE556 dual timer | TI NE556P | 3 |
| 1 | PC817 optocoupler | Sharp PC817 | 2 |
| 1 | Omron G5V-1 5 V relay | G5V-1-5V | 12 |
| 1 | DB107 bridge rectifier | DB107 | 1.5 |
| 1 | LM2936Z-5 LDO | LM2936Z-5.0 | 6 |
| 1 | 18 V TVS diode | P6KE18A | 1 |
| 1 | Polyfuse 50 mA | MF-R005 | 2 |
| 1 | 2N3904 NPN | 2N3904 | 1 |
| 1 | 1N4148 flyback diode | 1N4148 | 0.2 |
| 1 | 470 µF 25 V electrolytic | any | 1.5 |
| 1 | Resistor kit 1/4 W | assortment | 15 |
| 1 | Toggle SPST 6 mm | any | 5 |
| 1 | 5 mm red LED + 1 kΩ | | 1 |
| 3 | Screw terminal 2.54 mm 2-pos | | 2 |
| 1 | Kradex Z-31 ABS enclosure 60×40×25 | | 7 |
| 1 | Perfboard 50×70 mm | | 4 |
| 3 m | 24 AWG silicone wire (3 colours) | | 10 |
| 1 set | Alligator-clip test leads | | 5 |
| | **Total** | | **~80** |
| | + TME shipping (Paczkomat) | | ~12 |
| | **Landed** | | **~92 PLN** |

---

## Budget reconciliation

| Item | PLN |
|------|-----|
| 2× Nuki Opener (x-kom, free delivery) | 798 |
| DIY backup kit (TME, optional) | 92 |
| **Total planned** | **890** |
| Budget floor / ceiling | 1000 / 2000 |
| Headroom vs ceiling | +1110 |

Under budget by design. Adding a JLCPCB PCBA run (5× assembled boards, ~300 PLN)
would still fit but adds 2–3 weeks lead time for a path that almost certainly won't
be needed given Nuki's high compatibility.

---

## Design choices & rationale

- **Door pulse 1500 ms, not the original spec's 500 ms** — per tested reference design
  ([ESPBell-LITE](https://github.com/pesh000/ESPHOME-DoorbellLite)), 500 ms is marginal
  on 4+N bus. 1500 ms is the documented working value.
- **Ring-to-open delay 1500 ms, not 400 ms** — clears the documented ~1 s off-hook
  settling window on analog 4+N systems
  ([reprapy.pl analysis of Proel PC512](https://reprapy.pl/viewtopic.php?t=5200)).
- **556 dual timer, not ATmega328P + firmware** — cheaper, no flashing step, both
  timings trimmable by swapping 0603 R/C. Dropped in favour of all-hardware since
  Nuki is the primary path and the DIY fallback should be maximally simple.
- **Illuminated-button current leakage mitigation** — if phantom rings happen, add a
  10 kΩ bleed resistor across pins 4↔3 or disable the outdoor-panel light.
- **Self-powered from the call pulse** — untested in the wild for 80447, all known
  4+N automation projects use external 5 V. Listed as known risk; fall-back is a
  5 V micro-USB wall wart to the same Nuki or to the DIY board.

---

## Reversibility guarantee

- Nuki Opener: loosen 3 CN1 screws, pull 3 wires, peel 3M adhesive. <5 min.
- DIY board: same — it lives entirely on CN1 taps, no Fermax PCB modification.
- Handset tape (if needed): remove foam. Instant.

---

## Research sources (primary)

- [Nuki Opener compatibility PDF](https://media.home2link.nl/Nuki/Nuki%20Opener/Nuki%20Opener%20Compatibility%20list%20tm%2020-12-19.pdf)
- [Nuki developer forum — Fermax installs](https://developer.nuki.io/t/opener-installation-fermax/17423)
- [ESPBell-LITE (closest 4+N reference design)](https://github.com/pesh000/ESPHOME-DoorbellLite)
- [ESPBell-MAX (assembled but HA-only)](https://www.pricelesstoolkit.com/en/assembled-pcbs/37-espbell-max-intercom-doorbell-module-0741049314467.html)
- [roscoe81/Doorbell-Monitor (RPi 4+N reference)](https://github.com/roscoe81/Doorbell-Monitor)
- [elektroda.pl topic 3933004 — Fermax 80447 wiring](https://www.elektroda.pl/rtvforum/topic3933004.html)
- [elektroda.pl topic 3978834 — universal auto-open discussion](https://www.elektroda.pl/rtvforum/topic3978834.html)
- [reprapy.pl — ESP8266 auto-opener for Proel PC512](https://reprapy.pl/viewtopic.php?t=5200)
- [Fermax CityMax Basic 4+N install manual (ManualsLib)](https://www.manualslib.com/manual/2090537/Fermax-Citymax-Basic-4Plusn.html)

---

_Source issue: c4d5d313. Total research cost: ~$4 (3 parallel web sub-agents + build)._
