from random import  randint
print('-=-'*15)
print("\033[36mVamos jogar Par ou Impar ?\033[m")
print('-=-'*15)
v = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0,10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar ?')).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total foi {total}",end=' ')
    print('DEU PAR ' if total % 2 == 0 else 'DEU IMPAR !')
    if escolha == 'P':
        if total % 2 == 0:
            v += 1
            print("Você VENCEU !")
        else:
            print('Você PERDEU !')
            break
    if escolha == 'I':
        if total % 2 == 1:
            v += 1
            print('Você VENCEU !')
        else:
            print("Você PERDEU !")
            break
    print('Vamos jogar novamente !')
print('\033[31m=== GAME OVER ====\033[m')
print(f'Você Ganhou {v} vez(es) ' )