palavras = ('Mercado','playstation','jogos','Pedro','Milena','Carro','Amor','Paz','Bem financeiramente','Saude',
        'Apartamento')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos--',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')