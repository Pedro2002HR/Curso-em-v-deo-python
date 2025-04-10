print(f'\033[36m=====   {'PRÁTICA SHOP':^15}  =====\033[m')
produto = float(input('Preço dos produtos R$:'))
print('[1] Dinheiro ou cheque 10% de desconto\n'
      '[2] À vista no cartão\n'
      '[3] em até 2x no cartão-- preço normal\n'
      '[4] 3x ou mais no cartão-- COM ACRÉSCIMO DE 20% DE JUROS! ')
escolha = int(input('Sua opção de pagamento:'))
if escolha == 1:
    print(f'O Valor do produto com 10% de desconto vai para R${produto - (produto*10/100):.2f} reais.')
elif escolha == 2:
    print(f'O Valor do produto com 5% de desconto vai para R${produto - (produto*5/100):.2f} reais.')
elif escolha == 3:
    dividindo = produto / 2
    print(f'Dividindo o total de R${produto:.2f} reais.')
    print(f'Você paga 2x parcelas de R${dividindo:.2f} reais.')
elif escolha == 4:
    preçojuros = produto + (produto*20/100)
    parcelas = int(input('Quantas vezes você quer parcelar:'))
    dividindo = preçojuros / parcelas
    print(f'Dividindo um total de R${preçojuros:.2f} reais com juros.')
    print(f'Você paga {parcelas}x parcelas de R${dividindo:.2f} reais.')