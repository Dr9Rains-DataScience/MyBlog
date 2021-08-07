from flask import render_template,redirect,flash,url_for
from mainapp import app
from mainapp.forms import LoginForm
user={"username":"Dr9Rains","loggedIn":False}
@app.route('/')
@app.route('/index')
def index():
    
    if not user["loggedIn"]:
        form = LoginForm()
        return redirect(url_for('login'))
    return render_template('index.html',title="Home", user=user)

@app.route("/login",methods=["GET","POST"])    
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user["loggedIn"]=True
        flash('Login requested for user {}, remember_me ={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In", form = form)
    