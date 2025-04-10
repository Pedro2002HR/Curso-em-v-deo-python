preço = float(input('Digite o valor do produto:R$'))
desconto = preço - (preço*5/100)
print(f'O valor do produto é R${preço:.2f}, com desconto de 5% o valor é R${desconto:.2f} ')