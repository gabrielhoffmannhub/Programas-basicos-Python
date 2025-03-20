def mostrar_menu():
    print("\n=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"descricao": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista!")
        return
    
    print("\nSuas Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['descricao']}")

def marcar_concluida(tarefas):
    ver_tarefas(tarefas)
    if not tarefas:
        return
    
    try:
        indice = int(input("\nDigite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido!")
    except ValueError:
        print("Por favor, digite um número válido!")

def remover_tarefa(tarefas):
    ver_tarefas(tarefas)
    if not tarefas:
        return
    
    try:
        indice = int(input("\nDigite o número da tarefa a ser removida: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida!")
        else:
            print("Número de tarefa inválido!")
    except ValueError:
        print("Por favor, digite um número válido!")

def main():
    tarefas = []
    
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            ver_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("\nObrigado por usar a Lista de Tarefas!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    main()
