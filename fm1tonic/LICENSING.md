# X0X licensing

X0X is free software under the GNU General Public License, version 3 only
(`GPL-3.0-only`, full text in `LICENSE`). It is a fork of Felucca and keeps Felucca's
licence. If you distribute X0X, or firmware derived from it, you must give your
recipients its complete corresponding source under the same licence.

## Where the code comes from

| What | Origin | Licence |
| --- | --- | --- |
| Platform: `firmware/hal/`, `firmware/loader/`, `firmware/src/{libc,lcd,gfx,usb,storage,ota}.c`, `tools/` (build, package, install, upload), `web/` (installer) | [Felucca](https://github.com/hugelton/Felucca), Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments; `usb.c` and `storage.c` changed for X0X | GPL-3.0-only |
| `firmware/src/app/{slots,editor,panel,main_fm1}.c` | adapted from Felucca's `eng_sample.c`, `editor.c`, `panel.c`, `main.c` / `audio.c` | GPL-3.0-only |
| reverb, delay and master stage (`dsp/fxbus*`, `dsp/drum909_dsp.h`) | ported from [9W9](https://github.com/athousanddetails/schwung-9W9) (athousanddetails), itself after [ER-99](https://github.com/matthewcieplak/er-99) (Matthew Cieplak) | GPL-3.0 |
| Break generator (`dsp/breaks*`) | ported from [schwung-breakbeat](https://github.com/mestela/schwung-breakbeat) (BB Gen) by mestela, **used with the author's permission** (that repository carries no licence file) | GPL-3.0-only here, by permission |
| The second core's start-up and job hand-off (`firmware/hal/fm1_cpu1.*`) | X0X, after what [Melodee](https://github.com/keremimo/melodee) (keremimo)'s dual-core audio found, with [Jangada](https://github.com/zednaked/jangada) (zednaked)'s measurements and mailbox layout | GPL-3.0-only |
| The idea of a browser emulator for FM-1 firmware (`web/emu/`) | [Groove OS](https://www.groove-os.com/) by Peter Gombos, whose site runs its firmware in the browser; no code from it | credit only |
| Bluetooth audio's calls (`firmware/src/bt/plat_bta.h`, a declaration only, not used yet) | [fm1-base](https://github.com/charlesvestal/fm1-base)'s `include/plat.h`, Copyright (C) 2026 Charles Vestal and the fm1-base authors | MPL-2.0 (the file keeps its header; changes to it are published under MPL-2.0) |
| Bluetooth audio's host stand-in (`firmware/src/bt/plat_bta_sim.c`, host simulator and tests only, never in the firmware image) | rewritten after [fm1-loom](https://github.com/charlesvestal/fm1-loom)'s `app/bt.c` (the fake "Speaker" and its timings), Copyright (C) 2026 Charles Vestal and the fm1-loom authors | MPL-2.0 (the file keeps its header; changes to it are published under MPL-2.0) |
| Bluetooth Classic audio stack (`firmware/src/bt/br/`: BR/EDR inquiry, page, ACL, LMP, SSP, L2CAP, AVDTP, AVRCP, SDP, AFH, the A2DP source; NOT BUILT into the firmware yet), except the two parts below. Copyright (C) 2026 Henri David (hdavid) | fm1-base's `bt/br/` ([fm1-base](https://github.com/charlesvestal/fm1-base)), from [Optimist](https://github.com/w0ts/optimist) (`3274ce5`), unchanged (the AVR assembly files left out: not our chip) | `GPL-3.0-only OR MPL-2.0` (each file's header); taken here under GPL-3.0-only, as the rest of X0X; changes to a file stay under its licence |
| SBC encoder (`firmware/src/bt/br/sbc/`, set up by `bt_sbc.c`): Android's Bluetooth stack, Copyright 1999-2012 Broadcom Corporation, AOSP; two files changed and marked so by fm1-base | Android Open Source Project / Broadcom | Apache-2.0 (`LICENSES/Apache-2.0.txt`; the files keep their headers) |
| micro-ecc (`firmware/src/bt/br/uECC*`, `types.h`, `*.inc`) by Kenneth MacKay, Copyright 2014-2015, the P-192 keys of pairing | [micro-ecc](https://github.com/kmackay/micro-ecc) | BSD-2-Clause (`LICENSES/BSD-2-Clause-micro-ecc.txt`; a binary built with it must carry that notice in its documentation) |
| The radio's registers for Bluetooth (`firmware/src/bt/hal/fm1_bredr.h`, `fm1_ble.h`, `fm1_ble_rf.h`; NOT BUILT into the firmware yet). Copyright (C) 2026 Henri David (hdavid) | [felucca-bsp](https://github.com/hugelton/felucca-bsp) `chip/`, from [Optimist](https://github.com/w0ts/optimist), unchanged; offered as GPL-3.0-only OR MPL-2.0 (we take GPL-3.0-only, the file keeps its header) | GPL-3.0-only OR MPL-2.0 |
| The radio's start-up program (`firmware/src/bt/hal/ble_rf_tables_v15.h`: writes captured from M-VAVE's stock FM-1 V15 firmware, which is JieLi's radio start-up) and its calibration in C (`firmware/src/bt/hal/fm1_rf_cal.h`, also Copyright (C) 2026 Charles Vestal) | felucca-bsp `chip/` unchanged; M-VAVE (Zhuhai Shengke, `m-vave/fm1_open`) and Zhuhai Jieli Technology Co., Ltd. (AC79 AIoT SDK) | Apache-2.0 (`LICENSES/Apache-2.0.txt`; the files keep their headers). The full credits are in `firmware/src/bt/hal/NOTICE.felucca-bsp` and `LICENSING.felucca-bsp.md`, copied unchanged |
| AOSP's SBC decoder (Copyright 2014 The Android Open Source Project, 2002-2006 Open Interface North America), unchanged, used by a host test only (`tests/host/bt_sbc_test.c`) and never built into a firmware | fm1-base `tests/bt/ref/sbc_dec/` ([fm1-base](https://github.com/charlesvestal/fm1-base)) | Apache-2.0 (`LICENSES/Apache-2.0.txt`; the files keep their headers) |
| `tests/host/bta_crypto_test.c`, `bt_crypto_vectors.h` (the pairing maths against the Bluetooth Core Specification's sample data) | fm1-base's `tests/bt/` (include paths changed), Optimist / Henri David | `GPL-3.0-only OR MPL-2.0` (the vectors: the specification's data) |
| Everything else in `firmware/src/{app,dsp,seq}`, `host/`, `tests/` | X0X | GPL-3.0-only |

No recordings and no samples are in this tree or in the firmware (wip474: the built-in break loops, which were rendered from the ER-99 cymbals, are gone). `tools/import_breaks.py` and `tools/upload_breaks.py` can put recordings of your choosing onto a device; those recordings keep their own copyright.

## Felucca Assets

Felucca's non-GPL assets — the icon atlas, the panel photo and the Hügelton drum pack —
are **not** part of this fork and are not used by it. Felucca's section 7 additional
permission concerns those assets only, so it is not needed here.

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Barlow Semi Condensed (The Barlow Project Authors), the default UI face | SIL OFL 1.1 | `assets/fonts/BarlowSemiCondensed-*.ttf`, `assets/fonts/Barlow-OFL.txt` |
| Terminus (Dimitar Toshkov Zhekov), the `terminus` font set | SIL OFL 1.1 | `assets/fonts/ter-u*.bdf`, `assets/fonts/Terminus-LICENSE.txt` |
| Fukiai icon font (Hügelton Instruments), web pages only | MIT | `web/fukiai.ttf`, `web/FUKIAI-LICENSE.txt` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. "M-VAVE" and
"FM-1" are trademarks of their respective owners. TR-808, TR-909 and TB-303 are
trademarks of Roland Corporation, used only to describe what the parts emulate. X0X is
independent firmware; it is not affiliated with, endorsed by or supported by any of them.

## Radio

X0X never enables the Bluetooth / Wi-Fi radio of the hardware.
