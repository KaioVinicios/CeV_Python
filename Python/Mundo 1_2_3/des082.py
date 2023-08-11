num_par = []
num_impar = []
numeros = []
cont = 0

while True:
    cont += 1
    numeros.append(int(input(f'Digite o {cont}° número: ')))
    while True:
        menu = input('Quer continuar ? [S/N] ').upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break

for n in range(0, cont):
    num = numeros[n]
    if num % 2 == 0:
        num_par.append(num)
    else:
        num_impar.append(num)    

print(f'Você digitou {numeros} números. Os quais {num_par} são pares e {num_impar} são ímpares.')
