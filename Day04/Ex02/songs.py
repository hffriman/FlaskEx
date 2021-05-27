# Source: Course material
# Comment 'm' means that I did not remember the syntaxes correctly or at all

from flask import Flask, render_template, request, redirect, flash

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm

from wtforms.ext.sqlalchemy.orm import model_form #m accidentally used uppercases in model_form


app = Flask(__name__)

app.secret_key="hieShoh9co5utopeefohMuhit0Har4"

db = SQLAlchemy(app)


class Song(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	artist = db.Column(db.String, nullable=False)


SongForm = model_form(Song, base_class=FlaskForm, db_session = db.session) #m


@app.before_first_request
def initDb():

	db.create_all()

	song = Song(title="One Last Kiss", artist="Hikaru Utada")
	db.session.add(song)

	song = Song(title="Live and Learn", artist="Crush 40")
	db.session.add(song)

	db.session.commit()



@app.route("/")
def index():

	songs = Song.query.all() #m accidentally used lowercase in 'Song.query.all()'

	return render_template("index.html", songs=songs)


@app.route("/<int:id>/edit", methods=["GET", "POST"]) # new annotation
@app.route("/new", methods=["GET", "POST"]) #m did not remember most of the function 'newsong()'
def newsong(id=None):

	song = Song()

	if id: song = Song.query.get_or_404(id)

	form = SongForm(obj=song)

	if form.validate_on_submit():

		form.populate_obj(song)

		db.session.add(song)
		db.session.commit()

		flash("Song Added")
		return redirect("/")

	return render_template("new.html", form=form)



if __name__ == "__main__":
	app.run()
