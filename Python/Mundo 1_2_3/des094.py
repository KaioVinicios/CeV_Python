lista_geral = []
pessoa = {}
menu = ''
idades = []
maiores_media = []

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))

    idades.append(pessoa['idade'])
    lista_geral.append(pessoa.copy())
    pessoa.clear()
    while True:
        menu = input('Quer continuar [S/N]: ').upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break

idade_m = (sum(idades))/len(lista_geral)

for c in range(0,len(lista_geral)):
    if lista_geral[c]['idade'] > idade_m:
        maiores_media.append(lista_geral[c])

print('-----------------------------------')
print(f'Foram cadastradas {len(lista_geral)} pessoas.')
print(f'A idade média do grupo foi de {idade_m} anos.')
print(f'Os dados das pessoas mulhereres são: ', end= '')
for c in lista_geral:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='')
print()
print(f'''As pessoas acima da idade média são:
{maiores_media}''')
