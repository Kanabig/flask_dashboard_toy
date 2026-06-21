from utils.timestamper import get_current_time_stamp_formated
from blueprints.account import configs
from utils import json_manager


def load_accounts():
    return json_manager.load_json(json_manager.ACCOUNT_FILE)


def save_accounts(accounts):
    json_manager.save_json(json_manager.ACCOUNT_FILE, accounts)


def is_id_exists(accounts, id):
    return id in accounts


def is_account_exist(accounts, id, pw):
    return is_id_exists(accounts, id) and accounts[id].get(configs.KEY_PW) == pw


def create_account(accounts, id, pw, mail, phone):
    now = get_current_time_stamp_formated()
    accounts[id] = {
        configs.KEY_ID: id,
        configs.KEY_PW: pw,
        configs.KEY_MAIL: mail,
        configs.KEY_PHONE: phone,
        configs.KEY_REG_DATE: now,
        configs.KEY_MOD_DATE: now,
    }


def get_account_by_id(account_id):
    return load_accounts().get(account_id)


def update_account(accounts, id, pw, mail, phone):
    if not is_id_exists(accounts, id):
        return False

    accounts[id][configs.KEY_PW] = pw
    accounts[id][configs.KEY_MAIL] = mail
    accounts[id][configs.KEY_PHONE] = phone
    accounts[id][configs.KEY_MOD_DATE] = get_current_time_stamp_formated()
    return True


def delete_account(accounts, id):
    if is_id_exists(accounts, id):
        del accounts[id]
        return True

    return False


def modify_account(account_id, pw, mail, phone):
    accounts = load_accounts()
    if update_account(accounts, account_id, pw, mail, phone):
        save_accounts(accounts)
        return True

    return False


def remove_account_by_id(account_id):
    accounts = load_accounts()
    if delete_account(accounts, account_id):
        save_accounts(accounts)
        return True

    return False


def sign_up(id, pw, mail, phone):
    accounts = load_accounts()
    if is_id_exists(accounts, id):
        return False

    create_account(accounts, id, pw, mail, phone)
    save_accounts(accounts)
    return True


def sign_in(id, pw):
    accounts = load_accounts()
    return is_account_exist(accounts, id, pw)
