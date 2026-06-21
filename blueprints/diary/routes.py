from flask import Blueprint, render_template, request, redirect, session
# from utils.json_manager import load_members, save_members

diary_bp = Blueprint(
    "diary",
    __name__,
    url_prefix="/diary",
)


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
    return render_template("diary/write_result.html")

# read_form
@diary_bp.route("/read_form", methods=["GET"])
def diary_read_form():
    return render_template("")
    
# update_form
@diary_bp.route("/update_form", methods=["PUT"])
def diary_update_form():
    return render_template("")

# delete_form
@diary_bp.route("/delete_form", methods=["DELETE"])
def diary_delete_form():
    return render_template("")