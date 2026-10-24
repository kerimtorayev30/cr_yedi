# Advanced Plus vocabulary import — source and audit notes

## Result

- `content/data/advancedplus.json` contains **643 unique headwords** across all 16 lessons.
- All **192 legacy entries were retained**. The import adds **451 new unique headwords** from **452 source rows**; `childish` is one card with a second 7B source reference.
- `content/pdf/advp-candidates.json` contains **644 source/decision rows**: 192 retained legacy entries, 451 new headwords, and one additional source occurrence linked to an already-added headword.
- All Advanced Plus references in `books[]` now include the lesson, `page` and `section`.

## Source files and processing

Student's Book source PDFs:

- `uploads/advanced plus-1-45.pdf`
- `uploads/advanced plus-46-88.pdf`
- `uploads/advanced plus-89-132_compressed.pdf`
- `uploads/advanced plus-133-159.pdf`

Teacher's Guide source: `uploads/Advanced plus Teacher's guide book.pdf`.

The OCR working texts are `content/pdf/advp-sb.txt` (159 Student's Book physical pages) and `content/pdf/advp-tg.txt` (202 Teacher's Guide physical pages). Scanned Student's Book pages were processed one at a time; no intermediate page raster images were retained. Teacher's Guide text extraction succeeded without a password; no credentials were used or required.

**Page convention:** Student's Book `books.page` is the printed page number. The OCR physical-page marker is one lower (`printed page = SB OCR physical page + 1`). Teacher's Guide page numbers in the audit are PDF physical pages and are supporting evidence only.

## Reviewed vocabulary locations

| Lesson | Student's Book printed pages | Teacher's Guide PDF page(s) | Source / section |
|---|---:|---:|---|
| 1A | 140 | 188 | Vague language — Vocabulary Bank |
| 1B | 141–142 | 189 | Phrasal nouns — Vocabulary Bank; `input`/`output` are explicitly marked as TG worksheet extensions |
| 2A | 143 | 190 | Prefixes and suffixes — Vocabulary Bank; `microcosm`, `paranormal`, `extracurricular`, `circumspect`, and `forewarned` are TG-only extensions, not claimed as exact SB hits |
| 2B | 144–145 | 191 | Ways of moving — Vocabulary Bank |
| 3A | 26 | — | Research language — in-lesson Vocabulary box |
| 3B | 146–147 | 192 | Shakespeare idioms — Vocabulary Bank |
| 4A | 148 | 193 | Binomials — Vocabulary Bank |
| 4B | 149 | 194 | Acronyms and initialisms — Vocabulary Bank |
| 5A | 150–151 | 195 | Sophisticated emotions — Vocabulary Bank |
| 5B | 51 | — | Individuals and populations — in-lesson Vocabulary box |
| 6A | 58; 152–153 | 196 | Making-things verbs box on p.58; adverb collocations in the Vocabulary Bank |
| 6B | 154–155 | 197 | Mathematical terms, diagrams, measurements, and measurement idioms — Vocabulary Bank |
| 7A | 156–157 | 198 | Punishment — Vocabulary Bank |
| 7B | 70 | — | Connotation — in-lesson Vocabulary box |
| 8A | 158–159 | 199 | Eating/drinking on p.158; idioms on p.159 cross-referenced from lesson 8A |
| 8B | 80 | — | Ways of seeing — in-lesson Vocabulary box |

## How to read the audit

`advp-candidates.json` is the machine-readable audit. It records the headword, lesson, section, printed SB page, corresponding SB OCR physical page, supporting TG PDF page (where relevant), evidence type, page role, decision, and confidence.

For the inherited 192 entries, a normalized literal OCR search was limited to that lesson's source pages. **64** have an exact normalized OCR headword hit and **128** are retained with a lesson-section page assignment only. The latter are not described as exact word/page matches. OCR normalization treats hyphens and punctuation as separators; OCR misses are handled conservatively, not used as grounds for deleting a legacy entry.

For additions, Student's Book Vocabulary Bank/box entries are mapped to their reviewed printed page. Items supported only by the Teacher's Guide are explicitly labelled `teacher_guide_extension` and point to the related Student's Book section page without claiming an exact Student's Book occurrence. Section labels are `vocabulary_bank` for bank items and `vocabulary` for in-lesson boxes.

## Checks and review status

- Regenerated `advancedplus.json`, merged all book packs, validated the merged data, and built the compact app pack. The content check passed all **52 loader assertions**. A staged HTML copy was embedded, then passed `verify.sh`: **143 baseline assertions**, **110 integration assertions**, and sandbox checks all passed. That verified copy is now `uploads/app-yatla.html`; its pre-existing `.preembed.bak` was left untouched.
- The validator reported one non-blocking warning in the pre-existing `cabin crew` entry (`tm` character set). No validation errors were reported.
- The new Turkmen and Russian glosses and examples are **not native-speaker proofread**; `proofread` remains `false`.
