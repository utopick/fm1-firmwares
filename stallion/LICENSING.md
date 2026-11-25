# Stallion licensing

Stallion is free software: firmware for the M-VAVE FM-1, a fork of Clipper, which grew out of SLOOP, which is
based on Felucca. Its code is licensed under the GNU General Public License, version 3 only (`GPL-3.0-only`,
full text in `LICENSE`), and the firmware image Stallion builds is **GPL-3.0-only as a whole**. Every data file
in the tree (images, icons, samples, fonts, preset data) is under a licence that lets you use, change and share
it: GPL-3.0, CC0 1.0, CC BY 3.0, SIL OFL 1.1 or MIT, each listed below and file by file in `assets/MANIFEST`.
Nothing in Stallion is "all rights reserved" or under terms "to be published later".

Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments (Felucca: the platform, the engines, the
editor and the installer); 3dSam / isod89 (SLOOP, Clipper); Eberon Limited (John Gorman) (Stallion); and the authors named in the
files and the table below. Thanks to Leo Kuroshita for Felucca, whose code, under the GPL, Stallion still runs on.

## What is code (GPL-3.0-only)

Every file in this tree that carries an `SPDX-License-Identifier: GPL-3.0-only` header. A few third-party source
files carry another, GPL-compatible, licence and keep it (`firmware/src/fm6_core.c`: Apache-2.0; the MIT notices
in `phys_dsp.c`, `phys_symp.c`; below); the firmware built with them is GPL-3.0-only as a whole:

- the firmware: `firmware/` (app, HAL, update loader)
- the build scripts and tools: `build.sh`, `tools/` (including the generators of the data, below)
- the web pages (installer, editor) and their tests: `web/` (not the Fukiai font, below)
- the host tests: `tests/`

You may use, study, change and share it under the GPL. If you distribute Stallion, or firmware derived from it,
you must also give your recipients its complete corresponding source under the same licence. That includes
devices that ship with modified Stallion inside.

## No additional permission

