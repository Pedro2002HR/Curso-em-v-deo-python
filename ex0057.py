sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
while not sexo in 'MF':
    sexo = str(input('Opção inválida. Por favor, tente novamente.Sexo [M/F]:')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')
