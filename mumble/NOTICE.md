# MUMBLE: licence notice

MUMBLE's sources are licensed under the GNU General Public License version 3 only (its text is in
[LICENSE](LICENSE)), with the additional permission under its section 7 that follows (SPDX:
`GPL-3.0-only WITH GPL-3.0-linking-exception`, as the files' headers say). Files carrying a different license keep it; fm1-base (`base/`)
has its own (MPL-2.0).

## Origin

`app/paint.inc` (the panel's colours, 5x7 font, damage-marking painter and band buffers) and parts of `app/app.c` (the
encoders' acceleration) are adapted from FM1 Open's panel code (`app/screen.c`):

> Copyright (c) 2026 珠海笙科智能科技有限公司 (M-VAVE). Licensed under the GNU GPL version 3 only, with the additional
> permission below.

They were modified for MUMBLE on fm1-base in November 2026. The rest of MUMBLE was written for it.

## Additional permission under GNU GPL version 3 section 7

If you modify this Program, or any covered work, by linking or combining it with the FM1 binary SDK (sdk/lib/libfm1_engine.a and the accompanying binary SDK components listed in sdk/manifest.json) (or a modified version of that library), containing parts covered by the terms of the FM1 Binary SDK terms in THIRD_PARTY.md and the applicable original component licenses, the licensors of this Program grant you additional permission to convey the resulting work.

This permission applies to code marked with this exception. The APP and its modifications remain subject to GPLv3; the SDK keeps its separate terms. This exception does not require disclosure of proprietary SDK source and does not grant rights in third-party code beyond its applicable license. Include this license and THIRD_PARTY.md with distributions, and provide the corresponding APP source and build/install scripts as required by GPLv3.

The permission is kept as M-VAVE granted it. MUMBLE does not use the FM1 binary SDK, which (with its THIRD_PARTY.md)
belongs to FM1 Open and is not part of this repository.
