import flask
from flask import render_template
from flask import request
app = flask.Flask(__name__)


book1=["Book1","Author1",0,'']
book2=["Book2","Author2",0,'']
books=[book1,book2]

@app.route('/')
def homepage():
	return("Welcome to the home page new page")

@app.route('/allbooks')
def allbooks():
	global books
	return render_template("allBooks.html",booo=books)

@app.route('/addbook')
def addbook():
	return render_template("addBook.html")

@app.route('/addingBook',methods=['POST'])
def addingBook():
	global books
	var1 = request.form['title']
	var2 = request.form['author']
	
	new_book = [var1,var2]
	books.append(new_book)
	return "Task Done"


@app.route('/welcome')
def welcome():
	return("This your welcome page")
@app.route('/booksissued/<user>')
def booksIssue(user):
	#return('<center>Hello m\'lad <b>' + user + '</b></center>')
	return render_template("allBooks.html",var1=user)
@app.route('/issueBook')
def issueBook():
	return render_template("issueBook.html")
if __name__ == "__main__" :
	app.run(debug=True)