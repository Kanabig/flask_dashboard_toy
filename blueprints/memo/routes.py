from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_json, save_json, ACCOUNT_FILE


memo_bp = Blueprint(
    'memo',
    __name__,
    url_prefix='/memo'
)

#/memo/
@memo_bp.route("/")
def memo_main():
    return render_template("memo/memo_Service.html")

# /memo/write/
@memo_bp.route("/write", methods=['GET'])
def memo_write():
    return render_template("memo/memo_Write.html")
    
# /memo/read/
@memo_bp.route("/read", methods=['GET'])
def memo_read():
    return render_template("memo/memo_Read.html")
# /memo/write/
@memo_bp.route("/update", methods=['GET'])
def memo_update():
    return render_template("memo/memo_Update.html")
# /memo/delete/
@memo_bp.route("/delete", methods=['GET'])
def memo_delete():
    return render_template("memo/memo_Delete.html")