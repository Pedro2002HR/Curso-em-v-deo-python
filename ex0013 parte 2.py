preço = float(input('Digite o valor do produto:R$'))
PA = preço - (preço*10/100)
PR = preço + (preço*8/100)
print(f'O valor do produto é R${preço}, com desconto de 10% o valor vai para R${PA:.2f}')
print(f'Comprando esse produto a prazo você tem 8% de taxa , totalizando R${PR:.2f}')
