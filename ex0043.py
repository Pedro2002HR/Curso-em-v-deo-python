peso = float(input('Peso (kg):'))
altura = float(input('Altura (kg):'))
imc = peso / altura**2
print(f'O imc dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal. ')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal.Parabéns!')
elif imc > 25 and imc <= 30:
    print('Você está SOBREPESO.Tenha cuidado.')
elif imc > 30 and imc <= 40:
    print('Você está com OBESIDADE.Procure um médico!')
elif imc > 40:
    print('\033[31mVocê está com OBESIDADE MORBIDA\033[m. PROCURE UM MÉDICO, CUIDE DA SAÚDE.')