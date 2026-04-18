"""
Fermax DIY adapter PCB v3 — larger board (90x70), spaced placement, no overlaps.
Through-hole only. Critical power traces routed; signal traces left as airwire
guidance for hand-assembly with thin wire on B.Cu side.
"""
import sys, os
sys.path.insert(0, '/Users/kolinko/Applications/KiCad.app/Contents/Frameworks/python.framework/Versions/3.9/lib/python3.9/site-packages')
import pcbnew
from pcbnew import VECTOR2I, FromMM, EDA_ANGLE

FP_LIB = "/Users/kolinko/Applications/KiCad.app/Contents/SharedSupport/footprints"
def mm(x): return FromMM(x)
def pt(x, y): return VECTOR2I(mm(x), mm(y))

def add_fp(board, lib, name, ref, value, x, y, angle=0):
    fp = pcbnew.FootprintLoad(f"{FP_LIB}/{lib}.pretty", name)
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetPosition(pt(x, y))
    if angle: fp.SetOrientation(EDA_ANGLE(angle, pcbnew.DEGREES_T))
    board.Add(fp); return fp

def track(board, x1, y1, x2, y2, layer=pcbnew.F_Cu, w=0.5):
    t = pcbnew.PCB_TRACK(board); t.SetStart(pt(x1, y1)); t.SetEnd(pt(x2, y2))
    t.SetWidth(mm(w)); t.SetLayer(layer); board.Add(t); return t

def via(board, x, y, drill=0.4, dia=0.8):
    v = pcbnew.PCB_VIA(board); v.SetPosition(pt(x, y)); v.SetWidth(mm(dia))
    v.SetDrill(mm(drill)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); board.Add(v)

def outline(board, w, h):
    pts = [(0, 0), (w, 0), (w, h), (0, h), (0, 0)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        s = pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_SEGMENT)
        s.SetStart(pt(x1, y1)); s.SetEnd(pt(x2, y2)); s.SetWidth(mm(0.15))
        s.SetLayer(pcbnew.Edge_Cuts); board.Add(s)

def silk(board, x, y, text, size=0.8, layer=pcbnew.F_SilkS):
    t = pcbnew.PCB_TEXT(board); t.SetText(text); t.SetPosition(pt(x, y))
    t.SetTextSize(VECTOR2I(mm(size), mm(size))); t.SetLayer(layer); board.Add(t)

def pad(fp, n):
    p = fp.FindPadByNumber(str(n))
    if p is None: return None
    pos = p.GetPosition()
    return (pcbnew.ToMM(pos.x), pcbnew.ToMM(pos.y))

# ==========================================
board = pcbnew.BOARD()
BW, BH = 92.0, 78.0
outline(board, BW, BH)

# Mounting holes inside the board (4mm clearance from edge so M3 head doesn't overhang)
for x, y in [(4.0, 4.0), (BW-4.0, 4.0), (4.0, BH-4.0), (BW-4.0, BH-4.0)]:
    add_fp(board, "MountingHole", "MountingHole_3.2mm_M3", "MH", "M3", x, y)

# === Top row: Power & input ===
# J1 input terminal - vertical pads
J1 = add_fp(board, "TerminalBlock", "TerminalBlock_MaiXu_MX126-5.0-02P_1x02_P5.00mm",
            "J1", "FERMAX 4-3", 8.0, 18.0, 90)
silk(board, 8.0, 12.5, "J1 IN", 0.9)
silk(board, 8.0, 24.0, "P4 P3", 0.6)

# F1 polyfuse
F1 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "F1", "MFR050", 22.0, 15.5)
silk(board, 22.0, 12.5, "F1 50mA", 0.7)

# TVS clamp - vertical between p4 and p3 nets
TVS1 = add_fp(board, "Diode_THT", "D_DO-41_SOD81_P10.16mm_Horizontal",
              "TVS1", "P6KE18A", 33.0, 18.5, 90)
silk(board, 38.0, 18.5, "TVS1 18V", 0.6)

