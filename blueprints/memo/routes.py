from flask import Blueprint, render_template, request, redirect, session

memo_bp = Blueprint(
    'memo',
    __name__,
    url_prefix='/memo'
)

#/memo/
@memo_bp.route("/")
def memo_main():
    return render_template("memo/memo_Service.html")

# /memo/create/
# /memo/read/
# /memo/write/
# /memo/delete