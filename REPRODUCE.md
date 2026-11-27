# How this repository was made (Kazakhstan)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Adilet editions (2026-11-27)

The first build above (7 acts, one capture-dated version each) is superseded: its folders are removed by
`Kind: correction` commits as each act's dated history is added. The record is now built by
`scripts/kazakhstan-law/runner` (kz_fetch.py, kz_build.py) from the JSON API the Adilet site itself reads:

- listing: `POST https://adilet.zan.kz/api/search` with `{"filters": {"document_type": <type>, "language": "rus",
  "years": [<year>]}}`, by type (and by year for laws and Supreme Court resolutions);
- per act: `GET /api/documents/by-ngr/<registration number>`, `GET /api/documents/<id>/versions`, and
  `GET /api/documents/<edition id>` for each edition's HTML text.

No login. robots.txt allows `by-ngr`, `versions` and `documents/<id>` for general agents and disallows `/api/search`
(advisory; the listing is read once, slowly). Pace: one request in flight about a second apart, stepping up to at
most three after ten clean minutes and back to one at the first timeout or 5xx; 403/429 stop the run. Adilet's Terms
of Use bar bots that load it heavily and require it to be named as the source.

Each edition is dated as STRUCTURE.md says; editorial notes (span.note, red ИЗПИ notes) are left out of the text.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Adilet (adilet.zan.kz), Ministry of Justice of the Republic of Kazakhstan | <https://adilet.zan.kz/rus/docs/K2600000000> | 2026-08-27 | Laws are not objects of copyright (Law on Copyright and Related Rights, art. 7). |
| Adilet captures of core statutes (Internet Archive) | <https://adilet.zan.kz> | 2026-10-30 | Laws are not objects of copyright (Law on Copyright and Related Rights, art. 7). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `konstitutsiya` | Конституция Республики Казахстан (2026) | 1 | 2026-07-01 to 2026-07-01 |
| `ugolovnyi-kodeks` | Уголовный кодекс Республики Казахстан | 1 | 2026-09-09 to 2026-09-09 |
| `grazhdanskii-kodeks-obshchaya` | Гражданский кодекс Республики Казахстан (Общая часть) | 1 | 2026-09-08 to 2026-09-08 |
| `grazhdanskii-kodeks-osobennaya` | Гражданский кодекс Республики Казахстан (Особенная часть) | 1 | 2026-07-23 to 2026-07-23 |
| `predprinimatelskii-kodeks` | Предпринимательский кодекс Республики Казахстан | 1 | 2026-09-06 to 2026-09-06 |
| `ugolovno-protsessualnyi-kodeks` | Уголовно-процессуальный кодекс Республики Казахстан | 1 | 2026-09-05 to 2026-09-05 |
| `trudovoi-kodeks` | Трудовой кодекс Республики Казахстан | 1 | 2026-09-06 to 2026-09-06 |

The build made 7 commits:

| Commits | Kind |
| ---: | --- |
| 7 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 13 laws in the record.
- 8 tags.

## Dates

Each commit is dated at noon (Asia/Almaty) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Article 94 of the Constitution: it enters into force on 1 July 2026, ending the Constitution of 30 August 1995. https://adilet.zan.kz/rus/docs/K2600000000

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `577ccc8134396741546f9025f0da57b65fe9ee9e4a5df29235deb3ad71d1ce3d` (8573188 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `3024ff164c261807dfc4d5b7b1b4a2cde4357da1`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

7 versions of 7 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 7 history commits and 8 tags (history tip `d828a30e4d57d4d157436964b56e5f7d87d5f196`).

## Decisions made by hand

- Only the current Constitution is built. The Constitution of 30 August 1995, which it replaced on 1 July 2026, is not in this record.
- Version date 2026-07-01 is the entry-into-force date in article 94; the referendum date 2026-03-15 is the enactment date. The publication date was not read.
- The text is the Russian text, an official language; Adilet lists the English version as an unofficial translation.
- The Adilet note "Примечание ИЗПИ" (about the order of entry into force) is editorial and left out.
- Уголовный кодекс Республики Казахстан: one version, dated 2026-09-09 (the date of the Adilet capture), credited to the publisher as "oldest version available"; Adilet keeps earlier editions but they were not read. The adopting law is named as an earlier law only.
- Гражданский кодекс Республики Казахстан (Общая часть): one version, dated 2026-09-08 (the date of the Adilet capture), credited to the publisher as "oldest version available"; Adilet keeps earlier editions but they were not read. The adopting law is named as an earlier law only.
- Гражданский кодекс Республики Казахстан (Особенная часть): one version, dated 2026-07-23 (the date of the Adilet capture), credited to the publisher as "oldest version available"; Adilet keeps earlier editions but they were not read. The adopting law is named as an earlier law only.
- Предпринимательский кодекс Республики Казахстан: one version, dated 2026-09-06 (the date of the Adilet capture), credited to the publisher as "oldest version available"; Adilet keeps earlier editions but they were not read. The adopting law is named as an earlier law only.
- Уголовно-процессуальный кодекс Республики Казахстан: one version, dated 2026-09-05 (the date of the Adilet capture), credited to the publisher as "oldest version available". Adilet keeps earlier editions, but no archived copies of them were found, so they were not read. The adopting law is named as an earlier law only.
- Трудовой кодекс Республики Казахстан: one version, dated 2026-09-06 (the date of the Adilet capture), credited to the publisher as "oldest version available". Adilet keeps earlier editions, but no archived copies of them were found, so they were not read. The adopting law is named as an earlier law only.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the deterministic parser; no model wrote or altered any legal text.
- Claude Code wrote the parser; it did not write or alter any legal text.
- Claude Code wrote the parser; it did not write or alter any legal text.
