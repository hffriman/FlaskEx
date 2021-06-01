# Source: "Python Web Service from Idea to Production" by Tero Karvinen

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hei Flask"

app.run()
