# The World in One Day — Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/DataNinjaqe/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/DataNinjaqe/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for make.fun's [**news-image-20261122** bounty](https://make.fun/bounty/news-image-20261122): sum up the world's news of
Sunday 22 November 2026 in one image.

## The image

A newspaper front page, 1024 × 1024, laid out in `image.html` and stored as `entry.png`:

- **Justice, The Hague** — The International Court of Justice rules 9–6 that Myanmar committed genocide against the Rohingya in its 2017 crackdown, citing evidence of some 10,000 killed; the first time a state has been held responsible for genocide, with reparations and a safe return ordered.
- **Conflict, the Gulf** — The Iran war has cost the US more than $48bn, the Pentagon says; a cargo ship catches fire after a drone strike in the Baltic.
- **Climate, COP31** — Talks are close to a final deal, but the fossil-fuel dispute could still scupper it.
- **France** — Protesters rally for a sixth weekend over living costs and public services.
- **Africa** — The G20 summit opens in Johannesburg, the first on African soil.
- **Markets** — Bitcoin crashes to a two-year low; Nvidia faces a US accounting probe.
- Also: Serbia's president resigns, the Pentagon moves to restrict defence ties with Canada, Trump vows to cap credit-card interest at 10%, Houthi revenge strikes on the Saudi capital, 39 missing after a factory fire in Indonesia, 24 dead as a boat capsizes in Nigeria.

Every fact was checked against reporting published on 22 November 2026 before
the image was drawn (ICJ verdict cross-checked in Le Monde, CNA, Al Jazeera and
the Daily Star; COP31 and the Baltic drone strike in Dawn, Arab News and the
Manila Times; G20 opening in Xinhua).

## How it is built

`image.html` is the source of the front page. It is rendered once, by hand,
into `entry.png` (1024 × 1024, 148,645 bytes, sha256
`2a9ad3d8b9edbf6da23cc51fc4c0db0011a790c87d9e7a4624505fbbeeb550b5`):

```sh
python3 render.py   # draws entry.png from the same layout and text (PIL)
```

`main.ts` (Node 22, standard library only) copies `entry.png` to the
grader's output directory, so both graded runs write identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
sha256sum out/entry.png entry.png   # identical
```
