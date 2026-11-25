# Licensing

RhinoTiger as a whole is distributed under **GPL-3.0-only** (LICENSE). Its parts keep their own notices:

| Part | From | Licence |
| --- | --- | --- |
| `app/app.c`, `app/app.h`, `app/auto.h`, `app/hands.h`, `app/face.h`, `app/logo.h`, `app/dsp/` (`psy.c`, `psy.h`, `events.c`, `fx.c`, `hands.c`, `line.c`), `app/words.tsv`, `app/tests/`, `tools/`, `serve.sh`, `site.sh`, `install.sh`, `test.sh` | RhinoTiger, by hacha | GPL-3.0-only |
| `app/docs/` (the manuals and their screenshots), `docs/` (the AUTO PLAY specification), `app/site/` (the front pages, the site's colours `theme.css` and `theme.py`, `pages.py`), `app/fm1.toml`, `fmhub.json`, `README.md` | RhinoTiger, by hacha | GPL-3.0-only |
| `build.sh` | [AMB-1](https://github.com/charlesvestal/fm1-amb)'s by Charles Vestal, its name changed | MPL-2.0 |
| `.github/workflows/release.yml` | [fm1-base](https://github.com/charlesvestal/fm1-base)'s template by Charles Vestal (after X0X's and Melodee's), filled in | MPL-2.0 |
| `base/` (submodule) | [a fork of fm1-base](https://github.com/hacha/fm1-base) (branch `rhinotiger`): fm1-base by Charles Vestal plus one change ("MASTER read before the audio starts"), on felucca-bsp from [Felucca](https://github.com/hugelton/Felucca) by Leo Kuroshita | MPL-2.0 |

`app/app.c` started from fm1-base's template app (MPL-2.0) and was rewritten; a few of its idioms remain (the settings'
defaults, `app_say()`, the keys' edges). Its pages, the rule over the knobs and the knob strip follow PaperLagoon's
(also by hacha), which follow HYP-1's look. fm1-base says of its template: changes to its files are published under
MPL-2.0, your own files may use any licence.

MPL-2.0 is file-level: the MPL files stay MPL-2.0 (changes to them too) and may be combined with GPL code
(MPL-2.0 section 3.3).

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Noto Sans JP Black (Google): the glyphs of 犀 and 虎 drawn into the boot logo's pixels (`app/logo.h`, made by `tools/kanji.py`); the font itself is not in this tree | SIL OFL 1.1 | <https://fonts.google.com/noto/specimen/Noto+Sans+JP> |
| Fonts: Barlow Semi Condensed (The Barlow Project Authors), drawn on the screen and built into the firmware. Terminus (Dimitar Toshkov Zhekov) is in the same folder but is not used by this build's default font set | SIL OFL 1.1 | `base/assets/fonts/`, with their licences (`Barlow-OFL.txt`, `Terminus-LICENSE.txt`) |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners, used here only to say what hardware RhinoTiger runs
on. "Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. RhinoTiger is independent firmware; it
is not affiliated with, endorsed by or supported by any of them.

## Radio

RhinoTiger never enables the Bluetooth / Wi-Fi radio of the hardware (`ble = false` in `app/fm1.toml`).
