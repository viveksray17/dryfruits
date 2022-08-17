import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.djhtml", title="Home Page")


if __name__ == "__main__":
    app.run(debug=False if os.getenv("DEBUG") == "false" else True,
            port=os.getenv("PORT") if os.getenv("PORT") is not None else 8000,
            host=os.getenv("HOST") if os.getenv("HOST") is not None else "127.0.0.1")
