import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "json", "accounts.json")


def load_json():
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return {}


def save_json(json_data):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)
