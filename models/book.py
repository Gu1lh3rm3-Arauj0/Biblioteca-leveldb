import uuid
from typing import List
import pickle
import json

from models.category import BookCategory

class Book:
    def __init__(self, title, author, acessBook, category):
        self.title = title
        self.idBook = str(uuid.uuid4())
        self.author = author
        self.status = True
        self.acessBook = acessBook
        self.category = category
        self.waitingList: List[str] = []

    def upStatusBook(self, book, library):
        db = library.db
        # Gera a chave do livro no banco de dados
        book_key = f'book:{book.idBook}'
        
        # Busca o livro no banco de dados
        book_data = db.get(book_key.encode('utf-8'))
        if not book_data:
            print(f"Livro com ID {book.idBook} não encontrado.")
            return
        
        try:
            # Desserializa os dados do livro usando pickle
            book_stored = pickle.loads(book_data)
        except (pickle.UnpicklingError, EOFError) as e:
            print(f"Erro ao desserializar os dados do livro: {e}")
            return
        
        #Altera o status do livro
        book_stored.status = not book_stored.status
        
        #Serializa os dados atualizados do livro
        updated_book_data = pickle.dumps(book_stored)
        
        #Salva o livro atualizado no banco de dados
        db.put(book_key.encode('utf-8'), updated_book_data)


    def __getstate__(self):
        state = self.__dict__.copy()
        # Se você tem atributos não serializáveis, remova-os aqui
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
