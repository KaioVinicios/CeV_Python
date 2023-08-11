c = 0 
numeros = []
menu = ''

while True:
    c += 1
    numeros.append(int(input(f'Digite o {c}° número: ')))
    while True:
        menu = input('Quer continuar ? [S/N] ').upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break

numeros.sort(reverse=True)

print(f'''Foram digitados {c} números.
a lista dos valores ordenados de forma decrescente é: {numeros} ''') 

if 5 in numeros:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')      
