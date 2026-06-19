import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ACCOUNT_FILE = os.path.join(BASE_DIR, "json", "accounts.json")
BANK_FILE = os.path.join(BASE_DIR, "json", "banks.json")
DIARYS_FILE = os.path.join(BASE_DIR, "json", "diarys.json")
MEMOS_FILE = os.path.join(BASE_DIR, "json", "memos.json")
TODOLIST_FILE = os.path.join(BASE_DIR, "json", "todolist.json")


def load_json(file):
    try:
        with open(file, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return {}


def save_json(file, json_data):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)


# # 사용법
# if __name__ == "__main__":
#     accounts = load_json(ACCOUNT_FILE)
#     save_json(ACCOUNT_FILE, accounts)
