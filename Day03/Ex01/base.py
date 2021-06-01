# Sources:
# "Python Web Service from Idea to Production" by Tero Karvinen
# Flask documentation: Message Flashing (version 1.0)

from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form



app = Flask(__name__)
app.secret_key = "yeeshaePae2rux7Bohqu3eC7ahz5ai"
db = SQLAlchemy(app)


class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	year = db.Column(db.String, nullable=False)
	director = db.Column(db.String, nullable=False)

MovieForm = model_form(Movie, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initMe():
	db.create_all()

	movie = Movie(name="Shiki-Jitsu", year = "2000",  director="Hideaki Anno")
	db.session.add(movie)

	movie = Movie(name="Moonlight", year = "2016", director="Barry Jenkins")
	db.session.add(movie)

	db.session.commit()


@app.route("/new", methods=["GET", "POST"])
def addForm():
	form = MovieForm()
	print(request.form) #test only
	return render_template("new.html", form=form)


@app.route("/msg")
def msgPage():
	flash("This is information")
	return redirect("/")


@app.route("/")
def index():
	movies = Movie.query.all()
	return render_template("index.html", movies=movies)



if __name__ == "__main__":
	app.run()
