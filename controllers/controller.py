from flask import render_template, request, redirect # ADDED
from app import app
from models.book_list import books,add_book,delete_book_at_index
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Book Store', books=books)

@app.route('/books/<index>')
def order(index):
    return render_template('book.html', title="Single Book", index = index, books=books)

@app.route('/books',methods=['POST'])
def create():
    title=request.form['title']
    author=request.form['author']
    genre=request.form['genre']
    checked_out=bool(request.form['checked_out'])
    add_book(title,author,genre,checked_out)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
  delete_book_at_index(int(index))
  return redirect('/books')