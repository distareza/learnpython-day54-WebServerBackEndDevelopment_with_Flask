from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def main():
    return "<H1 style=\"text-align: center\">Hello World</H1>" \
           "<p>this is a paragraph</p>" \
           "<img src='https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif'>"


def make_bold(func):
    def wrapper():
        return f"<B>{func()}</B>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    # execute only if run as a script
    # run in debug mode
    app.run(debug=True)