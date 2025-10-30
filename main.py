
funcionarios = []

def adicionar_funcionario(nome, salario):
    funcionarios.append({"nome": nome, "salario": salario})
    print(f"Funcionário {nome} adicionado com sucesso!")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\n--- Lista de Funcionários ---")
        for f in funcionarios:
            print(f"Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")

def buscar_funcionario(nome):
    encontrados = [f for f in funcionarios if f['nome'].lower() == nome.lower()]
    if encontrados:
        print("\n--- Funcionário encontrado ---")
        for f in encontrados:
            print(f"Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")
    else:
        print(f"Nenhum funcionário encontrado com o nome '{nome}'.")

def calcular_media_salarial():
    if not funcionarios:
        print("Não há funcionários para calcular a média salarial.")
    else:
        media = sum(f['salario'] for f in funcionarios) / len(funcionarios)
        print(f"\nMédia salarial: R$ {media:.2f}")


# Programa Principal
while True:
    print("\n=== MENU ===")
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário por nome")
    print("4 - Calcular média salarial")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do funcionário: ")
        salario = float(input("Salário: R$ "))
        adicionar_funcionario(nome, salario)

    elif opcao == "2":
        listar_funcionarios()

    elif opcao == "3":
        nome = input("Digite o nome para busca: ")
        buscar_funcionario(nome)

    elif opcao == "4":
        calcular_media_salarial()

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
