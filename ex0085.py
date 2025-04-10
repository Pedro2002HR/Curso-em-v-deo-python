núm = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor:'))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[1].sort()
núm[0].sort()
print('-='*30)
print(f'Os valores pares são: {núm[0]}')
print(f'Os valores ímpares são: {núm[1]}')

