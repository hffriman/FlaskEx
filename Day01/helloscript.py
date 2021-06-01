# Source: "Python Web Service from Idea to Production" by Tero Karvinen

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello Henry!"

@app.route("/info")
def info():
	return "This is my first exercise for Python Web Service course"

@app.route("/feelings")
def feelings():
	return "This course is fascinating"

app.run()
