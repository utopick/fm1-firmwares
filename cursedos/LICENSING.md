# Licensing

cursed os is custom firmware for the M-VAVE FM-1. It is a fork of
[JIANT FM](https://github.com/juanjiant-bit/JIANT) (Juan Jiant), which is built on
[Felucca](https://github.com/hugelton/Felucca) (Leo Kuroshita, Hügelton Instruments). All three are free software
under the GNU General Public License, version 3 only (`GPL-3.0-only`, the full text in `LICENSE`).

**In short:**

- The firmware as a whole, and every package built from this tree, is `GPL-3.0-only`. If you share it, or something
  made from it, you share its complete source under the same licence.
- cursedsound's own work in this tree is also yours to use under the MIT licence (below): do what you like with it,
  just keep the credit.
- Parts by other people keep their own licences. They are listed below, with their licence texts in `LICENSES/`.

## cursed os (cursedsound's own work)

Copyright (C) 2026 cursedsound

The files whose header reads `SPDX-License-Identifier: GPL-3.0-only OR MIT` and
`Copyright (C) 2026 cursedsound` are cursedsound's own. You may use them under either licence: the GPL like the
rest of the tree, or the MIT licence (`LICENSES/MIT-cursedsound.txt`), which lets you do anything with them as long as
the copyright notice stays (a credit). They are:

- the interface: `firmware/src/cos.c`, `cos_drm.c`, `cos_iso.c`, `cos_live.c`, `cos_meter.c`, `cos_morph.c`,
  `cos_remote.c`, `cosfx.c`, `ui_acid.c`, `ui_bleep.c`, `ui_dub.c`
- the engines and sounds: `eng_acid.c` (the wrapper; the 303 voice it wraps is X0X's, below), `eng_dub.c`,
  `eng_kick.c`, `kits.c`, `rumble.c`, `x0x/acid_glue.c`
- the tools: `tools/cursed_remote.py`, `tools/cursed_remote_proto.py`, `tools/fm1_uboot.py`, `tools/gen_cos_font.py`
- cursed os's host tests in `tests/` with the same header

cursedsound's changes inside other people's files (JIANT's and Felucca's sources) are offered on the same terms, but
those files as a whole stay `GPL-3.0-only`: the MIT offer covers only cursedsound's own lines. Not covered, as they
follow or contain other people's work: `eng_fmdrum.c`, `xr_tables.h` and `tools/gen_xr_tables.py` (after the LXR
firmware, GPL-3.0-only), and the copied X0X files in `firmware/src/x0x/` (GPL-3.0-only, the Open303 parts MIT).

## JIANT FM

[JIANT FM](https://github.com/juanjiant-bit/JIANT) by Juan Jiant, `GPL-3.0-only`: the engines, the sequencer, the songs,
MIDI, storage and JIANT's own interface. cursed os is a fork of JIANT V10.19 and keeps its history; JIANT's README is
in `docs/JIANT-README.md`. JIANT's song system follows [SLOOP](https://github.com/isod89/sloop-fm1) 2.4.1 by isod89
(GPL-3.0: `firmware/src/song_chain.c` names the files).

## Felucca

Felucca's own text follows, unchanged in substance: what it says of Felucca holds for cursed os, which is firmware
derived from it.

Felucca is free software, licensed under the GNU General Public License, version 3 only
(`GPL-3.0-only`, full text in `LICENSE`). That covers the code and its own assets. A few
bundled or ported parts keep their own licences; they are listed below, and their licence
texts are in `LICENSES/`.

Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments

## What is GPL-3.0-only

Every file in this tree that carries an `SPDX-License-Identifier: GPL-3.0-only` header:

- the firmware: `firmware/` (app, HAL, update loader)
- the build script and tools: `build.sh`, `tools/`
- the web pages (installer, editor, the browser emulator `web/emu/`) and their tests: `web/` (not the Fukiai and DotGothic16 fonts, below)
- the host tests: `tests/`
- JIANT FM's interface art: `assets/ui-art/`, `assets/ui-shapes/` and the concept image `docs/jiant-fm-ui-concept.jpg`
  (by JIANT's author, under GPL-3.0-only like the rest of JIANT)

One source file is a port and keeps the licence of its original: `firmware/src/fm6_core.c`
(msfa, Apache-2.0). The Bluetooth files (below, "Radio") keep their own headers too. The firmware built with it is GPL-3.0-only as a whole. (The PHYS engine, ported
from DaisySP and Rings, MIT, was removed in FELUCCA TONIC.)

You may use, study, change and share Felucca under the GPL. If you distribute Felucca, or
firmware derived from it, you must also give your recipients its complete corresponding
source under the same licence. That includes devices that ship with modified Felucca inside.

## Hügelton Instruments' own work

All by Hügelton Instruments (Leo Kuroshita), in this tree:

| What | Licence | Where |
| --- | --- | --- |
| Felucca: firmware, tools, web pages, tests | GPL-3.0-only | `LICENSE` |
| The PHASE engine's waveforms: a C port of the oscillator of CrispyZebra (<https://github.com/hugelton/CrispyZebra>) | GPL-3.0 | `firmware/src/eng_phase.c` |
| The DRUM voices and kit | GPL-3.0-only | `firmware/src/drum_voice.c`, `firmware/src/eng_drum.c` |
| The Hügelton Sample Pack: Felucca's drum sounds, made by `tools/gen_waves.py` (not CC0; JIANT builds none of them in: SLICE, which played its BREAK, is retired) | GPL-3.0-only | `tools/gen_waves.py` |
| The Fukiai icon font (<https://github.com/hugelton/Fukiai>): the firmware's icons (rasterised at build time by `tools/gen_aa_icons.py`) and the web editor's | MIT | `web/fukiai.ttf`, `LICENSES/MIT-Fukiai.txt`, `web/FUKIAI-LICENSE.txt` |
| fm1-clk320-probe by curist (<https://github.com/curist/fm1-clk320-probe>): the switch from the FM-1's 360 MHz to JieLi's rated 320 MHz behind MENU > SYSTEM > CPU CLOCK (JIANT 0.9.9-stab, as 0.9.12; the check of the clock registers and the switch), unchanged; its sequence after the JieLi AC79 SDK's `sys_clock_update` (Apache-2.0) | MIT | `firmware/hal/fm1_clk320.h`, `LICENSES/MIT-fm1-clk320.txt` |

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| IBM Plex Mono (SemiBold) by IBM Corp. and Michroma by The Michroma Project Authors: the UI's values and big titles since JIANT 0.6.56, rasterised into the firmware at build time (`tools/gen_aa_font.py --preset jiant-lab`; the generated tables are not offered as a font) | SIL OFL 1.1 | `assets/fonts/IBMPlexMono-SemiBold.ttf`, `assets/fonts/Michroma-Regular.ttf`, `LICENSES/OFL-IBMPlexMono.txt`, `LICENSES/OFL-Michroma.txt` |
| Chakra Petch font by The Chakra Petch Project Authors: the UI text since JIANT 0.5 (the labels since 0.6.56), rasterised into the firmware at build time (`tools/gen_aa_font.py --preset chakra-petch`; the generated tables are not offered as a font) | SIL OFL 1.1 | `assets/fonts/ChakraPetch-*.ttf`, `LICENSES/OFL-ChakraPetch.txt` (also `assets/fonts/OFL-ChakraPetch.txt`) |
| Press Start 2P font by The Press Start 2P Project Authors (CodeMan38): cursed-os's text, rasterised into the firmware at build time as a 1-bit 8 x 8 table (`tools/gen_cos_font.py`; the generated table is not offered as a font; Press Start 2P's Reserved Font Name is not used for it) | SIL OFL 1.1 | `assets/fonts/PressStart2P-Regular.ttf`, `LICENSES/OFL-PressStart2P.txt` |
| Inter Tight font by The Inter Project Authors: the UI text up to JIANT 0.4 (kept for the `inter-tight` preset; the font declares no Reserved Font Name) | SIL OFL 1.1 | `assets/fonts/InterTight[wght].ttf`, `LICENSES/OFL-InterTight.txt` (also `assets/fonts/OFL.txt`) |
| msfa by Google Inc. and Pascal Gauthier, from Dexed (<https://github.com/asb2m10/dexed>): the FM6 engine's synthesis, ported to integer C (Dexed itself is GPL-3.0; only msfa is used; the FM6 factory patches are Felucca's own) | Apache-2.0 | `firmware/src/fm6_core.c`, `LICENSES/Apache-2.0-msfa.txt` |
| klattsch by Tony Gies (<https://github.com/tgies/klattsch>): design reference for the VOICE engine; no code copied. Formant data from Klatt (1980) / Hillenbrand et al. (1995) | MIT (klattsch) | credit only |
| The CMU Pronouncing Dictionary (cmudict 0.7b, <https://github.com/cmusphinx/cmudict>) by Carnegie Mellon University: VOICE's English words (JIANT 0.8.5), a subset of ~2100 common words with their pronunciations, packed into the firmware at build time (`tools/gen_lyrics.py`) | BSD-2-Clause | `tools/lyrics/en_dict.txt` (the notice in its header), `LICENSES/BSD-2-Clause-CMUdict.txt` |
| X0X by charlesvestal (<https://github.com/charlesvestal/fm1-x0x>, ca2d377): the ACID engine's 303 voice, `dsp/bass303.c`, `bass303.h`, `fastmath.h`, `x0x_param.h` copied unchanged (cursed-os's `eng_acid.c` wraps them); X0X ported it from schwung-303: Open303 by Robin Schmidt (MIT: the notice in `LICENSES/MIT-Open303.txt`), the Devilfish ranges after jc303 (midilab), the RAT drive after dm-Rat (Dave Mollen), the speed-ups after Optimist (henri / hdavid); portions of `bass303.c` by Kerem Kilic (Ellic Studio), as its header says | GPL-3.0-only (the Open303 parts MIT) | `firmware/src/x0x/`, `LICENSES/MIT-Open303.txt` |
| FM-1 Transporter by Leo Kuroshita (<https://github.com/kurogedelic/FM-1-transporter>) and jl-uboot-tool by kagaimiq (<https://github.com/kagaimiq/jl-uboot-tool>): the JieLi boot mode's protocol behind `tools/fm1_uboot.py` (its commands, their codes and the loader's address), written again in Python for cursed os, no code copied; the JieLi loader blob it needs (`wl82loader.bin`) is not in this tree or any package, you bring your own copy | MIT (both) | credit only |
| The Elektron Syntakt's MIDI CC list by Pencil Research (<https://github.com/pencilresearch/midi>, `Elektron/Syntakt.csv` at 23d2527): test data only, copied unchanged; `tests/syntakt_cc_test.c` sends every CC in it into the FM-1 and checks the Syntakt CCs GLO > LINK 2 sends. Not in the firmware or the download | GPL-3.0 | `tests/data/syntakt_cc.csv` |
| HYP-1 by RedtailWorks (<https://github.com/RustyPawz/fm1-HYP1>): the idea of a key pressed setting the song's key (cursed os's SCL); written fresh, no HYP-1 code | (idea only) | credit only |
| The LXR drum machine's firmware by Erica Synths (<https://github.com/erica-synths/lxr-desktop-app>, `Core/Src/Soundengine/DSPAudio/FX/Distortion.c`): the TUBE (ECC83) and RAT (1N914) transfer curves, converted to Q15, and its twelve transient samples (`transientTables.c`, signed 8 bits as it has them), by `tools/gen_xr_tables.py` into `firmware/src/xr_tables.h`; FMDRUM's voices (`eng_fmdrum.c`), DIST TUBE / RAT / RING and the TIGHT reverb (`fx.c`) follow its DrumVoice, CymbalVoice, HiHat, distortion, `Ringmod.c` and `Reverb.c` designs, written again in integers. No LXR or Erica Synths name on the device or in its interface. Erica Synths' NOTICE.md (GPL-3.0 §7 additional terms) is kept to: its copyright line (Copyright (C) 2012-2026 Erica Synths) stays in `xr_tables.h` and `gen_xr_tables.py`; §7(e), no right to the names "Erica Synths", "LXR", "LXR-02" beyond truthful statements (such as this credit), and cursed os is not presented as theirs or approved by them; §7(c), a modified version marked as different: cursed os is another firmware for another device, its own name on its start-up screen. Their terms: <https://github.com/erica-synths/lxr-desktop-app/blob/main/NOTICE.md> | GPL-3.0-only (with Erica Synths' §7 terms) | `firmware/src/xr_tables.h` (the curves and samples), `tools/gen_xr_tables.py` |
| X0X by charlesvestal (<https://github.com/charlesvestal/fm1-x0x>), a Felucca fork: the design of the browser emulator (the worklet, the device clock driven by its audio, the exports); its files credit it in their headers | GPL-3.0 | `web/emu/` |
| DotGothic16 font by The DotGothic16 Project Authors (<https://github.com/fontworks-fonts/DotGothic16>): the browser emulator's knob labels, served with its page (cut to printable ASCII; the font declares no Reserved Font Name) | SIL OFL 1.1 | `web/emu/fonts/DotGothic16-subset.woff`, `LICENSES/OFL-DotGothic16.txt` (also `web/emu/fonts/OFL.txt`) |
| Optimist's Bluetooth LE stack by Henri David (hdavid, <https://github.com/w0ts/optimist>), the hardware-tested copy in fm1-base by Charles Vestal (<https://github.com/charlesvestal/fm1-base>, `bt/ble` at 4039a8b, with its UBSan fix): JIANT's Bluetooth (V10.12), unchanged but for one hook (V10.14: `ble_hw_wl82.c` hands each good packet's RSSI word to `BLE_HW_RX_RSSI` when defined); used under the GPL-3.0-only option of its dual licence, headers kept; (V10.13) the host test of its BLE-MIDI codec from the same copy (`tests/bt/ble_midi_test.c`, include path only changed) | GPL-3.0-only OR MPL-2.0 | `firmware/bt/ble/`, `tests/ble_midi_test.c`, `LICENSES/MPL-2.0.txt` |
| Melodee by Kerem Kilic (Ellic Studio, <https://github.com/keremimo/melodee>, 1.6.0-rc.7, 022bab7): the radio drivers as Melodee carries them (Optimist's, with Melodee's iterative start-up replay and pool placement), and the model of the integration (the radio started on demand with the audio quiet, IRQ 45 / 29 at priority 2 below the audio, the live calibration's constants); `hal/fm1_power.h` (V10.11) | GPL-3.0-only | `firmware/hal/fm1_ble.h`, `firmware/hal/fm1_ble_rf.h` (JIANT: one include renamed), `firmware/hal/fm1_power.h` |
| The radio's own calibration, JieLi's (the AC79 SDK's `wl_rf_common.a`) rewritten in C by Charles Vestal for felucca-bsp (<https://github.com/jmarianski/felucca-bsp>, `chip/`, b0b2428) | Apache-2.0 | `firmware/hal/fm1_rf_cal.h`, `LICENSES/Apache-2.0.txt` |
| The radio's start-up values captured from M-VAVE's V15 (published under Apache-2.0 in fm1_open) and JieLi's SDK, as Optimist and felucca-bsp carry them | Apache-2.0 | `firmware/hal/ble_rf_tables_v15.h`, `LICENSES/Apache-2.0.txt` |
| JieLi AC79 SDK by JieLi Technology: three of its files go into every `.fwsc` package (below); none are in this tree | Apache-2.0 | `LICENSES/Apache-2.0.txt` |

On the device, HOME held > ABOUT opens the information screen; turning PRESETS scrolls on into
CREDITS, a short list of these authors, licences and source URLs.

## JieLi SDK files in the packages (Apache-2.0)

A `.fwsc` package made by `tools/build.py` (with `tools/fm1pkg_make.py`; this is the package the
web installer installs) holds three unmodified files from the JieLi AC79 SDK
(<https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK>, `cpu/wl82/tools/`). They are read from your SDK
checkout at build time (see BUILDING.md); no SDK files are in this tree.

| File in the package | What it is |
| --- | --- |
| `uboot.boot` | the first-stage boot loader (SPL) |
| `cfg_tool.bin` | the chip configuration block |
| `eq_cfg_hw.bin` | the default hardware EQ table |

They are licensed under the Apache License, Version 2.0 (`LICENSES/Apache-2.0.txt`), not under
the GPL, and their copyright stays with JieLi Technology. The SDK has no NOTICE file. Apache-2.0
files may be distributed together with GPL-3.0 code; Felucca itself stays GPL-3.0-only.

Every distribution of a package carries the licence texts with it: the release folder
(`tools/build.py --release`) and the site (`web/make_site.py`, next to the package in
`firmware/` and linked from the installer page).

## No vendor material

No M-VAVE material is part of Felucca. The firmware links no vendor code and contains no vendor
data, and the packages hold only Felucca and the three SDK files above. The installer's
"Return to official V15" holds only the official file's size and SHA-256: you select the
official firmware file you downloaded yourself, and it is checked and installed in your browser,
never uploaded or redistributed.

## Contributions

Contributions are welcome under GPL-3.0-only. A contribution to one of cursedsound's own files (above) is taken under
its header's terms, `GPL-3.0-only OR MIT`.

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments.

"M-VAVE" and "FM-1" are trademarks of their respective owners. Felucca is independent
firmware that runs on FM-1 hardware. It is not affiliated with, endorsed by or supported
by those owners.

"Elektron" and "Syntakt" are trademarks of Elektron Music Machines. cursed os works with a Syntakt over MIDI; it is
not affiliated with, endorsed by or supported by Elektron, M-VAVE, Hügelton Instruments or JIANT FM's author.

## Radio

Felucca never enables the Bluetooth / Wi-Fi radio of the hardware. JIANT FM (V10.12) does, only when MENU > SYSTEM >
BLUETOOTH is ON (the default is OFF): a Bluetooth LE MIDI peripheral on Optimist's own stack, no JieLi library. Its
code is a segment of its own at flash 0xEA000 (`firmware/bt/`), linked with the app; the package carries it as a third
entry, `bt.bin`. The stack's files are offered by their author under GPL-3.0-only OR MPL-2.0; JIANT, and every package
built from it, is GPL-3.0-only as a whole (the Apache-2.0 radio files above are one-way compatible with it, as
`fm6_core.c`).
