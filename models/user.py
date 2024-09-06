import uuid
import plyvel
import pickle
import tkinter as tk
from tkinter import messagebox
from typing import List

from models.book import Book

class User:
    def __init__(self, name, email, type):
        self.name = name
        self.idUser = str(uuid.uuid4())
        self.email = email
        self.type = type

    import plyvel

    def searchBooks(self, library, busca):
        # Usa o banco de dados LevelDB a partir do objeto library
        db = library.db

        found_book = None

        try:
            # Itera sobre todas as entradas do banco de dados para buscar o livro
            for key, value in db:
                try:
                    # Desserializa os dados do livro do banco de dados
                    book = pickle.loads(value)  # Usando pickle para desserializar o objeto
                    
                    # Verifica se algum dos atributos do livro corresponde ao termo de busca
                    if busca == book.title or busca == book.author or busca == book.category:
                        found_book = {
                            'id': book.idBook,
                            'title': book.title,
                            'author': book.author,
                            'category': book.category,
                            'status': 'Disponível' if book.status else 'Indisponível'
                        }
                        break  # Para o loop se o livro for encontrado

                except (pickle.UnpicklingError, AttributeError) as e:
                   # print(f"Erro ao desserializar ou acessar atributos ao ler a entrada com chave {key}. Erro: {e}. Pulando esta entrada.")
                    continue  # Pula para a próxima entrada se houver um erro de desserialização

            # Exibe os resultados da busca
            if found_book:
                message = (
                    f"\nSeu livro foi encontrado! Segue informações:\n"
                    f"Titulo: {found_book['title']}\n"
                    f"Autor: {found_book['author']}\n"
                    f"Disponível: {found_book['status']}\n"
                    f"Categoria: {found_book['category']}\n"
                )
                messagebox.showinfo("Livro Encontrado", message)
                #print('\nSeu livro foi encontrado! Segue informações:')
                #print(f"Titulo: {found_book['title']}, Autor: {found_book['author']}, Disponível: {found_book['status']}, Categoria: {found_book['category']}\n")
            else:
                print('Seu livro não foi encontrado :(\n')

        except plyvel.IOError as e:
            print(f"Erro ao acessar o banco de dados: {e}")

    def requestLoan(self, user, book):
        if not BookAvailabilityHandler().verifyStatus(book):
            return False
        elif not UserEligibilityHandler().verifyAcess(user, book):
            return False
        else:
            return True

    def __getstate__(self):
        state = self.__dict__.copy()
        # Se você tem atributos não serializáveis, remova-os aqui
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

class UserStudent(User):
    def __init__(self, name, email, type):
        super().__init__(name, email, type)
        self.idStudent = str(uuid.uuid4())

class UserTeacher(User):
    def __init__(self, name, email, type):
        super().__init__(name, email, type)
        self.idTeacher = str(uuid.uuid4())

#####################################################

class UserEligibilityHandler:

  def verifyAcess(self, user: 'User', book: Book):
    if isinstance(user, UserStudent):
      user_type = 'STUDENT'
    elif isinstance(user, UserTeacher):
      user_type = 'TEACHER'
    else:
      user_type = 'NOTHING'

    #print(f'Confere UserEligibilityHandler: {book.acessBook} == {user_type}')
    #def verifyAcess(self, user: 'User', book: Book):
    return (book.acessBook == user_type or book.acessBook == 'BOTH')

########################################

class BookAvailabilityHandler:

  def verifyStatus(self, book: Book):  #vari retornar True(estatos disponivel)
    #print(f'\nConfere BookAvailabilityHandler: status ->{book.status}')
    return book.status
