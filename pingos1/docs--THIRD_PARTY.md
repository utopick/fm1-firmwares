# Third-party code in PING FM-1

This file lists code PING FM-1 takes from other projects, with its origin, its licence and the notices those
licences ask for. Everything not listed here is PING FM-1's own.

## The Felucca sound engines (engine/ch_fe*)

The SYNTH device's WHEEL, PHASE, TRIO, LOFI and FM6 models are ports of the sound engines of **Felucca**, the
FM-1 firmware by **Leo Kuroshita (@kurogedelic), Hügelton Instruments**. They were adapted for PING FM-1 in 2026
(per-voice state for a 4-track x 4-voice host, three macro knobs per engine, 44.1 kHz constants, prefixed names,
no mutable static state, float at the API edge, the changes listed at the head of each file).

| File | Origin | Licence |
| --- | --- | --- |
| `engine/ch_fe.h` (the part under `CH_FE_INTERNAL`) | Felucca-Engines `src/dsp.c`, `src/felucca_engine.h` | MIT |
| `engine/ch_fe_tables.c` | Felucca-Engines `tools/gen_engine_tables.py` (its formulas; regenerated) | MIT |
| `engine/ch_fe_wheel.c` | Felucca-Engines `src/eng_wheel.c` | MIT |
| `engine/ch_fe_phase.c` | Felucca-Engines `src/eng_phase.c` | MIT |
| `engine/ch_fe_trio.c` | Felucca-Engines `src/eng_trio.c` | MIT |
| `engine/ch_fe_lofi.c` | Felucca-Engines `src/eng_lofi.c` | MIT |
| `engine/ch_fe_fm6core.c` | Felucca `firmware/src/fm6_core.c`: Leo Kuroshita's C port of msfa (Dexed) | Apache-2.0 |
| `engine/ch_fe_fm6tab.c` | the msfa start-up tables (formulas as in Felucca `tools/gen_tables.py`; regenerated) | Apache-2.0 |
| `engine/ch_fe_fm6.c` | Felucca `firmware/src/eng_fm6.c` (the FM6 engine around the core) | MPL-2.0, by grant |
| `engine/ch_fe_fm6pat.c` | Felucca `tools/gen_fm6_patches.py` (the eight factory patches, as data) | MPL-2.0, by grant |
| `engine/ch_fe.c`, `bench/fe_test.c`, `bench/fe_build.ps1` | PING FM-1's own | (PING FM-1's licence) |

Sources and commits:

- Felucca-Engines: <https://github.com/hugelton/Felucca-Engines>, commit `d0260074ce100a47675814b7f38d61f11176c926`.
  Every file taken was written by Leo Kuroshita alone (the one outside contribution to that repository, to
  `eng_analog.c`, is in an engine not used here).
- Felucca: <https://github.com/hugelton/Felucca>. The FM6 files are taken at commit
  `63f88ec18b71c6ed4371d03d6f04dd93f4193ad3`, the parent of `f9a98fc` (whose fixes to `fm6_core.c` are another
  author's, under the GPL, and are **not** used; PING FM-1 avoids the same signed-overflow and signed-shift issues
  its own way: unsigned phases and multiplies instead of left shifts). At that commit `fm6_core.c`, `eng_fm6.c` and
  `gen_fm6_patches.py` have Leo Kuroshita as their only author. Felucca's history up to `a4f007c9` was surveyed.
- Not taken from Felucca: SLOOP, `fx.c`, `adpcm_dsp.c`, and the ANALOG, NOISE, DRUM, VOICE, GRAIN, SAMPLE and SLICE
  engines; nothing of Felucca's GPL-3.0 code other than the FM6 files granted below.
- The tables were regenerated for PING FM-1 by a stand-alone script from the published formulas (the same values);
  no script of either project was run.

### FM6: the MPL-2.0 grant

Felucca as a whole is GPL-3.0-only. Leo Kuroshita, the author of the FM6 engine and its factory patches, has
granted the use of the code he authored under the Mozilla Public License 2.0:
<https://github.com/hugelton/felucca-bsp/issues/4>. `engine/ch_fe_fm6.c` and `engine/ch_fe_fm6pat.c` are used under
that grant and carry the MPL-2.0 notice. The MPL-2.0 text: <https://mozilla.org/MPL/2.0/>. Under the MPL, these two
files (with any changes made to them) stay available in source form under the MPL-2.0 when the firmware is
distributed. Credit: the FM6 engine and its patches are the work of Leo Kuroshita, Hügelton Instruments.

`engine/ch_fe_fm6core.c` is Leo Kuroshita's port of msfa and keeps msfa's Apache-2.0 licence (below).

### msfa (Apache-2.0)

msfa, the synthesis core of Dexed: <https://github.com/asb2m10/dexed> (`Source/msfa`). Only msfa is used; Dexed as a
whole is GPL-3.0.

    Copyright 2012 Google Inc.
    Copyright 2016-2025 Pascal Gauthier.
    C port for Felucca (integer only, no float), 2026: Leo Kuroshita (@kurogedelic), Hügelton Instruments
    Adapted for PING FM-1, 2026.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Modified files carry a notice of the changes at their head (Apache-2.0 section 4(b)): `ch_fe_fm6core.c` lists what
Felucca changed from msfa and what PING FM-1 changed from Felucca. The full licence text is at the end of this file.

### Felucca-Engines (MIT)

```
MIT License

Copyright (c) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Mutable Instruments DSP (engine/ch_mi*)

The SYNTH device's FOLD, FORMANT, CHORD, STRING and MODAL models, and ANALOG's triangle, are C ports of Mutable
Instruments code by **Emilie Gillet**, from
Plaits and stmlib (<https://github.com/pichenettes/eurorack>, commit `f4cfa7697095a28d292bff758beb51deb49b5a86`;
<https://github.com/pichenettes/stmlib>), all under the MIT licence below. Ported to C for PING-1 in 2026: a
sample at a time instead of in blocks, 44.1 kHz instead of 48 kHz, the string's delay line in 16 bits and its
all-pass line shortened, 16 modal resonances instead of 24, the chord engine without its wavetable half, the
changes listed at the head of `engine/ch_mi.c`.

| File | Origin | Licence |
| --- | --- | --- |
| `engine/ch_mi.c`, `engine/ch_mi.h` | Plaits `dsp/oscillator/oscillator.h`, `grainlet_oscillator.h`, `string_synth_oscillator.h`, `dsp/engine/waveshaping_engine.cc`, `grain_engine.cc`, `chord_engine.cc`, `dsp/chords/chord_bank.cc`, `dsp/physical_modelling/string.cc`, `string_voice.cc`, `modal_voice.cc`, `resonator.cc`, `dsp/noise/dust.h`; stmlib `dsp/polyblep.h`, `dsp/filter.h`, `dsp/delay_line.h`, `dsp/dsp.h` | MIT |
| `engine/ch_mi_tables.c` | Plaits `resources/lookup_tables.py` (its formulas; regenerated by `tools/gen_mi_tables.py`) | MIT |

```
Copyright 2016-2021 Emilie Gillet.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## Apache License 2.0 (full text)

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
```
