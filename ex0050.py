soma = cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º número:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares, e a soma deles foi {soma}')