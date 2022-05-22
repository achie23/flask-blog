from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# setting secret key
app.config['SECRET_KEY'] = '96409b439ae36e08a1dbbbff50521040'

blog_posts = [
    {
        'author': 'Nana Cobby',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 11, 2020'
    },
    {
        'author': 'Jane Cobby',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 12, 2020'
    },
    {
        'author': 'John Cobby',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 13, 2020'
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash(f'Account created for {register_form.username.data}!', 'success')
        return redirect(url_for('home')) 
    return render_template("register.html", title="Register", form=register_form) 

@app.route("/login")  
def login():
    login_form = LoginForm()
    return render_template("login.html", title="Login", form=login_form) 


# used to run the app directly with python
if __name__ == "__main__":
    app.run(debug=True)