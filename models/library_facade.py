
from models.mediator import LibraryMediator, Mediator


class LibraryFacade:

  def operation(self, option, data, library):

    mediator = LibraryMediator()

    if option==1: #opção de busca
      #data = [name_user, livro_busca, adapter]
      data[0]= mediator.searchUser(data[0], library)  #encontra o usuario
      mediator.searchBooks(data,library)              #aqui vai procurar o livro msm
    
    elif option==2: #opcao de realizar um emprestimo
      user=mediator.searchUser(data[0], library) #encontra o usuario
      book=mediator.foundBook(data[1], library) #encontra o livro
      mediator.lendBook(user, book, library)
    
    elif option==3: #opcao para devolver um livro
      loan=mediator.searchLoan(data[0], library) #encontra o loan
      mediator.returnBook(loan, library) #aqui ele tem q passar o id do livro dele
    
    elif option==4: #opcao para adicionar um livro
      mediator.createBook(data, library)
    
    elif option==5: 
      #opção para adicionar um usuario  #esse aqui ja faz quando a pessoa ja entra né?
      mediator.createUser(data, library)
    
    elif option == 6:
      mediator.searchUser(data, library)
    
    elif option == 7:
      pass
    #mediator.foundBook(data, library)