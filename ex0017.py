#ca = float(input('Comprimento do cateto adjacente:'))
#co = float(input('Comprimento do cateto oposto:'))
#hy = ( ca ** 2 + co ** 2 ) ** (1/2)
#print(f'A hypotenusa é {hy:.2f}')

from math import hypot
co = float(input('Comprimento do cateto adjacente:'))
ca = float(input('Comprimento do cateto oposto:'))
hy = hypot(co,ca)
print(f'A hypotenusa é {hy:.2f}')