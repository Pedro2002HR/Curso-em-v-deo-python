from datetime import date
maioridade = menoridade = totalpessoas =  0
for c in range (1,8):
    anodenascimento = int(input(f'Ano de nascimento da {c}º pessoa:'))
    anoatual = date.today().year
    idade = anoatual - anodenascimento
    if idade >= 21  :
        maioridade += 1
    else:
        menoridade += 1
print(f'O total de pessoas maiores de idade são {maioridade}')
print(f'O total de pessoas menores de idade são {menoridade}')