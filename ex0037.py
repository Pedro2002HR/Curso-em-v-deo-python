num = int(input('Digite um número inteiro:'))
print("[ 1 ] para converter para binário\n"
      "[ 2 ] para converter para octal\n"
      "[ 3 ] para converter para  hexadecimal")
escolha = int(input('Opção:'))
if escolha == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL {hex(num)[2:]}')
else:
    print('Opção inválida! tente novamente.')