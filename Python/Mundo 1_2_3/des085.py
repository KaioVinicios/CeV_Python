
lista_geral = [[], []]

for c in range(1,8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        lista_geral[0].append(num)
    else:
        lista_geral[1].append(num)

lista_geral[0].sort()
lista_geral[1].sort()

print(f'''Os valores ímpares digitados foram: {lista_geral[0]}
Os valores pares digitados foram {lista_geral[1]}''')
