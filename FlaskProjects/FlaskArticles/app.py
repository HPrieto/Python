from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# 21:00 stop time

# create instance of flask
app = Flask(__name__) #placeholder for current module

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_user'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kaos612'
app.config['MYSQL_DB'] = 'FlaskArticles'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# initialize MySQL
mysql = MySQL(app)

Articles = Articles()

# create route for index
@app.route('/')
def index():
	return render_template('home.html')

# about route
@app.route('/about')
def about():
	return render_template('about.html')

# articles route
@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

# dynamic articles route
@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id=id)

# Register form class
class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
			validators.DataRequired(),
			validators.EqualTo('confirm', message="Passwords do not match")
	])
	confirm = PasswordField('Confirm Password')

# Create Route CLass
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	# check if method is a validated GET or POST request
	if request.method == 'POST' and form.validate():
		# Get user info for POST
		name = form.name.data
		email = form.email.data
		username = form.username.data
		# encrypt password before posting
		password = sha256_crypt.encrypt(str(form.password.data))
		# create cursor
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
		# commit credentials to db
		mysql.connection.commit()
		# close mysql connection
		cur.close()
		# Create success message
		flash('You are now registered and can log in', 'success')
		# redirect user
		return redirect(url_for('login'))
	# render template
	return render_template('register.html', form=form)

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Get username and password from form submitted by user
		username = request.form['username']
		password_candidate = request.form['password']
		# Create a database cursor
		cur = mysql.connection.cursor()
		# GET user by username
		result = cur.execute('SELECT * FROM users WHERE username = %s', [username])
		# check results if any
		if result > 0:
			# get stored hash, fetch first query found
			data = cur.fetchone()
			# get password from database query
			password = data['password']
			# compare passwords
			if sha256_crypt.verify(password_candidate, password):
				app.logger.info('PASSWORD MATCHED')
			else:
				app.logger.info('PASSWORD NOT MATCHED')
		else:
			app.logger.info('NO USER FOUND')
	return render_template('login.html')

# check if __name__ will be executed
if __name__ == '__main__':
	# secret key
	app.secret_key='secret123'
	# run application 
	app.run(debug=True) # debug mode turned on















































