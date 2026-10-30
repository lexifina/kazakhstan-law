# Kazakhstan: law history in git

The law of Kazakhstan as a git history: one file per provision, one commit per law on the day its change took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `kz/`.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `konstitutsiya/` | Constitution of the Republic of Kazakhstan, adopted at the referendum of 15 March 2026 | 1 | In force from 1 July 2026 (article 94). Files: `preambula`, `razdel-NN` (the 11 sections' headings) and `st-NNN` (articles 1 to 96) |
| `ugolovnyi-kodeks/` | Criminal Code (Law of 3 July 2014 No. 226-V), consolidated text | 1 | Oldest version available: Adilet text as captured 9 September 2026; files `div-NNN` (part and section headings) and `st-NNN` (articles) |
| `grazhdanskii-kodeks-obshchaya/` | Civil Code, General Part (resolution of the Supreme Council of 27 December 1994), consolidated text | 1 | Oldest version available: Adilet text as captured 8 September 2026 |
| `grazhdanskii-kodeks-osobennaya/` | Civil Code, Special Part (Code of 1 July 1999 No. 409-I), consolidated text | 1 | Oldest version available: Adilet text as captured 23 July 2026 |
| `predprinimatelskii-kodeks/` | Entrepreneurial (Commercial) Code (Code of 29 October 2015 No. 375-V), consolidated text | 1 | Oldest version available: Adilet text as captured 6 September 2026 |

**Language.** The text is in Russian, one of the two official languages (with Kazakh). Adilet publishes an English version only as an unofficial translation, so it is not used.

**Limits of this first build**

- It holds only the current Constitution. The Constitution of 30 August 1995, which this one replaced on 1 July 2026, and its amendments are not in the record, so there is no earlier history yet.
- The version is dated by the entry-into-force day in article 94. The referendum date (15 March 2026) is the enactment date. The publication date was not read.
- Only the statutes listed above are included (core codes are being added one at a time). The consolidated codes have one version each, dated by the Adilet capture, not by their original entry into force.

**Source.** The statutes' consolidated texts are the Adilet pages, read from Internet Archive captures (dates in each version's note). The Constitution: the Adilet legal information system of the Ministry of Justice of Kazakhstan, [adilet.zan.kz/rus/docs/K2600000000](https://adilet.zan.kz/rus/docs/K2600000000), read from an Internet Archive capture of 27 August 2026. The sha256 of the bytes it was parsed from is in `data/versions.json`.

All sources, with their status, are in [SOURCES.md](SOURCES.md) where present. How these files were made is in [REPRODUCE.md](REPRODUCE.md). This repository is not legal advice and not an official publication; for anything that matters, read the original.
