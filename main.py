from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python-projects")
def load_py_projects():
    return render_template("python-projects.html")

@app.route("/web-development-projects")
def load_web_dev_projects():
    return render_template("web-development-projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)