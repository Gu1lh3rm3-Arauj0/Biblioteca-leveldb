import plyvel
import pickle
from models.book import Book
from models.user import User
from models.loan import Loan

class Library:

    def __init__(self):
        # Inicializa o banco de dados LevelDB
        self.db = plyvel.DB('./library_bd', create_if_missing=True)
        for key, serialized_value in self.db:
            # Desserializar o valor
            value = pickle.loads(serialized_value)

            if isinstance(value, Book):
                print(f'Chave: {key.decode("utf-8")}')
                print(f'Valor: {{title: {value.title}, author: {value.author}, status: {value.status}, acessBook: {value.acessBook}, category: {value.category}}}')
                print()  # Linha em branco para separar as saídas
            elif isinstance(value, Loan):
                print(f'Chave: {key.decode("utf-8")}')
                print(f'Valor: {{idLoan: {value.idLoan}, book: {value.book.title}, user: {value.user.name}, loanDate: {value.loanDate}, endDate: {value.endDate}, statusLoan: {value.statusLoan}}}')
                print()  # Linha em branco para separar as saídas
            elif isinstance(value, User):
                print(f'Chave: {key.decode("utf-8")}')
                print(f'Valor: {{idUser: {value.idUser}, name: {value.name}, email: {value.email}, type: {value.type}}}')
                print()  # Linha em branco para separar as saídas
            else:
                print(f'Chave: {key.decode("utf-8")} - Valor não é um objeto do tipo Book, Loan ou User.')

    def addBook(self, book):
        # Serializa o objeto Book e armazena no LevelDB
        self.db.put(f'book:{book.idBook}'.encode(), pickle.dumps(book))
        #for key, value in self.db:
        #    print(f'Chave: {key}, Valor: {value}')

    def addUser(self, user):
        # Serializa o objeto User e armazena no LevelDB
        self.db.put(f'user:{user.idUser}'.encode(), pickle.dumps(user))

    def addLoan(self, loan):
        # Serializa o objeto Loan e armazena no LevelDB
        self.db.put(f'loan:{loan.idLoan}'.encode(), pickle.dumps(loan))

    def searchUser(self, name: str) -> User:
        # Itera sobre os usuários no banco de dados
        for key, value in self.db.iterator(prefix=b'user:'):
            user = pickle.loads(value)
            if user.name == name:
                return user
        return None

    def foundBook(self, title: str) -> Book:
        # Itera sobre os livros no banco de dados
        for key, value in self.db.iterator(prefix=b'book:'):
            book = pickle.loads(value)
            if book.title == title:
                return book
        return None

    def searchLoan(self, idLoan: str) -> Loan:
        # Recupera um empréstimo do banco de dados usando o ID
        loan = self.db.get(f'loan:{idLoan}'.encode())
        if loan:
            return pickle.loads(loan)
        return None

    def close(self):
        # Fecha o banco de dados LevelDB
        self.db.close()
