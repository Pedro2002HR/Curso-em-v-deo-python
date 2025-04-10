soma = cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c,end=' - ')
        soma += c
        cont += 1
print(f'\nA soma de todos os {cont} números multiplos de 3 é {soma}')