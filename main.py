# ==========================================
#   Sistema de Estoque - Mini ERP
#   Autor: (coloque seu nome)
#   Linguagem: Python
# ==========================================

produtos = []


def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")

    try:
        preço = float(input("Preço (R$): "))
        quantidade = int(input("Quantidade inicial: "))
    except ValueError:
        print("Erro: preço e quantidade devem ser valores numéricos.")
        return

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preço": preço,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print(f"\nProduto '{nome}' cadastrado com sucesso!\n")


def excluir_produto():
    print("\n--- Excluir Produto ---")
    nome_remove = input("Digite o nome do produto a remover: ")

    for produto in produtos:
        if produto["nome"].lower() == nome_remove.lower():
            produtos.remove(produto)
            print(f"Produto '{nome_remove}' removido!\n")
            return

    print("Produto não encontrado.\n")


def listar_produtos():
    print("\n--- Lista de Produtos Cadastrados ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.\n")
        return

    for i, produto in enumerate(produtos, start=1):
        print(f"\nID: {i}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R${produto['preço']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

        if produto["quantidade"] < 5:
            print("⚠️ Estoque baixo!")

    print()


def menu():
    while True:
        print("====== Sistema de Estoque - Mini ERP ======")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Mostrar relatório de produtos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            excluir_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


menu()
