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
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def cadastrar_usuario(self, id, nome, endereco, telefone):
        usuario = Usuario(id, nome, endereco, telefone)
        self.usuarios.append(usuario)

    def cadastrar_livro(self, id, titulo, autor, quantidade):
        livro = Livro(id, titulo, autor, quantidade)
        self.livros.append(livro)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"ID: {usuario.id} | Nome: {usuario.nome} | Endereço: {usuario.endereco} | Telefone: {usuario.telefone}")

    def listar_livros(self):
        for livro in self.livros:
            print(f"ID: {livro.id} | Título: {livro.titulo} | Autor: {livro.autor} | Quantidade: {livro.quantidade}")

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
        print("Livro adicionado com sucesso!")

    def adicionar_usuario(self):
        id = int(input("Digite o ID do usuário: "))
        nome = input("Digite o nome do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        telefone = input("Digite o telefone do usuário: ")

        usuario = Usuario(id, nome, endereco, telefone)
        self.usuarios.append(usuario)
        print("Usuário adicionado com sucesso!")

    def executar(self):
        opcao = 0
        while opcao != 6:
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
        print("6 - Encerrar programa")

if __name__ == "__main__":
    controladora = Controladora()
    controladora.executar()
