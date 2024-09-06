import tkinter as tk
from tkinter import messagebox

from abc import ABC, abstractmethod

from models.book import Book
from models.library import Library
from models.loan import Loan
from models.user import User, UserStudent, UserTeacher


class Mediator(ABC):

  @abstractmethod
  def searchBooks(self, data, library):
    pass

  @abstractmethod
  def lendBook(self, user, book, library):
    pass

  @abstractmethod
  def returnBook(self, loan, library):
    pass

  @abstractmethod
  def createBook(self, data, library):
    pass

  @abstractmethod
  def createUser(self, data, library):
    pass
    
  @abstractmethod
  def searchUser(self, data, library):
    pass

  @abstractmethod
  def foundBook(self, data, library):
    pass

####################################################################

class LibraryMediator(Mediator):
  
  def __init__(self):
    #library = Library()
    #self.adapter = ExternalCatalogAdapter()
    #self.library = library
    pass

  def searchBooks(self, data, library):
    #data = [user, livro_busca]
    user= data[0]
    busca=data[1]        # lista de adapters
    user.searchBooks(library, busca)

  def lendBook(self, user: 'User', book: 'Book', library: 'Library'):
    #aqui agrupamos alguns metodos
    #vemos se o usuario pode fazer o emprestimo
    # se pode, fazemos e adicionamos a lista de loans
    if user.requestLoan(user, book):
      new_loan = Loan(book, user, library)
      library.addLoan(new_loan)
      message = (
            f"Seu empréstimo foi realizado! \nVocê tem até dia {new_loan.endDate} para devolver.\n"
            f"Ah, o código de empréstimo é {new_loan.idLoan}. Lembre-se de anotá-lo para a devolução do livro.\n"
            f"Aproveite a leitura :)\n"
        )
      messagebox.showinfo("Empréstimo Realizado", message)
    else:
      messagebox.showerror("Erro", "Seu empréstimo não foi aprovado :( \nTente novamente!")

  def returnBook(self, loan: 'Loan', library): 
    #aqui a gente vai perguntar o id do livro que o usuario quer devolver
    loan.returnLoan(loan, loan.user, loan.book, library)
    message = (
            f"Livro devolvido com sucesso!\n"
        )
    messagebox.showinfo("Sucesso!!", message)
  
  def createBook(self, data, library):
    title=data[0]
    author=data[1]
    category=data[2]
    acessBook = data [3]
    book=Book(title, author, category, acessBook)
    library.addBook(book)

  def createUser(self, data, library):
    if data[2] == 'STUDENT':
      user=UserStudent(data[0], data[1], data[2])
    else:
      user=UserTeacher(data[0], data[1], data[2])
    library.addUser(user)
    print(f'{user.name}, seja bem vindo a nossa biblioteca!\n')

  def searchUser(self, data, library):
    user= library.searchUser(data)
    return user

  def searchLoan(self, data, library):
    loan= library.searchLoan(data)
    return loan

  def foundBook(self, data, library):
    book= library.foundBook(data)
    return book