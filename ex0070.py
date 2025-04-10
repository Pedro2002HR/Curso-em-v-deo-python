totalmil = totalgasto = cont = menor =  0
maisbarato = ''
while True:
    produto = str(input('Produto:')).strip()
    preço = float(input('Preço R$:'))
    escolha = ' '
    totalgasto += preço
    cont += 1
    if preço > 1000:
        totalmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        maisbarato = produto


    while escolha not in 'SN':
        escolha = str(input('Quer continuar ?[S/N]:')).upper().strip()[0]
    if escolha == 'N':break
print(f'O total da compra foi R${totalgasto:.2f}')
print(f'Temos {totalmil} produto(s) custando mais de R$1000 reais. ')
print(f'O produto mais barato foi {maisbarato} custando R${menor:.2f}')
