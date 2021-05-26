# Source: course material

from flask import Flask, render_template, flash, redirect


app = Flask(__name__)

app.secret_key = "ahfeiphu4soo0iethiphoSi2omohng"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/left")
def left():
	flash("<----- You have pressed the left button")
	return redirect("/")

@app.route("/right")
def right():
	flash("You have pressed the right button ----->")
	return redirect("/")


if __name__ == "__main__":
	app.run()
