# Pianola Licensing

Pianola is free software under the **Mozilla Public License 2.0** (`MPL-2.0`, full text in [LICENSE](LICENSE)), file by file. If you modify any MPL-licensed file and distribute the result, make that file's source available under MPL-2.0.

It is built on [fm1-base](https://github.com/charlesvestal/fm1-base) and [felucca-bsp](https://github.com/hugelton/felucca-bsp) (`base/`, a git submodule), both under `MPL-2.0`.

## Synthesis & Piano Rolls (Zero Audio Samples)

- **Audio synthesis (`sounds: "none – all synthesised"`):** Pianola contains **no audio samples, PCM recordings, wavetables, or SoundFonts**. Every string partial, dispersion wavelet, hammer felt thud, damper noise, bridge resonance, and hall reflection is computed mathematically at boot or in real time by `app/dsp_piano.c`.
- **Built-in piano rolls (`app/piano_data.h`):** All 87 built-in rolls are strictly **public domain** compositions and public-domain transcriptions:
  - Claude Debussy (*Clair de lune*, *Première Arabesque*), Erik Satie (*Gymnopédies* Nos. 1 & 2), Frédéric Chopin, Ludwig van Beethoven, J. S. Bach, W. A. Mozart, Franz Schubert, Robert Schumann, Johannes Brahms, Edvard Grieg, Muzio Clementi, Friedrich Burgmüller, Carl Czerny, and Scott Joplin — sourced from transcriptions explicitly dedicated to the **Public Domain** in the [Mutopia Project](https://www.mutopiaproject.org), plus Beethoven Op. 109 from the 1915 Durand public-domain edition and *Afterlight* (an original composition written in code for this project).

## Code & Third-Party Components

| Component | Origin | Licence |
|---|---|---|
| `app/` (`app.c`, `app.h`, `dsp_piano.c`, `dsp_piano.h`, `pianist.c`, `pianist.h`, `piano_data.h`, `tools/gen_piano_data.py`), `tests/` | Simon Tokumine | MPL-2.0 |
| `base/` platform (boot, USB audio/MIDI, TRS MIDI, flash storage for `0x856014` & `0xB36014`, update loader, silicone key velocity/pressure sensing, own-stack BLE MIDI, host simulator, WebAssembly browser emulator) | [fm1-base](https://github.com/charlesvestal/fm1-base) by Charles Vestal and [felucca-bsp](https://github.com/hugelton/felucca-bsp) from [Felucca](https://github.com/hugelton/Felucca) by Leo Kuroshita (@kurogedelic), Hügelton Instruments | MPL-2.0 (`base/ble/` SDK shims: Apache-2.0; own BLE host parts: Apache-2.0 & BSD-2-Clause, see `LICENSES/`) |
| Fonts: Barlow Semi Condensed, Terminus | The Barlow Project Authors; Dimitar Toshkov Zhekov | SIL OFL 1.1 (`base/assets/fonts/`) |
| JieLi AC79 SDK boot & radio libraries (`uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin`, `btctrler.a`, `wl_rf_common.a`, `crypto_toolbox_Osize.a`, `lib_ccm_aes.a`) | Fetched from JieLi's official AC79 SDK repository at build time (`zvenson/fm1-build@v1`); no SDK binaries are stored in this repository | Apache-2.0 (`LICENSES/Apache-2.0.txt`) |

## Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners, used only to identify compatible hardware. "Felucca" and "Hügelton Instruments" belong to Hügelton Instruments. Pianola is independent community firmware and is not affiliated with or endorsed by M-VAVE.
