class BookAvailabilityNotifier:

  def notifyAddBook(self, book):
    print(f'O livro {book.title} foi adicionado ao catálago')
  
  #manda notificação pra usuarios da lista de espera
  def notifyChangedStatus(self, book):
    if book.waitingList:
      self.idUserWatingList = book.waitingList.pop(0)
      print(f'\nMensagem para {self.idUserWatingList}: ')
      print(f'O livro {book.title} agora esta disponível! \n')
    else:
      pass
