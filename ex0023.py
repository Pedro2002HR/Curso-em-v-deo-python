num = int(input('DIgite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número:')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centeza: {c}')
print(f'Milhar: {m}')