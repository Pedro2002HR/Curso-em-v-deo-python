larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg*alt
print(f'Sua parede tem a dimensão de {larg}x{alt} é a sua área de {área}m²')
tinta = área / 2
print(f'Para pintar sua parede será necessário {tinta}L de tinta.')