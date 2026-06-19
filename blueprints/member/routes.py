from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_json, save_json
from utils.timestamper import get_current_time_stamp_formated

member_bp = Blueprint(
    "member",
    __name__,
    url_prefix="/member",
)


# account main --------------------------------------------------------------
@member_bp.route("/", methods=["GET"])
def member_service_main():
    return render_template("member/member_main.html")


# signup --------------------------------------------------------------------
@member_bp.route("/signup_form", methods=["GET"])
def signup_form():
    return render_template("member/signup_form.html")


@member_bp.route("/signup_confirm", methods=["POST"])
def signup_confirm():
    mId = request.form["mId"]
    mPw = request.form["mPw"]
    mMail = request.form["mMail"]
    mPhone = request.form["mPhone"]

    members = load_json()

    if mId in members:
        return render_template("member/signup_result.html", result="NG")

    members[mId] = {
        "mId": mId,
        "mPw": mPw,
        "mMail": mMail,
        "mPhone": mPhone,
        "reg_date": get_current_time_stamp_formated(),
        "mod_date": get_current_time_stamp_formated(),
    }

    save_json(members)

    return render_template("member/signup_result.html", result="OK")


# signin --------------------------------------------------------------------
@member_bp.route("/signin_form", methods=["GET"])
def signin_form():
    result = request.args.get("result")
    return render_template("member/signin_form.html", result=result)


@member_bp.route("/signin_confirm", methods=["POST"])
def signin_confirm():
    mId = request.form["mId"]
    mPw = request.form["mPw"]

    members = load_json()

    if mId in members and members[mId]["mPw"] == mPw:
        session["signinedMemberId"] = mId
        return render_template("/member/signin_result.html")

    return redirect("/member/signin_form?result=fail")


# signout -------------------------------------------------------------------
@member_bp.route("/signout_confirm", methods=["GET"])
def signout_confirm():
    session.clear()
    return redirect("/")
