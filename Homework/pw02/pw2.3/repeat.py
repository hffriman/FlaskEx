from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	drinks=["Wine", "Soda", "Milk", "Water"]
	return render_template("loop.html", drinks=drinks)


if __name__ == "__main__":
	app.run()


