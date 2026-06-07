import json
import csv
import sys
import os

def validate_json(file_path):
    print(f"Validating JSON: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("Error: JSON root must be a list.")
                return False
            for i, entry in enumerate(data):
                required_keys = ['lemma', 'pos', 'gloss_en']
                for key in required_keys:
                    if key not in entry:
                        print(f"Error: Entry {i} is missing required key '{key}'.")
                        return False
        print("JSON validation successful.")
        return True
    except Exception as e:
        print(f"Error validating JSON: {e}")
        return False

def validate_csv(file_path):
    print(f"Validating CSV: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            required_keys = ['lemma', 'pos', 'gloss_en']
            for i, row in enumerate(reader):
                for key in required_keys:
                    if key not in row or not row[key]:
                        print(f"Error: Row {i+1} is missing required value for '{key}'.")
                        return False
        print("CSV validation successful.")
        return True
    except Exception as e:
        print(f"Error validating CSV: {e}")
        return False

if __name__ == "__main__":
    success = True
    dict_dir = "dictionary"
    
    json_file = os.path.join(dict_dir, "core_100.json")
    if os.path.exists(json_file):
        if not validate_json(json_file):
            success = False
            
    csv_file = os.path.join(dict_dir, "core_100.csv")
    if os.path.exists(csv_file):
        if not validate_csv(csv_file):
            success = False
            
    if not success:
        sys.exit(1)
    print("All dictionary validations passed.")
