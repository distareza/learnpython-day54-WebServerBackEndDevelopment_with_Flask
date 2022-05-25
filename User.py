class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user.is_logged_in:
            function(user)
        else:
            print("User not logged in")

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog")


new_user = User('Reza')
create_blog_post(new_user)
# will return "User not logged in"

new_user.login()
create_blog_post(new_user)
# will return the text "This is Reza's new blog"
