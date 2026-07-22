import pcbnew
from pathlib import Path

PCB_PATH = Path(r"d:\UPES\Projects\Pill Despensor\Pill_Dispenser_V3\Pill_Dispenser_V3.kicad_pcb")


def add_edge_rect(board: pcbnew.BOARD, x0: float, y0: float, x1: float, y1: float):
    segments = [
        (x0, y0, x1, y0),
        (x1, y0, x1, y1),
        (x1, y1, x0, y1),
        (x0, y1, x0, y0),
    ]
    for sx, sy, ex, ey in segments:
        shape = pcbnew.PCB_SHAPE(board)
        shape.SetShape(pcbnew.SHAPE_T_SEGMENT)
        shape.SetStart(pcbnew.VECTOR2I_MM(sx, sy))
        shape.SetEnd(pcbnew.VECTOR2I_MM(ex, ey))
        shape.SetLayer(pcbnew.Edge_Cuts)
        shape.SetWidth(pcbnew.FromMM(0.1))
        board.Add(shape)


def add_keepout(board: pcbnew.BOARD, x0: float, y0: float, x1: float, y1: float):
    zone = pcbnew.ZONE(board)
    zone.SetIsRuleArea(True)
    zone.SetDoNotAllowCopperPour(True)
    zone.SetDoNotAllowTracks(False)
    zone.SetDoNotAllowVias(False)
    zone.SetDoNotAllowPads(False)
    zone.SetRuleAreaPlacementEnabled(False)
    zone.SetLayerSet(pcbnew.LSET.AllCuMask())
    outline = zone.Outline()
    outline.NewOutline()
    for x, y in [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]:
        outline.Append(pcbnew.VECTOR2I_MM(x, y))
    board.Add(zone)


def main():
    board = pcbnew.LoadBoard(str(PCB_PATH))

    edge_items = [d for d in board.GetDrawings() if d.GetLayer() == pcbnew.Edge_Cuts]
    for item in edge_items:
        board.Delete(item)

    while board.GetAreaCount() > 0:
        board.Delete(board.GetArea(0))

    add_edge_rect(board, 0, 0, 100, 80)

    u1 = board.FindFootprintByReference("U1")
    if u1 is None:
        raise RuntimeError("U1 not found")
    u1.SetPosition(pcbnew.VECTOR2I_MM(75, 35))

    add_keepout(board, 68, 15, 100, 55)

    pcbnew.SaveBoard(str(PCB_PATH), board)
    print(f"Updated board: {PCB_PATH}")
    print("New outline: (0,0) to (100,80) mm")
    print("U1 moved to: (75,35) mm")
    print("Keepout moved to: (68,15) to (100,55) mm")


if __name__ == "__main__":
    main()
