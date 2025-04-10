from random import randint
from time import sleep
computador = randint(0,5)
print('\033[32m-=\033[m'*30)
print('\033[36mJogo da advinhação. Pensei em um número de 0 a 5, tente advinhar...\033[m')
print('\033[32m-=\033[m'*30)
jogador = int(input('Qual número eu pensei ?'))
print('Pensando...')
sleep(0.7)
if jogador == computador:
    print('Você acertou!! PARABÉNS !')
else:
    print(f'Você errou ! eu pensei no número {computador} não no número {jogador}')

