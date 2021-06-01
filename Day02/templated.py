# Sources:
# --  "Python Web Service from Idea to Production" by Tero Karvinen
# !!  Special thanks to co-students for sharing their
# !!  problems during class: it helped me to fix my
# !!  own problem in rendering the "music" array

from flask import Flask, render_template, request

app = Flask(__name__)

name = "Henry"

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/extension")
def extension():
	music = ["Classic", "Pop", "Rock", "Rap"]
	return render_template("extension.html", music=music)

@app.route("/postform", methods=["GET", "POST"])
def postform():
	area = 0
	if "side" in request.form:
		side = int(request.form["side"])
		area = side*side
	return render_template("postform.html", area=area)


@app.route("/getform")
def getform():
	return render_template("getform.html")

if __name__ == "__main__":
	app.run()
