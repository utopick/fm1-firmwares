# Notices

FMY262 is free software under the GNU General Public License, version 2 or (at your option) any later version
(`LICENSE`). It is not made, endorsed or supported by M-VAVE; "M-VAVE" and "FM-1" are named only to say which
device it runs on.

## Code from others

| What | Where it is used | Licence |
|---|---|---|
| DBOPL OPL3 emulator, (C) 2002–2010 The DOSBox Team; C version from Chocolate Doom 2.0.0, with changes marked at the top of the file | `firmware/opl3bench/emu/dbopl/` (firmware), `web/opl3fn.js` (the same code as WebAssembly → JavaScript, for the web pages) | GPL-2.0-or-later |
| fm1-base, (C) 2026 Charles Vestal and others — <https://github.com/charlesvestal/fm1-base> | linked into the firmware; its install page, USB companion client and emulator page are in the workbench | MPL-2.0 (its `LICENSE`, `LICENSES/`) |
| felucca-bsp, (C) 2026 Leo Kuroshita, Hugelton Instruments — <https://github.com/hugelton/felucca-bsp> | linked into the firmware (through fm1-base) | MPL-2.0 |
| m-bootloader, (C) 2026 Julius Vitkauskas | installed by the workbench's install page when the FM-1 needs it | MIT (`firmware/m-bootloader-LICENSE.txt` in the site) |
| Barlow font, (C) 2017 The Barlow Project Authors; Terminus font, Dimitar Toshkov Zhekov | the device screen and the workbench (through fm1-base) | SIL OFL-1.1 |
| Nuked OPL3, (C) 2013–2020 Nuke.YKT | `opl3/` and `web/nukedfn.js`: the earlier sound core of the web prototype, kept for comparison; not in the releases | LGPL-2.1-or-later (`opl3/LICENSE`) |

The sources of fm1-base and felucca-bsp are not in this repository: `tools/fetch-vendor.sh` fetches them at the
commits each release was built with.

## File formats followed (no code of them is here)

- **Adlib Tracker II** by subz3ro / Altair — <https://adlibtracker.net>. FMY262 follows its effects and reads and
  writes its A2M song format.
- **Reality AdLib Tracker** by Shayde / Reality. FMY262's workbench imports its RAD 1.0 and 2.1 song files. The
  import is checked against AdPlug's RAD replayer (LGPL-2.1), which the test `tests/t48.cjs` builds from a copy fetched
  separately; it is not part of FMY262.
