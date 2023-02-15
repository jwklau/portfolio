from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year=current_year)

@app.route("/python-projects")
def load_py_projects():
    return render_template("python-projects.html", year=current_year)

@app.route("/web-development-projects")
def load_web_dev_projects():
    return render_template("web-development-projects.html", year=current_year)

@app.route("/contact")
def contact():
    return render_template("contact.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)