# Sources:
# -- Course material
# !!  Special thanks to co-students for sharing their
# !!  problems during class: it helped me to fix my
# !!  own problem in rendering the "music" array

from flask import Flask, render_template

app = Flask(__name__)

name = "Henry"

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/extension")
def extension():
	music = ["Classic", "Pop", "Rock", "Rap"]
	return render_template("extension.html", music=music)

@app.route("/postform")
def postform():
	return render_template("postform.html")

@app.route("/getform")
def getform():
	return render_template("getform.html")

if __name__ == "__main__":
	app.run()
