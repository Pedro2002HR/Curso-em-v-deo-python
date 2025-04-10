frase = str(input('Digite um frase qualquer:')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes')
print('A letra A apareceu pela primeira vez na posição ',frase.find('A')+1)
print('A letra A apareceu pela ultima vez na posição ',frase.rfind('A')+1)

