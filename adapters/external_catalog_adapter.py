from typing import List


class ExternalCatalogAdapter:

  def __init__(self, externalDataBank):
    self.externalDataBank = externalDataBank
    
  def searchDataBank(self, library: 'Library', busca: str):
    found_author= next((book for book in library.list_adapter if book.author == busca), None)
    found_title= next((book for book in library.list_adapter if book.title == busca), None)
    found_category= next((book for book in library.list_adapter
                          if book.category == busca),None)
    if found_title :
      found_book=found_title
    elif found_author:
      found_book=found_author
    elif found_category:
      found_book=found_category
    else:
      found_book=None
      
    return found_book


#############################################
class ExternalDataBank:

  def __init__(self, title: str, idBook: int, author: str, category: str):
    self.title = title
    self.idBook = idBook
    self.author = author
    self.category = category