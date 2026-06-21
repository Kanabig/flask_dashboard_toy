from flask import Blueprint, render_template, request, redirect, session, url_for
from blueprints.account import access

account_bp = Blueprint(
    "account",
    __name__,
    url_prefix="/account",
)

KEY_SESSION_ID = "signinedMemberId"


# --- utils ---
def get_signed_in_account_id():
    return session.get(KEY_SESSION_ID)


def require_signed_in_account():
    account_id = get_signed_in_account_id()
    if not account_id:
        return None, redirect(url_for("account.signin_form"))
    return account_id, None


def get_form_value(key):
    return request.form.get(key, "").strip()


# --- ACCOUNT SERVICE ROOT ---
@account_bp.route("/", methods=["GET"])
def account_service_main():
    account_id = get_signed_in_account_id()
    return render_template("account/account_main.html", id=account_id)


# --- SIGN UP ---
@account_bp.route("/signup_form", methods=["GET"])
def signup_form():
    return render_template("account/signup_form.html")


@account_bp.route("/signup_confirm", methods=["POST"])
def signup_confirm():
    id = get_form_value("mId")
    password = get_form_value("mPw")
    mail = get_form_value("mMail")
    phone = get_form_value("mPhone")

    result = access.sign_up(id, password, mail, phone)
    return render_template(
        "account/signup_result.html",
        result=result,
    )


# --- SIGN IN ---
@account_bp.route("/signin_form", methods=["GET"])
def signin_form():
    result = request.args.get("result")
    return render_template("account/signin_form.html", result=result)


@account_bp.route("/signin_confirm", methods=["POST"])
def signin_confirm():
    id = get_form_value("mId")
    password = get_form_value("mPw")

    if access.sign_in(id, password):
        session[KEY_SESSION_ID] = id
        return redirect(url_for("account.account_service_main"))

    return redirect(url_for("account.signin_form", result="False"))


# --- SIGN OUT ---
@account_bp.route("/signout_confirm", methods=["GET"])
def signout_confirm():
    session.clear()
    return redirect(url_for("main_page"))


# --- DELETE ACCOUNT ---
@account_bp.route("/delete_confirm", methods=["GET", "POST"])
def delete_confirm():
    id, redirect_response = require_signed_in_account()
    if redirect_response:
        return redirect_response

    if request.method == "POST":
        if access.remove_account_by_id(id):
            session.clear()
        return redirect(url_for("main_page"))

    return render_template("account/delete_confirm.html", id=id)


# --- MODIFY ACCOUNT ---
@account_bp.route("/modify_form", methods=["GET"])
def modify_form():
    id, redirect_response = require_signed_in_account()
    if redirect_response:
        return redirect_response

    account = access.get_account_by_id(id)
    if not account:
        session.clear()
        return redirect(url_for("account.signin_form"))

    return render_template("account/modify_form.html", account=account)


@account_bp.route("/modify_confirm", methods=["POST"])
def modify_confirm():
    id, redirect_response = require_signed_in_account()
    if redirect_response:
        return redirect_response

    password = get_form_value("mPw")
    mail = get_form_value("mMail")
    phone = get_form_value("mPhone")

    access.modify_account(id, password, mail, phone)
    return redirect(url_for("account.account_service_main"))
