# Licensing

LOOPHEADS and its Dinghy foundation are free software under the GNU General Public License, version 3 only (`GPL-3.0-only`, full text in
`LICENSE`). You may use, study, change and share the firmware. If you give someone a firmware built from it, give them its
complete source under the same licence too.

## LOOPHEADS and its influences

- **Dinghy by zvenson** provides the firmware foundation, including hardware support, host testing, and the USB update and rescue path. Its inherited code and credits are listed below. [Dinghy source](https://github.com/zvenson/dinghy)
- **Kerem Kilic (Ellic Studio)** is credited in the source for the original tape engine. LOOPHEADS adapted note-loop timing and loop-boundary handling from the earlier LOOPHEAD v0.3.0. [Tape source and copyright notice](firmware/src/tape.h)
- **Kevin Karplus and Alex Strong** developed the plucked-string synthesis method described in *Digital Synthesis of Plucked-String and Drum Timbres* (1983). The LOOPHEADS String, Tube, and Blow resonators are implemented in [pluck.h](firmware/src/pluck.h). [Original paper](https://doi.org/10.2307/3680062)

## Inherited code

| | |
| --- | --- |
| The platform: `firmware/hal/`, `firmware/loader/`, `crt0.S`, `app.ld`, `firmware/src/` (`usb.c`, `ota.c`, `recovery.c`, `lcd.c`, `gfx.c`, `libc.c`, `bootguard.h`, `uac_fir.h`), `tools/` | Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments ([Felucca](https://github.com/hugelton/Felucca)), with the changes of [SLOOP](https://github.com/isod89/sloop-fm1) (isod89) |
| The SMK-37 board layer: `firmware/hal/smk_input.h`, `fm1_flash_map.h`, the SMK-37 parts of `fm1_cc.h`, `fm1_flash.h`, `fm1_lcd_hw.h`, `lcd.c`, `ota.c`, `bootguard.h`, `firmware/loader/`, `tools/fm1pkg_make.py`, `tools/fm1_install.py`, `tools/build.py`; `firmware/src/smk_wheel.h`; `tests/ota_test.c`, `ldr_test.c`, `install_test.py`, `smk_wheel_test.c`, `smk_pkg_test.py` | Copyright (C) 2026 M. Geisler (genkigenki/makkuro), from [genkigenki/sloop-fm1](https://github.com/genkigenki/sloop-fm1) branch `smk37` (the reference port of the [fm1-to-smk37](https://github.com/genkigenki/fm1-to-smk37) kit) |
| The TRS MIDI IN `firmware/src/midi_uart.c` | Felucca's, as sloopDX carries it, with the ring read by content from Felucca [Salt] 0.9-salt14 by ChanceTheMaker (found by keremimo) |
| The update loader's screen: `firmware/loader/ldr_screen.c`, `tests/ldr_screen_test.c` | Copyright (C) 2026 zvenson (from OberVave, the Firmware Hub's look); the idea, a loader that draws, its 5 x 7 letters and the order of things from [Skiff](https://github.com/illuminus5/skiff) by illuminus5, GPL-3.0 |
| From OberVave: the storage (blobs, slots), `LCD_IDLE`, the SMK-37 wiring of `platform.c`, `store.h`, the pad event queue in `smk_input.h`, `tests/smk_flash_test.c`, `tests/run_tests.sh`, the CI workflow | Copyright (C) 2026 zvenson |
| The app `firmware/src/dinghy.c`, the wiring `platform.c`, the host mode `tests/`, the docs | zvenson |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Terminus font 8x16 (ter-u16n), rendered into `firmware/gen/felucca_font.h` | SIL OFL 1.1 | `assets/fonts/Terminus-LICENSE.txt` |
| [IBM Plex Mono Medium](https://github.com/IBM/plex) by IBM Corp., rendered for LOOPHEADS menus by `tools/gen_ui_font.py` | SIL OFL 1.1 | `assets/fonts/IBMPlexMono-Medium.ttf`, `assets/fonts/IBMPlexMono-OFL.txt` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Logos

The LOOPHEADS boot screen uses [the four-loop artwork](assets/loopheads-boot.png).

`assets/logo.svg` / `logo.png` carry the designburg signet: Copyright (C) designburg, all rights reserved, not under
the GPL. It marks Dinghy itself; a fork uses its own logo.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments; "M-VAVE", "FM-1", "SMK-37" and "MKE-P37"
belong to their owners. LOOPHEADS is an independent firmware project.
