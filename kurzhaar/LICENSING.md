# Licensing

Kurzhaar, der Basshund, is free software under the GNU General Public License, version 3 only (`GPL-3.0-only`, full text in
`LICENSE`). You may use, study, change and share it. If you give someone a firmware built from it, give them its
complete source under the same licence too.

## Who made what

| | |
| --- | --- |
| The platform: `firmware/hal/`, `firmware/loader/`, `crt0.S`, `app.ld`, `firmware/src/` (`usb.c`, `ota.c`, `recovery.c`, `lcd.c`, `gfx.c`, `libc.c`, `bootguard.h`, `uac_fir.h`), `tools/` | Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments ([Felucca](https://github.com/hugelton/Felucca)), with the changes of [SLOOP](https://github.com/isod89/sloop-fm1) (isod89) |
| The SMK-37 board layer: `firmware/hal/smk_input.h`, `fm1_flash_map.h`, the SMK-37 parts of `fm1_cc.h`, `fm1_flash.h`, `fm1_lcd_hw.h`, `lcd.c`, `ota.c`, `bootguard.h`, `firmware/loader/`, `tools/fm1pkg_make.py`, `tools/fm1_install.py`, `tools/build.py`; `firmware/src/smk_wheel.h`; `tests/ota_test.c`, `ldr_test.c`, `install_test.py`, `smk_wheel_test.c`, `smk_pkg_test.py` | Copyright (C) 2026 M. Geisler (genkigenki/makkuro), from [genkigenki/sloop-fm1](https://github.com/genkigenki/sloop-fm1) branch `smk37` (the reference port of the [fm1-to-smk37](https://github.com/genkigenki/fm1-to-smk37) kit) |
| The TRS MIDI IN `firmware/src/midi_uart.c` | Felucca's, as sloopDX carries it, with the ring read by content from Felucca [Salt] 0.9-salt14 by ChanceTheMaker (found by keremimo) |
| The update loader's screen: `firmware/loader/ldr_screen.c`, `tests/ldr_screen_test.c` | Copyright (C) 2026 zvenson (from OberVave, the Firmware Hub's look); the idea, a loader that draws, its 5 x 7 letters and the order of things from [Skiff](https://github.com/illuminus5/skiff) by illuminus5, GPL-3.0 |
| From OberVave: the storage (blobs, slots), `LCD_IDLE`, the SMK-37 wiring of `platform.c`, `store.h`, the pad event queue in `smk_input.h`, `tests/smk_flash_test.c`, `tests/run_tests.sh`, the CI workflow | Copyright (C) 2026 zvenson |
| Dinghy: the app `firmware/src/dinghy.c`, the wiring `platform.c`, the host mode `tests/`, the docs (`docs/DINGHY.md` was its README) | zvenson |
| Kurzhaar, der Basshund: the app `firmware/src/bass.c` and `splash.h`, the splash's dog layer `assets/splash/dog.png`, the sound engine, clock, player, sequencer and reverb `firmware/engine/`, the patches `patches/`, `tools/` (render, tests, gen_*), `tests/run_kurzhaar_tests.sh`, `README.md`, `docs/DESIGN.md`, `docs/img/` | Copyright (C) 2026 JazzMasterT |

## Changes to the upstream files

Kurzhaar is a modified version of Dinghy (<https://github.com/zvenson/dinghy>, forked at its `main` of 2026-11-13).
The files Kurzhaar changed carry a line *Modified by JazzMasterT, 2026-11* saying what changed; the git history has
every change in detail. Changed: `firmware/src/dinghy.c`, `gfx.c`, `midi_uart.c`, `platform.c`, `usb.c`,
`tests/host.c`, `run_host.sh`, `run_tests.sh`, `tools/build.py`, `firmware/loader/ldr_screen.c`,
`.github/workflows/release.yml`,
`docs/MAKE-IT-YOURS.md`; Dinghy's README is `docs/DINGHY.md`; Dinghy's logo is removed. Everything else from
Dinghy is unchanged.

USB audio on macOS 15 and earlier (`firmware/src/usb.c`, `FELUCCA_UAC_MIDI_LAST`): the audio streaming interface
right after audio control and MIDI last, as found in [Felucca issue #67](https://github.com/hugelton/Felucca/issues/67)
and its fix, [PR #322](https://github.com/hugelton/Felucca/pull/322) by dhilowitz (after felucca-bsp's
`FELUCCA_UAC_MIDI_LAST`), GPL-3.0.

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Terminus font 8x16 (ter-u16n), rendered into `firmware/gen/felucca_font.h` | SIL OFL 1.1 | `assets/fonts/Terminus-LICENSE.txt` |
| Audiowide by Brian J. Bonislawsky (Astigmatic): the splash's lettering (KURZHAAR, der Basshund), rendered as an image into `firmware/src/splash_art.h` by `tools/gen_splash_art.py` | SIL OFL 1.1 | `assets/fonts/Audiowide-OFL.txt` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package (each `.fwsc` carries them, unmodified); no SDK files are in this tree | Apache-2.0 | `assets/JieLi-AC79-SDK-LICENSE.txt` (attached to each release), <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## The images

`docs/img/` holds the splash (rendered from `firmware/src/splash_art.h`) and screens from host mode, and
`assets/splash/dog.png` is the splash's dog layer (Lucca, from the author's own photo; the source of the splash): Copyright (C)
2026 JazzMasterT, GPL-3.0 like the rest. Dinghy's logo (the designburg signet, not under the GPL) is not part of
Kurzhaar.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments; "M-VAVE", "FM-1", "SMK-37" and "MKE-P37"
belong to their owners. Kurzhaar is an independent project, not made, endorsed or supported by Hügelton Instruments,
by Dinghy's author or by M-VAVE.
