from flask import Flask, render_template
from blueprints.account.routes import account_bp
from blueprints.diary.routes import diary_bp
from blueprints.memo.routes import memo_bp
from blueprints.bank.routes import bank_bp
# essentials
app = Flask(__name__)
app.secret_key = "KLASFkjduiqw18asdBCbnkpq-2098418"

# bluprints
app.register_blueprint(memo_bp)
app.register_blueprint(account_bp)
app.register_blueprint(diary_bp)
app.register_blueprint(bank_bp)


# entrypoint
@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
