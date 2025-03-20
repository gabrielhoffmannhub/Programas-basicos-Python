lista = []
i = 2000

while i <= 3200:  
    if i % 7 == 0 and i % 5 != 0:  
        lista.append(i)
    i = i + 1

print(lista)
