from math import radians,sin,cos,tan
ângulo = float(input('Digite o ângulo que você deseja:'))
sen = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {sen:.2f}')
cos = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cos:.2f}')
tan = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o TANGENTE de {tan:.2f}')

