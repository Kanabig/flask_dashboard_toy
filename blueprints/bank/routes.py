from flask import Blueprint
from flask import render_template
from flask import session, request, redirect
import uuid

bank_bp = Blueprint('bank', __name__)

bankDb = {"1":{"accountNo":"1001", "balance":50000}}

@bank_bp.route('/bank/', methods=['GET','POST'])

def bank():

    memberId = session.get('signinedMemberId')

    if memberId is None:

        return "로그인 필요"
    if request.method == 'POST':

        pw = request.form.get('password')

        # 비밀번호 최대 6자리 입력하게 설정
        if len(pw) > 6:
            return "비밀번호는 최대 6자리입니다."
        
        # UUID 계좌 생성
        accountNo = str(uuid.uuid4())[:8]
        
        bankDb[memberId]={"accountNo": accountNo, "password":pw, "balance":0}

        return redirect('/bank/')

    if memberId in bankDb:

        return render_template(
            'bank/home.html',
            memberId=memberId,
            account=bankDb[memberId]
        )

    return render_template('bank/create_account.html')