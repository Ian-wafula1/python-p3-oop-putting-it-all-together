#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    # @property
    # def title(self):
    #     return self._title
    
    # @title.setter
    # def title(self, title):
    #     if 
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) not in (int,):
            print("page_count must be an integer")
        else:
            self._page_count = page_count
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        