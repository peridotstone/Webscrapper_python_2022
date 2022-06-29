from flask import Flask


app = Flask("superscrapper")


@app.route("/")
def home():
    return "Hello! welcome to mi casa!"


@app.route("/contact")
def contact():
    return "contact me!"


app.run(host="0.0.0.0")
