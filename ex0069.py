total18 = totalhomens = totalmulher = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F]:')).upper().strip()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        totalmulher += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar ?[S/N]:')).upper().strip()[0]
    if escolha == 'N':
        break
print(f"Total de pessoa(s) maiores de 18 anos {total18}")
print(f'Ao todo temos {totalhomens} homens cadastrados ')
print(f'E temos {totalmulher} mulher(es) com menos de 20 anos ')
























'''total18 = homens = totalmulher = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/f]:')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if idade > 18:
        total18 += 1
    if sexo == 'F' and idade < 20:
        totalmulher += 1
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar ?[S/N]:')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {total18}')
print(f'Ao todo temos {homens} homens cadastrados ')
print(f'E temos {totalmulher} mulher(es) com menos de 20 anos ')'''

