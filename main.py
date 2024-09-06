from models.library import Library
from models.library_facade import LibraryFacade

#comunicação com o usuário
def main():
    
  library= Library()
  facade = LibraryFacade()
  print(
      'Olá, seja bem-vinde à nossa biblioteca RaMoura!\nO que você deseja fazer?\n'
  )
  acao = 0
  list = []

  while acao < 5:
    #acao será o que o usuário escolher
    acao = int(
        input(
            '  ⓵  Pesquisar um livro\n  ⓶  Realizar um empréstimo\n  ⓷  Devolver um livro\n  ⓸  Adicionar um novo livro\n  ⓹  Sair\n\nDigite aqui o número correspondente: '
        ))
    
    #se o usuario escolher 1 ou 2 sera perguntado se ele possui cadastro
    if acao in [1, 2]:
        cadastro = int(
          input(
              "\nVocê possui cadastro em nossa biblioteca?\n\n  Digite:\n    ⓵  para não\n    ⓶  para sim\n"
          ))

        if cadastro == 1:
            print("Por favor, cadastre-se antes de continuar.\n")
            name_user = input("\nDigite seu nome completo: ")
            email = input("Digite seu email: ")
            tipo = int(
                    input(
                "Você é:\n  ⓵  Estudante\n  ⓶  Professor\nDigite o número correspondente: "
                  ))
            if tipo == 1:
                tipo_str = 'STUDENT'
            elif tipo == 2:
                tipo_str = 'TEACHER'
            list = []
            list = [name_user, email, tipo_str]
            facade.operation(5, list, library)
            print("\nÓtimo! Vamos prosseguir.\n")

      ###########################################################
        #depois de fazer o cadastro se necessario, ele pode prosseguir
        if acao == 1: #pesquisar livro

            name_user = input("\nDigite seu nome completo: ")
            livro_busca = input(
                print(f"Olá {name_user}, qual livro vocẽ deseja pesquisar:\n"))
            data=[name_user, livro_busca]
            facade.operation(1,data, library)  #busca os livros no catalogo externo

        ######################################################
        elif acao == 2: #Emprestimo de livros
            name_user = input("\nDigite seu nome completo: ")
            print(f'\nOlá, {name_user}! Vamos dar inicio ao seu empréstimo.')
            title= input("\nDigite o título do livro que você deseja: ")
            data= [name_user, title]
            #operação de fazer o emprestimo (pode ou nao dar certo)
            facade.operation(2, data, library) 

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")
    
    ######################################################

    elif acao==3: #devolver livro
        print("\nVamos iniciar seu processo de devolução!")
        idLoan= input("\nDigite o código de empréstimo do livro: ")
        data= [idLoan]
        facade.operation(3, data, library) 

    ###########################################################
    elif acao==4: #adicionar livro
        print("\nPara adicionarmos um novo livro, precisamos de algumas informações")
        acessBook: str
        title= input("\nDigite o titulo do livro: ")
        author= input("\nDigite o nome do autor: ")
        acesso = int(
            input(
        "\n    Qual é o tipo de acesso desse livro?\n        ⓵  Estudante\n        ⓶  Professor \n    ⓷   Ambos \nDigite o número correspondente: "
          ))
        if acesso == 1:
            acessBook = 'STUDENT'
        elif acesso == 2:
            acessBook = 'TEACHER'
        else:
            acessBook='BOTH'

        category= input("\nDigite a categoria do livro: ")
        data=[title, author, acessBook, category]
        facade.operation(4, data, library) 
        
    
  print("\nObrigado por visitar nossa biblioteca!\n")

if __name__ == "__main__":
  main()

