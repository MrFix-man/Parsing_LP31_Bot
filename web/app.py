from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/drom")
def drom():
    return render_template("drom.html")


@app.route("/avito")
def avito():
    return render_template("avito.html")


if __name__ == "__main__":
    app.run(debug=True)





