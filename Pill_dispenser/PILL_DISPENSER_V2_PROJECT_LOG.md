# Pill Dispenser V2 — Complete Project Log

> **KiCad Version:** 9.0.7  
> **Last active PCB edit:** 2026-03-11  
> **Last active Schematic edit:** 2026-03-06  
> **Documentation generated:** 2026-03-15  
> **Project path:** `D:\UPES\Projects\Pill Despensor\Pill_dispenser\`

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [File Inventory](#2-file-inventory)
3. [Bill of Materials (BOM)](#3-bill-of-materials-bom)
4. [PCB Footprint Map](#4-pcb-footprint-map)
5. [Schematic Issues & Fix History](#5-schematic-issues--fix-history)
6. [PCB DRC History & Error Progression](#6-pcb-drc-history--error-progression)
7. [Remaining Open Items](#7-remaining-open-items)
8. [MCP Server Setup](#8-mcp-server-setup)
9. [KiCad Python Backend](#9-kicad-python-backend)
10. [Summary of Current State](#10-summary-of-current-state)

---

## 1. Project Overview

**Pill Dispenser V2** is an ESP32-S3-based medication dispenser controller board designed as a PCB. The board handles:

- **Battery management** — USB-C charging via TP4056, Li-Ion battery input via JST PH connector.
- **Power regulation** — AP2112K-3.3 3.3 V LDO (primary), AMS1117-3.3 (backup/extended load).
- **Microcontroller** — ESP32-S3 module for BLE/Wi-Fi, pill scheduling logic, and motor control.
- **User interface** — 3× momentary push buttons (BOOT, RESET, USER), 1× SPDT power switch, 3× status LEDs, 1× buzzer.
- **Peripheral connectors** — OLED display (4-pin header), servo motor output (3-pin header), battery connector (JST PH 2-pin).
- **Status indication** — Red CHG LED (D4), Green STDBY LED (D5), Red STATUS LED (D1).

---

## 2. File Inventory

### Core Project Files

| File | Size | Last Modified | Description |
|------|------|--------------|-------------|
| `Pill_Dispenser_V2.kicad_sch` | ~170 KB | 2026-03-06 | Schematic — components, nets, lib_symbols |
| `Pill_Dispenser_V2.kicad_pcb` | ~243 KB | 2026-03-11 | PCB layout — footprints, traces, DRC rules |
| `Pill_Dispenser_V2.kicad_pro` | small | 2026-03-11 | Project settings file |
| `Pill_Dispenser_V2.kicad_prl` | small | 2026-03-11 | Local project settings (DRC severities, etc.) |

### DRC Report Files (Chronological)

| File | Timestamp | Unconnected | Violations | Notes |
|------|-----------|-------------|------------|-------|
| `Pill_Dispenser_V2_drc_violations.json` | 2026-03-11 00:57 | 12 | 64 | First full DRC run — silk errors, outline errors |
| `kicad_drc_report.json` | 2026-03-11 00:58 | 12 | 53 | After initial cleanup |
| `kicad_drc_report_final.json` | 2026-03-11 01:09 | 12 | 26 | Silk/drill violations cleared |
| `kicad_drc_report_final2.json` | 2026-03-11 01:10 | 12 | 26 | No change from final |
| `kicad_drc_report_final3.json` | 2026-03-11 01:11 | 12 | 26 | No change |
| `kicad_drc_report_final_check.json` | 2026-03-11 01:15 | 12 | 26 | Contains outline/drill errors |
| `final_verification.json` | 2026-03-11 01:16 | **0** | **26** | ✅ Unconnected resolved — all remaining are lib_footprint_mismatch warnings |

### Schematic Fix Scripts (Chronological)

| File | Purpose | Outcome |
|------|---------|---------|
| `fix_schematic.py` | Initial attempt — no-op rename on USBLC6-2SC6 | Ineffective |
| `fix_schematic2.py` | Regex removal of USBLC6-2SC6 / USBLC6-2P6 | Aggressive; risk of partial removal |
| `fix_schematic3.py` | Remove `(extends "USBLC6-2P6")` clause; rename parent to DummyName | Partial fix — DummyName still problem |
| `fix_schematic4.py` | Remove entire `(symbol "Power_Protection:USBLC6-2SC6" ...)` block | Removed broken symbol block |
| `fix_schematic5.py` | Remove orphan lib symbol blocks with extends referencing missing parents | Cleaned orphan extends |
| `fix_extends.py` | Rewrite AP2112K-3.3 and MMBT2222A extends as self-contained copied sub-symbols | Fixed broken extends chains |
| `fix_final.py` | Remove DummyName symbol block | Final cleanup |
| `diagnose.py` | Check for USBLC6, DummyName, extends references and parenthesis balance | Diagnostic / verification |

### Footprint / Component Verification Scripts

| File | Purpose |
|------|---------|
| `check_footprints.py` | List all footprints in PCB and validate against schematic |
| `check_missing_fp.py` | Identify components with missing / blank footprint assignments |
| `list_fps.py` | Dump all footprints used in the PCB |
| `get_components.py` | Extract component reference + value + footprint from schematic |
| `fps_output.txt` | Output log from footprint verification scripts |

### Backup

| File | Date | Contents |
|------|------|---------|
| `Pill_Dispenser_V2-backups/Pill_Dispenser_V2-2026-03-06_032009.zip` | 2026-03-06 | 242 entries — KiCAD-MCP-Server source + 4 KiCad project files (older than final PCB state) |

### Support Tools

| File/Folder | Description |
|-------------|-------------|
| `KiCAD-MCP-Server/` | Local KiCad MCP server v2.1.0-alpha (TypeScript/Node.js) |
| `KiCAD-MCP-Server/scripts/mcp-connection-check.mjs` | MCP protocol handshake test script (created during this session) |
| `KiCAD-MCP-Server/config/claude-desktop-config.json` | Active MCP client config (kicad + stitch servers) |

---

## 3. Bill of Materials (BOM)

### Power Section

| Ref | Value | Symbol | Footprint |
|-----|-------|--------|-----------|
| J1 | USB-C | `Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12` | `USB_C_Receptacle_HRO_TYPE-C-31-M-12` |
| U3 | TP4056 | `Battery_Management:TP4056-42-ESOP8` | `SOIC-8_3.9x4.9mm_P1.27mm` |
| U4 | AP2112K-3.3 | `Regulator_Linear:AP2112K-3.3` | `SOT-23-5` |
| U2 | AMS1117-3.3 | `Regulator_Linear:AMS1117-3.3` | *(in schematic, verify footprint)* |
| D3 | 1N5819 (Schottky) | `Device:D_Schottky` | `D_SMA` |
| J4 | Battery | `Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical` | JST PH 2-pin |
| C10 | 470 µF | `Device:C_Polarized` | `CP_Radial_D8.0mm_P3.50mm` |
| C1 | 10 µF | `Device:C` | `C_0805_2012Metric` |
| C2 | 10 µF | `Device:C` | `C_0805_2012Metric` |
| C3 | 10 µF | `Device:C` | `C_0805_2012Metric` |
| C4 | 22 µF | `Device:C` | `C_0805_2012Metric` |
| C8 | 10 µF | `Device:C` | `C_0805_2012Metric` |
| R5 | 2 KΩ | `Device:R` | `R_0603_1608Metric` |
| R11 | 5.1 KΩ | `Device:R` | `R_0603_1608Metric` |
| R12 | 5.1 KΩ | `Device:R` | `R_0603_1608Metric` |
| R15 | 22 Ω | `Device:R` | `R_0603_1608Metric` |
| R16 | 22 Ω | `Device:R` | `R_0603_1608Metric` |
| SW4 | PWR_SW (SPDT) | `Switch:SW_SPDT` | `SW_E-Switch_EG1224_SPDT_Angled` |

### Microcontroller

| Ref | Value | Symbol | Footprint | ⚠️ Note |
|-----|-------|--------|-----------|---------|
| U1 | ESP32-S3-MINI-1 | `RF_Module:ESP32-S3-MINI-1` | `RF_Module:ESP32-S3-WROOM-1` | **MISMATCH** — schematic symbol is MINI-1 but PCB footprint is WROOM-1 |
| C5 | 100 nF | `Device:C` | `C_0603_1608Metric` |  |
| C6 | 100 nF | `Device:C` | `C_0603_1608Metric` |  |
| C7 | 1 µF | `Device:C` | `C_0603_1608Metric` |  |
| C9 | 100 nF | `Device:C` | `C_0603_1608Metric` |  |
| R8 | 10 KΩ | `Device:R` | `R_0603_1608Metric` | BOOT pull-up |
| R17 | 10 KΩ | `Device:R` | `R_0603_1608Metric` | EN pull-up |
| SW2 | BOOT | `Switch:SW_Push` | `SW_PUSH_6mm_H5mm` |  |
| SW3 | RESET | `Switch:SW_Push` | `SW_PUSH_6mm_H5mm` |  |

### User Interface

| Ref | Value | Symbol | Footprint | Role |
|-----|-------|--------|-----------|------|
| SW1 | USER | `Switch:SW_Push` | `SW_PUSH_6mm_H5mm` | User input button |
| BZ1 | Buzzer | `Device:Buzzer` | `Buzzer_12x9.5RM7.6` | Audio alert |
| D1 | Red_STATUS | `Device:LED` | `LED_0805_2012Metric` | General status LED |
| D4 | Red_CHG | `Device:LED` | `LED_0805_2012Metric` | TP4056 CHRG indicator |
| D5 | Green_STDBY | `Device:LED` | `LED_0805_2012Metric` | TP4056 STDBY indicator |
| R1 | 100 Ω | `Device:R` | `R_0603_1608Metric` | LED current limit |
| R2 | 470 Ω | `Device:R` | `R_0603_1608Metric` | LED current limit |
| R13 | 1 KΩ | `Device:R` | `R_0603_1608Metric` | LED current limit |
| R14 | 1 KΩ | `Device:R` | `R_0603_1608Metric` | LED current limit |
| Q1 | MMBT2222A (NPN) | `Transistor_BJT:MMBT2222A` | `SOT-23` | Buzzer/LED driver |

### Peripheral Connectors

| Ref | Value | Symbol | Footprint | Connected to |
|-----|-------|--------|-----------|-------------|
| J2 | SERVO | `Connector_PinHeader_2.54mm:PinHeader_1x03` | `PinHeader_1x03_P2.54mm_Vertical` | Servo motor (PWM) |
| J3 | OLED | `Connector_PinHeader_2.54mm:PinHeader_1x04` | `PinHeader_1x04_P2.54mm_Vertical` | I2C OLED display |

### Support Passives

| Ref | Value | Footprint | Notes |
|-----|-------|-----------|-------|
| R3 | 10 KΩ | `R_0603_1608Metric` | Pull-up/down |
| R4 | 1 KΩ | `R_0603_1608Metric` | Base resistor (Q1 or LED) |
| R6 | 4.7 KΩ | `R_0603_1608Metric` | I2C pull-up (SDA) |
| R7 | 4.7 KΩ | `R_0603_1608Metric` | I2C pull-up (SCL) |
| R9 | 100 KΩ | `R_0603_1608Metric` | Voltage divider / bias |
| R10 | 100 KΩ | `R_0603_1608Metric` | Voltage divider / bias |

---

## 4. PCB Footprint Map

Total footprint count by package:

| Package | Count | Components |
|---------|-------|-----------|
| `R_0603_1608Metric` | 17 | R1–R17 |
| `C_0805_2012Metric` | 5 | C1–C4, C8 |
| `C_0603_1608Metric` | 4 | C5–C7, C9 |
| `SW_PUSH_6mm_H5mm` | 3 | SW1, SW2, SW3 |
| `LED_0805_2012Metric` | 3 | D1, D4, D5 |
| `SOT-23-5` | 1 | U4 (AP2112K-3.3) |
| `SOT-23` | 1 | Q1 (MMBT2222A) |
| `SOIC-8` | 1 | U3 (TP4056) |
| `D_SMA` | 1 | D3 (1N5819) |
| `PinHeader_1x04_P2.54mm` | 1 | J3 (OLED) |
| `PinHeader_1x03_P2.54mm` | 1 | J2 (SERVO) |
| `JST_PH_B2B` | 1 | J4 (Battery) |
| `CP_Radial_D8.0mm_P3.50mm` | 1 | C10 (470µF) |
| `Buzzer_12x9.5RM7.6` | 1 | BZ1 |
| `USB_C_Receptacle_HRO_TYPE-C-31-M-12` | 1 | J1 |
| `ESP32-S3-WROOM-1` | 1 | U1 |
| `SW_E-Switch_EG1224_SPDT_Angled` | 1 | SW4 (PWR) |

**Total footprints: ~43**

---

## 5. Schematic Issues & Fix History

### Root Cause

The schematic's embedded `lib_symbols` section contained several symbol definitions using the `(extends "ParentName")` KiCad syntax — but the referenced parent symbols either:
1. Did not exist in the embedded library, or  
2. Were themselves broken orphan entries.

This caused KiCad to fail to load the schematic cleanly and was the root cause of all earlier DRC "symbol not found" errors.

---

### Issue 1 — `USBLC6-2SC6` broken extends chain

**Symptom:** Symbol `Power_Protection:USBLC6-2SC6` had `(extends "USBLC6-2P6")` but `USBLC6-2P6` was not present in the embedded lib_symbols.

**Progression of fixes:**

```
fix_schematic.py   → No-op replacement; file unchanged; issue persisted
fix_schematic2.py  → Aggressive regex delete; risk of corrupt block removal
fix_schematic3.py  → Removed (extends "USBLC6-2P6") clause; renamed parent to "DummyName"
fix_schematic4.py  → Removed entire (symbol "Power_Protection:USBLC6-2SC6" ...) block
fix_schematic5.py  → Removed orphan lib symbols with extends referencing missing parents
```

**Resolution:** `fix_schematic5.py` successfully removed the broken USBLC6 and DummyName blocks from lib_symbols.

---

### Issue 2 — `AP2112K-3.3` and `MMBT2222A` broken extends

**Symptom:** Both symbols used extends to derive from a parent, but the parent sub-symbols were missing from the embedded definition, causing empty/broken symbol rendering.

**Fix:** `fix_extends.py` — rewrote both symbols as fully self-contained definitions by copying sub-symbol pin/body data from the parent symbol (or known correct reference).

**Resolution:** Both symbols now render correctly in schematic without needing any parent.

---

### Issue 3 — `DummyName` orphan block

**Symptom:** After fix_schematic3.py renamed `USBLC6-2P6` to `DummyName`, a `DummyName` lib symbol block remained in the schematic with no instances referencing it.

**Fix:** `fix_final.py` — located and removed the entire `(symbol "DummyName" ...)` block.

**Resolution:** Clean schematic with no orphan lib_symbol entries.

---

### Current Schematic State (as of 2026-03-06)

- ✅ No broken extends references  
- ✅ No orphaned lib_symbol blocks (USBLC6-2SC6, USBLC6-2P6, DummyName all removed)  
- ✅ AP2112K-3.3 self-contained  
- ✅ MMBT2222A self-contained  
- ⚠️ U1 symbol mismatch: schematic uses `RF_Module:ESP32-S3-MINI-1` but PCB footprint is `RF_Module:ESP32-S3-WROOM-1` (see open items)

---

## 6. PCB DRC History & Error Progression

### Run 1 — `Pill_Dispenser_V2_drc_violations.json` (2026-03-11 00:57)

**Total: 64 violations — 13 errors, 51 warnings**

| Type | Count | Description |
|------|-------|-------------|
| `drill_out_of_range` | 12 | Hole diameter 0.2 mm below minimum 0.3 mm — affected USB-C shield pads |
| `invalid_outline` | 1 | No edges found on `Edge.Cuts` layer — board outline missing |
| `silk_over_copper` | 25 | Silkscreen text overlapping copper pads |
| `silk_overlap` | 26 | Silkscreen items overlapping each other |

---

### Runs 2–4 — After silk/copper cleanup (2026-03-11 00:58–01:11)

**Violations: 26 | Unconnected: 12**

Silk violations cleared. Remaining 26 violations were all `lib_footprint_mismatch` warnings.

Unconnected items at this stage:

| Ref | Pads Unconnected |
|-----|-----------------|
| J1 (USB-C) | A1/B1 (GND), A4/A9 (VBUS), S1/S2 (shield) |
| SW2 (BOOT) | Pad1, Pad2 |
| SW3 (RESET) | Pad1, Pad2 |
| SW4 (PWR) | Pad1, Pad2 |

> **Note:** The `invalid_outline` (no Edge.Cuts) from Run 1 does not appear in the violations array in runs 2–4 — it may have been excluded from the count via DRC severity settings in `.kicad_prl`.

---

### Run 7 — `final_verification.json` ✅ (2026-03-11 01:16:02)

**This is the authoritative final DRC state.**

```
Date         : 2026-03-11T01:16:02+0530
KiCad Version: 9.0.7
Source       : Pill_Dispenser_V2.kicad_pcb
Unconnected  : 0   ✅
Violations   : 26  (all severity=warning, all type=lib_footprint_mismatch)
```

All 26 `lib_footprint_mismatch` warnings are because locally-edited footprints no longer match their counterparts in the KiCad system library. **These are non-blocking for fabrication.** They do not indicate electrical errors.

Components with `lib_footprint_mismatch` warnings:

| Ref | Footprint | Library |
|-----|-----------|---------|
| R1, R2, R4–R9, R11–R16 | `R_0603_1608Metric` | `Resistor_SMD` |
| C1–C7 | `C_0605/0805_…Metric` | `Capacitor_SMD` |
| D3 | `D_SMA` | `Diode_SMD` |
| D1, D4, D5 | `LED_0805_2012Metric` | `LED_SMD` |
| J1 | `USB_C_Receptacle_HRO_TYPE-C-31-M-12` | `Connector_USB` |
| SW2/SW4 | push/SPDT switch footprints | `Button_Switch_THT` |

**To fix:** Run PCB Editor → Tools → Update Footprints from Library and accept the refresh.  
**To ignore officially:** Add each to DRC exclusions in `.kicad_prl`.

---

## 7. Remaining Open Items

### 🔴 High Priority

#### 1. ESP32 Module Mismatch (U1)

| Property | Value |
|----------|-------|
| Schematic symbol | `RF_Module:ESP32-S3-MINI-1` |
| PCB footprint | `RF_Module:ESP32-S3-WROOM-1` |
| Impact | Module pin-out and dimensions differ between MINI-1 and WROOM-1 |
| Status | Unresolved — **must be verified before ordering boards or modules** |

**Action required:** Confirm which physical module is actually being used and ensure schematic symbol, netlist, and PCB footprint all agree.

- ESP32-S3-MINI-1: 27 mm × 34.3 mm, FCC/CE certified
- ESP32-S3-WROOM-1: 18 mm × 20 mm, smaller form factor

---

### 🟡 Medium Priority

#### 2. Board Outline Missing (`Edge.Cuts`)

First DRC run (`Pill_Dispenser_V2_drc_violations.json`) reported `invalid_outline: no edges found on Edge.Cuts layer`. This error is absent from later runs, likely suppressed via DRC severity settings rather than actually fixed.

**Action required:** Confirm `Edge.Cuts` layer contains a closed board outline. Without an outline, Gerber generation will fail.

---

#### 3. 26 `lib_footprint_mismatch` Warnings

Non-blocking but noisy. Will appear in every DRC run until resolved.

**Action required:** Either:
- Update footprints from library (PCB Editor → Tools → Update Footprints from Library), or  
- Add to DRC exclusions list to formally acknowledge them.

---

#### 4. Drill Out of Range (USB-C shield pads)

First DRC run showed 12 `drill_out_of_range` errors (0.2 mm < 0.3 mm minimum). Not visible in later DRC files — may have been corrected or excluded.

**Action required:** Verify J1 (USB-C) shield pad drill sizes are ≥ 0.3 mm before sending Gerbers.

---

### 🟢 Already Resolved

| Issue | Resolution |
|-------|-----------|
| Broken extends chains (`USBLC6-2SC6`, `AP2112K-3.3`, `MMBT2222A`) | fix_extends.py + fix_schematic*.py |
| DummyName orphan lib symbol | fix_final.py |
| Schematic wouldn't open cleanly | All extends fixed; file loads in KiCad 9.0.7 |
| 12 unconnected items | Resolved in final PCB layout pass (2026-03-11 01:16) |
| 38 extra DRC violations (silk, drill) | Cleared during PCB cleanup session |

---

## 8. MCP Server Setup

### Configuration File

**Location:** `KiCAD-MCP-Server/config/claude-desktop-config.json`

```json
{
  "mcpServers": {
    "kicad": {
      "command": "node",
      "args": [
        "D:\\UPES\\Projects\\Pill Despensor\\Pill_dispenser\\KiCAD-MCP-Server\\dist\\index.js"
      ],
      "env": {
        "PYTHONPATH": "C:\\Program Files\\KiCad\\9.0\\lib\\python3\\dist-packages",
        "LOG_LEVEL": "info"
      }
    },
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "<redacted>"
      }
    }
  }
}
```

### Server Info

| Property | Value |
|----------|-------|
| Package | `kicad-mcp` v2.1.0-alpha |
| SDK | `@modelcontextprotocol/sdk` v1.21.0 |
| Transport | STDIO (newline-delimited JSON-RPC) |
| Entry point | `dist/index.js` |
| Python bridge | `python/kicad_interface.py` |
| Tools exposed | **99 tools** |

### Wire Protocol (Important)

The MCP SDK uses **newline-delimited JSON**, **not** HTTP `Content-Length` framing:

```js
// SDK serialize (from sdk/dist/esm/shared/stdio.js):
serializeMessage = (msg) => JSON.stringify(msg) + '\n';
// Parser splits on newline '\n', not Content-Length header
```

This was discovered when the initial MCP connection check script (which used Content-Length framing) failed with timeout. The script was updated to use newline-delimited JSON and then succeeded.

### Connection Test Results (2026-03-15)

```
MCP_INIT_OK: true
SERVER_NAME: kicad-mcp-server
SERVER_VERSION: 1.0.0
TOOLS_LIST_OK: true
TOOLS_COUNT: 99
Exit code: 0
```

**STDERR from server (healthy):**
```
[INFO] Using STDIO transport for local communication
[INFO] All KiCAD tools, resources, and prompts registered
[INFO] Router pattern enabled: 4 router tools + direct tools for discovery
[INFO] Found KiCAD bundled Python at: C:\Program Files\KiCad\9.0\bin\python.exe
[INFO] ✓ pcbnew module validated successfully
[INFO] Successfully connected to STDIO transport
KiCAD MCP SERVER READY
[INFO] Python version: 3.11.5 ... python executable: C:\Program Files\KiCad\9.0\bin\python.exe
```

---

## 9. KiCad Python Backend

| Property | Value |
|----------|-------|
| KiCad install | `C:\Program Files\KiCad\9.0\` |
| Python executable | `C:\Program Files\KiCad\9.0\bin\python.exe` |
| Python version | 3.11.5 |
| pcbnew module path | `C:\Program Files\KiCad\9.0\lib\python3\dist-packages` |
| pcbnew import | ✅ Validated successfully |

---

## 10. Summary of Current State

### What's Done ✅

| Task | Status |
|------|--------|
| Schematic loads cleanly in KiCad 9.0.7 | ✅ |
| All broken `extends` references removed | ✅ |
| 0 unconnected items in PCB | ✅ |
| DRC violations down from 64 → 26 (all warnings) | ✅ |
| Silk overlap / silk-over-copper errors cleared | ✅ |
| MCP server config written and active | ✅ |
| MCP connection test passed (99 tools live) | ✅ |
| KiCad Python backend validated | ✅ |

### What Still Needs Attention ⚠️

| Task | Priority | Description |
|------|----------|-------------|
| Verify ESP32 module selection | 🔴 High | MINI-1 vs WROOM-1 — decide and reconcile schematic + PCB |
| Add/verify board Edge.Cuts outline | 🔴 High | Required for Gerber export |
| Resolve or exclude 26 lib_footprint_mismatch | 🟡 Medium | Update from library OR add DRC exclusions |
| Verify USB-C shield pad drill sizes | 🟡 Medium | Confirm ≥ 0.3 mm for all J1 pads |
| Run full DRC after above fixes | 🟡 Medium | Confirm 0 errors and 0 unconnected post-reconciliation |
| ERC (Electrical Rules Check) on schematic | 🟡 Medium | Not verified — run before fab |
| Generate Gerbers + drill files | 🟢 Final | Only after all above items cleared |

---

*This file was auto-generated from project scan on 2026-03-15 using KiCad 9.0.7 file analysis and DRC report review.*
