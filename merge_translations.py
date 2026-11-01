
import json

def merge(target, source):
    for key, value in target.items():
        if key not in source:
            continue

        english_value = source[key]

        if isinstance(value, dict) and isinstance(english_value, dict):
            merge(value, english_value)

        elif value == "" and isinstance(english_value, str):
            target[key] = english_value


with open("hu.json", "r", encoding="utf-8") as f:
    hu = json.load(f)

with open("en.json", "r", encoding="utf-8") as f:
    en = json.load(f)

merge(hu, en)

with open("hu_merged.json", "w", encoding="utf-8") as f:
    json.dump(hu, f, ensure_ascii=False, indent=4)
    f.write("\n")

print("Translations merged successfully!")
