lista = ('Hambúrguer ', 22.50,
         'pizza', 6.60,
         'suco',5.50,
         'café',2.30,
         'coxinha', 6.00,
         'refrigerante',5.50,
         'Pastel', 6.00,
         'caipirinha',8.00,
         'cerveja',7.00)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
