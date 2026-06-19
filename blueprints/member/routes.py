from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_members, save_members

member_bp = Blueprint(
    "member",
    __name__,
    url_prefix="/member",
)


# signup form
@member_bp.route("/signup_form", methods=["GET"])
def signup_form():
    return render_template("member/signup_form.html")


# signup confirm
@member_bp.route("/signup_confirm", methods=["POST"])
def signup_confirm():
    mId = request.form["mId"]
    mPw = request.form["mPw"]
    mMail = request.form["mMail"]
    mPhone = request.form["mPhone"]

    members = load_members()

    if mId in members:
        return render_template("member/signup_result.html", result="NG")

    members[mId] = {
        "mId": mId,
        "mPw": mPw,
        "mMail": mMail,
        "mPhone": mPhone,
    }

    save_members(members)

    return render_template("member/signup_result.html", result="OK")


# signin form
@member_bp.route("/signin_form", methods=["GET"])
def signin_form():
    result = request.args.get("result")
    return render_template("member/signin_form.html", result=result)


# signin confirm
@member_bp.route("/signin_confirm", methods=["POST"])
def signin_confirm():
    mId = request.form["mId"]
    mPw = request.form["mPw"]

    members = load_members()

    if mId in members and members[mId]["mPw"] == mPw:
        session["signinedMemberId"] = mId
        return render_template("/member/signin_result.html")

    return redirect("/member/signin_form?result=fail")


# signout confirm
@member_bp.route("/signout_confirm", methods=["GET"])
def signout_confirm():
    session.clear()
    return redirect("/")
