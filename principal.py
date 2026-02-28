
import Clientes.cliente as cl
import Fornecedores.fornecedores as fn
import os; os.system('cls')


def menuPrincipal():
    while True:
        print("===Escolha como deseja se cadastrar!===")
        print("1 - Menu Cliente")
        print("2 - Menu Fornecedor")
        print("0 - Sair")         

        opcao = input("Escolha a opção: ")
        
        if opcao == "1":
            principalCliente()
        elif opcao == "2":
            principalFornecedor()
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def principalCliente():
    while True:
        os.system('cls')
        print("=== MENU DE Clientes ===")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Pesquisar Cliente")
        print("4 - Alterar Cliente")
        print("5 - Deletar Cliente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        os.system('cls')
        if opcao == "1":
            cl.cadastrarCliente()
        elif opcao == "2":
            cl.listarCliente()
        elif opcao == "3":
            cl.pesquisarCliente()
        elif opcao == "4":
            cl.alterarCliente()
        elif opcao == "5":
           cl.deletarCliente()
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def principalFornecedor():
    while True:
        os.system('cls')
        print("=== MENU DE Fornecedores ===")
        print("1 - Cadastra Fornecedor")
        print("2 - Listar Fornecedores")
        print("3 - Pesquisar Fornecedor")
        print("4 - Alterar Fornecedor")
        print("5 - Deletar Fornecedor")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        os.system('cls')
        if opcao == "1":
           fn.cadastrarFornecedor()
        elif opcao == "2":
           fn.listarFornecedor()
        elif opcao == "3":
            fn.pesquisarFornecedor()
        elif opcao == "4":
            fn.alterarFornecedor()
        elif opcao == "5":
            fn.deletarFornecedor()
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menuPrincipal()