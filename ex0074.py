from random import randint
números = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
print('Os valores sorteados foram:',end='')
for num in  números:
    print(f'{num}',end=' ')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')