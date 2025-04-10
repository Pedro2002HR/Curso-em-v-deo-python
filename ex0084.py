temp = []
princ = []
maiorp = menorp = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        maiorp = menorp = temp[1]
    else:
        if temp[1] > maiorp:
            maiorp = temp[1]
        if temp[1] < menorp:
            menorp = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar ?[S/N]:')).upper().strip()[0]
    if r == 'N':
        break
print('-=-'*30)
print(f'O total de pessoas cadastradas foi {len(princ)}')
print(f'O maior peso lido foi {maiorp}kg. Peso de ',end='')
for p in princ:
    if p[1] == maiorp:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso lido foi {menorp}kg. Peso de ',end='')
for p in princ:
    if p[1] == menorp:
        print(f'[{p[0]}]',end='')
print()