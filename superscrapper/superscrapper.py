from flask import Flask, render_template, request, redirect


app = Flask(__name__, template_folder="template")


@app.route("/")
def home():
    return render_template("template.html")


@app.route("/report")
def report():
    word = request.args.get("word").lower()
    if not (word):
        return redirect("/")
    else:
        return render_template("result_template.html", searchingBy=word)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
