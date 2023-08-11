
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))



numeros = (num1, num2, num3, num4)


print(f'O número 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O primeiro número 3 está na posição {numeros.index(3)} da memória.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')