Felucca's licensing granted an additional permission under GPL-3.0 section 7, to combine the firmware with the
"Felucca Assets" (an icon atlas, a panel image and a generated drum library, Hügelton Instruments, all rights
reserved). Stallion removes that permission, as section 7 allows ("you may at your option remove any additional
permissions from that copy"), because it no longer contains any of those assets (Stallion R51):

| Felucca Asset | In Stallion |
| --- | --- |
| The icon atlas `assets/icons.png` | Replaced: a new atlas drawn from primitives by `tools/draw_icons.py` (GPL-3.0, Stallion's own, the same 86 icons by name and meaning; `tests/run_tests.sh` checks the PNG is what the script draws). `assets/icons.json`, kept, is only the list of the icons' names, in cell order: the firmware's `ICON_*` identifiers, not a drawing |
| The panel image `docs/panel.jpg` | Not in the tree, and nothing refers to it |
| The Hügelton Sample Pack, `tools/gen_waves.py` | Removed. Nothing Stallion builds used it: the GM kit is the CC0 KIT (`assets/samples-cc0/KIT`, every GM role), and the SLICE engine's BREAK, its only other use, is a groovebox engine Stallion does not build (it now takes the CC0 KIT too) |

Contributions are welcome under GPL-3.0-only.

## Additional terms for Stallion's own files (GPL-3.0 section 7)

These terms apply **only to the files Stallion wrote**: the files created in Stallion after its fork from Clipper,
as git history shows, whose notice reads `Copyright (C) 2026 Eberon Limited (John Gorman)`. They are additional
terms that section 7 of the GPL-3.0 allows the copyright holder of those files to add:

1. **Section 7(b), attribution.** The notice `Copyright (C) 2026 Eberon Limited (John Gorman)` must be kept in the
   reasonable legal notices of these files and of works that contain them: in the files themselves, and, where the
   firmware or a page shows its credits or legal notices (the device's ABOUT screen, the editor's and the
   installer's credits), in those credits.
2. **Section 7(e), trademarks.** These terms grant no right to use the name "Stallion" as the name of the firmware,
   or its logo (the longship whose stem rises into a horse's head) or other marks, for a modified version. A modified
   version must not be presented as Stallion; it may say truthfully that it is based on Stallion.

Everything else is plain GPL-3.0-only: you may use, study, change and share these files as the licence says. These
two are the only additional terms; any other restriction is a "further restriction" in section 7's words, which a
recipient may remove.

**Upstream files carry no additional terms.** Files Stallion took from Felucca, SLOOP, Clipper, Clipper Pro and the
other projects listed below stay under their own licences exactly as their authors released them, with no term
added. Their copyright and licence notices are never removed or altered (GPL-3.0 sections 4 and 5); where Stallion
changed such a file, its authors' lines stay as they are.

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Felucca by Leo Kuroshita (@kurogedelic), Hügelton Instruments (<https://github.com/hugelton/Felucca>): the platform, the engines, the editor and the installer, through SLOOP and Clipper | GPL-3.0-only | the files whose header names him |
| SLOOP and Clipper by 3dSam / isod89 (<https://github.com/isod89/sloop-fm1>, <https://github.com/isod89/clipper-fm1>): Stallion's upstream | GPL-3.0-only | the files whose header names them, and most of the tree |
| Instrument and drum samples (Versilian Studios VSCO-2 CE, VCSL; Sonic Pi: SCRCH) | CC0 1.0 | `assets/samples-cc0/`, provenance in `ATTRIBUTION.txt` there |
| The hip-hop pack for the user slots (`tools/gen_hiphop_pack.py`): VSCO-2 CE, VCSL and Sonic Pi sounds; E.PIANO from Greg Sullivan's Wurlitzer EP200 samples (<http://www.sullivang.net/>, mapped by kinwie, <https://github.com/sfzinstruments/GregSullivan.E-Pianos>) | CC0 1.0; E.PIANO CC BY 3.0, credit: Greg Sullivan | `assets/hiphop-pack/`, `CREDITS.txt` there |
| Terminus font 8x16 (ter-u16n): the FM-1's screen, and the web editor's font (`tools/gen_webfont.py` makes it a TrueType font inlined in `web/editor.html`) | SIL OFL 1.1 | `assets/fonts/ter-u16n.bdf`, `assets/fonts/Terminus-LICENSE.txt` |
| Fukiai icon font (Hügelton Instruments), web editor only | MIT | `web/fukiai.ttf`, `web/FUKIAI-LICENSE.txt` |
| CrispyZebra by Leo Kuroshita (<https://github.com/hugelton/CrispyZebra>): the PHASE engine's waveforms are a C port of its oscillator | GPL-3.0 | `firmware/src/eng_phase.c` |
| klattsch by Tony Gies (<https://github.com/tgies/klattsch>): design reference for the VOICE (formant) engine; no code copied. Formant data from Klatt (1980) / Hillenbrand et al. (1995) | MIT (klattsch) | credit only |
| msfa by Google Inc. and Pascal Gauthier, from Dexed (<https://github.com/asb2m10/dexed>): the FM6 engine's synthesis (SLOOP 2.4), ported to integer C for Felucca 1.0 by Leo Kuroshita (Dexed itself is GPL-3.0; only msfa is used; the FM6 factory patches are Felucca's own) | Apache-2.0 | `firmware/src/fm6_core.c`, `LICENSES/Apache-2.0-msfa.txt` |
| DaisySP (Electrosmith, Emilie Gillet) and Rings' sympathetic strings (Emilie Gillet): the PHYS engine's models (SLOOP 2.5, from Felucca 1.0, ported to fixed point by Leo Kuroshita) | MIT | `firmware/src/phys_dsp.c`, `firmware/src/phys_symp.c` (the notice is in each file) |
| The second core's HAL (Clipper 0.7): Charles Vestal's X0X (<https://github.com/charlesvestal/fm1-x0x>), after Kerem Kilic's Melodee; `cpu1.c`, `cpu1.h` and the host double by Andre Rezemini (<https://github.com/andrerezemini/sloop-lab>), through SLOOP 2.7 | GPL-3.0 | `firmware/hal/fm1_cpu1.h`, `firmware/hal/fm1_cpu1.S`, `firmware/src/cpu1.c`, `firmware/src/cpu1.h`, `tests/cpu1_host.c` (the notice is in each file) |
| OberVave by zvenson (<https://github.com/zvenson/obervave>): the RODEO engine's oscillators (polyBLEP one sample late, the band-limited hard sync), X-MOD and state-variable filter, ported to Clipper's engine; its factory programs mapped to RODEO's presets | GPL-3.0-only | `firmware/src/eng_ober.c` (the notice is in the file) |
| TripDeck by anonymousacademe (<https://github.com/anonymousacademe/FM-1-TripDeck>, `firmware/src/fx.h` `ps_run`, `ps_rd`): the two-head pitch shifter of the INSERT's PITCH and PIT2 (Clipper 1.1), adapted per sound | GPL-3.0-only | `firmware/src/fx.c` (`ins_pitch`; the notice is there) |
| CS-1 by twochannels (<https://github.com/twochannels/CS-1>, `firmware/src/cs1_fx.h` `fx_phaser`, its `PH_A` table from `tools/gen_tables.py`): the six-stage phaser of the INSERT's PHAS6 (Clipper 1.1), made mono | GPL-3.0-only | `firmware/src/fx.c` (`ins_phase6`, `PH6_A`; the notice is there) |
| Airwindows Pop3 by Chris Johnson (<https://github.com/airwindows/airwindows>): the compressor's law of the INSERT's LOCMP (Clipper 1.1), in fixed point a block at a time; no file copied | MIT | `firmware/src/fx.c` (`ins_locomp`), `LICENSES/MIT-Airwindows.txt` (upstream's `LICENSE`, byte for byte) |
| Lunar Modulator by ip2k (<https://github.com/ip2k/lunar-modulator>, `engines/src/fx_squash.cc`, Squash > Snap): its port and description of Pop3 (the law, the defaults, the ratio's mapping) that LOCMP follows; no code copied | MIT | `firmware/src/fx.c` (`ins_locomp`), `LICENSES/MIT-Lunar-Modulator.txt` |
| ESTAMPIE by Drew Robinson (<https://github.com/ocean/estampie>, `firmware/src/key_touch.c`, `hal/fm1_input.h`, `hal/fm1_adc.h` at af5a871), after Charles Vestal's Velo (<https://github.com/charlesvestal/fm1-velocity>) and MONK-1 (<https://github.com/charlesvestal/fm1-monk>): KEY TOUCH, velocity and pressure from the keys (the converter on the key rows, the driven row, the landing's depth on a log scale, the learning, the calibration, the pressure past the key's rest), adapted to Stallion's settings (GLO > TOUCH); its test ported as `tests/key_touch_test.c`. Reviewed in the pull request that brings it in (Stallion `key-touch`) | GPL-3.0-only | `firmware/src/key_touch.c`, `firmware/hal/fm1_input.h` (KEY TOUCH's sampling), `firmware/hal/fm1_adc.h` (the short conversions), `tests/key_touch_test.c` (the notice is in each) |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

The data Stallion's own tools make (the icon atlas, Clipper's synthesised sample sources in `assets/clipper-sets/`,
the factory wavetables, the synthesised drum kits, the FM6 patches, Stallion's logo, boot splash and web app icons, drawn
from code by `tools/gen_logo.py` with no outside artwork) are
GPL-3.0-only, as the code that makes them; `assets/MANIFEST` lists each file with its origin.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. "SLOOP" and "Clipper" are the names of
their authors' projects. "Stallion", its logo and its other marks are the names and marks of Eberon Limited's
project: see the section 7(e) term above.

"M-VAVE" and "FM-1" are trademarks of their respective owners. Stallion is independent firmware that runs on FM-1
hardware. It is not affiliated with, endorsed by or supported by those owners, nor by Hügelton Instruments.

## Radio

Stallion, as Felucca, never enables the Bluetooth / Wi-Fi radio of the hardware.
