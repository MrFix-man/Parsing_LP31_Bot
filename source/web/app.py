from flask import Flask, render_template
from source.lib.db import DB

app = Flask(__name__)
db = DB("sqlite:////home/mr_fix-man/PycharmProjects/Parsing_LP31_Bot/source/my_database.db")


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





