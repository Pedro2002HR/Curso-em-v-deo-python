# MINHA VERSÃO DO PROGRAMA
'''from random import randint
from time import  sleep
computador = randint(0,10)
tentativas = 0
print('\033[1;31;42mJOGO DA ADVINHAÇÃO\033[m')
print('Tente advinhar em qual número o computador pensou... de 0 a 10')
jogador = int(input('Sua escolha:'))
print('\033[1;35mAcert......\033[m')
sleep(0.7)
tentativas += 1
while jogador != computador:
    if jogador > computador:
        jogador = int(input('Um pouco menos... :'))
        tentativas += 1
    if jogador < computador:
        jogador = int(input('Um pouco mais...:'))
        tentativas += 1
    if jogador == computador:
        print('\033[1;35mtooooouuuu !!!\033[m')

print(f'Você errou {tentativas} vez(es)')'''

# VERSÃO DO GUANABARA

from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 a 10')
print('Será consegue adivinhar qual é ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual vai ser seu palpite ?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez ')
        elif jogador > computador:
            print('Menos... tente mais uma vez ')
print(f"Você acetou com {palpites} tentativa(s). Parabéns")


