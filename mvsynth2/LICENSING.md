# Licensing

M-Vsynth2 is free software under the GNU General Public License, version 3 only (`GPL-3.0-only`, full text in
`LICENSE`). You may use, study, change and share it. If you give someone a firmware built from it, give them its
complete source under the same licence too. It is built on Dinghy (zvenson) and keeps its platform; its engine is
being ported from Synth2, which is MIT-licensed. The table says who made what.

## Who made what

| | |
| --- | --- |
| The platform: `firmware/hal/`, `firmware/loader/`, `crt0.S`, `app.ld`, `firmware/src/` (`usb.c`, `ota.c`, `recovery.c`, `lcd.c`, `gfx.c`, `libc.c`, `bootguard.h`, `uac_fir.h`), `tools/` | Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments ([Felucca](https://github.com/hugelton/Felucca)), with the changes of [SLOOP](https://github.com/isod89/sloop-fm1) (isod89) |
| The SMK-37 board layer: `firmware/hal/smk_input.h`, `fm1_flash_map.h`, the SMK-37 parts of `fm1_cc.h`, `fm1_flash.h`, `fm1_lcd_hw.h`, `lcd.c`, `ota.c`, `bootguard.h`, `firmware/loader/`, `tools/fm1pkg_make.py`, `tools/fm1_install.py`, `tools/build.py`; `firmware/src/smk_wheel.h`; `tests/ota_test.c`, `ldr_test.c`, `install_test.py`, `smk_wheel_test.c`, `smk_pkg_test.py` | Copyright (C) 2026 M. Geisler (genkigenki/makkuro), from [genkigenki/sloop-fm1](https://github.com/genkigenki/sloop-fm1) branch `smk37` (the reference port of the [fm1-to-smk37](https://github.com/genkigenki/fm1-to-smk37) kit) |
| The TRS MIDI IN `firmware/src/midi_uart.c` | Felucca's, as sloopDX carries it, with the ring read by content from Felucca [Salt] 0.9-salt14 by ChanceTheMaker (found by keremimo) |
| The update loader's screen: `firmware/loader/ldr_screen.c`, `tests/ldr_screen_test.c` | Copyright (C) 2026 zvenson (from OberVave, the Firmware Hub's look); the idea, a loader that draws, its 5 x 7 letters and the order of things from [Skiff](https://github.com/illuminus5/skiff) by illuminus5, GPL-3.0 |
| From OberVave: the storage (blobs, slots), `LCD_IDLE`, the SMK-37 wiring of `platform.c`, `store.h`, the pad event queue in `smk_input.h`, `tests/smk_flash_test.c`, `tests/run_tests.sh`, the CI workflow | Copyright (C) 2026 zvenson |
| The wiring `platform.c`, the host mode `tests/host.c`, the Dinghy docs (`docs/API.md`, `RULES.md`, `MAKE-IT-YOURS.md`, `SMK37.md`) | zvenson |
| The second core: `firmware/hal/fm1_multicore.h`, `fm1_core1_stop.h`, `fm1_core1_bar.h`, `fm1_power.h`, `firmware/src/audio_worker.h`, the CPU1 parts of `fm1_irq.h`, `fm1_sys.h`, `fm1_vec.S`, `crt0.S` and `app.ld` | Copyright (C) 2026 Kerem Kilic (Ellic Studio), from [Melodee](https://github.com/keremimo/melodee) `165d177`; its CPU1 hold from Felucca 1.6.1 (Leo Kuroshita, Hügelton Instruments); the hand-over of voices to it (`vs_voice.c`, `vs_dsp.c`, `hal/fm1_dual.h`) Kris (bk40-home) |
| From M-vance: the USB audio wiring and the MIDI clock out in `platform.c` / `usb.c`, the `-O2` DSP unit in `tools/build.py`, the host's SysEx and tick counter in `tests/host.c`, `firmware/src/vs_fixed.h` (its `mv_fixed.h`), `flash.ps1` | Copyright (C) 2026 Kris (bk40-home) |
| The USB audio output `firmware/src/uac_out.h`, `uac_out.c` and its test `tests/uac_out_test.c` | **MPL-2.0**, not GPL (each file's header): ported from [felucca-bsp](https://github.com/hugelton/felucca-bsp) `bsp/chip/usb.c`, Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments; the integer port Copyright (C) 2026 Kris (bk40-home). MPL-2.0 is compatible with the GPL (its section 3.3): the firmware as a whole stays GPL-3.0-only |
| The screen reader's protocol `firmware/src/announce.c` and words tool `tools/gen_words.py` | **MPL-2.0**, not GPL (each file's header): copied unchanged from [fm1-base](https://github.com/charlesvestal/fm1-base) (`device/announce.c`, `tools/gen_words.py`) for [fm1-reader](https://github.com/charlesvestal/fm1-reader), Copyright (C) 2026 Charles Vestal. Change them there and copy them again (fm1-reader's `tools/sync_announce.sh`). MPL-2.0 is compatible with the GPL: the firmware as a whole stays GPL-3.0-only |
| Bluetooth MIDI: fm1-kit's `third_party/fm1-kit/firmware/fk_ble/` (built in by `platform.c`) | **MPL-2.0 and Apache-2.0 parts**, not GPL (each file's header; `fk_ble/README.md` and `LICENSES/`): Henri David's own BLE stack from [Optimist](https://github.com/w0ts/optimist) as [fm1-base](https://github.com/charlesvestal/fm1-base) carries it (`bt/ble`, GPL-3.0-only OR MPL-2.0), felucca-bsp's radio drivers (MPL-2.0) and its calibration and start-up tables (Apache-2.0: JieLi's SDK and M-VAVE's V15, as Charles Vestal and Optimist rewrote them), copied unchanged; the glue `fk_ble.c` after fm1-base's `device/bt_own.c` (Charles Vestal), Kris (bk40-home). No JieLi binary library is linked. MPL-2.0 and Apache-2.0 are compatible with the GPL-3.0: the firmware as a whole stays GPL-3.0-only |
| Velocity and pressure from the keys: fm1-kit's `third_party/fm1-kit/firmware/fk_touch/` (built in by `platform.c`; its float half `fk_touch_fpu.c` by `tools/build.py`) | **MPL-2.0**, not GPL (each file's header; `fk_touch/README.md` and `LICENSES/`): [fm1-base](https://github.com/charlesvestal/fm1-base)'s `lib/touch.c`, `lib/touch.h`, `lib/sense.c` and `include/fastmath.h`, Copyright (C) 2026 Charles Vestal (from fm1-velocity, CTL-1 and MONK-1), copied unchanged; the glue `fk_touch.h`, `fk_touch.c`, `fk_touch_fpu.c` and its tests, Kris (bk40-home). MPL-2.0 is compatible with the GPL-3.0: the firmware as a whole stays GPL-3.0-only |
| The analog key rows `firmware/hal/fm1_input_an.h` (included by `fm1_input.h`) and the converter `firmware/hal/fm1_adc.h` | **MPL-2.0**, not GPL (each file's header): from [felucca-bsp](https://github.com/hugelton/felucca-bsp) `boards/fm1/fm1_input.h` and `fm1_adc.h` (commit 2bd9dbe), the code unchanged: Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments; the analog key rows Copyright (C) 2026 Charles Vestal (fm1-velocity, fm1-monk). `fm1_input.h` itself stays Dinghy's (GPL-3.0-only), with the few lines that call them |
| **M-Vsynth2:** the app `firmware/src/mvsynth2.c`; the engine `firmware/src/vs_osc.*`, `vs_env.*`, `vs_voice.*`, `vs_patch.*`, `vs_dsp.c`, `vs_build.h`; the screens `vs_ui.c`, `tools/gen_ui.py`, the screen reader's side `vs_speak.c`, `firmware/words.tsv`, `docs/words/`, `firmware/gen/ann_words.h`, `tests/run_speak.sh`, `tests/scripts/speak.*`, `tests/speak_allow.txt`, `firmware/gen/vs_ui_gen.h` (its font tables are DejaVu's, below); the patch library `library/adapter-mvsynth2.js`, `library/mock-mvsynth2.js`, `tools/gen_library_page.py`, `docs/library.html`, `tests/library_test.js`, `tests/library_browser_test.py`; fm1-kit (`third_party/fm1-kit/`, its own LICENSE, GPL-3.0-only, to become its own repo); the gate `vs_gate.*`; the generators `tools/gen_wave.py`, `gen_tables.py`, `gen_params.py`, `tools/vsynth2-params.yaml`, `tools/synth2.py`, and what they write in `firmware/gen/` (`vs_wave.h`, `vs_tables.h`, `vs_params.h`, `vs_gate_tab.h`); the patch tools `tools/sy1.py`, `make_bank.py`; the compare tools `tools/compare/`, `tests/vs_render.c`, `tests/run_compare.sh`; the bench `tools/bench/`; the tests `tests/vs_*`, `tests/sy1_test.py`, `tests/run_unit.sh`, `tests/scripts/gate.txt`, `play.txt`; the design `docs/design/` | Copyright (C) 2026 Kris (bk40-home). The engine is ported from [Synth2](https://github.com/chab/oxo_synth2) `EngineCore/` (MIT), Copyright (c) 2026 Francois Chabloz: its laws and tables, its oscillators, envelopes, filter and voice handling, its patch codec and legacy conversion. GPL-3.0-only here, with Synth2's notice kept (below). `tools/compare/ref_render.cpp` compiles Synth2's own sources, on the computer only |
| The factory bank: `tools/bank/factory/*.sy1`, `firmware/gen/vs_factory.h` | Synth2's "Synth2 Factory" bank, copied unchanged (MIT, Copyright (c) 2026 Francois Chabloz): shipped under MIT with his permission (by email, 14 Nov 2026: "the 'Synth2 Factory' bank is mine and may be shipped under the MIT license"; keep the "Madame Eljay" bank out) |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Terminus font 8x16 (ter-u16n), rendered into `firmware/gen/felucca_font.h` | SIL OFL 1.1 | `assets/fonts/Terminus-LICENSE.txt` |
| DejaVu Sans Condensed Bold (`assets/fonts/dejavu/`), rendered into `firmware/gen/vs_ui_gen.h` by `tools/gen_ui.py` | Bitstream Vera licence (DejaVu changes: public domain) | `assets/fonts/dejavu/LICENSE` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Synth2's licence

The files ported from Synth2 carry this notice, as its licence asks:

```
MIT License

Copyright (c) 2026 Francois Chabloz
Copyright (c) 2026 sl23 (Windows version)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## What is not used

- No Synth1 code, binary or artwork. Synth2 studied the original through its audio output only, and this port
  reads Synth2, never the original.
- None of the names "Oxo", "Oxo Music" or "Oxo Synth2", and none of Synth2's icons: its README keeps them out of
  the code licence.
- No third-party patch bank: Synth2's "Madame Eljay" starter bank is a designer's work and is not in this tree.
- Dinghy's logo (the designburg signet, not under the GPL) is not in this tree. M-Vsynth2 has no logo yet.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments; "M-VAVE", "FM-1", "SMK-37" and "MKE-P37"
belong to their owners. Synth1 is the work of Daichi Laboratory. M-Vsynth2 is not made by, endorsed by or affiliated
with any of them, or with Oxo Music.
