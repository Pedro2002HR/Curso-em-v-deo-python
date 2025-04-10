print('Analisador de triângulo')
p1 = float(input('Primeiro segmento:'))
p2 = float(input('Segundo segmento:'))
p3 = float(input('Terceiro segmento:'))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Esses segmentos PODEM formar um triângulo.')
    if p1 == p2 == p3:
        print('EQUILÁTERO')
    elif p1 != p2 != p3 != p1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esses segmentos NÃO podem formar um triângulo.')