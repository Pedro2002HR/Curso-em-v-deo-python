from random import randint
from time import sleep
computador = randint(0,2)
items = ('Papel','Pedra','Tesoura')
print('Jogo jokenpô')
print('Faça sua escolha\n'
      '[0] Papel\n'
      '[1] Pedra\n'
      '[2] Tesoura\n')
jogador = ' '
while jogador not in (0,1,2):
      jogador = int(input('Qual vai ser sua escolha ?'))

print(f'Jogador jogou {items[jogador]}')
print(f'Computador jogou {items[computador]}')
if jogador == computador:
      print('Empate. Vamos jogar novamente!')
elif jogador == 0 and computador == 2:
      print('Computador venceu !')
elif jogador == 0 and computador == 1:
      print('Você venceu !')
elif jogador == 1 and computador == 0:
      print('Computador Venceu !')
elif jogador == 1 and computador == 2:
      print('Você venceu !')
elif jogador == 2 and computador == 0:
      print('Você venceu !')
elif jogador == 2 and computador == 1:
      print('Computador venceu !')
elif computador == 0 and jogador == 2:
      print('Você venceu !')
elif computador == 0 and jogador == 1:
      print('Computador venceu !')
elif computador == 1 and jogador == 0:
      print('Você venceu !')
elif computador == 1 and jogador == 2:
      print('Computador venceu !')
elif computador == 2 and jogador == 0:
      print('Computador venceu !')
elif computador == 2 and jogador == 1:
      print('Jogador venceu !')
