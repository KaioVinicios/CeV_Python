menu = 'S'
cont = maior = menor = 0
lista_ = []

while menu == 'S':
    num = int(input('Digite um número: '))
    menu = input('Quer continuar ? [S/N] ').upper().strip()
    cont += 1 
    lista_.append(num)
   
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num

print('''Você digitou {} números, e a média foi de {}.
O maior valor foi {} e o menor {}''' .format(cont, (sum(lista_)/cont), maior, menor))

