# class Usuario:
#     def __init__(self, id, nome, endereco, telefone):
#         self.id = id
#         self.nome = nome
#         self.endereco = endereco
#         self.telefone = telefone

# class Livro:
#     def __init__(self, id, titulo, autor, quantidade):
#         self.id = id
#         self.titulo = titulo
#         self.autor = autor
#         self.quantidade = quantidade

# class Emprestimo:
#     def __init__(self, id, usuario, livro, data_emprestimo, data_devolucao):
#         self.id = id
#         self.usuario = usuario
#         self.livro = livro
#         self.data_emprestimo = data_emprestimo
#         self.data_devolucao = data_devolucao

# class Controladora:
#     def __init__(self):
#         self.usuarios = []
#         self.livros = []
#         self.emprestimos = []

#     def cadastrar_usuario(self, id, nome, endereco, telefone):
#         usuario = Usuario(id, nome, endereco, telefone)
#         self.usuarios.append(usuario)

#     def cadastrar_livro(self, id, titulo, autor, quantidade):
#         livro = Livro(id, titulo, autor, quantidade)
#         self.livros.append(livro)

#     def listar_usuarios(self):
#         for usuario in self.usuarios:
#             print(f"ID: {usuario.id} | Nome: {usuario.nome} | Endereço: {usuario.endereco} | Telefone: {usuario.telefone}")

#     def listar_livros(self):
#         for livro in self.livros:
#             print(f"ID: {livro.id} | Título: {livro.titulo} | Autor: {livro.autor} | Quantidade: {livro.quantidade}")

#     def adicionar_emprestimo(self, id, usuario, livro, data_emprestimo, data_devolucao):
#         emprestimo = Emprestimo(id, usuario, livro, data_emprestimo, data_devolucao)
#         self.emprestimos.append(emprestimo)

#     def listar_emprestimos(self):
#         for emprestimo in self.emprestimos:
#             print(f"ID: {emprestimo.id} | Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.livro.titulo} | Data de Empréstimo: {emprestimo.data_emprestimo} | Data de Devolução: {emprestimo.data_devolucao}")

#     def adicionar_livro(self):
#         id = int(input("Digite o ID do livro: "))
#         titulo = input("Digite o título do livro: ")
#         autor = input("Digite o nome do autor do livro: ")
#         quantidade = int(input("Digite a quantidade disponível do livro: "))

#         livro = Livro(id, titulo, autor, quantidade)
#         self.livros.append(livro)
#         print("Livro adicionado com sucesso!")

#     def adicionar_usuario(self):
#         id = int(input("Digite o ID do usuário: "))
#         nome = input("Digite o nome do usuário: ")
#         endereco = input("Digite o endereço do usuário: ")
#         telefone = input("Digite o telefone do usuário: ")

#         usuario = Usuario(id, nome, endereco, telefone)
#         self.usuarios.append(usuario)
#         print("Usuário adicionado com sucesso!")

#     def executar(self):
#         opcao = 0
#         while opcao != 6:
#             self.mostrar_menu()
#             opcao = int(input("Digite o número da opção desejada: "))
#             if opcao == 1:
#                 self.listar_livros()
#             elif opcao == 2:
#                 self.listar_usuarios()
#             elif opcao == 3:
#                 self.listar_emprestimos()
#             elif opcao == 4:
#                 self.adicionar_livro()
#             elif opcao == 5:
#                 self.adicionar_usuario()
#             elif opcao == 6:
#                 print("Encerrando programa...")
#             else:
#                 print("Opção inválida!")

#     def mostrar_menu(self):
#         print("")
#         print("1 - Listar livros")
#         print("2 - Listar usuários")
#         print("3 - Listar empréstimos")
#         print("4 - Adicionar livro")
#         print("5 - Adicionar usuário")
#         print("6 - Encerrar programa")

# if __name__ == "__main__":
#     controladora = Controladora()
#     controladora.executar()






import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

class Usuario:
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Livro:
    def __init__(self, id, titulo, autor, quantidade):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

class Emprestimo:
    def __init__(self, id, usuario, livro, data_emprestimo, data_devolucao):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

