# FORMA QUE EU FIZ O EXERCÍCIO
'''lista = list()
listapar = list()
listaimpar = list()
while True:
    num = int(input('Digite um valor:'))
    if num not in lista:
        lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    if num % 2 == 1:
        listaimpar.append(num)
    r = ' '
    while r not in "SN":
        r = str(input('Quer continuar ?')).upper().strip()[0]
    if r == 'N':
        break
print(f'Você digitou os valores {lista}')
print(f'Valores pares:{listapar}')
print(f'Valores ímpares:{listaimpar}')'''


num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar ? [S/N]:'))
    if resp in "Nn":
        break
for i,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares {pares}')
print(f'A lista de ímpares {ímpares}')
