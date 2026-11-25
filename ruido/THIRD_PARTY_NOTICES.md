# Licensing & Third-Party Notices

**Ruido** (`v0.7.3`, FM-1 package identity `FM-1_312`)
Copyright (C) 2026 Miguel Hernández Domenech (<https://github.com/miguelhd/ruido>)

All synthesis DSP, scanline CRT UI, 3-model pressure keybed logic, and WebAssembly/macOS simulator code in `src/` and `platforms/sim/` are original first-party Ruido code. Firmware images built for the M-VAVE FM-1 (`build/fm1/ruido.fwsc`) link against the open-source FM-1 platform layer (`GPL-3.0-only`) and are distributed under the **GNU General Public License, version 3 only (`GPL-3.0-only`)**. See [`LICENSE`](LICENSE) for the full license text.

If you distribute a compiled `.fwsc` or `.bin` firmware image built from this project, you must provide or offer the complete corresponding source code under `GPL-3.0-only` as required by Section 6 of the license.

---

## 1. FM-1 Hardware Platform, Bootguard & USB Updater (`GPL-3.0-only`)

The FM-1 hardware abstraction layer, `Hold OCT-` USB rescue mode, `FELUCCA-LOADER-1` RAM OTA updater, USB Audio/MIDI + 3.5 mm TRS MIDI IN stack, `.fwsc` packaging tools, and NVS sector wrapper are fetched at container build time via [`zvenson/dinghy`](https://github.com/zvenson/dinghy) (`GPL-3.0-only`, no third-party files vendored in this repository) and comprise work by:

- **Felucca** (<https://github.com/hugelton/Felucca>) — Copyright (C) 2026 Leo Kuroshita (`@kurogedelic`), Hügelton Instruments (`firmware/hal/`, `firmware/loader/` `FELUCCA-LOADER-1`, `crt0.S`, `app.ld`, `usb.c`, `ota.c`, `recovery.c` `Hold OCT-` rescue, `midi_uart.c` 3.5 mm TRS MIDI IN, `lcd.c`, `libc.c`, `bootguard.h`, `uac_fir.h`, and `tools/` `fm1pkg_make.py` & `fm1_install.py`).
- **Dinghy / OberVave** (<https://github.com/zvenson/dinghy>) — Copyright (C) 2026 `zvenson` (`platform.c` integration runtime, `LCD_IDLE` DMA hook, and `store.h` NVS sector/blob wrapper; Dinghy's `ldr_screen.c`, Skiff `5x7` loader font, and `gfx.c` / Terminus font are stripped at build time and not linked into Ruido).
- **SLOOP (`sloop-fm1`)** (<https://github.com/isod89/sloop-fm1>) — `48 kHz` USB audio polyphase resampling (`FELUCCA_UAC_48K` in `usb.c`) and platform refinements by `isod89`, plus the content-polled `midi_uart.c` ring fix from **Felucca [Salt]** by `ChanceTheMaker` (identified by `keremimo`).
- **genkigenki / `sloop-fm1` (`smk37` branch)** (<https://github.com/genkigenki/sloop-fm1>) — Copyright (C) 2026 M. Geisler (`@genkigenki` / `makkuro`) (`fm1_flash_map.h` flash map header and shared `#if BOARD_SMK37` header/tool support; Ruido builds exclusively with `BOARD_SMK37 = 0`).

*(Dual-core `Core 1` SRAM bring-up `fm1_cpu1`, carbon-pill `SARADC` pressure sensing `fm1_panel_io`, `ΔΣ` LED modulation `fm1_led_modulator`, append-only NVS tail journals, and monochrome operational/loader screens `fm1_ops_screen` / `fm1_ldr_screen.h` in `platforms/fm1/` are original first-party Ruido code.)*

---

## 2. JieLi `AC79NN` SoC Bootloader & Audio EQ Blobs (`Apache-2.0`)

At `.fwsc` container packaging time (`platforms/fm1/build_fm1.py`), three unmodified SDK binary blobs (`uboot.boot`, `cfg_tool.bin`, and `cfg/eq_cfg_hw.bin`, verified by SHA-256) are read from the JieLi `fw-AC79_AIoT_SDK` (`AC79NN_SDK_V1.2.1_2023-12-13`, <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK>):

- Copyright (C) JieLi Tech, licensed under the **Apache License, Version 2.0 (`Apache-2.0`)** (<http://www.apache.org/licenses/LICENSE-2.0>). No JieLi SDK files are stored in this Git repository.

---

## 3. Build-Time Verification Emulator (`MIT`, Not Linked Into Firmware)

- **fm1-emu** (<https://github.com/joakimeriksson/fm1-emu>) — Copyright (C) Joakim Eriksson, licensed under the **MIT License**. Used exclusively during offline build/CI verification (`make fm1-check`); no `fm1-emu` code is linked into `ruido.bin` or `ruido.fwsc`.

---

## 4. Trademarks

"M-VAVE" and "FM-1" are trademarks of their respective owners. "Felucca" and "Hügelton Instruments" are trademarks of Hügelton Instruments. All other product, instrument, and integrated-circuit names mentioned in documentation or source comments (including "Korg", "MS-20", "Korg35", "Yamaha", "CS-80", "Roland", "TB-303", "Buchla", and "Soma" / "Lyra-8") are trademarks of their respective owners and are referenced strictly for nominative technical description of analog circuit topologies. Ruido is an independent open-source firmware project and is not affiliated with, sponsored by, or endorsed by M-VAVE or any third-party trademark holder.
