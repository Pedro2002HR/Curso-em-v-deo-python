distância = float(input('Qual a distância da sua viagem ?'))
print(f'Você está prestes a começar uma viagem de {distância}km.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da passagem é R${preço:.2f}')