import pandas as pd
class Booklover:
    def __init__(self,book_list,num_books=None):
        self.num_books = 0
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    def __init__(self,name, email,fav_genre):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
    def add_book(self,book_name, book_rating): 
        try:
            if book_name in self.book_list:
                return ValueError
            print("Book is already in Book list")
            return None 
        except:
            self.book_list = pd.DataFrame({'book_name':[book_name], 'book_rating':[book_rating]})
            new_book = self.book_list
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.book_list.index.name='num_books'
    def has_read(self,book_name):
        try:
            if book_name in self.book_list:
                return ValueError("False")
            return False
                
        except:
            if book_name in self.book_list:
                print("True")
                return True                
    def num_books_read(self):
        len(num_books)
    def fav_books(self,book_rating):
        lambda booklover: booklover.book_rating >3    
    
  
    