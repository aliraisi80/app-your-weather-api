from flask import Flask,render_template
app = Flask("website")

@app.route("/")
def index():
    return"Home Page"
@app.route("/home")
def home():
    return render_template("tutorial.html")

@app.route("/about")
def about():
    return render_template("about.html")
app.run(debug=True)