# BR1 bridge rectifier
BR1 = add_fp(board, "Diode_THT", "Diode_Bridge_DIP-4_W7.62mm_P5.08mm",
             "BR1", "DB107", 43.0, 18.5)
silk(board, 43.0, 12.0, "BR1", 0.7)

# C1 bulk cap
C1 = add_fp(board, "Capacitor_THT", "CP_Radial_D8.0mm_P3.50mm",
            "C1", "470uF", 54.0, 18.5)
silk(board, 54.0, 12.5, "C1 470µF", 0.7)

# U1 LDO TO-92
U1 = add_fp(board, "Package_TO_SOT_THT", "TO-92_Inline",
            "U1", "MCP1700-5002", 64.0, 18.5)
silk(board, 64.0, 13.5, "U1", 0.7)

# C2 LDO output cap
C2 = add_fp(board, "Capacitor_THT", "C_Disc_D5.0mm_W2.5mm_P5.00mm",
            "C2", "1uF", 68.0, 18.5)
silk(board, 68.0, 13.5, "C2", 0.7)

# SW1 enable header
SW1 = add_fp(board, "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical",
             "SW1", "ENABLE", 80.0, 18.0)
silk(board, 80.0, 12.5, "SW1", 0.7)

# === Middle row: opto, R1, R2, status LED ===
R1 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R1", "2.2k", 22.0, 32.0)
silk(board, 22.0, 29.0, "R1 2.2k", 0.6)

OK1 = add_fp(board, "Package_DIP", "DIP-4_W7.62mm",
             "OK1", "PC817", 33.0, 32.0)
silk(board, 33.0, 27.0, "OK1 PC817", 0.7)

R2 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R2", "10k", 44.0, 32.0)
silk(board, 44.0, 29.0, "R2 10k", 0.6)

LED1 = add_fp(board, "LED_THT", "LED_D5.0mm",
              "LED1", "RED", 76.0, 32.0)
silk(board, 76.0, 27.5, "LED1 RING", 0.6)
R7 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R7", "1k", 76.0, 38.0, 90)
silk(board, 80.0, 38.0, "R7 1k", 0.6)

# === U3 NE556 timer (DIP-14) — center ===
U3 = add_fp(board, "Package_DIP", "DIP-14_W7.62mm",
            "U3", "NE556", 56.0, 36.0)
silk(board, 56.0, 28.5, "U3 NE556", 0.9)

# C7 AC-couple between OUT_A and TRIG_B
C7 = add_fp(board, "Capacitor_THT", "C_Disc_D3.8mm_W2.6mm_P2.50mm",
            "C7", "10nF", 65.0, 32.0)
silk(board, 65.0, 29.5, "C7", 0.6)

R6 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R6", "10k", 65.0, 36.5, 90)
silk(board, 69.0, 36.5, "R6", 0.6)

# === Bottom row: timing + driver + relay ===
R3 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R3", "1M", 50.0, 47.0)
silk(board, 50.0, 50.0, "R3 1M", 0.6)
C4 = add_fp(board, "Capacitor_THT", "C_Disc_D5.0mm_W2.5mm_P5.00mm",
            "C4", "1.5uF", 50.0, 53.0)
silk(board, 50.0, 56.0, "C4", 0.6)

R5 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R5", "1M", 64.0, 47.0)
silk(board, 64.0, 50.0, "R5 1M", 0.6)
C5 = add_fp(board, "Capacitor_THT", "C_Disc_D5.0mm_W2.5mm_P5.00mm",
            "C5", "1.5uF", 64.0, 53.0)
silk(board, 64.0, 56.0, "C5", 0.6)

R8 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R8", "1k", 72.0, 47.0)
silk(board, 72.0, 50.0, "R8 1k", 0.6)
Q1 = add_fp(board, "Package_TO_SOT_THT", "TO-92_Inline",
            "Q1", "2N3904", 80.0, 47.0)
