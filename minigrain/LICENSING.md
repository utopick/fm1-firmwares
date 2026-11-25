# Licensing

Mini-Grain is free software, licensed under the GNU General Public License, version 3 only
(`GPL-3.0-only`, full text in `LICENSE`).

It is built on two pieces of work, and keeps their credits:

- **Felucca / Mini-Tone**, the firmware platform of the M-Vave FM-1: the hardware layer (`firmware/hal/`), the
  boot code, USB (MIDI, audio, the update entry), TRS MIDI, flash storage, the update loader, the build tools
  (`tools/build.py`, `fm1pkg_make.py`, `fm1_install.py`, ...) and the text and drawing code. Copyright (C) 2026
  Leo Kuroshita (@kurogedelic), Hügelton Instruments, GPL-3.0-only. Files that come from it carry that header.
- **Granular Synth for ESP32-S3**: the granular engine, the parameters, the effects, the sample generators and the
  design of the screens, which `firmware/src/gr_*.c` rewrite in fixed point for the FM-1.

`assets/fonts/` holds Inter Tight (SIL Open Font License 1.1, `assets/fonts/OFL.txt`), from which the screen's text
is rasterised at build time.

Building the update package uses three files of the JieLi AC79 SDK (Apache-2.0) that are not part of this tree; see
`BUILDING.md`. The package contains them, so distribute its licence text with it.
