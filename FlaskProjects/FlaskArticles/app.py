from flask import Flask, render_template
from data import Articles

# create instance of flask
app = Flask(__name__) #placeholder for current module

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

# check if __name__ will be executed
if __name__ == '__main__':
	# run application 
	app.run(debug=True) # debug mode turned on