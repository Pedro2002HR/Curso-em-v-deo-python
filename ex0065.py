# FORMA QUE EU FIZ
'''respo = 'S'
maior = menor = média = cont = 0
n = 1
while respo == 'S':
    n = int(input('Digite um número:'))
    respo = str(input('Quer continuar ? [S/N]:')).upper().strip()[0]
    cont += 1
    média += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
média = média / cont
print(f'Você digitou {cont} números')
print(f'O maior valor digitado foi {maior} e o menor é {menor}')
print(f'A média foi {média}')'''



respo = 'Ss'
maior = menor = cont = média = soma = 0
n = 1
while respo in 'Ss ':
    n = int(input('Digite um número:'))
    respo = str(input('Quer continuar ? [S/N]:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maio = n
        elif n < menor:
            menor = n

média = soma/ cont
print(f'Você digitou {cont} números e a média foi {média} ')
print(f'O maior valor é {maior} e o menor foi {menor}')