cont = 0
lista_temp = []
lista_def = []


while True:
    cont += 1
    lista_temp.append(input(f'Digite o nome da {cont}° pessoa: ').strip())
    lista_temp.append(float(input(f'Digite o peso da {cont}° pessoa: ')))
    lista_def.append(lista_temp[:])
    
    if cont == 1:
        maior = menor = lista_temp[1]

    elif maior < lista_temp[1]:
        maior = lista_temp[1]

    elif menor > lista_temp[1]:
        menor = lista_temp[1]

    del lista_temp[:]

    while True:
        menu = input('Quer continuar [S/N] ? ').upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break


print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso registrado foi {maior} das pessoas: ', end='')
for p in lista_def:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'O menor peso foi de {menor} das pessoas: ', end='')
for p in lista_def:
    if p[1] == menor:
        print(p[0], end=' ')