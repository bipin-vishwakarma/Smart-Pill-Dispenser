# Pill Dispenser V4 — Claude Code Complete PCB Finalization
## With All Plugins, Tools & MCP Servers

---

## WHO YOU ARE
Claude Code running inside:
`d:\UPES\Projects\Pill Despensor\Pill_Dispenser_V4\`

You have access to KiCad Python API, KiCad CLI, Java (freerouting),
PowerShell, and ALL plugins listed below. Use them intelligently.

---

## WHAT EXISTS IN THIS FOLDER
```
Pill_Dispenser_V4.kicad_pcb      ← PCB, components placed, no routes
Pill_Dispenser_V4.kicad_sch      ← Schematic, fully wired
Pill_Dispenser_V4.kicad_pro      ← Project file
Pill_Dispenser_V4_compact.dsn    ← Specctra DSN ready for freerouting
freerouting.jar                  ← Autorouter
export_dsn.py                    ← DSN exporter
import_ses.py                    ← SES importer
gap_check_v2.py                  ← Gap checker
draw_outline_v2.py               ← Board outline drawer
placement_v3.py                  ← Placement script
```

---

## TOOLS & EXECUTABLES
```
KiCad Python:  C:\Program Files\KiCad\9.0\bin\python.exe
KiCad CLI:     C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
Java:          java (in PATH)
Freerouting:   java -jar freerouting.jar
PowerShell:    pwsh or powershell
```

---

## ALL INSTALLED KICAD PLUGINS — USE THESE

### 1. FreeRouting Plugin
**What**: KiCad-integrated autorouter (also have standalone JAR)
**Use for**: Full autorouting after placement
**GUI**: PCB Editor → Tools → External Plugins → Freerouting
**CLI**:
```powershell
java -jar freerouting.jar -de input.dsn -do output.ses -mp 3000 -mt 1
```
**When to use**: After all components placed, USB pair manually routed

---

### 2. KiKit
**What**: KiCad automation toolkit — most powerful CLI automation tool
**Use for**: Panelization, board separation, automated workflows
**Install check**: `python -m kikit --version`
**Key commands**:
```powershell
# Panelize board (for ordering multiple PCBs)
python -m kikit panelize \
  --layout 'grid; rows: 2; cols: 2; space: 2mm' \
  --tabs 'fixed; width: 3mm; vcount: 2' \
  --cuts 'mousebites; drill: 0.5mm; spacing: 0.8mm' \
  Pill_Dispenser_V4.kicad_pcb panel.kicad_pcb

# Export fabrication files automatically
python -m kikit fab jlcpcb \
  --assembly \
  --schematic Pill_Dispenser_V4.kicad_sch \
  Pill_Dispenser_V4.kicad_pcb \
  ./kikit_fab_output/
```
**When to use**:
- Task 9: Use `kikit fab jlcpcb` instead of manual gerber export
- After routing: panelize for cheaper JLCPCB ordering

---

### 3. Fabrication Toolkit (JLCPCB)
**What**: Auto-generates JLCPCB-ready gerbers, BOM, CPL in one click
**Use for**: Final production file generation
**GUI**: PCB Editor → Tools → External Plugins → Fabrication Toolkit
**CLI equivalent**:
```powershell
# This plugin generates: gerbers + drill + BOM + CPL
# all formatted exactly for JLCPCB upload
# Trigger via KiCad scripting console:
& "C:\Program Files\KiCad\9.0\bin\python.exe" -c "
import subprocess
subprocess.run(['kicad-cli', 'pcb', 'export', 'gerbers',
  '--output', './fab_output/',
  'Pill_Dispenser_V4.kicad_pcb'])
"
```
**PREFER this over manual gerber export** — formats are guaranteed correct

---

### 4. Interactive HTML BOM
**What**: Generates an interactive BOM webpage for assembly
**Use for**: Manual assembly reference, component sourcing
**GUI**: PCB Editor → Tools → External Plugins → Generate Interactive BOM
**CLI**:
```powershell
# Run ibom generation
& "C:\Program Files\KiCad\9.0\bin\python.exe" `
  "$env:APPDATA\kicad\9.0\scripting\plugins\InteractiveHtmlBom\generate_interactive_bom.py" `
  --no-browser `
  --output-dir "./bom/" `
  "Pill_Dispenser_V4.kicad_pcb"
