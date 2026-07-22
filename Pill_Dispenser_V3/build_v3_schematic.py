import uuid
from pathlib import Path

PROJECT = "Pill_Dispenser_V3"
PROJECT_UUID = str(uuid.uuid4())
SCH_PATH = Path(r"d:\UPES\Projects\Pill Despensor\Pill_Dispenser_V3\Pill_Dispenser_V3.kicad_sch")


def uid() -> str:
    return str(uuid.uuid4())


def esc(value: str) -> str:
    return value.replace('"', '\\"')


def symbol_block(ref: str, value: str, lib_id: str, footprint: str, x: float, y: float, pins: list[str], in_bom: bool = True, on_board: bool = True):
    suid = uid()
    lines = []
    lines.append("\t(symbol")
    lines.append(f"\t\t(lib_id \"{esc(lib_id)}\")")
    lines.append(f"\t\t(at {x:.2f} {y:.2f} 0)")
    lines.append("\t\t(unit 1)")
    lines.append("\t\t(exclude_from_sim no)")
    lines.append(f"\t\t(in_bom {'yes' if in_bom else 'no'})")
    lines.append(f"\t\t(on_board {'yes' if on_board else 'no'})")
    lines.append("\t\t(dnp no)")
    lines.append(f"\t\t(uuid \"{suid}\")")

    def prop(name: str, val: str, px: float, py: float, hide: bool = False):
        lines.append(f"\t\t(property \"{name}\" \"{esc(val)}\"")
        lines.append(f"\t\t\t(at {px:.2f} {py:.2f} 0)")
        lines.append("\t\t\t(effects")
        lines.append("\t\t\t\t(font")
        lines.append("\t\t\t\t\t(size 1.27 1.27)")
        lines.append("\t\t\t\t)")
        if hide:
            lines.append("\t\t\t\t(hide yes)")
        lines.append("\t\t\t)")
        lines.append("\t\t)")

    prop("Reference", ref, x, y - 2.54)
    prop("Value", value, x, y + 2.54)
    prop("Footprint", footprint, x, y, hide=True)
    prop("Datasheet", "~", x, y, hide=True)
    prop("Description", "", x, y, hide=True)

    lines.append("\t\t(instances")
    lines.append(f"\t\t\t(project \"{PROJECT}\"")
    lines.append(f"\t\t\t\t(path \"/{PROJECT_UUID}\"")
    lines.append(f"\t\t\t\t\t(reference \"{esc(ref)}\")")
    lines.append("\t\t\t\t\t(unit 1)")
    lines.append("\t\t\t\t)")
    lines.append("\t\t\t)")
    lines.append("\t\t)")
    lines.append("\t)")
    return "\n".join(lines)


def global_label_block(name: str, x: float, y: float):
    return f'''\t(global_label "{esc(name)}"
\t\t(at {x:.2f} {y:.2f} 0)
		(shape bidirectional)
\t\t(effects
\t\t\t(font
\t\t\t\t(size 1.27 1.27)
\t\t\t)
\t\t\t(justify left bottom)
\t\t)
\t\t(uuid "{uid()}")
\t)'''


def text_note_block(text: str, x: float, y: float):
    return f'''\t(text "{esc(text)}"
		(at {x:.2f} {y:.2f} 0)
		(effects
			(font
				(size 1.50 1.50)
				(bold yes)
			)
		)
		(uuid "{uid()}")
	)'''


symbols = []

