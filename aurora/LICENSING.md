# Licensing

AURORA is free software under the GNU General Public License v3.0 ([LICENSE](LICENSE)).

It is built on [GR!MM](https://github.com/GRiMMBIENT/grimm) (GPL-3.0): its platform, DSP and reverb, used as they are, with
two small patches applied at build time for newer FM-1s (`tools/build_fwsc.sh`). GR!MM stands on Felucca (Leo Kuroshita,
Hügelton Instruments), Dinghy (zvenson), SLOOP (isod89) and X0X (charlesvestal), all GPL-3.0; their copyright lines and
licence texts are in GR!MM's [LICENSING.md](https://github.com/GRiMMBIENT/grimm/blob/main/LICENSING.md). The newer FM-1s'
screen setup is M-VAVE's register values as Jake Handy found them for [h1](https://github.com/jakehandy/h1), as
Dinghy 0.6.1 carries them.

## The choir

The keys' CHOIR mode plays single cycles from GR!MM's `grimm_choir.h`, made from:

> **VocalSet: A Singing Voice Dataset**, by Julia Wilkins, Prem Seetharaman, Alison Wahl and Bryan Pardo, Northwestern
> University, 2018. <https://doi.org/10.5281/zenodo.1442513>. Licensed under
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Changed: single cycles were measured from the singers' straight long tones (GR!MM's `tools/gen_choir.py`). AURORA plays
them as they are in GR!MM.

## Fonts

The screen font is Terminus by Dimitar Zhekov (SIL Open Font License 1.1).
