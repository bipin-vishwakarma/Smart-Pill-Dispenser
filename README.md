# 💊 Smart Pill Dispenser

An **ESP32-S3 based automated pill dispenser** — a biomedical hardware project taken end-to-end in **KiCad**: schematic → PCB layout → ERC/DRC → Gerber export → fab-ready.

> Designed to dispense scheduled medication doses reliably — built as a real, manufacturable board, not just a breadboard prototype.

---

## 🧭 Design Iterations

This repo captures the **full evolution** of the board across seven revisions — the way real hardware gets designed:

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
- **Outputs:** Gerbers, drill files, ERC/DRC-clean design
- **Domain:** Biomedical / medication-adherence hardware

## 📂 Opening the project

Install [KiCad](https://www.kicad.org/) (8.x+), then open any version's `.kicad_pro`. Gerbers under `Pill_Dispenser_V4/` can be sent straight to a fab house or previewed in an online Gerber viewer.

---

<sub>Part of my biomedical hardware portfolio · <a href="https://github.com/bipin-vishwakarma">@bipin-vishwakarma</a></sub>
