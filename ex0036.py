casa = float(input('Valor da casa R$:'))
salário = float(input('Digite seu salário R$:'))
anos = int(input('Quantos anos de financiamento:'))
mínimo = salário * 30/100
financiamento = casa / (anos*12)
print(f'Para comprar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${financiamento:.2f}.')
if mínimo <= financiamento:
    print('\033[31mEmpréstimo negado.\033[m')
else:
    print('\033[36mEmpréstimo consedido.\033[m')

