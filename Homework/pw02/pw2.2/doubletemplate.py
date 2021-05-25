#Sources: course material

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("info.html")


@app.route("/extra")
def extra():
	return render_template("extra.html")

if __name__ == "__main__":
	app.run()
