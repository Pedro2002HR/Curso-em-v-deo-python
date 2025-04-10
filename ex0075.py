# ESSE PROGRAMA ABAIXO TEM UM ERRO, SE NÃO TIVER UM NÚMERO 3 NA LISTA DE NÚMEROS DIGITADOS
'''num = tuple(int(input('Digite um número:')) for c in range(0,4))
print(f'O número nove aparece {num.count(9)} vez(es)')
print(f'O número 3 apareceu pela primeira vez na posição {num.index(3)+1}')
print('Valores pares digitados foram ',end='')
print({n for n in num if n % 2 == 0},end='')'''
#

num = tuple(int(input('Digite um número:')) for c in range(0,4))
print(f'O número nove aparece {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número três apareceu pela primeira vez na {num.index(3)+1}ª posição')
else:
    print('O valor três não foi digitado nenhuma vez ')
print('Os valores pares digitados foram ',end=' ')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')