silk(board, 80.0, 51.0, "Q1", 0.6)
D2 = add_fp(board, "Diode_THT", "D_DO-35_SOD27_P7.62mm_Horizontal",
            "D2", "1N4148", 80.0, 53.5)
silk(board, 80.0, 56.0, "D2", 0.6)

# K1 relay + J2 door output - LEFT SIDE bottom row
K1 = add_fp(board, "Relay_THT", "Relay_SPDT_Omron_G5V-1",
            "K1", "G5V-1", 18.0, 48.0)
silk(board, 18.0, 42.5, "K1 DOOR", 0.7)

J2 = add_fp(board, "TerminalBlock", "TerminalBlock_MaiXu_MX126-5.0-02P_1x02_P5.00mm",
            "J2", "DOOR P1-P3", 30.0, 48.0, 90)
silk(board, 30.0, 56.5, "J2 DOOR", 0.7)

# === OPTIONAL P1 path - bottom area, separated ===
JP1 = add_fp(board, "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical",
             "JP1", "P1 EN", 8.0, 64.0)
silk(board, 8.0, 65.5, "JP1 P1-EN (opt)", 0.5)

R9 = add_fp(board, "Resistor_THT", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
            "R9", "1k", 16.0, 64.0)
silk(board, 16.0, 65.5, "R9 (opt)", 0.5)

Q2 = add_fp(board, "Package_TO_SOT_THT", "TO-92_Inline",
            "Q2", "2N3904", 24.0, 64.0)
silk(board, 24.0, 65.5, "Q2 (opt)", 0.5)

D3 = add_fp(board, "Diode_THT", "D_DO-35_SOD27_P7.62mm_Horizontal",
            "D3", "1N4148", 32.0, 64.0)
silk(board, 32.0, 65.5, "D3 (opt)", 0.5)

K2 = add_fp(board, "Relay_THT", "Relay_SPDT_Omron_G5V-1",
            "K2", "G5V-1", 44.0, 64.0)
silk(board, 44.0, 65.5, "K2 P1 (opt)", 0.5)

J3 = add_fp(board, "Connector_PinHeader_2.54mm", "PinHeader_1x02_P2.54mm_Vertical",
            "J3", "P1 LEADS", 56.0, 64.0)
silk(board, 56.0, 65.5, "J3 P1 leads (opt)", 0.5)

# === Title silk ===
silk(board, BW/2, 2.5, "FERMAX 80447 AUTO-OPEN ADAPTER v1 / DIY", 1.1)
silk(board, BW/2, BH-1.5, "kolinko.eu/fermax-adapter/diy   2026-04-18   Claude Opus", 0.7)

# === Routing — power & GND backbone (signal nets left for hand-wire) ===
j1p1, j1p2 = pad(J1, 1), pad(J1, 2)
f1a, f1b = pad(F1, 1), pad(F1, 2)
tvs1_1, tvs1_2 = pad(TVS1, 1), pad(TVS1, 2)
br1_1, br1_2, br1_3, br1_4 = [pad(BR1, n) for n in (1,2,3,4)]
c1_1, c1_2 = pad(C1, 1), pad(C1, 2)
u1_1, u1_2, u1_3 = pad(U1, 1), pad(U1, 2), pad(U1, 3)
c2_1, c2_2 = pad(C2, 1), pad(C2, 2)

# pin4-net: J1-1 → F1-1 → F1-2 → TVS1-top + BR1-1
track(board, j1p1[0], j1p1[1], j1p1[0]+5, j1p1[1], w=0.6)
track(board, j1p1[0]+5, j1p1[1], f1a[0], f1a[1], w=0.6)
track(board, f1b[0], f1b[1], f1b[0]+3, f1b[1], w=0.6)
track(board, f1b[0]+3, f1b[1], f1b[0]+3, tvs1_1[1], w=0.6)
track(board, f1b[0]+3, tvs1_1[1], tvs1_1[0], tvs1_1[1], w=0.6)
track(board, tvs1_1[0], tvs1_1[1], br1_1[0], br1_1[1], w=0.6)

