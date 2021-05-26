# Source: Course material


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "ihahWohhaiheeguegh3oozueth1ohm"
db = SQLAlchemy(app)


class Novel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	publisher = db.Column(db.String, nullable=False)
	year = db.Column(db.String, nullable=False)

NovelForm = model_form(Novel, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def init():
	db.create_all()

	novel = Novel(title="Violet Evergarden", author="Kana Akatsuki", publisher="KA Esuma Bunko", year="2015")
	db.session.add(novel)

	novel = Novel(title="The Melancholy of Haruhi Suzumiya", author="Nagaru Tanigawa", publisher="Kadokawa Shoten", year="2003")
	db.session.add(novel)

	novel = Novel(title="Kino's Journey", author="Keiichi Sigsawa", publisher="Dengeki Bunko", year="2000")
	db.session.add(novel)

	db.session.commit()


@app.route("/new", methods=["GET", "POST"])
def addForm():
	form = NovelForm()
	print(request.form) # NB: ONLY IN TEST PHASE
	return render_template("new.html", form=form)


@app.route("/")
def index():
	novels = Novel.query.all()
	return render_template("index.html", novels=novels)


if __name__ == "__main__":
	app.run()

