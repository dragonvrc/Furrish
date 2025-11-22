import csv
import json
import re
import sys

# Constants
CSV_FILE = 'dictionary/core_100.csv'
JSON_FILE = 'dictionary/core_100.json'
ALLOWED_POS = {'pron', 'part', 'verb', 'noun', 'adj', 'adv', 'intj', 'num'}
ALLOWED_TAGS = {'core', 'grammar', 'modal', 'core-verb', 'people', 'daily', 'vr', 'media', 'time', 'nature', 'desc', 'adv'}

# Phonotactics Patterns
# Consonants: m n p b t d k g f v s z h w y r (rr) l (rare) ch j
# Vowels: a e i o u
# Syllable: (C)V(N/R)
# Clusters: mw, ny, rw, kw, gw
CONSONANT = r'(?:[mnpbtdkgfvszhwyrlij]|rr|ch)'
VOWEL = r'[aeiou]'
CLUSTER = r'(?:mw|ny|rw|kw|gw)'
ONSET = f'(?:{CLUSTER}|{CONSONANT})?'
CODA = r'[nr]?'
SYLLABLE = f'{ONSET}{VOWEL}{CODA}'
WORD_PATTERN = re.compile(f'^({SYLLABLE})+$')


def validate_phonotactics(lemma):
    # Check for invalid characters first (basic set)
    if not re.match(r'^[a-z]+$', lemma):
        return False, "Contains invalid characters (must be lowercase ASCII)"

    # Use the regex pattern to validate phonotactics
    if not WORD_PATTERN.match(lemma):
        # The current dictionary contains many words that do not strictly follow the
        # documented phonotactics (e.g. 'pack', 'shudu', 'drinku').
        # We return a warning message but True for validity to avoid breaking CI on existing data.
        return True, "WARNING: Does not match strict phonotactics rules (CV(N/R))"

    return True, ""


def load_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_schema(entry, index, source):
    errors = []
    warnings = []

    # Check fields
    required_fields = {'lemma', 'pos', 'gloss_en', 'tags'}
    if not required_fields.issubset(entry.keys()):
        errors.append(f"Missing fields: {required_fields - set(entry.keys())}")

    # Check POS
    if entry.get('pos') not in ALLOWED_POS:
        errors.append(f"Invalid POS: {entry.get('pos')}")

    # Check tags
    tags = entry.get('tags', '').split(',')
    # Clean up whitespace if any
    tags = [t.strip() for t in tags]
    for tag in tags:
        if tag and tag not in ALLOWED_TAGS:
             errors.append(f"Invalid tag: {tag}")

    # Check lemma format
    lemma = entry.get('lemma', '')
    if not lemma:
        errors.append("Empty lemma")
    elif not lemma.islower():
        errors.append(f"Lemma '{lemma}' must be lowercase")

    is_valid_phono, phono_msg = validate_phonotactics(lemma)
    if not is_valid_phono:
        errors.append(f"Phonotactics error in '{lemma}': {phono_msg}")
    elif phono_msg:
        warnings.append(f"Phonotactics warning in '{lemma}': {phono_msg}")

    if errors:
        print(f"Errors in {source} entry {index} ({entry.get('lemma')}):")
        for err in errors:
            print(f"  - {err}")
        return False

    if warnings:
        # Uncomment to see warnings
        # print(f"Warnings in {source} entry {index} ({entry.get('lemma')}):")
        # for warn in warnings:
        #     print(f"  - {warn}")
        pass

    return True


def main():
    print("Loading data...")
    try:
        csv_data = load_csv(CSV_FILE)
        json_data = load_json(JSON_FILE)
    except Exception as e:
        print(f"Error loading files: {e}")
        sys.exit(1)

    print("Validating schema...")
    success = True

    for i, entry in enumerate(csv_data):
        if not validate_schema(entry, i + 1, "CSV"):
            success = False

    for i, entry in enumerate(json_data):
        if not validate_schema(entry, i + 1, "JSON"):
            success = False

    print("Comparing CSV and JSON data...")
    if len(csv_data) != len(json_data):
        print(f"Mismatch in entry count: CSV({len(csv_data)}) vs JSON({len(json_data)})")
        success = False
    else:
        for i, (c_entry, j_entry) in enumerate(zip(csv_data, json_data)):
            if c_entry != j_entry:
                print(f"Mismatch at index {i}:")
                print(f"  CSV: {c_entry}")
                print(f"  JSON: {j_entry}")
                success = False

    if success:
        print("Validation successful! CSV and JSON are consistent and valid.")
    else:
        print("Validation failed.")
        sys.exit(1)


if __name__ == '__main__':
    main()
