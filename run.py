import os
from flask import Flask, render_template
from django.conf import settings
settings.configure()
import django
django.setup()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/signinpage" , methods=['GET', 'POST'])
def signinpage():
    return render_template("signinpage.html")

@app.route("/signin" , methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")       


@app.route("/register" , methods=['GET', 'POST'])
def register():
    return render_template("register.html")    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
