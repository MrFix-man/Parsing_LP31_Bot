from flask import Flask, render_template, url_for, request, redirect
from source.lib.db import DB
from source.lib.models import ParsAvito, ParsDrom
app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/drom", methods=["GET"])
def drom():
    return render_template("drom.html", messages=ParsDrom.query.all)


@app.route("/avito", methods=["GET"])
def avito():
    return render_template("avito.html", messages=ParsAvito.query.all())


if __name__ == "__main__":
    app.run(debug=True)





