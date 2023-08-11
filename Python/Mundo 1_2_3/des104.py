def leiaInt():
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            num = int(num)
            print(f'Você digitou o número {num}.')
            break
        else:
            print('\033[0;31mErro! Digite um número inteiro válido. \033[m')

leiaInt()