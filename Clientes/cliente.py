clientes = {}

def cadastrarCliente():
    cpf = int(input("cpf: "))
    nome = str(input("Nome: "))
    telefone = int(input("Telefone: "))
    email = input("Email: ")
    clientes[cpf] = {"nome": nome, "telefone": telefone, "email": email}
    print("Cliente cadastrado com sucesso.\n")


def listarCliente():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return
    else:  
        for cpf, dados in clientes.items():
         print(
            f"cpf: {cpf} | Nome: {dados['nome']} | Telefone: {dados['telefone']} | Email: {dados['email']}")
    print()
    input("Pressione Enter para voltar ao menu...")


def pesquisarCliente():
    cpf = int(input("Informe o cpf do cliente: "))
    if cpf in clientes:
        print(f"Nome: {clientes[cpf]['nome']}")
        print(f"Telefone: {clientes[cpf]['telefone']}")
        print(f"Email: {clientes[cpf]['email']}\n")
        input("Pressione Enter para voltar ao menu...")
    else:
        print("Cliente não encontrado.\n")


def alterarCliente():
    cpf = int(input("Informe o cpf do cliente para alterar: "))
    if cpf in clientes:
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo email: ")
        clientes[cpf] = {"nome": nome, "telefone": telefone, "email": email}
        print("Dados alterados com sucesso.\n")
    else:
        print("Cliente não encontrado.\n")


def deletarCliente():
    cpf = int(input("Informe o cpf do cliente para deletar: "))
    if cpf in clientes:
        del clientes[cpf]
        print("Cliente removido com sucesso.\n")
        input("Pressione Enter para voltar ao menu...")
    else:
        print("Cliente não encontrado.\n")
        input("Pressione Enter para voltar ao menu...")