# Tap pin4-net to R1 left
r1a, r1b = pad(R1, 1), pad(R1, 2)
track(board, f1a[0], f1a[1], f1a[0], r1a[1], w=0.5)
track(board, f1a[0], r1a[1], r1a[0], r1a[1], w=0.5)

# pin3-net: J1-2 → TVS1-bot → BR1-3 (AC2)
track(board, j1p2[0], j1p2[1], j1p2[0]+5, j1p2[1], w=0.6)
track(board, j1p2[0]+5, j1p2[1], j1p2[0]+5, tvs1_2[1], w=0.6)
track(board, j1p2[0]+5, tvs1_2[1], tvs1_2[0], tvs1_2[1], w=0.6)
track(board, tvs1_2[0], tvs1_2[1], br1_3[0], br1_3[1], w=0.6)

# Vbus+ rail: BR1-2 → C1-1 → U1-1
track(board, br1_2[0], br1_2[1], br1_2[0]+3, br1_2[1], w=0.6)
track(board, br1_2[0]+3, br1_2[1], br1_2[0]+3, c1_1[1], w=0.6)
track(board, br1_2[0]+3, c1_1[1], c1_1[0], c1_1[1], w=0.6)
track(board, c1_1[0], c1_1[1], u1_1[0], u1_1[1], w=0.6)

# Vbus- rail: BR1-4 → C1-2 → U1-2
track(board, br1_4[0], br1_4[1], br1_4[0]+3, br1_4[1], w=0.6)
track(board, br1_4[0]+3, br1_4[1], br1_4[0]+3, c1_2[1], w=0.6)
track(board, br1_4[0]+3, c1_2[1], c1_2[0], c1_2[1], w=0.6)
track(board, c1_2[0], c1_2[1], u1_2[0], u1_2[1], w=0.6)

# +5V rail: U1-3 → C2-1 → +5V "rail" goes right and below
track(board, u1_3[0], u1_3[1], c2_1[0], c2_1[1], w=0.5)

# +5V to U3 VCC pin 14 (top-right of DIP-14)
u3_14 = pad(U3, 14)
u3_7 = pad(U3, 7)
track(board, c2_1[0], c2_1[1], c2_1[0], 24.0, w=0.5)
track(board, c2_1[0], 24.0, u3_14[0], 24.0, w=0.5)
track(board, u3_14[0], 24.0, u3_14[0], u3_14[1], w=0.5)

# +5V to R2-top (pullup)
r2a, r2b = pad(R2, 1), pad(R2, 2)
track(board, r2a[0], 24.0, r2a[0], r2a[1], w=0.4)
track(board, r2a[0], 24.0, r2b[0], 24.0, w=0.4)  # along +5V rail
# Continue +5V rail from c2 across to LED1 area
led1_a, led1_c = pad(LED1, 1), pad(LED1, 2)
track(board, u3_14[0], 24.0, led1_a[0], 24.0, w=0.4)

# === GND pour on B.Cu (no net assignment — physical isolated copper, will be wired by hand) ===
zone = pcbnew.ZONE(board)
zone.SetLayer(pcbnew.B_Cu)
poly = pcbnew.SHAPE_POLY_SET()
ch = pcbnew.SHAPE_LINE_CHAIN()
for x, y in [(2.0, 2.0), (BW-2.0, 2.0), (BW-2.0, BH-2.0), (2.0, BH-2.0)]:
    ch.Append(mm(x), mm(y))
ch.SetClosed(True)
poly.AddOutline(ch)
zone.SetOutline(poly)
zone.SetMinThickness(mm(0.25))
board.Add(zone)

out = "/Users/kolinko/claude/varia/static/fermax-adapter/diy/kicad/fermax_diy.kicad_pcb"
os.makedirs(os.path.dirname(out), exist_ok=True)
board.Save(out)
print(f"Saved {out}, {len(board.GetFootprints())} footprints, {len(list(board.GetTracks()))} tracks")
