# Структура / Structure

| Папка / Folder | Что в ней / What it holds |
| --- | --- |
| `конституция/<год>/` | Конституции: `конституция/1995/` (принята 30.08.1995, со всеми редакциями 1998, 2007, 2011, 2017, 2019, 2022), `конституция/2026/` (референдум 15.03.2026) / the Constitutions, each with its editions |
| `законы-о-поправках-к-конституции/<год>/<номер>-<название>/` | Законы о внесении изменений и дополнений в Конституцию / laws amending the Constitution |
| `кодексы/<год>/<название>/` | Кодексы по году принятия: `кодексы/2014/уголовный-кодекс/` / codes, by year of adoption |
| `конституционные-законы/<год>/<номер>-<название>/` | Конституционные законы / constitutional laws |
| `законы/<год>/<номер>-<название>/` | Законы: `законы/2021/62-VII-о-внесении-изменений-...` / laws, by year and number |
| `указы-имеющие-силу-закона/<год>/<номер>-<название>/` | Указы Президента, имеющие силу закона (1995-1996) / decrees with the force of law |
| `указы-имеющие-силу-конституционного-закона/<год>/...` | Указы, имеющие силу конституционного закона |
| `постановления-конституционного-суда/<год>/<номер>-<название>/` | Нормативные постановления Конституционного Суда (Совета) / Constitutional Court resolutions |
| `нормативные-постановления-верховного-суда/<год>/<номер>-<название>/` | Нормативные постановления Верховного Суда / Supreme Court normative resolutions |

Каждая папка акта: один файл на статью (`статья-001.md` = статья 1; `статья-065-1.md` = статья 65-1),
`преамбула.md` (текст до первой статьи), `README.md` (название, опубликование, источник). Акт без статей: `текст.md`.
В кодексе более чем с 990 статьями статьи лежат по главам (`глава-012/статья-150.md`). Ни в одной папке нет более
1 000 записей. Файл статьи: заголовок статьи, по абзацу на строку, затем строки `Раздел:`, `Глава:`, `Параграф:`.

Each act folder holds one file per article, a preamble file and a README; codes of more than 990 articles are split
into chapter folders. No folder holds more than 1,000 entries.

## Даты / Dates

Each Adilet edition of an act is one commit, dated 12:00 Asia/Almaty on the edition's day (`In-force:`), which is the
day Adilet gives the edition (its revision date). The first edition of an act is dated by the text's own commencement
article where it can be read (`вводится в действие с ...`, `со дня первого официального опубликования`, `по
истечении десяти календарных дней ...` counted from the publication day Adilet records); where that day falls after
a later edition, or cannot be read, the adoption day is used and `In-force-basis:` says so (`Takes-effect:` then
gives the stated day). `Amended-by:` names the amending acts whose notes first appear in that edition. Editions
dated after the build day are held. Commits before 1970 (which git cannot store) are dated 1 January 1970 with the
real day in the subject and in `In-force:`. No date here is the day anything was downloaded.

The first build's flat folders (`konstitutsiya/`, `ugolovnyi-kodeks/`, ...), each one version dated by an Internet
Archive capture day, are removed by `Kind: correction` commits as each act's dated Adilet history is added.
