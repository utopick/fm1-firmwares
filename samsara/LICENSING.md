# SAMSARA licensing

SAMSARA (built as TIDE) is a fork of AMB-1 1.3.2 by Tomorrow's Man, under the same licence, the **Mozilla Public
License 2.0**, file by file. The files SAMSARA changed carry its copyright line beside AMB-1's (`app/app.h`,
`app/host.c`, `app/dsp/amb.c`, `app/dsp/amb.h`, `app/ui.c`, `app/project.c`, the tests and tools it touched); the
files it added (`tools/render.c`, `.github/workflows/dev.yml`, the scenarios of its own) are its own, MPL-2.0 too.
fm1-base and felucca-bsp are in this tree as plain folders (`base/`, `base/bsp/`), unchanged but for what
`git log -- base` shows; their commits are in `UPSTREAM.md`. The Wheel of Samsara on the screen is drawn in code
(`app/ui.c`, `draw_wheel`) from the traditional eight-spoked form; no picture was copied. The Choir pad colour
(`app/dsp/choir.h`, added by SAMSARA, MPL-2.0) holds the first 32 harmonic amplitudes of three single-cycle
waveforms from **Adventure Kid Waveforms** (AKWF) by Kristoffer Ekstrand, `AKWF_hvoice_0024`, `_0076` and `_0052`,
which their author dedicated to the public domain (CC0 1.0 Universal:
<https://github.com/KristofferKarlAxelEkstrand/AKWF-FREE>); no attribution is owed, and this is one given in
thanks. Everything below is AMB-1's own text and stands as it is.

---

# AMB-1 licensing

AMB-1 is free software under the **Mozilla Public License 2.0** (`MPL-2.0`, full text in `LICENSE`), file by file.
If you change one of its files and share the result, share that file's source under the MPL. It is built on
[fm1-base](https://github.com/charlesvestal/fm1-base) and [felucca-bsp](https://github.com/hugelton/felucca-bsp)
(`base/`, a git submodule), both MPL-2.0.

Until 0.9, AMB-1 was GPL-3.0-only, built on Felucca's platform layer. That code is gone from this tree: the platform
is fm1-base's now, and AMB-1's own code (the engine, the UI, the pieces) is relicensed by its author. AMB-1 0.9 and
earlier stay under the GPL.

## Where the code comes from

| What | Origin | Licence |
| --- | --- | --- |
| The platform: `base/` (boot, USB and USB audio, the TRS jack, storage, the update path, screen, panel, the screen reader, the host simulator and the browser emulator, build and install tools) | [fm1-base](https://github.com/charlesvestal/fm1-base) and [felucca-bsp](https://github.com/hugelton/felucca-bsp), from [Felucca](https://github.com/hugelton/Felucca) by Leo Kuroshita (@kurogedelic), Hügelton Instruments, under MPL-2.0 with his permission ([felucca-bsp#4](https://github.com/hugelton/felucca-bsp/issues/4)) | MPL-2.0 |
| `app/` (`app.c`, `app.h`, `ui.c`, `project.c`, `host.c`, `dsp/amb.c` with its Dattorro plate from FoMni-1), `web/app/`, `tests/`, `tools/` | AMB-1, Charles Vestal | MPL-2.0 |
| The idea of a browser emulator for FM-1 firmware (fm1-base's emulator) | [Groove OS](https://www.groove-os.com/) by Peter Gombos, whose site runs its firmware in the browser; no code from it | credit only |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Fonts: Barlow Semi Condensed (The Barlow Project Authors), Terminus (Dimitar Toshkov Zhekov) | SIL OFL 1.1 | `base/assets/fonts/` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. "M-VAVE" and "FM-1" are trademarks of their
respective owners, used here only to say what hardware AMB-1 runs on. AMB-1 is independent firmware; it is not
affiliated with, endorsed by or supported by any of them.

## Radio

AMB-1 never enables the Bluetooth / Wi-Fi radio of the hardware.
