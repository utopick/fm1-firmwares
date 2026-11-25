# Fernbedienung licensing

Fernbedienung is free software, licensed under the GNU General Public License, version 3 only (`GPL-3.0-only`, full text
in `LICENSE`). That covers the firmware, the tools, the web installer and the tests. A few bundled parts keep their
own licences; they are listed below, and their licence texts are in `LICENSES/`.

Fernbedienung (Copyright (C) 2026 Daniel Pangerl) is a fork of Beiwagen (<https://github.com/DPangerl/beiwagen>), itself a fork of FM1_AudioBase by stevexfer, a fork of MOOD_FM1 (the FM-1
port of MOOD), itself a copy of GATOR (Copyright (C) 2026 npi3pak), which is built on the Felucca platform,
Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments (GPL-3.0-only), through SLOOP and ORBIT. The
files taken from them keep their copyright headers. The visualizer (`firmware/apps/*/avis.c`) is MOOD_FM1's audio
visualizer.

You may use, study, change and share Fernbedienung under the GPL. If you distribute it, or firmware derived from it,
you must also give your recipients its complete corresponding source under the same licence.

Fernbedienung is provided without any warranty (GPL-3.0 sections 15 and 16). Installing it is at your own risk.

**Source code.** The complete corresponding source of every released package is the tag `vX.Y` of
<https://github.com/DPangerl/fernbedienung> (GitHub attaches its archives to the release); the web installer links
the source of the version it installs. `BUILDING.md` describes how to build it.

**Modified files.** Files changed from what they were taken from keep their copyright lines and carry a line per
change: "Modified for GATOR by npi3pak, 2026, from ORBIT 0.6.0", "Modified for MOOD_FM1, 2026: …", "Modified for
FM1_AudioBase, 2026: …", "Modified for Beiwagen, 2026 (Daniel Pangerl): …". Files without such a line are unchanged (the HAL, and the update loader's code, whose binary
is byte-identical to ORBIT's).

## What is GPL-3.0-only

Every file in this tree that carries an `SPDX-License-Identifier: GPL-3.0-only` header:

- the firmware: `firmware/` (the Fernbedienung app, FM1_AudioBase's app and the demo app, the system layer, the HAL, the update loader)
- the build scripts and tools: `build.sh`, `tools/` (not `tools/sdk/`, below)
- the web installer and its tests: `web/` (not `web/emu/`, below)
- the host simulator and tests: `host/`

## Platform and third-party material

| What | Licence | Where |
| --- | --- | --- |
| Felucca by Leo Kuroshita, Hügelton Instruments (<https://github.com/hugelton/Felucca>): the HAL, the update loader, USB-MIDI, USB audio, OTA, recovery, flash storage, the `.fwsc` packer and the command-line installer | GPL-3.0-only | `firmware/hal/`, `firmware/loader/`, `firmware/sys/`, `tools/` |
| ORBIT by dspaudio (<https://github.com/dspaudio/orbit>), a fork of SLOOP: the platform GATOR was cut down from | GPL-3.0-only | as above |
| SLOOP by isod89 (<https://github.com/isod89/sloop-fm1>), a fork of Felucca: the web install protocol (`fm1pkg.js` unchanged from SLOOP 2.7; `fm1ota.js` from SLOOP 2.7 with the loader's macOS port names added), the stock supply levels at start | GPL-3.0-only | `web/fm1ota.js`, `web/fm1pkg.js`, `firmware/hal/fm1_sys.h` |
| ChoralRoot by Quixotic7 (<https://github.com/Quixotic7/ChoralRootFM1>): the order of the audio interrupt's acknowledge (0.18); the release and Pages workflows follow its layout | GPL-3.0-only | `firmware/sys/audio.c`, `.github/workflows/` |
| Inter by The Inter Project Authors (<https://github.com/rsms/inter>): the UI text of the Fernbedienung app (Medium, SemiBold, Display SemiBold), rasterised into the firmware at build time (`tools/gen_font.py`) | SIL OFL 1.1 | `assets/fonts/Inter-*.ttf`, `assets/fonts/InterDisplay-SemiBold.ttf`, `LICENSES/OFL-Inter.txt` |
| Terminus font by Dimitar Toshkov Zhekov: the UI text, rasterised into the firmware at build time (`tools/gen_font.py`) | SIL OFL 1.1 | `assets/fonts/ter-u16n.bdf`, `LICENSES/OFL-Terminus.txt` |
| Shinonome Gothic fonts by Yasuyuki Furukawa and /efont/ (xfonts-shinonome 0.9.11): the few kanji and kana of KAIRO's screens, as 1-bit bitmaps (`tools/gen_kanji.py` -> `firmware/apps/fernbedienung/fb_kanji.h`) | Public domain | `assets/fonts/shnmk16.bdf`, `assets/fonts/shnmk12.bdf`, `LICENSES/PD-Shinonome.txt` |
| JieLi AC79 SDK by JieLi Technology: three of its files go into every `.fwsc` package (below) | Apache-2.0 | `tools/sdk/`, `LICENSES/Apache-2.0-JieLi-SDK.txt` |
| Fernbedienung protocol (`docs/fernbedienung/`): the SysEx protocol between the FM-1 and Steckfeld SF1, public domain so any app may implement it | CC0-1.0 | `docs/fernbedienung/` |
| FM-1Ception (<https://github.com/stevexfer/FM-1Ception>), a fork of fm1-emu by Joakim Eriksson (<https://github.com/joakimeriksson/fm1-emu>): the browser emulator on the site, built by `tools/vendor_emu.sh` (the commit is in `web/emu/VERSION`) | MIT | `web/emu/`, `web/emu/LICENSE` |

## JieLi SDK files in the packages (Apache-2.0)

A `.fwsc` package made by `tools/build.py` holds three unmodified files from the JieLi AC79 SDK, tag
`AC79NN_SDK_V1.2.1_2023-12-13` (<https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK>, `cpu/wl82/tools/`), vendored in
`tools/sdk/` with the SDK's licence:

| File in the package | What it is |
| --- | --- |
| `uboot.boot` | the first-stage boot loader (SPL) |
| `cfg_tool.bin` | the chip configuration block |
| `eq_cfg_hw.bin` | the default hardware EQ table |

They are licensed under the Apache License, Version 2.0, not under the GPL, and their copyright stays with JieLi
Technology. The SDK has no NOTICE file. Every distribution of a package carries the licence texts with it: the
release (`tools/release.py`) and the site (`web/make_site.py`, next to the packages in `firmware/`).

## No vendor material

No M-VAVE or teenage engineering material is part of Fernbedienung. The firmware links no vendor code and contains no vendor data. The web
installer's "Back to the official firmware" holds only the official file's size and SHA-256: you select the file you
downloaded from M-VAVE yourself, and it is checked and installed in your browser, never uploaded or redistributed.

## Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners; "teenage engineering" and "OP-1" are trademarks of
teenage engineering. Fernbedienung is independent firmware that runs on FM-1 hardware; it is not affiliated with,
endorsed by or supported by them. It names itself "Fernbedienung FM-1" on USB so that the host and
the installers recognise the device.

## Contributions

Contributions are welcome under GPL-3.0-only.
