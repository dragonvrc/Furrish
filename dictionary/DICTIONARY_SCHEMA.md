# Furrish Dictionary Schema (v0.1, EN-only)

**Canonical formats:** CSV and JSON (mirrored).

Fields:
- `lemma` (string): Furrish headword (lowercase ASCII).
- `pos` (string): part of speech (`pron`, `part`, `verb`, `noun`, `adj`, `adv`, `intj`, `num`).
- `gloss_en` (string): short English gloss.
- `tags` (string): label for grouping (e.g., `grammar`, `core-verb`, `people`, `daily`, `vr`, `safety`, `num`).

Style rules:
- Lemmas follow Furrish phonotactics (CV or CVN/R; clusters: mw, ny, rw, kw, gw).
- Prefer single-sense entries; avoid synonym bloat.
- Borrowings ok if adapted to Furrish orthography.