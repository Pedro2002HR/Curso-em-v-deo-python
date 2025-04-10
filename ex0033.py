a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')



