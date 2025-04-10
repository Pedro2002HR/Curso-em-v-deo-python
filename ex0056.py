somaidade = mulhermenos20 = maioridadehomem = 0
homemvelho = ' '
for c in range(1,5):
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    somaidade += idade
    if sexo in 'Mm':
        homemvelho = nome
        maioridadehomem = idade
    if idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
     if sexo in 'Ff':
         if idade < 20:
             mulhermenos20 += 1
            
média = somaidade / 4
print(f'A média de idade do grupo é {média}')
print(f'O nome do Homem mais velho é {homemvelho} com {maioridadehomem} anos')
print('O total de mulheres com menos de 20 anos é {mulhermenos20}')      
