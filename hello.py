"""
    https://flask.palletsprojects.com/en/1.1.x/quickstart/
    https://pypi.org/project/Flask/

    how to run
    mac / linux :
        pip install flask
        export FLASK_APP=hello.py
        flask run
    windows : (open cmd as administrator and go to this directory)
        python -m pip install mitmproxy
        python -m pip install flask
        SET FLASK_APP=hello.py
        python -m flask run
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"
