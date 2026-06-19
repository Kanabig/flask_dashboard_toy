from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_json, save_json, ACCOUNT_FILE
from utils.timestamper import get_current_time_stamp_formated

account_bp = Blueprint(
    "account",
    __name__,
    url_prefix="/account",
)

KEY_ID = "id"
KEY_PW = "pw"
KEY_MAIL = "mail"
KEY_PHONE = "phone"
KEY_REG_DATE = "reg_date"
KEY_MOD_DATE = "mod_date"
KEY_SESSION_ID = "signinedMemberId"


# account main --------------------------------------------------------------
@account_bp.route("/", methods=["GET"])
def account_service_main():
    id = session.get("signinedMemberId")
    return render_template("account/account_main.html", id=id)


# signup --------------------------------------------------------------------
@account_bp.route("/signup_form", methods=["GET"])
def signup_form():
    return render_template("account/signup_form.html")


@account_bp.route("/signup_confirm", methods=["POST"])
def signup_confirm():
    id = request.form["mId"]
    pw = request.form["mPw"]
    mail = request.form["mMail"]
    phone = request.form["mPhone"]

    account = load_json(ACCOUNT_FILE)

    if id in account:
        return render_template("account/signup_result.html", result="NG")

    account[id] = {
        KEY_ID: id,
        KEY_PW: pw,
        KEY_MAIL: mail,
        KEY_PHONE: phone,
        KEY_REG_DATE: get_current_time_stamp_formated(),
        KEY_MOD_DATE: get_current_time_stamp_formated(),
    }

    save_json(ACCOUNT_FILE, account)

    return render_template("account/signup_result.html", result="OK")


# signin --------------------------------------------------------------------
@account_bp.route("/signin_form", methods=["GET"])
def signin_form():
    result = request.args.get("result")
    return render_template("account/signin_form.html", result=result)


@account_bp.route("/signin_confirm", methods=["POST"])
def signin_confirm():
    id = request.form["mId"]
    pw = request.form["mPw"]

    members = load_json(ACCOUNT_FILE)

    if id in members and members[id][KEY_PW] == pw:
        session[KEY_SESSION_ID] = id
        return redirect("/account/")
        # return render_template("/account/signin_result.html")

    return redirect("/account/signin_form?result=fail")


# signout -------------------------------------------------------------------
@account_bp.route("/signout_confirm", methods=["GET"])
def signout_confirm():
    session.clear()
    return redirect("/")