```
**Output**: `bom/ibom.html` — open in browser, click component to highlight on board

---

### 5. Round Tracks
**What**: Converts 90-degree track corners to smooth arcs
**Use for**: Professional aesthetics + slightly better signal integrity
**GUI**: PCB Editor → Tools → External Plugins → Round Tracks
**Settings**: subdivision=4, min_distance=0.1mm
**CLI/Script**:
```python
# Run AFTER freerouting import, BEFORE final DRC
import pcbnew
import sys
sys.path.append(r"C:\Users\%USERNAME%\AppData\Roaming\kicad\9.0\scripting\plugins")
# trigger via scripting console in KiCad GUI
# Tools → Scripting Console → 
# import round_tracks; round_tracks.RoundTracks().Run()
```
**When to use**: Task after importing SES, before DRC

---

### 6. Teardrops (Native KiCad 9)
**What**: Adds teardrop reinforcement at pad-to-trace junctions
**Use for**: Manufacturing reliability, prevents pad lifting
**GUI**: PCB Editor → Edit → Edit Teardrops → Add to All → Apply
**Script**:
```python
import pcbnew
board = pcbnew.LoadBoard("Pill_Dispenser_V4.kicad_pcb")
# KiCad 9 native teardrops via DRC settings
# or use Edit menu in GUI — takes 10 seconds
board.Save("Pill_Dispenser_V4.kicad_pcb")
```
**When to use**: After routing, before DRC

---

### 7. Place Footprints Plugin
**What**: Arrange footprints on a line, circle or grid automatically
**Use for**: Auto-arranging passives in a tight grid
**GUI**: PCB Editor → Tools → External Plugins → Place Footprints
**When to use**: If passives need re-gridding after routing conflicts

---

### 8. Parts Placer
**What**: Declarative placement using a spreadsheet/CSV
**Use for**: Precise placement from coordinates in a CSV file
**CSV format**:
```csv
Reference,X,Y,Rotation,Layer
J1,3,28,270,F.Cu
U1,47,30,0,F.Cu
U3,20,28,0,F.Cu
```
**When to use**: Alternative to Python placement script — more readable

---

### 9. PosOrient
**What**: Positioning and Orientation tool for footprints
**Use for**: Batch rotate/flip components, align to grid
**GUI**: PCB Editor → Tools → External Plugins → PosOrient
**When to use**: If components need orientation fixes before routing

---

### 10. pcb2blender
**What**: Exports KiCad PCB to Blender for photorealistic 3D render
**Use for**: Product renders, documentation, presentation
**GUI**: PCB Editor → Tools → External Plugins → pcb2blender
**CLI**:
```powershell
# Export STEP first, then import to Blender
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb export step `
  --output "Pill_Dispenser_V4_3D.step" `
  "Pill_Dispenser_V4.kicad_pcb"
