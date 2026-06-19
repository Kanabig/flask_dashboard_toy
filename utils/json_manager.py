import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "json", "members.json")


def load_members():
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return {}


def save_members(members):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            return json.dump(members, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)
