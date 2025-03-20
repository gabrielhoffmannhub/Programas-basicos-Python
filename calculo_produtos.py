def calcular_desconto(quantidade, preco_total):
    if quantidade <= 10:
        return preco_total
    elif quantidade <= 20:
        return preco_total * 0.9  # 10% de desconto
    elif quantidade <= 50:
        return preco_total * 0.8  # 20% de desconto
    else:
        return preco_total * 0.75  # 25% de desconto

while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    
    if nome_produto.lower() == 'sair':
        break
    
    try:
        preco = float(input("Digite o preço unitário do produto: R$"))
        quantidade = int(input("Digite a quantidade comprada: "))
        
        if preco <= 0 or quantidade <= 0:
            print("Preço e quantidade devem ser maiores que zero!")
            continue
        
        preco_total = preco * quantidade
        valor_final = calcular_desconto(quantidade, preco_total)
        
        print("\nResumo da compra:")
        print(f"Produto: {nome_produto}")
        print(f"Quantidade: {quantidade} unidades")
        print(f"Preço unitário: R${preco:.2f}")
        print(f"Valor total sem desconto: R${preco_total:.2f}")
        
        if valor_final < preco_total:
            desconto = ((preco_total - valor_final) / preco_total) * 100
            print(f"Desconto aplicado: {desconto:.0f}%")
        
        print(f"Valor final a pagar: R${valor_final:.2f}")
        print("-" * 40 + "\n")
        
    except ValueError:
        print("Por favor, digite valores numéricos válidos!")
        continue

print("Programa encerrado!")
