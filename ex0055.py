maior = menor = 0
for c in range (1,6):
    peso = float(input(f'Peso da {c}º pessoa kg:'))
    if c == 1:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')