```
**When to use**: After final DRC passes — for documentation

---

### 11. HierarchicalPCB
**What**: Enforces sub-PCB layouts for hierarchical schematics
**Use for**: Not needed for this single-sheet design
**Skip for this project**

---

### 12. Bakery
**What**: Localizes KiCad symbols, footprints and 3D models
**Use for**: Ensuring all footprints have local copies (no missing 3D)
**GUI**: PCB Editor → Tools → External Plugins → Bakery
**When to use**: Before final export to ensure 3D models are embedded

---

### 13. Skyline Theme
**What**: Altium-inspired dark theme for KiCad
**Use for**: Visual aesthetics only
**Skip for automation**

---

### 14. Git Plugin
**What**: Git integration inside KiCad
**Use for**: Version control of PCB files
**CLI** (use directly, better):
```powershell
git add Pill_Dispenser_V4.kicad_pcb
git add Pill_Dispenser_V4.kicad_sch
git commit -m "routed PCB v4 compact layout 80x68mm"
```
**When to use**: After each major milestone

---

### 15. Set Hole Diameter
**What**: Sets drill hole diameter for all pads to specified value
**Use for**: Fixing drill_out_of_range DRC errors in batch
**GUI**: PCB Editor → Tools → External Plugins → Set Hole Diameter
**Settings**: Set to 0.3mm minimum
**When to use**: If DRC shows drill_out_of_range errors

---

### 16. kicad_ai_plugin
**What**: AI assistant inside KiCad
**Use for**: Ask it to help with routing decisions, DRC fixes
**GUI**: PCB Editor → Tools → External Plugins → KiCad AI
**When to use**: If stuck on specific routing problems

---

## MCP SERVERS — USE IF CONNECTED

If any MCP servers are connected in your Claude Code session,
use them for these tasks:

### File System MCP
```
Use for: Reading/writing PCB files, scripts, gerbers
Commands: read_file, write_file, list_directory
Prefer over: manual file operations
```

### GitHub/Git MCP
```
Use for: Committing PCB milestones, creating releases
Commands: git_commit, git_push, create_release
When: After each task milestone
```

### Sequential Thinking MCP
```
Use for: Complex routing decisions, DRC debugging
When: Before writing any complex script
Pattern: think step by step before coding
```

### Memory MCP
```
Use for: Remembering component positions, net names
Store: ESP32 pin coordinates, USB net names, keep-out bounds
```

---

## BOARD SPECS (REFERENCE)
```
Board size:        ~80 x 68mm (auto from bounding box)
Layers:            2 (F.Cu front, B.Cu back)
ESP32 position:    x=47mm, y=30mm
Antenna keep-out:  x=59..79mm, y=25..55mm — NOTHING HERE EVER
USB-C J1:          x=3mm, y=28mm, flush left edge
Servo J2:          x=70mm, y=15mm, right side
OLED J3:           x=70mm, y=38mm, right side
Battery J4:        x=5mm, y=42mm, left side
Min track width:   0.2mm signal, 0.4mm power
Min clearance:     0.15mm
Min drill:         0.2mm
```

---

## TASK ORDER — EXECUTE SEQUENTIALLY

### TASK 1 — Verify & Clean State
```powershell
& "C:\Program Files\KiCad\9.0\bin\python.exe" -c "
import pcbnew
b = pcbnew.LoadBoard('Pill_Dispenser_V4.kicad_pcb')
fps = list(b.GetFootprints())
tracks = list(b.GetTracks())
print(f'Components: {len(fps)}')
print(f'Tracks: {len(tracks)}')
print(f'Nets: {len(b.GetNets())}')
print(f'Zones: {len(list(b.Zones()))}')
for fp in fps:
    pos = fp.GetPosition()
    print(f'  {fp.GetReference():8s} ({pcbnew.ToMM(pos.x):6.1f}, {pcbnew.ToMM(pos.y):6.1f})')
"
```
Expected: 39+ components, 0 tracks
If tracks > 0: run `cleanup_pro.py` first

---

### TASK 2 — Fix Overlaps
```powershell
& "C:\Program Files\KiCad\9.0\bin\python.exe" gap_check_v2.py
```
If violations found, nudge non-critical components +3mm Y until clean.
Target: 0 courtyard overlaps, 0 keep-out violations.

---

### TASK 3 — Redraw Board Outline
```powershell
& "C:\Program Files\KiCad\9.0\bin\python.exe" draw_outline_v2.py
```
Expected output: `Board outline drawn: ~80 x 68mm`

---

### TASK 4 — Export Fresh DSN
```powershell
& "C:\Program Files\KiCad\9.0\bin\python.exe" export_dsn.py `
  "Pill_Dispenser_V4.kicad_pcb" `
  "Pill_Dispenser_V4_compact.dsn"

# Verify boundary is correct
Select-String "boundary" "Pill_Dispenser_V4_compact.dsn" -Context 0,3
```

---

### TASK 5 — Autoroute with FreeRouting
Try in this order, stop at first success:

```powershell
# Try 1
java -jar freerouting.jar `
  -de "Pill_Dispenser_V4_compact.dsn" `
  -do "Pill_Dispenser_V4_compact.ses" `
  -mp 3000 -mt 1

# Try 2 (if Try 1 fails)
java -jar freerouting.jar `
  -is "Pill_Dispenser_V4_compact.dsn" `
  -os "Pill_Dispenser_V4_compact.ses"

# Try 3 (if Try 2 fails) — GUI fallback
java -jar freerouting.jar
# Then manually: Open DSN → Autoroute → Export SES
```
Target: 0 or 1 unrouted connections in freerouting log.

---

