# Source: "Python Web Service from Idea to Production" by Tero Karvinen
# Comment 'm' means that I did not remember the syntaxes on my own

from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form #m

app = Flask(__name__)

app.secret_key = "Yiithien6poh7Afomeoph1Eighohgo"

db = SQLAlchemy(app)


class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	publisher = db.Column(db.String, nullable=False)


CharacterForm = model_form(Character, base_class=FlaskForm, db_session=db.session) #m


@app.before_first_request
def initDb():
	db.create_all()

	character = Character(name="Sonic the Hedgehog", publisher="SEGA")
	db.session.add(character)

	character = Character(name="Super Mario", publisher="Nintendo")
	db.session.add(character)

	db.session.commit()


@app.route("/")
def index():
	characters = Character.query.all() #m
	return render_template("index.html", characters=characters) #m


@app.route("/new", methods=["GET", "POST"]) #m most of the parts
def newCharacter():

	form = CharacterForm()

	if form.validate_on_submit():

		character = Character()

		form.populate_obj(character)

		db.session.add(character)

		db.session.commit()

		redirect("/")

	return render_template("new.html", form=form)



if __name__ == "__main__":
	app.run()
