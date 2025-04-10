nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2) / 2
print(f'Sua notas são {nota1:.1f} e {nota2:.1f}, sua média é {média:.1f}')
if média < 5:
    print('Reprovado. Estude mais.')
elif 7 > média >= 5:
    print('Recuperação. Tenha mais atenção.')
elif média >= 7:
    print('Aprovado. Parabéns.')
