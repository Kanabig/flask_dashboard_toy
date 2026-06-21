from flask import Blueprint, render_template, request, redirect, session, url_for
from utils.json_manager import load_json, save_json, MEMOS_FILE, ACCOUNT_FILE
from utils.timestamper import datetime

MEMOS_FILE = "json/memos.json"

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
@memo_bp.route("/write", methods=['GET', 'POST'])
def memo_write():

    if request.method == 'GET':
        return render_template("memo/memo_Write.html")

    member_id = session.get('signInedMemberId')
    content = request.form.get('content')
    memos = load_json(MEMOS_FILE)
    
    if member_id not in memos:
        memos[member_id] = []
    now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    memos[member_id].append({
        "content": content,
        "reg_date": now,
        "mod_date": now
    })
    
    save_json(MEMOS_FILE, memos)
    return redirect(url_for("memo.memo_main"))

# /memo/read/
@memo_bp.route("/read", methods=['GET'])
def memo_read():
    member_id = session.get("signinedMemberId")
    
    if member_id is None:
        return "로그인이 필요합니다."
    memos = load_json(MEMOS_FILE)

    user_memos = memos.get(member_id, [])
    return render_template("memo/memo_Read.html", memos=user_memos)
    

# /memo/update/
@memo_bp.route("/update", methods=['GET', 'POST'])
def memo_update():
    if request.method == 'GET':
        return render_template("memo/memo_Update.html")
    member_id = session.get('signinedMemberId')
    
    index= int(request.form.get('memo_id'))
    content = request.form.get('content')
    
    memos = load_json(MEMOS_FILE)
    user_memos = memos.get(member_id, [])
    now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    
    user_memos[index]['content'] = content
    user_memos[index]['mod_date'] = now
    
    save_json(MEMOS_FILE, memos)
    return redirect(url_for("memo.memo_main"))
# /memo/delete/
@memo_bp.route("/delete", methods=['GET', 'POST'])
def memo_delete():
    if request.method == 'GET':
        return render_template("memo/memo_Delete.html")
    member_id = session.get('signinedMemberId')
    index= int(request.form.get('memo_id'))
    
    memos = load_json(MEMOS_FILE)
    user_memos = memos.get(member_id, [])

    user_memos.pop(index)
    save_json(MEMOS_FILE, memos)

    return redirect(url_for("memo.memo_main"))
    

if __name__ == "__main__":
    accounts = load_json(ACCOUNT_FILE)
    save_json(ACCOUNT_FILE, accounts)