### TASK 6 — Import Routes
```powershell
& "C:\Program Files\KiCad\9.0\bin\python.exe" import_ses.py `
  "Pill_Dispenser_V4.kicad_pcb" `
  "Pill_Dispenser_V4_compact.ses"
```

---

### TASK 7 — Fix Board Settings
```python
# fix_settings.py
import pcbnew
board = pcbnew.LoadBoard("Pill_Dispenser_V4.kicad_pcb")
ds = board.GetDesignSettings()
ds.m_MinThroughDrill = pcbnew.FromMM(0.2)
ds.m_TrackMinWidth   = pcbnew.FromMM(0.1)
ds.m_MinClearance    = pcbnew.FromMM(0.15)
board.Save("Pill_Dispenser_V4.kicad_pcb")
print("Settings fixed")
```

---

### TASK 8 — Add Teardrops
In KiCad PCB Editor GUI:
```
Edit → Edit Teardrops → Add Teardrops to All → Apply → OK
```
OR via scripting console:
```python
# In KiCad scripting console (not external Python)
import pcbnew
pcbnew.GetBoard().BuildConnectivity()
```

---

### TASK 9 — Round Tracks
In KiCad PCB Editor GUI:
```
Tools → External Plugins → Round Tracks
subdivision = 4
min_distance = 0.1mm
Apply to All Tracks
```

---

### TASK 10 — Add GND Copper Pour
```python
# add_gnd_pour.py
import pcbnew

board = pcbnew.LoadBoard("Pill_Dispenser_V4.kicad_pcb")

gnd = None
for name, net in board.GetNets().items():
    if name.upper() in ['GND', '/GND', 'GNDD']:
        gnd = net
        print(f"GND net: {name}")
        break

if not gnd:
    print("GND not found. Nets:", list(board.GetNets().keys())[:15])
else:
    # Bounding box
    xs = [pcbnew.ToMM(fp.GetPosition().x) for fp in board.GetFootprints()]
    ys = [pcbnew.ToMM(fp.GetPosition().y) for fp in board.GetFootprints()]
    x1, y1 = min(xs)-3, min(ys)-3
    x2, y2 = max(xs)+3, max(ys)+3

    for layer in [pcbnew.F_Cu, pcbnew.B_Cu]:
        z = pcbnew.ZONE(board)
        z.SetLayer(layer)
        z.SetNet(gnd)
        z.SetMinThickness(pcbnew.FromMM(0.25))
        o = z.Outline()
        o.NewOutline()
        o.Append(pcbnew.FromMM(x1), pcbnew.FromMM(y1))
        o.Append(pcbnew.FromMM(x2), pcbnew.FromMM(y1))
        o.Append(pcbnew.FromMM(x2), pcbnew.FromMM(y2))
        o.Append(pcbnew.FromMM(x1), pcbnew.FromMM(y2))
        board.Add(z)

    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save("Pill_Dispenser_V4.kicad_pcb")
    print("GND pour added on F.Cu + B.Cu and filled")
```

---

### TASK 11 — Run Final DRC
```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb drc `
  --output "drc_final.txt" `
  "Pill_Dispenser_V4.kicad_pcb"

& "C:\Program Files\KiCad\9.0\bin\python.exe" -c "
import re
from collections import Counter
t = open('drc_final.txt', encoding='utf-8', errors='replace').read()
c = Counter(re.findall(r'\[(\w+)\]', t))
print('=== DRC FINAL ===')
for k,v in c.most_common(): print(f'  [{k}]: {v}')
print(f'TOTAL: {sum(c.values())}')
"
```
Target: unconnected=0, shorting=0, total < 25

---

### TASK 12 — Use KiKit for JLCPCB Export
```powershell
# Check if kikit is available
python -m kikit --version

# If available, use it (BEST METHOD):
python -m kikit fab jlcpcb `
  --assembly `
  --schematic "Pill_Dispenser_V4.kicad_sch" `
  "Pill_Dispenser_V4.kicad_pcb" `
  "./kikit_jlcpcb/"

# kikit generates:
# - gerbers (correct layer names for JLCPCB)
# - drill files
# - BOM with LCSC part numbers column
# - CPL (pick and place file)
# All formatted exactly as JLCPCB requires
```
If kikit not available, fall back to manual:
```powershell
New-Item -Force -ItemType Directory -Path "gerbers_final"
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb export gerbers `
  --output "./gerbers_final/" "Pill_Dispenser_V4.kicad_pcb"
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb export drill `
  --output "./gerbers_final/" "Pill_Dispenser_V4.kicad_pcb"
```

