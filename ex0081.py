listanum = list()
while True:
    listanum.append(int(input('Digite um número:')))
    r = str(input('Quer continuar ?')).strip().upper()[0]
    if r in "Nn":
        break
listanum.sort(reverse=True)
print(f'O total de números digitados foi {len(listanum)}')
print(f'A ordem dos números digitados é {listanum}')
if 5 in listanum:
    print('O número 5 está na lista')
else:
    print('O número 5 não está presente na lista')
