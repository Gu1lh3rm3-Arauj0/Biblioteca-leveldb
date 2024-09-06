# Aspectos e Implementações de Banco de Dados: Biblioteca com Python e LevelDB
Repositório dedicado ao trabalho final da disciplina de Aspectos e Implementações de Banco de Dados. O projeto consiste na implementação de um sistema de gerenciamento de uma biblioteca utilizando Python e o banco de dados NoSQL LevelDB.

## Descrição do Projeto
O objetivo deste projeto é desenvolver uma aplicação para gerenciar uma biblioteca, onde é possível realizar operações como:
- Cadastrar livros.
- Pesquisar livros por título, autor ou disponibilidade.
- Gerenciar empréstimos de livros para usuários.
- Cadastrar informações de usuários da biblioteca.

A escolha do LevelDB como banco de dados para o projeto se deve à sua simplicidade, alto desempenho e facilidade de integração com Python, o que o torna ideal para aplicações que requerem um armazenamento de dados eficiente e rápido.

## Funcionalidades
- Cadastro de Livros: Adicionar novos livros ao acervo da biblioteca.
- Pesquisa de Livros: Buscar título, autor ou disponibilidade.
- Gerenciamento de Empréstimos: Registrar e gerenciar empréstimos de livros a usuários.
- Gerenciamento de Usuários: Adicionar usuários.

## Tecnologias Utilizadas
- Python: Linguagem de programação principal utilizada para desenvolver a aplicação.
- LevelDB: Banco de dados NoSQL utilizado para armazenar os dados da biblioteca.
- Tkinter: Biblioteca de GUI (Interface Gráfica do Usuário) utilizada para criar uma interface amigável.
- WSL (Windows Subsystem for Linux): Utilizado para instalar e executar o LevelDB no ambiente Windows.

## Instalação e Execução
### Pré-requisitos
- Python
- WSL

### Instalação do cmake no WSL
sudo apt update

sudo apt install cmake

### Instalação do compilador C++ no WSL
sudo apt install g++

### Instalação do LevelDB no WSL
git clone --recurse-submodules https://github.com/google/leveldb.git

cd leveldb

git submodule update --init --recursive

mkdir -p build && cd build

cmake ..

make

sudo make install

sudo apt install libleveldb-dev 

### Clone o repositório
git clone https://github.com/Gu1lh3rm3-Arauj0/Biblioteca-AIBD.git 

cd Biblioteca-AIBD

### Instale as dependências do Python
apt install python3-pip

pip install -r requirements.txt

### Execute a aplicação
python main.py

## Estrutura do Projeto
main.py -> Arquivo principal que executa o programa

library_gui.py-> Interface gráfica do usuário (GUI) usando Tkinter

models/ ->  Modelos de dados utilizados pelo sistema

## Contato
- Aline Nataly Lima de Moura
- Guilherme Araújo Mendes de Souza
- Marcelo Machado
- Renata Moura Barreto
- Thamires Lima

## Licença
Este projeto é licenciado sob a Licença MIT.

  
