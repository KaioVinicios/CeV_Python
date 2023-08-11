menu = ''
cont = 0 
uniques = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in uniques:
        uniques.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado!')    
    while True:
        menu = input('Quer continuar ? [S/N] ').upper().strip()
        if menu in 'SN':
            break
    if menu == 'N':
        break
        

uniques.sort()

print(f'Os valores únicos digitados ordenados em ordem crescente são: {uniques}')
