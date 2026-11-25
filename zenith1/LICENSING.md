# ZENITH-1 licensing

ZENITH-1 is free software under the **Mozilla Public License 2.0** (`MPL-2.0`, full text in `LICENSE`), file by file.
If you change one of its files and share the result, share that file's source under the MPL.

ZENITH-1 is a modified version of **AMB-1** by Charles Vestal (<https://github.com/charlesvestal/fm1-amb>, MPL-2.0):
its engine, controls and structure are AMB-1's, changed and extended. Every file that came from AMB-1 keeps Charles
Vestal's copyright line, with ZENITH-1's beside it where the file was changed. It is built on
[fm1-base](https://github.com/charlesvestal/fm1-base) and [felucca-bsp](https://github.com/hugelton/felucca-bsp)
(`base/`), both MPL-2.0.

## Where the code comes from

| What | Origin | Licence |
| --- | --- | --- |
| The platform: `base/` (boot, USB and USB audio, the TRS jack, the headphone jack, storage, the update path, screen, panel, the screen reader, the host simulator and the browser emulator, build and install tools) | [fm1-base](https://github.com/charlesvestal/fm1-base) and [felucca-bsp](https://github.com/hugelton/felucca-bsp), from [Felucca](https://github.com/hugelton/Felucca) by Leo Kuroshita (@kurogedelic), Hügelton Instruments | MPL-2.0 |
| `app/` (`app.c`, `app.h`, `ui.c`, `project.c`, `host.c`), `app/dsp/zenith.c` and `zenith.h` (AMB-1's `amb.c` and `amb.h`, with their Dattorro plate from FoMni-1), `tests/`, `tools/gen_manual_figures.py` | AMB-1, Charles Vestal; changed and extended for ZENITH-1 by Polystellarflow | MPL-2.0 |
| `app/dsp/vis.c`, `vis.h` (the picture), `tools/emu_shim/`, `tools/build_emu.sh` | after HADAL-1's, by Polystellarflow | MPL-2.0 |
| `tools/sketch.c`, the worlds, the new sounds, Wander, the limiter, the night-horizon garden, the title | ZENITH-1, Polystellarflow | MPL-2.0 |
| The journey (parts, eras, the motif, worlds dissolving into others) and the FX menu, in `app/dsp/zenith.c` and `app/ui.c` | after HADAL-1's design, by Polystellarflow; written for ZENITH-1 | MPL-2.0 |
| The idea of a browser emulator for FM-1 firmware (fm1-base's emulator) | [Groove OS](https://www.groove-os.com/) by Peter Gombos; no code from it | credit only |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Fonts: Barlow Semi Condensed (The Barlow Project Authors), Terminus (Dimitar Toshkov Zhekov) | SIL OFL 1.1 | `base/assets/fonts/` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners, used here only to say what hardware ZENITH-1 runs on.
"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. ZENITH-1 is independent firmware; it is not
affiliated with, endorsed by or supported by any of them, nor by Charles Vestal or Brian Eno.

## Radio

ZENITH-1 never enables the Bluetooth / Wi-Fi radio of the hardware.
