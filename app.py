"""Flask app for feedback"""
from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import Unauthorized
from models import connect_db, db, User
from forms import LoginForm, RegisterForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_exercise'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route("/")
def root():
    """root"""

    return redirect("/register")


@app.route("/register",methods=["GET", "POST"])
def register():
    """Renders register form (GET) or handles register form submission (POST)"""
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(username, password, first_name, last_name, email)

        db.session.commit()
        session['username'] = user.username
        return redirect('/secret')
    else:
        return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    """login form get and submission post"""
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            
            session['username'] = user.username
            return redirect('/secret')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form)


@app.route("/secret", methods=["GET"])
def secret():
    return "you made it"

@app.route("/logout", methods=["GET"])
def logout():
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect('/')
