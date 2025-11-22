import csv
import json
import sys
import argparse

CSV_FILE = 'dictionary/core_100.csv'
JSON_FILE = 'dictionary/core_100.json'

def csv_to_json(csv_path, json_path):
    print(f"Converting {csv_path} to {json_path}...")
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n') # Add newline at end of file
        print("Conversion successful.")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        sys.exit(1)

def json_to_csv(json_path, csv_path):
    print(f"Converting {json_path} to {csv_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            print("JSON file is empty.")
            return

        fieldnames = data[0].keys()

        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Conversion successful.")
    except Exception as e:
        print(f"Error converting JSON to CSV: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert between CSV and JSON dictionary formats.")
    parser.add_argument('--to-json', action='store_true', help='Convert CSV to JSON')
    parser.add_argument('--to-csv', action='store_true', help='Convert JSON to CSV')

    args = parser.parse_args()

    if args.to_json:
        csv_to_json(CSV_FILE, JSON_FILE)
    elif args.to_csv:
        json_to_csv(JSON_FILE, CSV_FILE)
    else:
        print("Please specify --to-json or --to-csv.")
        sys.exit(1)

if __name__ == '__main__':
    main()
