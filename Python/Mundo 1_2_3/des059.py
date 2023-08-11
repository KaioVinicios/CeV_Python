menu = 0
num_1 = float(input('Escolha o primeiro valor: '))
num_2 = float(input('Escolha o segundo valor: '))

while menu != 5:
    menu = int(input('''
    Escolha uma opção: 
    [1] SOMAR 
    [2] MULTIPLICAR 
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR
    :::'''))

    if menu == 1:
        print(num_1 + num_2)
    elif menu == 2:
        print(num_1*num_2)
    elif menu == 3:
        print(max(num_1,num_2))
    elif menu == 4:
        num_1 = float(input('Escolha o primeiro valor: '))
        num_2 = float(input('Escolha o segundo valor: '))

if menu == 5:
    print('PROGRAMA FINALIZADO')
    