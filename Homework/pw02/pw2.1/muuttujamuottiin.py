#Sources:
#--> "Python Web Service from Idea to Production" by Tero Karvinen
#--> Geeks for Geeks: Python program to print current year, month and day

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
	currentdate = date.today()
	currentyear = currentdate.year
	return render_template("muuttujamuottiin.html", currentyear=currentyear)

if __name__ == "__main__":
	app.run()
