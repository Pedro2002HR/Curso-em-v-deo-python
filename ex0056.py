somaidade = mulhermenos20 = maioridadehomem = 0
homemvelho = ' '
for c in range(1,5):
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    somaidade += idade
    if sexo in 'Mm':
            
média = somaidade / 4
print(f'A média de idade do grupo é {média}')