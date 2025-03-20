nomealuno = input('Digite o nome do aluno: ')
notas = []
while True:
    nota = (input('Digite a nota (ou "fim" para finalizar): '))
    if nota.lower() == 'fim':
        break

    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)  
        else:
            print("Nota inválida. A nota deve ser entre 0 e 10.")

    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'fim' para finalizar.")        
        
if len(notas) > 0:  
    media = sum(notas) / len(notas)  
    print(f'Média: {round(media, 2)}')

    if media >= 7:
        print('Situação: Aprovado')
    elif 5 <= media < 7:
        print('Situação: Em recuperação')
    else:
        print('Situação: Reprovado')
else:
 print("Nenhuma nota foi inserida.")