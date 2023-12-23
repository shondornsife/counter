from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():
    count = session["count"]
    session["count"] += 1
    return render_template("index.html", count)


# I can't figure out why this isn't working :(


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
