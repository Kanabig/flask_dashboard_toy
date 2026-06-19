from flask import Blueprint, render_template, request, redirect, session
# from utils.json_manager import load_members, save_members

diary_bp = Blueprint(
    "diary",
    __name__,
    url_prefix="/diary",
)



@diary_bp.route("/", methods=["GET"])
def diary_service_main():
    return render_template("diary/diary_main.html")
    