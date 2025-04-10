listnum = list()
while True:
    num = int(input('Digite um valor:'))
    if num not in listnum:
        listnum.append(num)
    else:
        print('\033[31mNúmero dulicado, não vou adicionar\033[m')
    r = str(input('Quer continuar ?[S/N]:'))
    if r in "Nn":
        break
print('-=-'*30)
listnum.sort()
print(f'Você digitou os valores {listnum}')