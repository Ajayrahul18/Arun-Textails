from flask import Blueprint, render_template, session, redirect, request
# from .forms import LoginForm, SignUpForm, PasswordChangeForm
# from .models import Customer
# from . import db




auth = Blueprint('auth', __name__)


SINGLE_USER = {'username': 'test', 'password': 'test'}

def login_required(view_func):
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return view_func(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == SINGLE_USER['username'] and password == SINGLE_USER['password']:
            session['logged_in'] = True
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect('/')