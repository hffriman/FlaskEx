# Source: Course material

from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form


app = Flask(__name__)

app.secret_key = "yao0xai8wa0oor8uJ0eighaiy1mahw"

db = SQLAlchemy(app)


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	phone = db.Column(db.String, nullable=False)

ContactForm = model_form (Contact, base_class=FlaskForm, db_session=db.session)


@app.before_first_request
def contactDB():

	db.create_all()

	contact = Contact(name="Peter Griffin", email="peter.griffin@email.com", phone="0123456789")
	db.session.add(contact)

	contact = Contact(name="Bart Simpson", email="bart.simpson@email.com", phone="0987654321")
	db.session.add(contact)

	contact = Contact(name="Eric Cartman", email="eric.cartman@email.com", phone="0719203912")
	db.session.add(contact)

	db.session.commit()


@app.route("/")
def index():

	contacts = Contact.query.all()
	return render_template("index.html", contacts=contacts)



@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/new", methods=["GET", "POST"])
def newcontact(id=None):

	contact = Contact()

	if id: contact = Contact.query.get_or_404(id)

	form = ContactForm(obj=contact)

	if form.validate_on_submit():

		form.populate_obj(contact)

		db.session.add(contact)
		db.session.commit()

		flash("New Contact Added")
		return redirect("/")

	return render_template("new.html", form=form)


@app.route("/<int:id>/delete")
def deleteContact(id):

	contact = Contact.query.get_or_404(id)
	db.session.delete(contact)
	db.session.commit()

	flash("Contact Deleted")
	return redirect("/")


if __name__ == "__main__":
	app.run()
