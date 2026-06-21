from flask import Blueprint
from flask import render_template
from flask import session, request, redirect
from datetime import datetime
import uuid

bank_bp = Blueprint('bank', __name__)

# 테스트 데이터
bankDb = {"1":{"accountNo":"1001", "password":"1234", "balance":50000}}

# 메인
@bank_bp.route('/bank/', methods=['GET','POST'])

def bank():

    memberId = session.get('signinedMemberId')

    if memberId is None:

        return "로그인 필요"
    
    # 계좌 있음
    if memberId in bankDb:
        if not session.get('bankAuth', False):

            return redirect('/bank/auth')

        return render_template('bank/home.html', memberId=memberId, account=bankDb[memberId], auth=True)


    # 신규 계좌 생성
    if request.method=="POST":
        pw = request.form.get('password')

        if len(pw)>6:

            return "비밀번호 최대 6자리"

        accountNo = str(uuid.uuid4())[:8]

        bankDb[memberId]={"accountNo":accountNo, "password":pw, "balance":0}

        return redirect('/bank/auth')

    return render_template('bank/create_account.html')

    # 입금
@bank_bp.route('/bank/deposit', methods=['GET','POST'])

def deposit():
    memberId = session.get('signinedMemberId')
    account = bankDb[memberId]

    if request.method == 'POST':

        bank = request.form.get('bank')

        sender = request.form.get('sender')

        money = int(request.form.get('money'))

        memo = request.form.get('memo')

        account['balance'] += money

        if 'history' not in account:

            account['history']=[]

        account['history'].insert(0, {"type":"입금", "bank":bank, "sender":sender, "money":money, "memo":memo, "date":datetime.now().strftime("%Y.%m.%d %H:%M")})

        return redirect('/bank/')

    return render_template('bank/deposit.html')

@bank_bp.route('/bank/withdraw',methods=['GET','POST'])

def withdraw():
    memberId = session.get('signinedMemberId')
    account = bankDb[memberId]

    if request.method == 'POST':
        receiver = request.form.get('receiver')
        money = int(request.form.get('money'))
        memo = request.form.get('memo')

        # 잔액 부족 체크 ← 추가함
        if account['balance'] < money:

            return "잔액 부족"

        account['balance'] -= money

        # 거래내역 없으면 생성 ← 추가함
        if 'history' not in account:
            account['history']=[]

        account['history'].insert(0, {"type":"출금", "receiver":receiver, "money":money, "memo":memo, "date":datetime.now().strftime("%Y.%m.%d %H:%M")})
        return redirect('/bank/')

    return render_template('bank/withdraw.html', account=account)

@bank_bp.route('/bank/history/<int:index>')

def history_detail(index):
    memberId = session.get('signinedMemberId')
    account = bankDb[memberId]
    histories = account.get('history', [])

    if index >= len(histories):

        return "존재하지 않는 거래"

    history = histories[index]
    return render_template('bank/history_detail.html', history=history,balance=account['balance'])

@bank_bp.route('/bank/history')

def history():
    memberId = session.get('signinedMemberId')
    account = bankDb[memberId]
    histories = account.get('history',[])

    return render_template('bank/history.html',histories=histories)

@bank_bp.route('/bank/send',methods=['GET','POST'])

def send():
    memberId = session.get('signinedMemberId')
    account = bankDb[memberId]

    if request.method == 'POST':

        bank = request.form.get('bank')
        receiver = request.form.get('receiver')
        accountNo = request.form.get('accountNo')
        money = int(request.form.get('money'))
        memo = request.form.get('memo')

        if account['balance'] < money:

            return "잔액 부족"
        
        account['balance'] -= money

        if 'history' not in account:
            account['history']=[]

        account['history'].insert(0, {"type":"송금", "bank":bank, "receiver":receiver, "accountNo":accountNo, "money":money, "memo":memo, "date":datetime.now().strftime("%Y.%m.%d %H:%M")})

        return redirect('/bank/')

    return render_template('bank/send.html',account=account)

@bank_bp.route('/bank/auth', methods=['GET','POST'])

def auth():
    memberId = session.get('signinedMemberId')

    if memberId not in bankDb:
        return redirect('/bank/')

    account = bankDb[memberId]

    if request.method=='POST':
        pw = request.form.get('password')

        if pw == str(account['password']):
            session['bankAuth'] = True

            return redirect('/bank/')

        return render_template('bank/auth.html', error=True)

    return render_template('bank/auth.html')