import tkinter as tk
from tkinter import messagebox
from models.library import Library
from models.library_facade import LibraryFacade

# Configuração da biblioteca e fachada
library = Library()
facade = LibraryFacade()

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Virtual")
        self.root.geometry("800x600")  # Define o tamanho da janela
        self.root.configure(bg="#f0f4f7")  # Define uma cor de fundo suave
        self.user_name = ""  # Variável para armazenar o nome do usuário
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Seja bem-vindo à nossa biblioteca!", font=('Helvetica', 18, 'bold'), bg="#f0f4f7").pack(pady=20)

        # Botões com estilo moderno
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        
        tk.Button(self.root, text="Pesquisar um livro", command=lambda: self.create_user_check_menu(1), **button_style).pack(pady=10)
        tk.Button(self.root, text="Realizar um empréstimo", command=lambda: self.create_user_check_menu(2), **button_style).pack(pady=10)
        tk.Button(self.root, text="Devolver um livro", command=self.return_book_menu, **button_style).pack(pady=10)
        tk.Button(self.root, text="Adicionar um novo livro", command=self.add_book_menu, **button_style).pack(pady=10)
        tk.Button(self.root, text="Sair", command=self.root.quit, **button_style).pack(pady=20)

    def create_user_check_menu(self, action):
        self.clear_frame()
        self.action = action
        tk.Label(self.root, text="Você possui cadastro em nossa biblioteca?", font=('Helvetica', 16, 'bold'), bg="#f0f4f7").pack(pady=20)
        
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Não", command=self.register_user, **button_style).pack(pady=10)
        tk.Button(self.root, text="Sim", command=self.get_user_name, **button_style).pack(pady=10)

    def register_user(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite seu nome completo:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.name_entry.pack(pady=10)
        tk.Label(self.root, text="Digite seu email:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.email_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.email_entry.pack(pady=10)
        tk.Label(self.root, text="Você é:\n  1. Estudante\n  2. Professor", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        
        self.type_var = tk.IntVar()
        tk.Radiobutton(self.root, text="Estudante", variable=self.type_var, value=1, font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        tk.Radiobutton(self.root, text="Professor", variable=self.type_var, value=2, font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Cadastrar", command=self.submit_registration, **button_style).pack(pady=20)

    def submit_registration(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        user_type = "STUDENT" if self.type_var.get() == 1 else "TEACHER"
        if name and email and user_type:
            facade.operation(5, [name, email, user_type], library)
            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
            self.user_name = name  # Armazena o nome do usuário
            self.proceed_action()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def get_user_name(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite seu nome completo:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.name_entry.pack(pady=10)
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Continuar", command=self.set_user_name, **button_style).pack(pady=20)

    def set_user_name(self):
        self.user_name = self.name_entry.get()
        if self.user_name:
            self.proceed_action()
        else:
            messagebox.showerror("Erro", "Por favor, insira seu nome para continuar.")

    def proceed_action(self):
        if self.action == 1:
            self.search_book_menu()
        elif self.action == 2:
            self.loan_book_menu()

    def search_book_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite o título, autor ou categoria do livro que você deseja pesquisar:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.search_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.search_entry.pack(pady=10)
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Pesquisar", command=self.search_book, **button_style).pack(pady=20)

    def search_book(self):
        search_term = self.search_entry.get()
        name_user = self.user_name  # Obtém o nome do usuário armazenado
        data = [name_user, search_term]
        marcador=False

        result = facade.operation(1, data, library)  # Obtém o resultado da pesquisa
        
        if result:            
            if isinstance(result, dict) and result.get('title'):
                marcador=True
                message = (
                    f"Seu livro foi encontrado! Seguem informações:\n"
                    f"Título: {result.get('title', 'Desconhecido')}\n"
                    f"Autor: {result.get('author', 'Desconhecido')}\n"
                    f"Disponível: {result.get('status', 'Desconhecido')}\n"
                    f"Categoria: {result.get('category', 'Desconhecido')}\n"
                )
                messagebox.showinfo("Livro Encontrado", message)
        elif marcador==False:
               message = (
                    "Não encontramos nenhum livro correspondente a sua pesquisa em nossa biblioteca :("
            )
               messagebox.showinfo("Resultado", message)
        else:
            pass
        
        self.create_main_menu()


    def loan_book_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite o título do livro que você deseja emprestar:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.loan_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.loan_entry.pack(pady=10)
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Emprestar", command=self.loan_book, **button_style).pack(pady=20)

    def loan_book(self):
        title = self.loan_entry.get()
        name_user = self.user_name  # Obtém o nome do usuário armazenado
        data = [name_user, title]
        result = facade.operation(2, data, library)  # Obtém o resultado da operação de empréstimo
        if result:
            if isinstance(result, dict) and 'loan_id' in result:
                messagebox.showinfo("Empréstimo", 
                    f"Empréstimo realizado com sucesso!\nCódigo de empréstimo: {result['loan_id']}\n"
                    f"Você tem até o dia {result.get('endDate', 'Desconhecido')} para devolver o livro."
                )
        self.create_main_menu()


    def return_book_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite o código de empréstimo do livro:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        self.return_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.return_entry.pack(pady=10)
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Devolver", command=self.return_book, **button_style).pack(pady=20)

    def return_book(self):
        loan_id = self.return_entry.get()
        data = [loan_id]
        result = facade.operation(3, data, library)
        if result:
            messagebox.showinfo("Devolução", "Livro devolvido com sucesso!")
        else:
            messagebox.showerror("Erro", "Não foi possível devolver o livro. Verifique o código de empréstimo.")
        self.create_main_menu()

    def add_book_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="Digite as informações do livro:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=10)
        tk.Label(self.root, text="Título:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        self.title_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.title_entry.pack(pady=5)
        tk.Label(self.root, text="Autor:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        self.author_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.author_entry.pack(pady=5)
        tk.Label(self.root, text="Categoria:", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        self.category_entry = tk.Entry(self.root, font=('Helvetica', 14), bg="#e0e0e0", borderwidth=2, relief='solid')
        self.category_entry.pack(pady=5)
        tk.Label(self.root, text="Tipo de Acesso:\n  1. Estudante\n  2. Professor\n  3. Ambos", font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        
        self.access_var = tk.IntVar()
        tk.Radiobutton(self.root, text="Estudante", variable=self.access_var, value=1, font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        tk.Radiobutton(self.root, text="Professor", variable=self.access_var, value=2, font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        tk.Radiobutton(self.root, text="Ambos", variable=self.access_var, value=3, font=('Helvetica', 14), bg="#f0f4f7").pack(pady=5)
        
        button_style = {'padx': 20, 'pady': 10, 'font': ('Helvetica', 14), 'bg': '#4CAF50', 'fg': 'white', 'relief': 'flat'}
        tk.Button(self.root, text="Adicionar Livro", command=self.add_book, **button_style).pack(pady=20)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        category = self.category_entry.get()
        access = "STUDENT" if self.access_var.get() == 1 else "TEACHER" if self.access_var.get() == 2 else "BOTH"
        data = [title, author, access, category]
        facade.operation(4, data, library)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
        self.create_main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()  # Corrigir para instanciar a janela principal
    app = LibraryApp(root)
    root.mainloop()  # Inicia o loop principal do Tkinter
