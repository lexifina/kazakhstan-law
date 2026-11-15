# Kazakhstan: law history in git


The law of Kazakhstan as a git history: one file per article, one commit per version on the day it took effect, and the act that made each change as the commit's author (the publisher, for the oldest version available). `git blame` names the act behind every line; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Kazakhstan's national law, which global-law reads at `kazakhstan/national/acts/`.

**What is in it now:** the Constitution adopted at the referendum of 15 March 2026, in force from 1 July 2026; and six codes, each in the consolidated text Adilet published between July and September 2026: the Civil Code (its General Part and Special Part, two acts here), the Criminal Code, the Criminal Procedure Code, the Entrepreneurial Code and the Labour Code. Each of these 7 acts has one version so far; a code's version is dated by the day its text was captured (see Dates). [`REPRODUCE.md`](REPRODUCE.md) lists them with their dates; [`data/laws.csv`](data/laws.csv) lists the acts the commits name, with their Adilet pages.

Each act is one folder (`trudovoi-kodeks/` is the Трудовой кодекс Республики Казахстан, the Labour Code, Code of 23 November 2015 No. 414-V), with one file per article (`st-NNN.md`), one per heading of a part, section or chapter (`div-NNN.md`), and a `README.md` listing them. The Constitution is `konstitutsiya/`: `preambula.md`, `razdel-NN.md` (the headings of its 11 sections) and `st-001.md` to `st-096.md`.

The text is in Russian, as Adilet publishes it; state organisations and local self-government bodies use Russian officially alongside Kazakh, the state language (article 9 of the Constitution). Adilet's English version is an unofficial translation and is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 1 of the Labour Code | `git log -p --word-diff -- trudovoi-kodeks/st-001.md` |
| Which act wrote each line of Article 1? | `git blame trudovoi-kodeks/st-001.md` |
| Every version of the Labour Code, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- trudovoi-kodeks ":(exclude)trudovoi-kodeks/README.md"` |
| Article 1 as in force on 1 October 2026 | `python tools/on.py 2026-10-01 trudovoi-kodeks st-001` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about the law of Kazakhstan](https://global-law.lexifina.com/v1/try_claude?country=kazakhstan)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=kazakhstan)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=%D0%B5%D0%B6%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9+%D1%82%D1%80%D1%83%D0%B4%D0%BE%D0%B2%D0%BE%D0%B9+%D0%BE%D1%82%D0%BF%D1%83%D1%81%D0%BA&jurisdictions=kazakhstan)**: a search of Kazakhstan's law for "ежегодный трудовой отпуск" (annual leave), returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Russian or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add kazakhstan/national/acts
python3 tools/law.py show 2026-11-01 kazakhstan/national/acts/trudovoi-kodeks/st-001.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Almaty, on the day the version took effect, and carries it in its `In-force:` trailer:

- for the Constitution, 1 July 2026, the day its article 94 gives; the referendum day, 15 March 2026, is in its `Enacted:` trailer;
- for each code, the day of the Internet Archive capture of the Adilet page its text was read from (23 July to 9 September 2026), not the day the code first took effect (the Labour Code, for one, has applied since 1 January 2016).

The Constitution is credited to the Referendum of 15 March 2026. Each code's one text is the "oldest version available", credited to the publisher, the Adilet legal information system (Ministry of Justice of Kazakhstan); its commit message names the code that adopted it.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus it was built from: 7 versions of 7 acts, no mismatches.
- `tools/verify_part.py` compares an act's text word by word with its Adilet capture; the only differences allowed are Adilet's notes and other editorial matter, which the record leaves out. The sha256 of every capture is in [`data/versions.json`](data/versions.json).
- A second build from the same corpus gave the same hashes for every commit and tag; trailers parse, and there are no merge commits and no dates going backwards. Results are in [`REPRODUCE.md`](REPRODUCE.md).
- History is append-only: new acts and versions are added on top, and no published commit is rewritten.

## What it does not show

- **Earlier versions of the codes.** Adilet keeps them, but they were not read: each code has its 2026 text only, so `git blame` names the publisher, not the amending law.
- **The Constitution of 30 August 1995**, which the 2026 Constitution replaced on 1 July 2026, and its amendments.
- **Any other law**: other codes and laws, presidential decrees, government resolutions, local acts, case law and treaties are not here.
- **Adilet's notes**: the footnotes recording amendments («Сноска.») and the Institute's notes («Примечание ИЗПИ») are not in the files.
- **The Kazakh text.**

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Adilet](https://adilet.zan.kz) (Institute of Legislation and Legal Information, Ministry of Justice) | Official legal information system | yes, but only the current text was read | The Russian text of each act, read from Internet Archive captures of its page (27 August 2026 for the Constitution; each code's capture date is its version's date) |

## Licence

See [`LICENSE`](LICENSE). Laws are not objects of copyright in Kazakhstan (Law on Copyright and Related Rights, article 7); Lexifina's arrangement, tables, commit messages and tools may be reused under CC BY 4.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by Claude Code running Claude Opus 5.5 (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
