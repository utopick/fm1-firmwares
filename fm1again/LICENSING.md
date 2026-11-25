# Licensing

FM-1 Again by PolarPatch is GPL-3.0 as a whole (GPL-3.0-only, since parts of it are: the modules from Arctic Scream). Its parts:

| Part | Licence and source |
|---|---|
| `base/` (fm1-base, with felucca-bsp in `base/bsp/`) | MPL-2.0, Copyright (C) 2026 Charles Vestal, Leo Kuroshita (Hügelton Instruments) and the others named in `base/CREDITS.md` and `base/LICENSING.md`. Their files stay MPL-2.0 file by file |
| `app/app.c`, `app/app.h`, `app/tests/basic.txt`, `app/tests/screens.txt`, `app/words.tsv`, `app/fm1.toml`, `app/site/` | Started from fm1-base's template (MPL-2.0, Copyright (C) 2026 Charles Vestal), changed by PolarPatch (app.c: its sound, pages and screen rewritten) |
| `app/wave.h`, `app/engine/` (clock, drums, groove, keys, vox, chop, pump, rise, revecho, perform: its idea Arctic Scream's FX performance layer, none of its code), `app/dsp/fdsp.h`, `app/tools/gen_again_font.py`, `app/tools/again_chop.py`, `app/tools/make_reverse.py`, `app/tests/rise.txt`, `app/tests/loaf.txt`, `app/tests/groove.txt`, `app/tests/perform.txt`, `app/tests/listen.txt`, `app/tests/factory_chop.txt`, `app/docs/MANUAL.md` | GPL-3.0-or-later, Copyright (C) 2026 PolarPatch: written for FM-1 Again. The SVF in `fdsp.h` follows Andrew Simper's published trapezoidal SVF equations; the vowels' formants in `engine/vox.h` are the usual published values for a soprano's vowels; the IMA ADPCM coder in `engine/chop.h` and `again_chop.py` is the standard one (the IMA's published tables) |
| `app/gen/again_chop.h` (CHOP's factory sample) | GPL-3.0-or-later, Copyright (C) 2026 PolarPatch: a phrase sung by this firmware's own VOX in its own SPACE, recorded in the host simulator (`app/tests/factory_chop.txt`) and coded by `again_chop.py`: no recording of anyone |
| `app/dsp/space.h` (SPACE) | GPL-3.0-only. Arctic Scream's `firmware/src/hall.c`: Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments: Felucca's HALL reverb ([Felucca](https://github.com/hugelton/Felucca) `firmware/src/fx.c`: `rev_hall`, `hall_ap`, `hall_end_lp`, `sh_tz`, `HL_RUNS`; the Paley 8 x 8 feedback matrix, the half-rate design). GR!MM changes Copyright (C) 2026 GR!MM ([GR!MM](https://github.com/GRiMMBIENT/grimm): longer lines and 4 diffusers, DAMP on all 8 lines, decay 0.4 .. ~32 s and INF, a soft knee in the feedback, PRE-DELAY, MIX, the gliding taps, the idle skip). Arctic Scream's SHIMMER (its idea from ECHOFIELD's shimmer, Philip Bos, MIT: none of its code) and FM-1 Again's changes (the float send and return; Arctic Scream's season and breath taken out) Copyright (C) 2026 PolarPatch |
| `app/dsp/echo.h` (ECHO) | GPL-3.0-only. Arctic Scream's `firmware/src/tape.c` and `wear.c`, Copyright (C) 2026 GR!MM: a tape echo in integers whose design follows X0X's TAPE delay ([X0X](https://github.com/charlesvestal/fm1-x0x) `firmware/src/dsp/fxbus.c` `fx_delay`, charlesvestal, GPL-3.0, itself a port of 9W9's `er99_dly_tick`, GPL-3.0; none of X0X's code is copied), with Felucca's integer helpers. Arctic Scream's PING-PONG (the idea from ECHOFIELD, Philip Bos, MIT: none of its code) and FM-1 Again's changes (TIME in milliseconds from the tempo, the float send and return) Copyright (C) 2026 PolarPatch |
| `app/dsp/tape.h` (TAPE) | GPL-3.0-only. Arctic Scream's `firmware/src/tapefx.c`, Copyright (C) 2026 GR!MM (the short line the wow moves, the saturation as one curve, the low-pass, the hiss, the bypass cross-over; its wow and saturation are ECHO's, after X0X's TAPE as above). FM-1 Again's changes (the float mix in and out) Copyright (C) 2026 PolarPatch |
| `app/dsp/qdsp.h`, `app/tools/gen_tables.py` (→ `app/gen/again_tables.h`) | GPL-3.0-only. Felucca's `dsp.c` helpers (`mulq15`, `softclip`, `soft_knee`) and the parts of its `tools/gen_tables.py` these modules need, Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments, as Arctic Scream carries them; SPACE's tables GR!MM's (Copyright (C) 2026 GR!MM) |
| Bluetooth | fm1-base's own stack (`ble_stack = "own"`: Henri David's from Optimist, in `base/bt/`, MPL-2.0): nothing of JieLi's binary libraries is linked, so the GPL parts above may be part of the firmware |
| `app/assets/fonts/texgyreheros-bold.otf` and the faces made from it, `app/gen/again_font.h` | TeX Gyre Heros, Copyright 2007-2009 B. Jackowski, J. M. Nowacki (GUST e-foundry), under the GUST Font License (`app/assets/fonts/GUST-FONT-LICENSE.txt`) |
| `app/gen/again_pixfont.h` (the boot screen's letters) and `app/boot.h` | The pixfont: Press Start 2P by the Press Start 2P Project Authors, rasterised at its 8 px grid by Arctic Scream p0larpatch's `tools/gen_pixfont.py` (a Modified Version under the OFL, so called "pixfont", not by its Reserved Font Name), under the SIL Open Font License 1.1 (`LICENSES/OFL-PressStart2P.txt`). The boot screen follows Arctic Scream p0larpatch's (PolarPatch) |

## The look

- The screen's type and its stamped letters follow the posters of the USB002 tour, from the creative files its
  team shared with the community (Dropbox, 27 April 2026: "anyone in the community can now download, edit, and use
  the content however they want",
  <https://blog.dropbox.com/topics/news/fred-again-drops-exclusive-creative-files-from-his-usb002-tour>). The
  posters set Helvetica Bold; this firmware uses the free TeX Gyre Heros Bold in its place. The stamped letters are
  made anew from Heros's glyphs by `app/tools/gen_again_font.py`: no file of the drop is included in the type.
- The screensaver's film, `app/media/again_saver.bin` (the resource region), is made from short clips of the same
  creative drop's concert footage (the audience), cut, dithered to black and white and coded by
  `app/tools/again_saver.py`. It is not under the GPL: it is the drop's material, used as its terms allow, kept apart
  from the code (like the PolarPatch logo), and never used as branding. The tools that make it are GPL-3.0-or-later.
- The waveform follows the look of an audio editor's track view (peaks and RMS, left over right).
- The layout's ideas (the K1-K4 row, the pads on the black keys and their strip, the page tabs, the beat ticks, "Drop
  in N", SONG, the builds' styles and tempo rise, the step conditions, the tutor's tips) come from loaf-breaker by
  FLEXOR (<https://github.com/FLEXOR-R/loaf-breaker>, MPL-2.0): ideas only, in black and white, none of its code.
- FM-1 Again is not made, endorsed or approved by any artist.
