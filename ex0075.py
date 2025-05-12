


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
