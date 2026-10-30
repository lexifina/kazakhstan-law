"""Independent check of a Kazakhstan corpus.d part against its Adilet capture: the article text with every tag
stripped, compared word by word with the units' text in order (spacing before punctuation ignored). Every
difference must be an editorial note that the corpus leaves out (red-font or note spans, "Сноска."/"Примечание
ИЗПИ" paragraphs, "исключен" placeholders, Constitutional Court notes, table cell separators).
Usage: python -X utf8 verify_part.py <part.json> <capture.html>"""
import difflib, html, json, re, sys

PUNCT = re.compile(r'\s+([,.;:)])')
OPEN = re.compile(r'\(\s+')


def tidy(s: str) -> str:
    return OPEN.sub('(', PUNCT.sub(lambda m: m.group(1), s))


part = json.load(open(sys.argv[1], encoding='utf-8'))
t = open(sys.argv[2], encoding='utf-8').read()
a = t[t.find('<article>'):t.find('</article>')]
a = re.sub(r'<br\s*/?>|</p>|</h3>|</tr>|</t[dh]>', ' ', a)
txt = html.unescape(re.sub(r'<[^>]+>', ' ', a)).replace('\xa0', ' ').replace('​', '').replace('–', '-').replace('—', '-')
S = tidy(txt).split()
U = []
for u in part['acts'][0]['versions'][0]['units'].values():
    for line in u['text'].split('\n'):
        line = line[2:] if line.startswith('# ') else line
        U += tidy(line.replace(' | ', ' ')).split()
sm = difflib.SequenceMatcher(None, S, U, autojunk=False)
extra_src, extra_unit = [], []
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        continue
    if i2 > i1:
        extra_src.append(' '.join(S[i1:i2]))
    if j2 > j1:
        extra_unit.append((' '.join(S[i1:i2])[:200], ' '.join(U[j1:j2])[:200]))
print('source words', len(S), 'unit words', len(U), 'matched', sum(b.size for b in sm.get_matching_blocks()))
print('unit words not in source order:', len(extra_unit))
for s, u in extra_unit[:20]:
    print('  SRC:', s, '\n  UNIT:', u)
EDITORIAL = (r'^(Сноска|Примечание (ИЗПИ|РЦПИ)|ПРИМЕЧАНИЕ|Нормативным постановлением Конституционного Суда'
             r'|Статья [\d\-]+ (с изменени|в редакции|исключен)'
             r'|[\d\-]+[.)]\s+[Ии]сключен(а|о|ы)?\s+(Законом|в соответствии|Кодексом|Конституционным))')
notes = [x for x in extra_src if not re.match(EDITORIAL, x)]
print('source-only runs', len(extra_src), 'not starting as an editorial note:', len(notes))
for x in notes[:25]:
    print('  ', x[:300])
sys.exit(1 if extra_unit or notes else 0)
