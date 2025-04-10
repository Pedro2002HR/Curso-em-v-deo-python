dia = int(input('Quantos dias alugados ?'))
km = float(input('Quantos kilômetros rodados:'))
pago = dia*60 + km*0.15
print(f'Você tem que pagar R${pago:.2f}')