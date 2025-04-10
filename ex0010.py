real = float(input('Quanto de dinheiro você tem na carteira ? R$'))
dolar = real / 5.44
euro = real / 6.07
print(f'Com R${real:.2f} você pode comprar R${dolar:.2f} dolares')
print(f'Com R${real:.2f} você pode comprar R${euro:.2f} euros')