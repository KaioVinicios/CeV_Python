num = int(input('Digite um número: '))
escolha = int(input('Escolha uma das bases para conversão: \n[1] para binário \n[2] para octal \n[3] para hexadecimal \nSua escolha: '))

if escolha == 1:
    print('O número {} em binário é igual a {}.' .format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em octal é igual a {}.' .format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal é igual a {}.' .format(num, hex(num)[2:]))
else:
    print('Escolha inválida, tente novamente.')