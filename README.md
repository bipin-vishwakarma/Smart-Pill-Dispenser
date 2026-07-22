# 💊 Smart Pill Dispenser

An **ESP32-S3 based automated pill dispenser** — a biomedical hardware project taken end-to-end in **KiCad**: schematic → PCB layout → ERC/DRC → Gerber export → fab-ready.

> Designed to dispense scheduled medication doses reliably — built as a real, manufacturable board, not just a breadboard prototype.

---

## 🔧 From Prototype → Custom Board

<table>
<tr>
<td width="50%" align="center">
<img src="https://raw.githubusercontent.com/bipin-vishwakarma/Smart-Pill-Dispenser/main/board-photo-2.jpeg" width="100%" alt="Breadboard prototype" />
<br /><sub><b>① Prototype</b> — Arduino UNO + LCD + servo + buzzer (Tinkercad)</sub>
</td>
<td width="50%" align="center">
<img src="https://raw.githubusercontent.com/bipin-vishwakarma/Smart-Pill-Dispenser/main/render_v3.png" width="100%" alt="Custom KiCad PCB 3D render" />
<br /><sub><b>② Custom PCB</b> — ESP32-S3 board, designed in KiCad (3D render)</sub>
</td>
</tr>
</table>

The project evolved from a breadboard proof-of-concept into a **custom-routed PCB** — the way real hardware ships.

---

## 🧭 Design Iterations

Seven board revisions capture the full evolution:

| Version | Notes |
|:--|:--|
| `Pill_dispenser` (V2) | Early schematic + PCB |
| `Pill_Dispenser_1.0` (V4) | First wired revision |
| `V3` – `V5` | Layout refinement, routing, DRC cleanup |
| `V4` | **Full Gerber + drill set exported** (fab package) |
| `V6` – `V7` | Latest revisions |

## ⚙️ Tech

![ESP32-S3](https://img.shields.io/badge/MCU-ESP32--S3-E7352C?style=flat-square&logo=espressif&logoColor=white)
![KiCad](https://img.shields.io/badge/EDA-KiCad-314CB0?style=flat-square&logo=kicad&logoColor=white)
![Status](https://img.shields.io/badge/Status-Fab_Ready-38bdf8?style=flat-square)

- **MCU:** ESP32-S3
- **EDA:** KiCad (schematic capture + PCB layout)
- **Outputs:** Gerbers, drill files, ERC/DRC-clean design, 3D STEP model
- **Domain:** Biomedical / medication-adherence hardware

## 📂 Opening the project

Install [KiCad](https://www.kicad.org/) (8.x+), then open any version's `.kicad_pro`. Gerbers under `Pill_Dispenser_V4/` can be sent straight to a fab house or previewed in an online Gerber viewer.

---

<sub>Part of my biomedical hardware portfolio · <a href="https://github.com/bipin-vishwakarma">@bipin-vishwakarma</a></sub>
