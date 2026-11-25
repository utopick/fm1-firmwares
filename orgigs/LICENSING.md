# Licensing

OrGigs, like Dinghy (its platform, 0.4), is free software under the GNU General Public License, version 3 only (`GPL-3.0-only`, full text in
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
| Dinghy's app `dinghy.c` (not in OrGigs), the wiring `platform.c`, the host mode, Dinghy's docs | zvenson |
| OrGigs: `firmware/src/orgigs.c`, `firmware/core/`, `firmware/board/`, `sim/`, `tests/host.c` and the scripts, `tools/gen_*.py`, `docs/`; its changes to the platform, marked (OrGigs) | OrGigs's author (Bobo), with Claude |
| The web installer's update protocol: `web/fm1pkg.js` (unchanged), `web/fm1ota.js` (its changes for Windows 11's MIDI service marked (OrGigs)) | Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments (Felucca), as [Skiff](https://github.com/illuminus5/skiff) (illuminus5, GPL-3.0) carries it; `web/installer.html`, `tools/make_site.py` and `tests/web_test.mjs` are OrGigs's, after Skiff's installer page, site script and fake device |
| The SMK-37 protections after [Skiff](https://github.com/illuminus5/skiff) (illuminus5, GPL-3.0): the package size check in `ota.c`, the loader size limit in `tools/build.py` | marked (OrGigs, after Skiff) |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Varela Round (`assets/fonts/VarelaRound-Regular.ttf`), rendered into `firmware/gen/felucca_font.h` by `tools/gen_font_ttf.py` | SIL OFL 1.1 | `assets/fonts/VarelaRound-LICENSE.txt` |
| The Yamaha SEQTRAK's sound list (`assets/seqtrak/presets.csv`, generated into `firmware/gen/yst_presets.h`) and its MIDI protocol (`firmware/core/orgigs_yst.c` follows it), from [jaeggerr/seqtrak-docs](https://github.com/jaeggerr/seqtrak-docs) | MIT | `assets/seqtrak/LICENSE.seqtrak-docs` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## The drawbar registrations

The 36 tonewheel registrations in `firmware/core/orgigs_presets.c` are drawbar settings (nine digits each), not
sounds. Nos. 23-36 are the classic factory preset keys and stops as the organ maker's playing manuals of the 1950s and
Stevens Irwin's *Dictionary of Hammond-Organ Stops* give them; nos. 1-22 are common settings of jazz, soul, gospel and
rock players as books on the instrument (Mark Vail, *The Hammond Organ: Beauty in the B*; Dave Limina, *Hammond Organ
Complete*), *Keyboard* magazine and the organ community's references document them. They carry neutral style names of
OrGigs's own, no player, song or brand names. The pipe, free-reed and pedal registrations are OrGigs's own.

## The logo

`assets/logo.svg` / `logo.png` carry the designburg signet: Copyright (C) designburg, all rights reserved, not under
the GPL. It marks Dinghy itself; OrGigs keeps it in `assets/` unchanged and does not show it.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments; "M-VAVE", "FM-1", "SMK-37" and "MKE-P37"
belong to their owners. Dinghy and OrGigs are not made or endorsed by them.
