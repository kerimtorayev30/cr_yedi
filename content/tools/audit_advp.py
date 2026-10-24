#!/usr/bin/env python3
"""Build a reviewable source/decision audit for the Advanced Plus import."""
from collections import Counter
import json
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import gen_advp as gen  # noqa: E402
from advp_additions import ADDITIONS  # noqa: E402

PACK_PATH = ROOT / 'data' / 'advancedplus.json'
OUT_PATH = ROOT / 'pdf' / 'advp-candidates.json'


def key(text):
    return ' '.join(text.strip().casefold().split())


def main():
    pack = json.loads(PACK_PATH.read_text(encoding='utf-8'))
    words = {key(w['en']): w for w in pack['words']}
    sb_pages = gen.load_sb_page_text()
    records = []
    legacy_keys = set()
    legacy_exact = 0
    legacy_section_only = 0

    for lesson in sorted(gen.LESSONS, key=gen.lesson_sort_key):
        unit, title, topic, topics = gen.LESSONS[lesson]
        for topic_key in topics:
            for item in gen.T[topic_key]:
                en = item[0]
                k = key(en)
                legacy_keys.add(k)
                hits = gen.legacy_ocr_hits(en, lesson, sb_pages)
                word = words[k]
                ref = next(b for b in word['books']
                           if b.get('book') == 'advp' and b.get('lesson') == lesson)
                exact = bool(hits)
                if exact:
                    legacy_exact += 1
                else:
                    legacy_section_only += 1
                records.append({
                    'en': en,
                    'lesson': lesson,
                    'section': ref['section'],
                    'page': ref['page'],
                    'sb_pdf_page': ref['page'] - 1,
                    'ocr_hit_pages': hits,
                    'tg_pdf_page': None,
                    'evidence': ('legacy_entry_retained_with_normalized_OCR_hit'
                                 if exact else 'legacy_entry_retained_no_exact_OCR_hit'),
                    'page_role': ('exact_student_book_OCR_hit' if exact
                                  else 'lesson_section_assignment'),
                    'tg_evidence': '',
                    'decision': 'retained_existing',
                    'confidence': 'high',
                })

    seen_additions = set()
    for item in ADDITIONS:
        en = item['en']
        k = key(en)
        if k in legacy_keys:
            decision = 'source_occurrence_linked_to_retained_headword'
        elif k in seen_additions:
            decision = 'source_occurrence_linked_to_added_headword'
        else:
            decision = 'added'
        seen_additions.add(k)
        records.append({
            'en': en,
            'lesson': item['lesson'],
            'section': item['section'],
            'page': item['page'],
            'sb_pdf_page': item['page'] - 1,
            'ocr_hit_pages': ([item['page'] - 1]
                               if item['page_role'] == 'exact_student_book_page' else []),
            'tg_pdf_page': item['tg_pdf_page'],
            'evidence': item['evidence'],
            'page_role': item['page_role'],
            'tg_evidence': item['tg_evidence'],
            'source_note': item.get('source_note', ''),
            'decision': decision,
            'confidence': 'high',
        })

    records.sort(key=lambda r: (gen.lesson_sort_key(r['lesson']), r['page'], r['en'].casefold(), r['decision']))
    OUT_PATH.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    decisions = Counter(r['decision'] for r in records)
    sections = Counter((r['lesson'], r['section']) for r in records)
    print(f'wrote {OUT_PATH}: {len(records)} source decisions')
    print(f'legacy entries: 192 retained; {legacy_exact} exact normalized OCR hits, '
          f'{legacy_section_only} mapped by lesson section')
    print('decisions:', dict(decisions))
    print('section rows:', ', '.join(f'{lesson} {section}={n}'
          for (lesson, section), n in sorted(sections.items(), key=lambda x: (gen.lesson_sort_key(x[0][0]), x[0][1]))))


if __name__ == '__main__':
    main()
