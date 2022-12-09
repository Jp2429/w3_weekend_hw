from models.book import *

book_1=Book('Game of Thrones','G.R.R Martin','Fantasy',True)
book_2=Book('Harry Potter','J.K.Rowling','Fantasy',False)

books=[book_1,book_2]

def add_book(title,author,genre,checked_out):
    new_book=Book(title,author,genre,checked_out)
    books.append(new_book)

def delete_book_at_index(index):
    books.pop(index)
