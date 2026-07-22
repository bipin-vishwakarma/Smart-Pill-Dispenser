from pathlib import Path

import pcbnew


PCB_PATH = Path(r"d:\UPES\Projects\Pill Despensor\Pill_Dispenser_V3\Pill_Dispenser_V3.kicad_pcb")
FOOTPRINT_ROOT = Path(r"C:\Program Files\KiCad\9.0\share\kicad\footprints")
BOARD_W_MM = 80.0
BOARD_H_MM = 60.0
MIN_GAP_MM = 2.0
Y_MIN_MM = 2.0
Y_MAX_MM = 55.0


COMPONENTS = [
    {"ref": "U1", "value": "ESP32-S3-WROOM-1", "x": 62, "y": 30, "rot": 0, "options": [("RF_Module.pretty", "ESP32-S3-WROOM-1"), ("RF_Module.pretty", "ESP32-WROOM-32")]},
    {"ref": "J1", "value": "USB-C", "x": 6, "y": 8, "rot": 270, "options": [("Connector_USB.pretty", "USB_C_Receptacle_GCT_USB4135-GF-A_6P_TopMnt_Horizontal"), ("Connector_USB.pretty", "USB_C_Receptacle_HRO_TYPE-C-31-M-12")]},
    {"ref": "U3", "value": "TP4056", "x": 6, "y": 22, "rot": 0, "options": [("Package_SO.pretty", "SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm_ThermalVias"), ("Package_SO.pretty", "SOIC-8_3.9x4.9mm_P1.27mm")]},
    {"ref": "U4", "value": "AP2112K", "x": 6, "y": 35, "rot": 0, "options": [("Package_TO_SOT_SMD.pretty", "SOT-23-5"), ("Package_TO_SOT_SMD.pretty", "SOT-23")]},
    {"ref": "J4", "value": "BATTERY", "x": 70, "y": 56, "rot": 90, "options": [("Connector_JST.pretty", "JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical"), ("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x02_P2.54mm_Vertical")]},
    {"ref": "D3", "value": "1N5819", "x": 16, "y": 48, "rot": 0, "options": [("Diode_SMD.pretty", "D_SMA"), ("Diode_SMD.pretty", "D_SOD-123")]},
    {"ref": "SW4", "value": "PWR_SW", "x": 16, "y": 53, "rot": 0, "options": [("Button_Switch_THT.pretty", "SW_E-Switch_EG1224_SPDT_Angled"), ("Button_Switch_THT.pretty", "SW_SPDT_PCM12")]},
    {"ref": "C10", "value": "100uF", "x": 16, "y": 35, "rot": 0, "options": [("Capacitor_SMD.pretty", "CP_Elec_6.3x5.4"), ("Capacitor_SMD.pretty", "C_1206_3216Metric")]},
    {"ref": "R5", "value": "2k", "x": 16, "y": 22, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "C1", "value": "10uF", "x": 22, "y": 10, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "C2", "value": "10uF", "x": 22, "y": 16, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "R11", "value": "5.1k", "x": 22, "y": 22, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R12", "value": "5.1k", "x": 22, "y": 28, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R15", "value": "22", "x": 28, "y": 22, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R16", "value": "22", "x": 28, "y": 28, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "C5", "value": "100nF", "x": 34, "y": 24, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "C6", "value": "100nF", "x": 40, "y": 24, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "C7", "value": "100nF", "x": 40, "y": 30, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "C8", "value": "100nF", "x": 40, "y": 36, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "C9", "value": "10uF", "x": 40, "y": 42, "rot": 0, "options": [("Capacitor_SMD.pretty", "C_0603_1608Metric")]},
    {"ref": "R8", "value": "10k", "x": 40, "y": 48, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R17", "value": "10k", "x": 46, "y": 48, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "SW2", "value": "BOOT", "x": 46, "y": 54, "rot": 0, "options": [("Button_Switch_SMD.pretty", "SW_SPST_EVQP0")]},
    {"ref": "SW3", "value": "RESET", "x": 55, "y": 54, "rot": 0, "options": [("Button_Switch_SMD.pretty", "SW_SPST_EVQP0")]},
    {"ref": "SW1", "value": "USER", "x": 64, "y": 54, "rot": 0, "options": [("Button_Switch_SMD.pretty", "SW_SPST_EVQP0")]},
    {"ref": "J3", "value": "OLED", "x": 73, "y": 38, "rot": 90, "options": [("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x04_P2.54mm_Vertical")]},
    {"ref": "J2", "value": "SERVO", "x": 73, "y": 50, "rot": 90, "options": [("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x03_P2.54mm_Vertical")]},
    {"ref": "BZ1", "value": "Buzzer", "x": 22, "y": 40, "rot": 0, "options": [("Buzzer_Beeper.pretty", "MagneticBuzzer_Kingstate_KCG0601")]},
    {"ref": "Q1", "value": "MMBT2222A", "x": 28, "y": 44, "rot": 0, "options": [("Package_TO_SOT_SMD.pretty", "SOT-23")]},
    {"ref": "R4", "value": "1k", "x": 34, "y": 44, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "D1", "value": "LED STATUS", "x": 34, "y": 10, "rot": 0, "options": [("LED_SMD.pretty", "LED_0603_1608Metric")]},
    {"ref": "D4", "value": "LED CHG", "x": 34, "y": 16, "rot": 0, "options": [("LED_SMD.pretty", "LED_0603_1608Metric")]},
    {"ref": "D5", "value": "LED STDBY", "x": 34, "y": 22, "rot": 0, "options": [("LED_SMD.pretty", "LED_0603_1608Metric")]},
    {"ref": "R1", "value": "330R", "x": 34, "y": 28, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R2", "value": "330R", "x": 34, "y": 34, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R13", "value": "330R", "x": 34, "y": 38, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R14", "value": "330R", "x": 34, "y": 42, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R6", "value": "4.7k SDA", "x": 34, "y": 18, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R7", "value": "4.7k SCL", "x": 46, "y": 24, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R9", "value": "100k", "x": 46, "y": 30, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
    {"ref": "R10", "value": "100k", "x": 46, "y": 36, "rot": 0, "options": [("Resistor_SMD.pretty", "R_0603_1608Metric")]},
]


def add_board_outline(board: pcbnew.BOARD):
    edges = [
        (0, 0, BOARD_W_MM, 0),
        (BOARD_W_MM, 0, BOARD_W_MM, BOARD_H_MM),
        (BOARD_W_MM, BOARD_H_MM, 0, BOARD_H_MM),
        (0, BOARD_H_MM, 0, 0),
    ]
    for sx, sy, ex, ey in edges:
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetStart(pcbnew.VECTOR2I_MM(sx, sy))
        seg.SetEnd(pcbnew.VECTOR2I_MM(ex, ey))
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(pcbnew.FromMM(0.1))
        board.Add(seg)


def add_keepout(board: pcbnew.BOARD, x0: float, y0: float, x1: float, y1: float):
    zone = pcbnew.ZONE(board)
    zone.SetIsRuleArea(True)
    zone.SetDoNotAllowCopperPour(True)
    zone.SetDoNotAllowTracks(False)
    zone.SetDoNotAllowVias(False)
    zone.SetDoNotAllowPads(False)
    zone.SetRuleAreaPlacementEnabled(True)
    zone.SetLayerSet(pcbnew.LSET.AllCuMask())
    outline = zone.Outline()
    outline.NewOutline()
    for x, y in [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]:
        outline.Append(pcbnew.VECTOR2I_MM(x, y))
    board.Add(zone)


def load_footprint(options: list[tuple[str, str]]):
    for pretty, name in options:
        footprint = pcbnew.FootprintLoad(str(FOOTPRINT_ROOT / pretty), name)
        if footprint is not None:
            return footprint, f"{pretty}:{name}"
    return None, ""


def place_footprints(board: pcbnew.BOARD):
    placed = []
    failed = []
    for spec in COMPONENTS:
        footprint, source = load_footprint(spec["options"])
        if footprint is None:
            failed.append(spec["ref"])
            continue
        footprint.SetReference(spec["ref"])
        footprint.SetValue(spec["value"])
        footprint.SetOrientationDegrees(spec["rot"])
        footprint.SetPosition(pcbnew.VECTOR2I_MM(spec["x"], spec["y"]))
        board.Add(footprint)
        placed.append((spec["ref"], source))
    return placed, failed


def hide_silkscreen(board: pcbnew.BOARD):
    for footprint in board.GetFootprints():
        if footprint.Reference() is not None:
            footprint.Reference().SetVisible(False)
        if footprint.Value() is not None:
            footprint.Value().SetVisible(False)
        for item in footprint.GraphicalItems():
            if item.GetLayer() == pcbnew.F_SilkS:
                item.SetLayer(pcbnew.F_Fab)
            elif item.GetLayer() == pcbnew.B_SilkS:
                item.SetLayer(pcbnew.B_Fab)


def ensure_nets(board: pcbnew.BOARD, names: list[str]):
    result = {}
    existing = board.GetNetsByName()
    for name in names:
        if name in existing:
            result[name] = existing[name]
        else:
            net = pcbnew.NETINFO_ITEM(board, name)
            board.Add(net)
            result[name] = net
    return result


def set_j1_nets(board: pcbnew.BOARD):
    j1 = board.FindFootprintByReference("J1")
    if j1 is None:
        return None
    nets = ensure_nets(board, ["GND", "VBUS", "D+", "D-", "CC1", "CC2"])
    mapping = {
        "GND": {"A1", "B1", "A12"},
        "VBUS": {"A4", "B4", "A9"},
        "D+": {"A6", "B6"},
        "D-": {"A7", "B7"},
        "CC1": {"A5"},
        "CC2": {"B5"},
    }
    for pad in j1.Pads():
        number = pad.GetNumber()
        pad.SetLocalSolderMaskMargin(0)
        for net_name, members in mapping.items():
            if number in members:
                pad.SetNet(nets[net_name])
                break
    return j1


def pad_map(footprint: pcbnew.FOOTPRINT):
    result = {}
    for pad in footprint.Pads():
        if pad.GetNumber() and pad.GetNumber() not in result:
            result[pad.GetNumber()] = pad
    return result


def add_track(board: pcbnew.BOARD, net: pcbnew.NETINFO_ITEM, start: pcbnew.VECTOR2I, end: pcbnew.VECTOR2I, width_mm: float):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(start)
    track.SetEnd(end)
    track.SetLayer(pcbnew.F_Cu)
    track.SetWidth(pcbnew.FromMM(width_mm))
    track.SetNet(net)
    board.Add(track)


def add_j1_bridges(board: pcbnew.BOARD):
    return


def clear_existing_j1_bridges(board: pcbnew.BOARD):
    j1 = board.FindFootprintByReference("J1")
    if j1 is None:
        return
    pad_positions = set()
    for pad in j1.Pads():
        num = pad.GetNumber()
        if num in {"A4", "B4", "A1", "B1", "A6", "B6", "A7", "B7", "A9", "B9", "A12", "B12"}:
            pad_positions.add((pad.GetPosition().x, pad.GetPosition().y))
    to_remove = []
    for track in board.GetTracks():
        if not isinstance(track, pcbnew.PCB_TRACK):
            continue
        s = (track.GetStart().x, track.GetStart().y)
        e = (track.GetEnd().x, track.GetEnd().y)
        if s in pad_positions and e in pad_positions:
            to_remove.append(track)
    for track in to_remove:
        board.Remove(track)


def enforce_min_drill(board: pcbnew.BOARD, minimum_mm: float = 0.3):
    minimum = pcbnew.FromMM(minimum_mm)
    for footprint in board.GetFootprints():
        for pad in footprint.Pads():
            drill = pad.GetDrillSize()
            if drill.x <= 0 and drill.y <= 0:
                continue
            new_x = drill.x
            new_y = drill.y
            if 0 < drill.x < minimum:
                new_x = minimum
            if 0 < drill.y < minimum:
                new_y = minimum
            if new_x != drill.x or new_y != drill.y:
                pad.SetDrillSize(pcbnew.VECTOR2I(new_x, new_y))


def bboxes_overlap(a: pcbnew.BOX2I, b: pcbnew.BOX2I, gap_mm: float):
    gap = pcbnew.FromMM(gap_mm / 2.0)
    ax0, ay0, ax1, ay1 = a.GetX() - gap, a.GetY() - gap, a.GetRight() + gap, a.GetBottom() + gap
    bx0, by0, bx1, by1 = b.GetX() - gap, b.GetY() - gap, b.GetRight() + gap, b.GetBottom() + gap
    return not (ax1 < bx0 or bx1 < ax0 or ay1 < by0 or by1 < ay0)


def check_constraints(board: pcbnew.BOARD):
    issues = []
    footprints = list(board.GetFootprints())
    for footprint in footprints:
        ref = footprint.GetReference()
        y = pcbnew.ToMM(footprint.GetPosition().y)
        if y < Y_MIN_MM or y > Y_MAX_MM:
            issues.append(f"Y range violation: {ref} at y={y:.2f} mm")

    for index, footprint_a in enumerate(footprints):
        for footprint_b in footprints[index + 1:]:
            if bboxes_overlap(footprint_a.GetBoundingBox(), footprint_b.GetBoundingBox(), MIN_GAP_MM):
                issues.append(f"Min-gap violation (< {MIN_GAP_MM} mm): {footprint_a.GetReference()} vs {footprint_b.GetReference()}")

    return issues


def main():
    board = pcbnew.BOARD()
    add_board_outline(board)
    add_keepout(board, 44, 2, 80, 20)
    placed, failed = place_footprints(board)
    hide_silkscreen(board)
    set_j1_nets(board)
    clear_existing_j1_bridges(board)
    add_j1_bridges(board)
    enforce_min_drill(board, minimum_mm=0.3)
    issues = check_constraints(board)
    pcbnew.SaveBoard(str(PCB_PATH), board)

    print(f"PCB generated: {PCB_PATH}")
    print(f"Placed footprints: {len(placed)}")
    for ref, source in placed:
        print(f"  {ref} <- {source}")
    if failed:
        print(f"Failed footprints: {len(failed)}")
        for ref in failed:
            print(f"  {ref}")
    print(f"Constraint issues: {len(issues)}")
    for issue in issues:
        print(f"  {issue}")


if __name__ == "__main__":
    main()
