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

# __name__ : buildin object, to know which file is currently being run
# https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes
# https://docs.python.org/3/library/__main__.html
print(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/bye')
def bye():
    return "bye"

if __name__ == "__main__":
    # execute only if run as a script
    app.run()