---

### TASK 13 — Generate Interactive BOM
```powershell
# Find ibom plugin path
$ibom = Get-ChildItem `
  "$env:APPDATA\kicad\9.0\scripting\plugins" `
  -Recurse -Filter "generate_interactive_bom.py" `
  -ErrorAction SilentlyContinue | Select-Object -First 1

if ($ibom) {
    & "C:\Program Files\KiCad\9.0\bin\python.exe" $ibom.FullName `
      --no-browser `
      --output-dir "./bom/" `
      "Pill_Dispenser_V4.kicad_pcb"
    Write-Host "BOM generated at ./bom/ibom.html"
} else {
    Write-Host "ibom plugin not found, use GUI: Tools → Generate Interactive BOM"
}
```

---

### TASK 14 — Export 3D Model + pcb2blender
```powershell
# STEP export for Fusion360 / FreeCAD
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb export step `
  --subst-models `
  --output "Pill_Dispenser_V4_3D.step" `
  "Pill_Dispenser_V4.kicad_pcb"

# VRML export for Blender (pcb2blender compatible)
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb export vrml `
  --output "Pill_Dispenser_V4_3D.wrl" `
  "Pill_Dispenser_V4.kicad_pcb"

Write-Host "3D files ready"
ls Pill_Dispenser_V4_3D.*
```

---

### TASK 15 — Git Commit Milestone
```powershell
git add Pill_Dispenser_V4.kicad_pcb
git add Pill_Dispenser_V4.kicad_sch
git add gerbers_final/
git add Pill_Dispenser_V4_3D.step
git commit -m "feat: routed PCB v4 compact 80x68mm
- 0 unconnected pads
- GND copper pour F.Cu + B.Cu
- Teardrops added
- Round tracks applied
- Gerbers ready for JLCPCB"
```

---

## FINAL REPORT FORMAT

After all tasks, print this:

```
╔══════════════════════════════════════════════════╗
║     PILL DISPENSER V4 — PCB COMPLETE REPORT      ║
╠══════════════════════════════════════════════════╣
║ Board Size:        __ mm x __ mm                 ║
║ Components:        __                            ║
║ Nets:              __                            ║
║ Tracks:            __                            ║
║ Copper pours:      F.Cu GND + B.Cu GND           ║
╠══════════════════════════════════════════════════╣
║ DRC RESULTS                                      ║
║   Unconnected:     __ (TARGET: 0)                ║
║   Shorts:          __ (TARGET: 0)                ║
║   Total violations:__ (TARGET: <25)              ║
╠══════════════════════════════════════════════════╣
║ FILES GENERATED                                  ║
║   [ ] .kicad_pcb  routed board                   ║
║   [ ] .step       3D model                       ║
║   [ ] gerbers/    fab files                      ║
║   [ ] bom/        ibom.html                      ║
║   [ ] kikit_jlcpcb/ OR gerbers_final/            ║
╠══════════════════════════════════════════════════╣
║ PLUGINS USED                                     ║
║   [ ] FreeRouting  autoroute                     ║
║   [ ] KiKit        fab export                    ║
║   [ ] Teardrops    pad reinforcement             ║
║   [ ] Round Tracks aesthetic routing             ║
║   [ ] ibom         assembly reference            ║
║   [ ] pcb2blender  3D render                     ║
║   [ ] Git          version control               ║
╠══════════════════════════════════════════════════╣
║ READY FOR JLCPCB: YES / NO                       ║
╚══════════════════════════════════════════════════╝
```

---

## CRITICAL RULES — NEVER BREAK

1. Keep-out x=59..79, y=25..55mm — NEVER put anything here
2. Never modify netlist — only placement and routing
3. Always use KiCad Python, not system Python
4. Always call board.Save() after every script
5. USB D+/D- traces must be equal length ±0.5mm
6. Power traces (VBUS, VBAT, 3V3) use 0.4mm width
7. Signal traces use 0.2mm width
8. If freerouting CLI fails 3 times → use GUI
9. Run DRC after EVERY major change
10. Commit to git after each completed task
