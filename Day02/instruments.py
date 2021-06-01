# Source: "Python Web Service from Idea to Production" by Tero Karvinen

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	instruments=["Piano", "Violin", "Guitar"]
	return render_template("base.html", instruments=instruments)

if __name__ == "__main__":
	app.run()
