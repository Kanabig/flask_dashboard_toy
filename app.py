from flask import Flask, render_template
from blueprints.member.routes import member_bp
from blueprints.bank.routes import bank_bp

# essentials
app = Flask(__name__)
app.secret_key = "KLASFkjduiqw18asdBCbnkpq-2098418"

# bluprints
app.register_blueprint(member_bp)

# bank
app.register_blueprint(bank_bp)


# entrypoint
@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
