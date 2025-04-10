velocidade = int(input('Qual a velocidade atual do carro ?'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mVocê ultrapassou o limite permitido de 80km/h '
          f'\nVocê terá que pagar uma multa de R${multa:.2f}\033[m')
print('\033[34mTenha um bom dia, dirija com cuidado !\033[m')