class Controladora:
    def __init__(self):
        try:
            # Conectar ao banco de dados MySQL
            self.conexao = mysql.connector.connect(
                host='127.0.0.1',
                port='3306',
                user='root',
                password='----',
                database='teca'
            )
            if self.conexao.is_connected():
                print('Conectado ao MySQL.')
                self.cursor = self.conexao.cursor()
            else:
                print('Falha na conexão ao MySQL.')

            # Criar tabela de livros se não existir
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                    id INT PRIMARY KEY,
                    titulo VARCHAR(255),
                    autor VARCHAR(255),
                    quantidade INT
                )
            ''')
            self.conexao.commit()

            self.usuarios = []
            self.livros = []
            self.emprestimos = []

        except Error as e:
            print(f"Erro na conexão ao MySQL: {e}")


    def cadastrar_usuario(self, id, nome, endereco, telefone):
        usuario = Usuario(id, nome, endereco, telefone)
        self.usuarios.append(usuario)

    def cadastrar_livro(self, id, titulo, autor, quantidade):
        livro = Livro(id, titulo, autor, quantidade)
        self.livros.append(livro)

        # Adicionar livro ao banco de dados MySQL
        print(f"Valores a serem inseridos: {id}, {titulo}, {autor}, {quantidade}")
        self.cursor.execute('INSERT INTO livros (id, titulo, autor, quantidade) VALUES (%s, %s, %s, %s)',
                    (id, titulo, autor, quantidade))

        self.conexao.commit()

        print("Livro adicionado com sucesso!")

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"ID: {usuario.id} | Nome: {usuario.nome} | Endereço: {usuario.endereco} | Telefone: {usuario.telefone}")

    def listar_livros(self):
        # Listar livros do banco de dados
        self.cursor.execute('SELECT * FROM livros')
        livros = self.cursor.fetchall()

        if livros:
            for livro in livros:
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Quantidade: {livro[3]}")
        else:
            print("Nenhum livro cadastrado.")

    def adicionar_emprestimo(self, id, usuario, livro, data_emprestimo, data_devolucao):
        emprestimo = Emprestimo(id, usuario, livro, data_emprestimo, data_devolucao)
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        for emprestimo in self.emprestimos:
            print(f"ID: {emprestimo.id} | Usuário: {emprestimo.usuario.nome} | Livro: {emprestimo.livro.titulo} | Data de Empréstimo: {emprestimo.data_emprestimo} | Data de Devolução: {emprestimo.data_devolucao}")

    def adicionar_livro(self):
        id = int(input("Digite o ID do livro: "))
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor do livro: ")
        quantidade = int(input("Digite a quantidade disponível do livro: "))

        livro = Livro(id, titulo, autor, quantidade)
        self.livros.append(livro)

        # Adicionar livro ao banco de dados
        self.cursor.execute('INSERT INTO livros (id, titulo, autor, quantidade) VALUES (?, ?, ?, ?)',
                            (id, titulo, autor, quantidade))
        self.conexao.commit()

        print("Livro adicionado com sucesso!")

    def adicionar_usuario(self):
        id = int(input("Digite o ID do usuário: "))
        nome = input("Digite o nome do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        telefone = input("Digite o telefone do usuário: ")

        usuario = Usuario(id, nome, endereco, telefone)
        self.usuarios.append(usuario)

        print("Usuário adicionado com sucesso!")

    def realizar_emprestimo(self):
        self.listar_usuarios()
        usuario_id = int(input("Digite o ID do usuário para o empréstimo: "))
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)

        if not usuario:
            print("Usuário não encontrado.")
            return

        self.listar_livros()
        livro_id = int(input("Digite o ID do livro para o empréstimo: "))
        livro = next((l for l in self.livros if l.id == livro_id and l.quantidade > 0), None)

        if not livro:
            print("Livro não encontrado ou sem disponibilidade.")
            return

        data_emprestimo = datetime.now().strftime("%Y-%m-%d")
        data_devolucao = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

        emprestimo_id = len(self.emprestimos) + 1
        self.adicionar_emprestimo(emprestimo_id, usuario, livro, data_emprestimo, data_devolucao)

        # Atualiza a quantidade disponível do livro
        livro.quantidade -= 1

        print("Empréstimo realizado com sucesso!")

    def fechar_conexao(self):
        # Fechar a conexão com o banco de dados
        if self.conexao.is_connected():
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")

    def executar(self):
        opcao = 0
        while opcao != 7:
            self.mostrar_menu()
            opcao = int(input("Digite o número da opção desejada: "))
            if opcao == 1:
                self.listar_livros()
            elif opcao == 2:
                self.listar_usuarios()
            elif opcao == 3:
                self.listar_emprestimos()
            elif opcao == 4:
                self.adicionar_livro()
            elif opcao == 5:
                self.adicionar_usuario()
            elif opcao == 6:
                self.realizar_emprestimo()
            elif opcao == 7:
                print("Encerrando programa...")
            else:
                print("Opção inválida!")

    def mostrar_menu(self):
        print("")
        print("1 - Listar livros")
        print("2 - Listar usuários")
        print("3 - Listar empréstimos")
        print("4 - Adicionar livro")
        print("5 - Adicionar usuário")
        print("6 - Realizar empréstimo")
        print("7 - Encerrar programa")

if __name__ == "__main__":
    controladora = Controladora()
    try:
        controladora.executar()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    finally:
        controladora.fechar_conexao()
