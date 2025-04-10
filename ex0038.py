num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))
if num1 > num2 and num2 < num1:
    print('O primeiro número é maior e o segundo número é menor ')
elif num2 > num1 and num1 < num2:
    print('O segundo número é maior e o primeiro número é menor')
else:
    print('Os dois números são iguais.')