import plyvel
import pickle
from models.library import Library, Book, Loan, User
from collections import defaultdict

def list_db(library):
    db = library.db
    for key, serialized_value in db:
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

def consulta1(library): # Quantas users tem na biblioteca
    count = 0
    db = library.db
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, User):
            count += 1

    print("Consulta 1: Contar quantos usuarios temos em nossa biblioteca")
    print(f"Resultado: Temos {count} usuarios cadastrados em nossa biblioteca!")
    print()

def consulta2(library): #Listar loans ativos
    count = 0
    db = library.db
    print("Consulta 2: Listar empréstimos ativos")
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Loan) and value.statusLoan==True:
            print(f'Chave: {key.decode("utf-8")}')
            print(f'Valor: {{idLoan: {value.idLoan}, book: {value.book.title}, user: {value.user.name}, loanDate: {value.loanDate}, endDate: {value.endDate}, statusLoan: {value.statusLoan}}}\n')
            print()  # Linha em branco para separar as saídas


def consulta3(library): #Listar livros de romance
    count = 0
    db = library.db
    print("Consulta 3: Listar livros de romance")
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Book) and value.category=='Romance':
            print(f'Chave: {key.decode("utf-8")}')
            print(f'Valor: {{title: {value.title}, author: {value.author}, status: {value.status}, acessBook: {value.acessBook}, category: {value.category}}}')
            print()



def consulta4(library): #Listar livros com acesso exclusivo para alunos
    count = 0
    db = library.db
    print("Consulta 4: Listar livros com acesso exclusivo para alunos")
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Book) and value.acessBook=='STUDENT':
            print(f'Chave: {key.decode("utf-8")}')
            print(f'Valor: {{title: {value.title}, author: {value.author}, status: {value.status}, acessBook: {value.acessBook}, category: {value.category}}}')
            print()

    print()

def consulta5(library):
    db = library.db
    latest_loan_date = None
    latest_loan_key = None

    # Iterar sobre o banco de dados para encontrar o empréstimo mais recente
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Loan):
            if latest_loan_date is None or value.loanDate > latest_loan_date:
                latest_loan_date = value.loanDate
                latest_loan_key = key

    print(f"Consulta 5: Data/hora do último empréstimo\nResultado: O ultimo emprestimo na biblioteca foi feito em {latest_loan_date}")
    print()


def consulta6(library):
    db = library.db
    user_loan_counts = defaultdict(int)

    # Iterar sobre o banco de dados para contar empréstimos ativos por usuário
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Loan) and value.statusLoan:  # Verifica se o empréstimo está ativo
            user_loan_counts[value.user.name] += 1

    # Exibir o resultado
    print("Consulta 6: Quantidade de empréstimos ativos por usuário")
    for user_name, count in user_loan_counts.items():
        print(f'Usuário: {user_name} - Empréstimos ativos: {count}')
    print()

def consulta7(library): #Listar livros de disponiveis
    count = 0
    db = library.db
    print("Consulta 7: Listar livros de disponiveis")
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Book) and value.status==True:
            print(f'Chave: {key.decode("utf-8")}')
            print(f'Valor: {{title: {value.title}, author: {value.author}, status: {value.status}, acessBook: {value.acessBook}, category: {value.category}}}')
            print()

def consulta8(library):
    db = library.db
    book_loan_counts = defaultdict(int)

    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Loan):
            book_loan_counts[value.book.title] += 1

    print("Consulta 8: Contar quantas vezes cada livro foi emprestado")
    for book_title, count in book_loan_counts.items():
        print(f'Livro: {book_title} - Número de empréstimos: {count}')
    print()


def consulta9(library):
    db = library.db
    user_loan_counts = defaultdict(int)

    print("Consulta 9: Listar todos os empréstimos de Simba")
    # Iterar sobre o banco de dados para contar empréstimos ativos por usuário
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Loan) and value.user.name=='Simba':
            print(f'Chave: {key.decode("utf-8")}')
            print(f'Valor: {{idLoan: {value.idLoan}, book: {value.book.title}, user: {value.user.name}, loanDate: {value.loanDate}, endDate: {value.endDate}, statusLoan: {value.statusLoan}}}')
            print()  # Linha em branco para separar as saídas

def consulta10(library):
    db = library.db
    categories = set()

    # Iterar sobre o banco de dados para coletar todas as categorias de livros
    for key, serialized_value in db:
        value = pickle.loads(serialized_value)
        if isinstance(value, Book):
            categories.add(value.category)

    sorted_categories = sorted(categories)

    print("Consulta 10: Listar e ordenar todas as categorias de livros")
    for category in sorted_categories:
        print(f'Categoria: {category}')
    print()


if __name__ == "__main__":
    # Crie uma instância da biblioteca
    library = Library()
    # Chame as funções
    #list_db(library)
    consulta1(library)
    print('\n#################################################\n')
    consulta2(library)
    print('\n#################################################\n')
    consulta3(library)
    print('\n#################################################\n')
    consulta4(library)
    print('\n#################################################\n')
    consulta5(library)
    print('\n#################################################\n')
    consulta6(library)
    print('\n#################################################\n')
    consulta7(library)
    print('\n#################################################\n')
    consulta8(library)
    print('\n#################################################\n')
    consulta9(library)
    print('\n#################################################\n')
    consulta10(library)

    library.close()
