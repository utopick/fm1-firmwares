# Licensing

## The code: GPL-3.0-only

TRAPSTATION OS is a modified version of **BBL JAM BOX** by Blair (blairysbeatlab), itself a modified version of
**Felucca** by Leo Kuroshita (@kurogedelic), Hügelton Instruments. Like both, it is free software under the GNU General
Public License, version 3 only (`GPL-3.0-only`, full text in [LICENSE](LICENSE)).

Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments (Felucca)
Copyright (C) 2026 Blair (blairysbeatlab) (the BBL JAM BOX changes)
Copyright (C) 2026 TRAPSTATION OS contributors (the TRAPSTATION changes)

Every file keeps its own copyright line and `SPDX-License-Identifier` header. This covers the firmware (`firmware/`),
the build script and tools (`build.sh`, `tools/`) and the web pages (`web/`), except the parts listed below. If you
distribute the firmware or firmware made from it, give your recipients its complete source under the same licence.

## Parts under other licences

| What | Licence | Where |
| --- | --- | --- |
| The engine interface, shared DSP helpers and the generator of their tables, from [Felucca-Engines](https://github.com/hugelton/Felucca-Engines) | MIT | `firmware/src/engine.h`, `firmware/src/dsp.c`, `tools/gen_engine_tables.py`, `LICENSES/MIT-Felucca-Engines.txt` |
| The FM6 synthesis core: msfa, from [Dexed](https://github.com/asb2m10/dexed) (Google Inc., Pascal Gauthier), in the integer C port by Leo Kuroshita | Apache-2.0 | `firmware/src/fm6_core.c`, `LICENSES/Apache-2.0-msfa.txt` |
| The [Fukiai](https://github.com/hugelton/Fukiai) icon font, rasterised at build time | MIT | `assets/fonts/fukiai.ttf`, `LICENSES/MIT-Fukiai.txt` |
| BLB Pixel 7 Chunky font by blairysbeatlab, rasterised at build time and used by the web pages | SIL OFL 1.1 | `assets/fonts/BLBPixel7-Chunky.ttf`, `LICENSES/OFL-BLBPixel7.txt` |
| Inter Tight font by The Inter Project Authors, rasterised at build time | SIL OFL 1.1 | `assets/fonts/InterTight[wght].ttf`, `LICENSES/OFL-InterTight.txt` |
| The second core: start, mailbox and guards after [X0X](https://github.com/charlesvestal/fm1-x0x) (charlesvestal) and [Melodee](https://github.com/keremimo/melodee) (keremimo); audio split after [Jangada](https://github.com/zednaked/jangada) (zednaked) | GPL-3.0 | `firmware/hal/fm1_cpu1.*`, `firmware/src/fx.c` |
| Three files of the [JieLi AC79 SDK](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK) in every `.fwsc` package (`uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin`); none are in this repository | Apache-2.0 | `LICENSES/Apache-2.0.txt` |

The firmware built with the MIT and Apache-2.0 parts is GPL-3.0-only as a whole. `LICENSES/` also holds the texts for
parts of Felucca and BBL JAM BOX that are not in this build; they are kept for completeness.

## Not under the GPL

The **TRAPSTATION name, logo and artwork** (`assets/logo/`, the boot and screen artwork in `assets/ui/` and `docs/design/`)
are (C) 2026 Schlensog Audio Lab, all rights reserved. If you distribute a modified version, use your own name and logo.

## Sounds

All sounds are synthesised in the firmware or made by the author. TRAPSTATION OS carries no samples from other
instruments or recordings.

## No vendor material

No M-VAVE material is part of this firmware. The installer's "Return to official V15" only checks the official file you
downloaded yourself (size and SHA-256) and installs it from your browser; it is never uploaded or redistributed.

## Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners. "Felucca" and "Hügelton Instruments" are names of
Hügelton Instruments. TRAPSTATION OS is independent firmware that runs on FM-1 hardware; it is not affiliated with,
endorsed by or supported by them.

This firmware never enables the Bluetooth or Wi-Fi radio of the hardware.
