from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_json, save_json, ACCOUNT_FILE
from utils.timestamper import get_current_time_stamp_formated

account_bp = Blueprint(
    "account",
    __name__,
    url_prefix="/account",
)


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
    mId = request.form["mId"]
    mPw = request.form["mPw"]
    mMail = request.form["mMail"]
    mPhone = request.form["mPhone"]

    account = load_json(ACCOUNT_FILE)

    if mId in account:
        return render_template("account/signup_result.html", result="NG")

    account[mId] = {
        "mId": mId,
        "mPw": mPw,
        "mMail": mMail,
        "mPhone": mPhone,
        "reg_date": get_current_time_stamp_formated(),
        "mod_date": get_current_time_stamp_formated(),
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
    mId = request.form["mId"]
    mPw = request.form["mPw"]

    members = load_json(ACCOUNT_FILE)

    if mId in members and members[mId]["mPw"] == mPw:
        session["signinedMemberId"] = mId
        return redirect("/account/")
        # return render_template("/account/signin_result.html")

    return redirect("/account/signin_form?result=fail")


# signout -------------------------------------------------------------------
@account_bp.route("/signout_confirm", methods=["GET"])
def signout_confirm():
    session.clear()
    return redirect("/")