# Power block
symbols.append(symbol_block("J1", "USB-C", "Connector_Generic:Conn_01x16", "Connector_USB:USB_C_Receptacle_GCT_USB4135-GF-A_6P_TopMnt_Horizontal", 30, 48, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]))
symbols.append(symbol_block("R11", "5.1k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 50, 62, ["1", "2"]))
symbols.append(symbol_block("R12", "5.1k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 58, 62, ["1", "2"]))
symbols.append(symbol_block("R15", "22", "Device:R", "Resistor_SMD:R_0603_1608Metric", 50, 40, ["1", "2"]))
symbols.append(symbol_block("R16", "22", "Device:R", "Resistor_SMD:R_0603_1608Metric", 58, 40, ["1", "2"]))
symbols.append(symbol_block("U3", "TP4056-42-ESOP8", "Battery_Management:TP4056-42-ESOP8", "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm_ThermalVias", 84, 48, ["VCC", "BAT", "GND", "PROG", "CHRG", "STDBY", "CE"]))
symbols.append(symbol_block("R5", "2k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 100, 40, ["1", "2"]))
symbols.append(symbol_block("D4", "CHRG", "Device:LED", "LED_SMD:LED_0603_1608Metric", 100, 48, ["1", "2"]))
symbols.append(symbol_block("R2", "330", "Device:R", "Resistor_SMD:R_0603_1608Metric", 108, 48, ["1", "2"]))
symbols.append(symbol_block("D5", "STDBY", "Device:LED", "LED_SMD:LED_0603_1608Metric", 100, 56, ["1", "2"]))
symbols.append(symbol_block("R13", "330", "Device:R", "Resistor_SMD:R_0603_1608Metric", 108, 56, ["1", "2"]))
symbols.append(symbol_block("U4", "AP2112K-3.3", "Regulator_Linear:AP2112K-3.3", "Package_TO_SOT_SMD:SOT-23-5", 128, 32, ["IN", "GND", "EN", "OUT"]))
symbols.append(symbol_block("C1", "10uF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 118, 24, ["1", "2"]))
symbols.append(symbol_block("C2", "10uF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 136, 24, ["1", "2"]))
symbols.append(symbol_block("D3", "1N5819", "Device:D_Schottky", "Diode_SMD:D_SMA", 118, 48, ["1", "2"]))
symbols.append(symbol_block("J4", "BATTERY", "Connector_Generic:Conn_01x02", "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical", 76, 70, ["1", "2"]))
symbols.append(symbol_block("SW4", "PWR_SW", "Switch:SW_SPDT", "Button_Switch_THT:SW_E-Switch_EG1224_SPDT_Angled", 96, 70, ["1", "2", "3"]))
symbols.append(symbol_block("C10", "100uF", "Device:C", "Capacitor_SMD:CP_Elec_6.3x5.4", 118, 70, ["1", "2"]))

# MCU block
u1_pins = [
    "3V3", "GND", "EN", "GPIO0", "GPIO1", "GPIO2", "GPIO3", "GPIO4", "GPIO5", "GPIO6", "GPIO7", "GPIO8",
    "GPIO9", "GPIO10", "GPIO11", "GPIO12", "GPIO13", "GPIO14", "GPIO15", "GPIO16", "GPIO17", "GPIO18",
    "GPIO19", "GPIO20", "GPIO21", "GPIO26", "GPIO33", "GPIO34", "GPIO35", "GPIO36", "GPIO37", "GPIO38", "GPIO39", "GPIO40", "GPIO41", "GPIO42"
]
symbols.append(symbol_block("U1", "ESP32-S3-WROOM-1", "RF_Module:ESP32-S3-WROOM-1", "RF_Module:ESP32-S3-WROOM-1", 208, 48, u1_pins))
symbols.append(symbol_block("R8", "10k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 232, 34, ["1", "2"]))
symbols.append(symbol_block("R17", "10k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 240, 34, ["1", "2"]))
symbols.append(symbol_block("R9", "100k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 232, 62, ["1", "2"]))
symbols.append(symbol_block("R10", "100k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 240, 62, ["1", "2"]))
symbols.append(symbol_block("C5", "100nF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 182, 30, ["1", "2"]))
symbols.append(symbol_block("C6", "100nF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 188, 30, ["1", "2"]))
symbols.append(symbol_block("C7", "100nF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 194, 30, ["1", "2"]))
symbols.append(symbol_block("C8", "100nF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 200, 30, ["1", "2"]))
symbols.append(symbol_block("C9", "10uF", "Device:C", "Capacitor_SMD:C_0603_1608Metric", 206, 30, ["1", "2"]))

# UI block
symbols.append(symbol_block("J3", "OLED", "Connector_Generic:Conn_01x04", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 176, 86, ["1", "2", "3", "4"]))
symbols.append(symbol_block("J2", "SERVO", "Connector_Generic:Conn_01x03", "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical", 198, 86, ["1", "2", "3"]))
symbols.append(symbol_block("BZ1", "Buzzer", "Device:Buzzer", "Buzzer_Beeper:MagneticBuzzer_Kingstate_KCG0601", 162, 98, ["1", "2"]))
symbols.append(symbol_block("Q1", "MMBT2222A", "Transistor_BJT:Q_NPN_BCE", "Package_TO_SOT_SMD:SOT-23", 172, 98, ["1", "2", "3"]))
symbols.append(symbol_block("R4", "1k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 182, 98, ["1", "2"]))
symbols.append(symbol_block("D1", "STATUS", "Device:LED", "LED_SMD:LED_0603_1608Metric", 194, 98, ["1", "2"]))
symbols.append(symbol_block("R1", "330", "Device:R", "Resistor_SMD:R_0603_1608Metric", 202, 98, ["1", "2"]))
symbols.append(symbol_block("SW1", "USER", "Switch:SW_Push", "Button_Switch_SMD:SW_SPST_EVQP0", 188, 110, ["1", "2"]))
symbols.append(symbol_block("SW2", "BOOT", "Switch:SW_Push", "Button_Switch_SMD:SW_SPST_EVQP0", 196, 110, ["1", "2"]))
symbols.append(symbol_block("SW3", "RESET", "Switch:SW_Push", "Button_Switch_SMD:SW_SPST_EVQP0", 204, 110, ["1", "2"]))
symbols.append(symbol_block("R6", "4.7k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 182, 78, ["1", "2"]))
symbols.append(symbol_block("R7", "4.7k", "Device:R", "Resistor_SMD:R_0603_1608Metric", 190, 78, ["1", "2"]))


labels = []
label_points = []
for n, x, y in label_points:
    labels.append(global_label_block(n, x, y))
    
text_notes = []
text_notes.append(text_note_block("POWER RAIL", 72, 12))
text_notes.append(text_note_block("MCU CORE", 200, 12))
text_notes.append(text_note_block("UI + ACTUATORS", 184, 72))

no_connects = []

content = []
content.append("(kicad_sch")
content.append("\t(version 20250114)")
content.append("\t(generator \"KiCad Python API\")")
content.append("\t(generator_version \"9.0\")")
content.append(f"\t(uuid \"{PROJECT_UUID}\")")
content.append("\t(paper \"A4\")")
content.append("\t(lib_symbols)")
content.extend(labels)
content.extend(text_notes)
content.extend(symbols)
content.extend(no_connects)
content.append("\t(sheet_instances")
content.append("\t\t(path \"/\" (page \"1\"))")
content.append("\t)")
content.append(")")

SCH_PATH.write_text("\n".join(content) + "\n", encoding="utf-8")
print(f"Schematic generated: {SCH_PATH}")
print(f"Symbols: {len(symbols)}, Labels: {len(labels)}, No-connects: {len(no_connects)}")
