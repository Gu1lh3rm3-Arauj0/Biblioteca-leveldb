import uuid
from typing import Optional


class BookCategory():
  idCategory: str

  def init(self,
               nameCategory: str,
               subCategory: Optional['BookCategory'] = None):  #hierarquia
    self.nameCategory = nameCategory
    self.idCategory = str(uuid.uuid4())
    self.subCategory = subCategory