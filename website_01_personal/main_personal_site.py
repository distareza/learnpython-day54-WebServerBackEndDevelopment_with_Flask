"""
    https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    Flask will look for templates in the "templates" folder. So if your application is a module,
    this folder is next to that module, if it’s a package it’s actually inside your package

    https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
    Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from.
    Ideally your web server is configured to serve them for you, but during development Flask can do that as well.
    Just create a folder called static in your package or next to your module
    and it will be available at /static on the application.

"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    #return render_template("home.html")
    return render_template("my_website.html")


if __name__ == "__main__":
    app.run()