'''frase = str(input('Digite uma frase:')).upper().strip()
separapalavras = frase.strip()
tudojunto = ''.join(separapalavras)
fraseinverso = ''
for letra in range (len(separapalavras) - 1,-1,-1):
    fraseinverso += separapalavras[letra]
print(f'O inverso de {tudojunto} é {fraseinverso}')
if fraseinverso == tudojunto:
    print('Temos um palíndromo!')
else:
    print('Essa frase não é um palíndromo.')'''

# FORMA SIMPLIFICADA DE FAZER O PROGRAMA ACIMA
frase = str(input('Digite uma frase:')).upper().strip()
separafrase = frase.strip()
fraseinverso = separafrase[::-1]
print(f'O inverso de {separafrase} é {fraseinverso}')
if fraseinverso == separafrase:
    print('Temos um palíndromo!')
else:
    print('Essa frase não é um palíndromo.')