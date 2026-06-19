from flask import Flask, render_template
<<<<<<< Updated upstream
from blueprints.account.routes import account_bp
=======
from blueprints.diary.routes import diary_bp
from blueprints.member.routes import member_bp
>>>>>>> Stashed changes

# essentials
app = Flask(__name__)
app.secret_key = "KLASFkjduiqw18asdBCbnkpq-2098418"

# bluprints
<<<<<<< Updated upstream
app.register_blueprint(account_bp)

=======
app.register_blueprint(member_bp)
app.register_blueprint(diary_bp)
>>>>>>> Stashed changes

# entrypoint
@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
