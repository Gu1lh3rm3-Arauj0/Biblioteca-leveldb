import uuid
from datetime import datetime, timedelta
import pickle

from models.book import Book

class Loan:
    def __init__(self, book, user, library):
        self.idLoan = str(uuid.uuid4())
        self.book = book
        self.user = user
        self.loanDate = datetime.now()
        self.endDate = datetime.now() + timedelta(days=7)
        self.statusLoan = True
        book.upStatusBook(book, library)

    def upStatusLoan(self, loan, library):
        db = library.db
        # Gera a chave do livro no banco de dados
        loan_key = f'loan:{loan.idLoan}'
        
        # Busca o laon no banco de dados
        loan_data = db.get(loan_key.encode('utf-8'))
        if not loan_data:
            print(f"Livro com ID {loan.idLoan} não encontrado.")
            return
        
        try:
            # Desserializa os dados do livro usando pickle
            loan_stored = pickle.loads(loan_data)
        except (pickle.UnpicklingError, EOFError) as e:
            print(f"Erro ao desserializar os dados do loan: {e}")
            return
        
        loan_stored.statusLoan = not loan_stored.statusLoan
        
        updated_loan_data = pickle.dumps(loan_stored)
        
        db.put(loan_key.encode('utf-8'), updated_loan_data)


    def returnLoan(self, loan, user, book, library):
        loan.upStatusLoan(loan, library) 
        book.upStatusBook(book, library)

    def __getstate__(self):
        state = self.__dict__.copy()
        # Se você tem atributos não serializáveis, remova-os aqui
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
