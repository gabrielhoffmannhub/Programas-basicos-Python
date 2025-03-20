estoque = []

def exibir_menu():
    print("\n=== Controle de Estoque ===")
    print("1. Adicionar produto")
    print("2. Atualizar produto")
    print("3. Remover produto")
    print("4. Exibir estoque")
    print("5. Sair")

def adicionar_produto():
    try:
        nome = input("Digite o nome do produto: ").strip()
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
        estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Erro: Digite apenas números para quantidade e preço!")

def atualizar_produto():
    try:
        nome = input("Digite o nome do produto: ").strip()
        for produto in estoque:
            if produto["nome"].lower() == nome.lower():
                nova_quantidade = int(input("Digite a nova quantidade: "))
                produto["quantidade"] = nova_quantidade
                print(f"Produto '{nome}' atualizado com sucesso!")
                return
        print("Produto não encontrado!")
    except ValueError:
        print("Erro: Digite apenas números para a quantidade!")

def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ").strip()
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print("Produto não encontrado!")

def exibir_estoque():
    if not estoque:
        print("Estoque vazio!")
    else:
        print("\n=== Estoque Atual ===")
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto['nome']} - Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")

def main():
    print("Bem-vindo ao Controle de Estoque!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            atualizar_produto()
        elif opcao == '3':
            remover_produto()
        elif opcao == '4':
            print("\n=== Estoque Atual ===")
            exibir_estoque()
        elif opcao == '5':
            print("Saindo... Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()