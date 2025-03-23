import unittest
import pandas as pd
from booklover import Booklover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        book1=Booklover("tyler","vsg3se@virginia.edu","ficton")
        book1.add_book("Harry Potter",5)
        print(book1)
        print(book1.book_list)
    def test_2_add_book(self):
        book1=Booklover("tyler","vsg3se@virginia.edu","ficton")
        book1.add_book("Harry Potter",5)
        print(book1)
        print(book1.book_list)
    def test_3_has_read(self):
        book1=Booklover("Tom","Tom@virginia.edu","ficton")
        book1.add_book("The Lord of the Rings",4)
        book1.has_read("The Lord of the Rings")
        print(book1.book_list)
        print(book1)
    def test_4_has_read(self):
        book1=Booklover("Tim","Tim@virginia.edu","ficton")
        self.assertFalse(book1.book_list("Inferno"))
    def test_5_num_books_read(self):
        book1=Booklover("Sam","newemail@virginia.edu","ficton")
        book1.add_book("Foundations of Chemistry",5)
        book1.add_book("Star Wars",5)    
        book1.add_book("1984",4)
        book1.add_book("Jumanji",3)
        print(len(book1.book_list))
    def test_6_fav_books(self):
        book1=Booklover("John","favemail@virginia.edu","nonficton")
        book1.add_book("Business Analytics",4)
        book1.add_book("Linear Regression Analysis",4)
        book1.add_book("The Great Gatsby",4)
        book1.fav_books(book1.book_list.book_rating)
        
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)        