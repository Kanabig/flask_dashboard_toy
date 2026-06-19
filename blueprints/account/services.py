from utils.timestamper import get_current_time_stamp_formated
from utils.json_manager import load_json, save_json, ACCOUNT_FILE


def create_account(id, pw, mail, phone):

    account = load_json(ACCOUNT_FILE)

    account[id] = {
        "mId": id,
        "mPw": pw,
        "mMail": mail,
        "mPhone": phone,
        "reg_date": get_current_time_stamp_formated(),
        "mod_date": get_current_time_stamp_formated(),
    }

    save_json(ACCOUNT_FILE, save_json)
