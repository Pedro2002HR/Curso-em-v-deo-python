from time import sleep
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
usuário = 0
while usuário != 5:
    print('''Escolha uma das opções:    
          [1] Somar
          [2] Multiplicar
          [3] maior valor
          [4] Novos valores
          [5] Sair''')
    usuário = int(input('>>>>>>Opção:'))
    if usuário == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif usuário == 2:
        print(f'{num1} x {num2} = {num1*num2}')
    elif usuário == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior valor é {maior}')
    elif usuário == 4:
        num1 = int(input('Primeiro valor:'))
        num2 = int(input('Segundo valor:'))
    elif usuário == 5:
        print ('Finalizando...')
        sleep(1)
    else:
        print('\033[31mOpção inválida!\033[m')
    print('\033[37m-=-\033[m'*15)
    sleep(1)
print('\033[32mFim. Volte sempre !\033[m')