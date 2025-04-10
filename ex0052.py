num = int(input('Digite um número:'))
somanum = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[34m',end='')
        somanum += 1
    else:
        print('\033[31m',end='')
    print(f'{c}',end=' ')
print(f'\n\033[mO número {num} foi divisível {somanum} vez(es)')
print('Por isso ele é ',end='')
if somanum == 2:
    print('ELE É PRIMO!')
else:
    print('ELE NÃO É PRIMO!')