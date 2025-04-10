# Primeiro método
#nome = str(input('Digite seu nome completo:')).strip()
#print('Analisando seu nome...')
#print(f'Seu nome em maiúsculo é {nome.upper()}')
#print(f'Seu nome em minúsculo é {nome.lower()}')
#print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")}')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')


# Segundo método

nome = str(input('Digite seu nome completo:')).strip()
separanome = nome.split()
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')} ')
print(f'Seu primeiro nome é {separanome[0]} e ele tem {len(separanome[0])} letras.')