# FORMA QUE EU FIZ
'''while True:
    num = int(input('Digite um número para ver sua tabuada:'))
    if num < 0:
        print('\033[31mNúmero negativos não são válidos\033[m')
    else:
        for c in  range  (0,11,1):
            print(f'{num} x {c} = {num*c}')'''

# GUANABARA

while True:
    num = int(input('Digite um número para ver sua tabuada:'))
    print('-'*30)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre !')