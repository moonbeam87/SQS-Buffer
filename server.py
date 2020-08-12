from flask import Flask, render_template
from send import sendMessage

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/my-link/")
def my_link():
    print("I got clicked!")
    s = sendMessage()
    return s


if __name__ == "__main__":
    app.run(debug=True)
