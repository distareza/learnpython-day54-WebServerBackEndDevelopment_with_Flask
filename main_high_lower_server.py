from flask import Flask
import random
from markupsafe import escape

app = Flask(__name__)

img_logo = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
img_too_high = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
img_too_low = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
img_correct = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

@app.route('/')
def main():
    global random_no
    random_no = random.randint(0, 9)
    print(random_no)
    return "<H1 style=\"text-align: center\">Guess a number between 0 and 9</H1>" \
           f"<center><img src='{img_logo}'></center>"

@app.route("/<int:num>")
def guess(num):
    global random_no

    if num < random_no:
        return f"<h1 style='color: red'>Too Low</h1>" \
                f"<center><img src='{img_too_low}'></center>"
    elif num > random_no:
        return "<h1 style='color: purple'>Too High</h1>" \
                f"<center><img src='{img_too_high}'></center>"
    else:
        random_no = random.randint(0, 9)
        return "<h1 style='color: green'>You Found me!</h1>" \
               f"<center><img src='{img_correct}'></center>"

if __name__ == "__main__":
    # execute only if run as a script
    # run in debug mode
    app.run(debug=True)