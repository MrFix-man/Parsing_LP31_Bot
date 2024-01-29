from flask import Flask, render_template, url_for, request
from source.lib.db import DB

app = Flask(__name__)
db = DB("sqlite:////pars_db.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/drom")
def drom():
    auto = db.query_drom()
    return render_template("drom.html", auto=auto, current_page='drom')


@app.route("/avito")
def avito():
    home = db.query_avito()
    return render_template("avito.html", home=home, current_page='avito')


if __name__ == "__main__":
    app.run()





