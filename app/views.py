from flask import render_template, flash, redirect
from app import app 
from forms import LoginForm

# create mappings from urls to function
@app.route('/')
@app.route('/index')
def index(): 
	user = {'nickname': 'Miguel' } # fake user 
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html", 
		title = 'Home', 
		user = user,
		posts = posts)


# need to say that view is getting POST requests (default is just GET)
@app.route('/login', methods = ['GET', 'POST'])
def login():
	"""Instantiate a LoginForm object and send to template.""" 
	form = LoginForm()
	# does form processing work
	if form.validate_on_submit():
		# just show message to user and redirect 
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', 
		title = 'Sign In', 
		form = form, 
		providers = app.config['OPENID_PROVIDERS'])