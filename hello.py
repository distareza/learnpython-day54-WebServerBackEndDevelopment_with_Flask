"""
    https://flask.palletsprojects.com/en/1.1.x/quickstart/
    https://pypi.org/project/Flask/

    how to run a flask not as script
    mac / linux :
        pip install flask
        export FLASK_APP=hello.py
        flask run
    windows : (open cmd as administrator and go to this directory)
        python -m pip install mitmproxy
        python -m pip install flask
        SET FLASK_APP=hello.py
        python -m flask run

    how to run a flask as script
        python hello.py

"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# __name__ : buildin object, to know which file is currently being run
# https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes
# https://docs.python.org/3/library/__main__.html
print(__name__)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/bye')
def bye():
    return "bye"

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route('/greet/<name>')
def greet(name):
    return f"Hello There {name}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

if __name__ == "__main__":
    # execute only if run as a script
    # run in debug mode
    app.run(debug=True)

