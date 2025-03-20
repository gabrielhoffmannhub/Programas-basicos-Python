def adicionar(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "erro"
    return a/b

while True:
    print('===Calculadora Básica===')
    print('1. Adição')
    print('2. Subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. Sair') 

    opcao = int(input('Escolha uma opçâo: '))

    if opcao == 5:
        print('saindo...')
        break

    if opcao not in [1,2,3,4]:
            print ("opção inválida tente novamente")
            continue

    try:
        num1=float(input('Digite o primeiro número: '))
        num2=float(input('Digite o segundo número: '))
    except ValueError:
        print('insira apenas números')
        continue

    if opcao == 1:
        resultado = adicionar(num1, num2)
        print(f"{num1} + {num2} = {resultado}")
    elif opcao == 2:
        resultado = subtrair(num1, num2)
        print(f"{num1} - {num2} = {resultado}")
    elif opcao == 3:
        resultado = multiplicar(num1, num2)
        print(f"{num1} * {num2} = {resultado}")
    elif opcao == 4:
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")