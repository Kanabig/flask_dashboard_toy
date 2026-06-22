from flask import Blueprint, render_template, request, redirect, session
from utils.timestamper import get_current_time_stamp_formated
from utils import json_manager

diary_bp = Blueprint(
    "diary",
    __name__,
    url_prefix="/diary",
)

def load_diaries():
    return json_manager.load_json(json_manager.DIARYS_FILE)


def save_diaries(diarys):
    json_manager.save_json(json_manager.DIARYS_FILE, diarys)

    

# diary main
@diary_bp.route("/", methods=["GET"])
def diary_service_main():
    return render_template("diary/diary_main.html")

# write_form
@diary_bp.route("/write_form", methods=["GET"])
def write_form():

    return render_template("diary/write_form.html")

# write_result
@diary_bp.route("/write_result", methods=["POST"])
def write_confirm():
  
    now = get_current_time_stamp_formated()

    signinedMemberId = session.get(
        "signinedMemberId"
    )

    title = request.form["mTitle"]
    content = request.form["mContent"]

    diaries = load_diaries()

    if signinedMemberId not in diaries:
        diaries[signinedMemberId] = []

    diaries[signinedMemberId].append({
        "title": title,
        "content": content,
        "reg_date": now,
        "mod_date": now
    })

    save_diaries(diaries)
    
    return render_template("diary/write_form.html")
    

# read_form
@diary_bp.route("/read_form", methods=["GET"])
def diary_read_form():

    signinedMemberId = session.get(
        "signinedMemberId"
    )

    diaries = load_diaries()

    my_diaries = diaries.get(
        signinedMemberId,
        []
    )

    idx = request.args.get(
        "idx",
        default=0,
        type=int
    )

    selected_diary = None

    if len(my_diaries) > 0:
        selected_diary = my_diaries[idx]

    return render_template(
        "diary/read_form.html",
        diaries=my_diaries,
        selected_diary=selected_diary,
        idx=idx
    )


# update_form
@diary_bp.route("/update_form", methods=["GET"])
def update_form():

    signinedMemberId = session.get(
        "signinedMemberId"
    )

    idx = int(
        request.args.get("idx")
    )

    diaries = load_diaries()

    diary = diaries[
        signinedMemberId
    ][idx]

    return render_template(
        "diary/update_form.html",
        diary=diary,
        idx=idx
    )


# update_confirm
@diary_bp.route("/update_confirm", methods=["POST"])
def update_confirm():

    signinedMemberId = session.get(
        "signinedMemberId"
    )

    idx = int(
        request.form["idx"]
    )

    title = request.form["mTitle"]
    content = request.form["mContent"]

    diaries = load_diaries()

    diaries[
        signinedMemberId
    ][idx]["title"] = title

    diaries[
        signinedMemberId
    ][idx]["content"] = content

    diaries[
        signinedMemberId
    ][idx]["mod_date"] = (
        get_current_time_stamp_formated()
    )

    save_diaries(diaries)

    return redirect(
        "/diary/read_form"
    )


# delete_confirm
@diary_bp.route("/delete_confirm", methods=["GET"])
def delete_confirm():

    signinedMemberId = session.get(
        "signinedMemberId"
    )

    idx = int(
        request.args.get("idx")
    )

    diaries = load_diaries()

    del diaries[
        signinedMemberId
    ][idx]

    save_diaries(diaries)

    return redirect(
        "/diary/read_form"
    )





