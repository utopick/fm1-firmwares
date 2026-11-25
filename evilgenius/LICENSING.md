# Licensing

**FIZZ is MPL-2.0** (the full text is in `LICENSE`). Every source file carries an `SPDX-License-Identifier: MPL-2.0`
header and MPL's Exhibit A notice.
- If you change one of these files and distribute it, publish your change to that file under MPL-2.0.
- Files of your own that you build with FIZZ (a platform, an app, a closed library such as JieLi's Bluetooth stack)
  may use any licence.

Until L1 (2026-10-23) FIZZ was GPL-3.0-only. The owner, its author, relicensed his code. The code that came from
Felucca (Leo Kuroshita) through ChoralRoot was not relicensed: it was **rewritten**, clean-room, with every output
unchanged. `research/PROVENANCE.md` lists where each part came from.

## What is under which licence

| Code | Author | Licence |
|---|---|---|
| Everything in `core/` and `tools/` not named below | FIZZ, written for the owner (Michael P Jones, Quixotic7) | MPL-2.0 |
| FM TONE and the effects (`core/voice/quad/eng_quad.c`, `quad_tables.h`, `quad_times.h`; `core/voice/fx/cr_fx.c`, `cr_ram.h`, `fz_out.c`), from ChoralRoot FM-1 v0.25.1 | the owner (ChoralRoot's author) | MPL-2.0 |
| The building blocks, tables and voice parts that replace Felucca's (`core/voice/quad/fz_*.h`, `tools/gen_fz_tables.py`) | FIZZ (L1, clean-room from `research/L1-CLEANROOM-SPEC.md`) | MPL-2.0 |
| ChoralRoot's second-core code (`firmware/src/cr_cpu1.h`, ChoralRoot FM-1), for the port's reuse (P2.6), with a provenance line where it is used | the owner (ChoralRoot's author): relicensed MPL-2.0 for FIZZ on 2026-10-23 | MPL-2.0 |
| `core/tests/ref/cr_quad_ref.c`, `cr_fx_ref.c`: test oracles that compile ChoralRoot's own tree (Felucca code included), fetched into `tools/build/` at test time | the owner; they build GPL code | GPL-3.0-only (`LICENSES/GPL-3.0.txt`): development only, never part of the firmware |
| `site/`: EvilGenius's own site (the landing page, `css/`, `js/`, `img/`, `manager/`, `tools/`) | EvilGenius, written for the owner | MPL-2.0 |
| `site/try/`: the browser emulator (the firmware compiled to WebAssembly; its page is fm1-base's `web/` page, restyled by `tools/eg/make_try.py`) | EvilGenius, FIZZ, fm1-base (Charles Vestal) | MPL-2.0 (the firmware's licences) |
| `ios/`: FIZZ for iOS, and the FM1VST glue its emulated FIZZ compiles in (`core-api/fm1core.h`, `core-glue/common/nor.*`, `panel.h`, `sysex.h`, `version.h`, `fifo.*`, relicensed in FM1VST on 2026-10-28) | the owner | MPL-2.0 |
| `ios/FizzKit/Sources/CRemoteFM1/` (libremotefm1's portable core: `src/{codec,session,panel,screen,tiles_ref,fake}.c`, `src/remote_proto.h`, `include/rfm/*.h`, `include/rfm1.h`) and `ios/FizzKit/Sources/CRemoteFM1Checks/vendored/` (its host tests), copied unchanged from RemoteFM1 commit f44af95 (tag `relicense-mpl-2026-10-30`); `CRemoteFM1/PROVENANCE.md` lists them | RemoteFM1 contributors (the owner): relicensed MPL-2.0 in RemoteFM1 on 2026-10-30; earlier RemoteFM1 commits of these files stay GPL-3.0-only | MPL-2.0 |
| `ios/FizzKit/Sources/CMidiMap/RFMMidiMap.{h,cpp}`, `ios/FizzKit/Sources/FizzUI/MIDI/{MidiMap,MidiLearn,OmxWire,OmxViews,OmxScreen,OmxTransport,OmxLink}.swift` and `ios/FizzKit/Tests/FizzUITests/{MidiMapTests,MidiEngineTests,OmxTests}.swift` (PLAY's learned MIDI map, MIDI learn and the OMX-27), from RemoteFM1 for iOS commit af91bc5: OmxWire, OmxViews, OmxScreen and OmxTests unchanged, the rest adapted to FIZZ (each file's header says how); `FizzUI/MIDI/PROVENANCE.md` lists them | RemoteFM1 contributors (the owner): relicensed MPL-2.0 in RemoteFM1IOS af91bc5 on 2026-10-30; earlier RemoteFM1IOS commits of these files stay GPL-3.0-only | MPL-2.0 |
| `site/install/` (`index.html`, `install.js`, `notes.js`, `fm1lib.js`) and `site/tools/test_install.mjs`: the install page | fm1-base's web installer (Charles Vestal; Leo Kuroshita, Hügelton Instruments), FIZZ's and EvilGenius's changes by the owner | MPL-2.0, each file's header kept |
| `site/firmware/`: the released packages | FIZZ, fm1-base, felucca-bsp | MPL-2.0 (the firmware's licences) |
| `firmware/release.py`, `firmware/tools/sync_installer.py`, `CHANGELOG.md`, `.github/workflows/release.yml` | the owner | MPL-2.0 |

**The install page.** `site/install/fm1lib.js` is generated from the submodule (`firmware/tools/sync_installer.py`) and is fm1-base's code unchanged; `notes.js` is FIZZ's. FIZZ's own site (GPL-3.0-only) is not part of EvilGenius: nothing of it is in `site/`.

## Third parties in the firmware

| What | Licence | Where |
|---|---|---|
| plutovg v1.3.3 (Samuel Ugochukwu), the 2D drawing | MIT | `third_party/plutovg/` (`LICENSE`) |
| FreeType's rasterizer, stroker, math and types inside plutovg (`plutovg-ft-*`) | FreeType License (FTL) | `third_party/plutovg/source/FTL.TXT`. The binary credit: "Portions of this software are copyright © 2006 The FreeType Project (www.freetype.org). All rights reserved." FIZZ's changes to these files are listed in `third_party/README.md` |
| stb_truetype, stb_image, stb_image_write (Sean Barrett), inside plutovg | MIT OR Unlicense | `third_party/plutovg/source/plutovg-stb-*.h` |
| Inter Tight (The Inter Project Authors), the type | SIL OFL 1.1 (no Reserved Font Name) | `assets/fonts/` (`OFL.txt`); embedded in `core/gfx/fonts_gen.h` |
| DM Sans (The DM Sans Project Authors) and Unbounded (The Unbounded Project Authors), FIZZ for iOS's PLAY sheet and chip | SIL OFL 1.1 | `ios/FizzKit/Sources/FizzUI/Resources/` (`OFL-DMSans.txt`, `OFL-Unbounded.txt`), bundled in the iOS app |
| EvilGenius: SAM, the Software Automatic Mouth (`core/voice/sam/`: `sam.c`, `render.c`, `reciter.c`, their headers and tables), Sebastian Macke's C port (github.com/s-macke/SAM) of Don't Ask Software's 1982 program, changed as `core/voice/sam/README.md` lists | **none**: the port has no licence; the original's rights are SoftVoice, Inc.'s. Here by the owner's decision, outside EvilGenius's MPL-2.0 (`say.c`, `say.h`, `sam_names.h` there are EvilGenius's, MPL-2.0) | `core/voice/sam/README.md` |
| EvilGenius: the SID model (`core/voice/sid/sid.c`, `sid.h`, `sidsynth.c`, `sidsynth.h`), from FM-1 SID (Joakim Eriksson, github.com/joakimeriksson/fm1-sid, its own clean-room model in `src/`); EvilGenius's changes are marked in the files | BSD-2-Clause, Copyright (c) 2026 Joakim Eriksson | `LICENSES/BSD-2-Clause.txt` |

## Credits (designs and facts, no code)

- **SAM, the Software Automatic Mouth** (Don't Ask Software, 1982; now SoftVoice, Inc.), as Sebastian Macke's C port
  (github.com/s-macke/SAM): EvilGenius's VOX words (`core/voice/sid/eg_vox_data.h`) are rendered with it by
  `tools/eg/gen_vox.py`, and the firmware speaks with it live (SAY). Its code is in `core/voice/sam/` (see the table
  above).

- **SLOOP 2.6** (isod89, github.com/isod89/sloop-fm1): the designs of the Clean chain's one-block look-ahead
  limiter and of the stereo chorus's two taps, both written anew in ChoralRoot.
- **OMX-27** (okyeron/OMX-27, its Form sequencer and MIDI FX; contributors including j__r0d): the MIDI FX groups'
  mechanics, re-implemented from a behaviour description.
- **namesizer** (the owner's, MIT) and its phonic-nonsense adaptation (Euan Goddard, MIT): the name ideas and the
  phonics grapheme lists in `core/seq/names.c`.
- **The TAP ape** (`core/ui/ape_poses.h`): traced from the owner's own artwork.
- **Elektron's Digitone**: FM TONE's design and measured envelope times.
- **Felucca** (Leo Kuroshita, Hügelton Instruments): the firmware ChoralRoot began from. No Felucca code remains in
  FIZZ (L1).
- **Melodee** (Kerem Kilic): two saturation limits in the voice mix, through ChoralRoot.
