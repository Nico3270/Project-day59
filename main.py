from flask import Flask, render_template
import requests

allpost = requests.get("https://api.npoint.io/046ff1b0b99ae039ee33").json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts = allpost)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)