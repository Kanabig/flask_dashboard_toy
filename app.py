from flask import Flask, render_template
<<<<<<< HEAD
<<<<<<< HEAD
from blueprints.member.routes import member_bp
from blueprints.bank.routes import bank_bp
=======
from blueprints.account.routes import account_bp
>>>>>>> d71108042a4a7803b5f684ed0fd5d46ced29197f
=======
<<<<<<< Updated upstream
from blueprints.account.routes import account_bp
=======
from blueprints.diary.routes import diary_bp
from blueprints.member.routes import member_bp
>>>>>>> Stashed changes
>>>>>>> 265692cbf4ff708769f1aec922e217c130c2955c

# essentials
app = Flask(__name__)
app.secret_key = "KLASFkjduiqw18asdBCbnkpq-2098418"

# bluprints
<<<<<<< Updated upstream
app.register_blueprint(account_bp)

<<<<<<< HEAD
# bank
app.register_blueprint(bank_bp)

=======
=======
app.register_blueprint(member_bp)
app.register_blueprint(diary_bp)
>>>>>>> Stashed changes
>>>>>>> 265692cbf4ff708769f1aec922e217c130c2955c

# entrypoint
@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
