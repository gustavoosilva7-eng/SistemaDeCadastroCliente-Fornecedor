fornecedores = {}


def cadastrarFornecedor():
    cnpj = int(input("CNPJ: "))
    nome = str(input("Nome: "))
    telefone = int(input("Telefone: "))
    email = str(input("Email: "))

    # Armazena o fornecedor 
    fornecedores[cnpj] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    print("Fornecedor cadastrado com sucesso.\n")


def listarFornecedor():
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.\n")
        return
    else:
     for cnpj, dados in fornecedores.items():
        print(
            f"CNPJ: {cnpj} | Nome: {dados['nome']} | "
            f"Telefone: {dados['telefone']} | Email: {dados['email']}"
        )
    print()
    input("Pressione Enter para voltar ao menu...")


def pesquisarFornecedor():
    cnpj = int(input("Informe o CNPJ do fornecedor: "))
    if cnpj in fornecedores:
        print(f"Nome: {fornecedores[cnpj]['nome']}")
        print(f"Telefone: {fornecedores[cnpj]['telefone']}")
        print(f"Email: {fornecedores[cnpj]['email']}\n")
        input("Pressione Enter para voltar ao menu...")
    else:
        print("Fornecedor não encontrado.\n")


def alterarFornecedor():
    cnpj = int(input("Informe o CNPJ do fornecedor para alterar: "))
    if cnpj in fornecedores:
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo email: ")

        fornecedores[cnpj] = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        print("Dados do fornecedor alterados com sucesso.\n")
    else:
        print("Fornecedor não encontrado.\n")


def deletarFornecedor():
    cnpj = int(input("Informe o CNPJ do fornecedor para deletar: "))
    if cnpj in fornecedores:
        del fornecedores[cnpj]
        print("Fornecedor removido com sucesso.\n")
        input("Pressione Enter para voltar ao menu...")
    else:
        print("Fornecedor não encontrado.\n")

        
