lista_geral = []
info_jogador = {}
gols = []

while True:
    info_jogador['nome'] = input('Nome do jogador: ')
    info_jogador['partidas'] = int(input('Jogou quantas partidas: '))
    
    for p in range(1, info_jogador['partidas'] + 1):
        gols.append(int(input(f'Quantos gols na partida {p} ? ')))
    
    info_jogador['total_gols'] = sum(gols)    
    info_jogador['gols'] = gols[:]
    lista_geral.append(info_jogador.copy())
    info_jogador.clear()
    gols.clear()

    while True:
        menu = input('Quer continuar [S/N] ? ').upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break

print(lista_geral)

print('-='*30)
print('  cod    gols    nome total')
for c in range(0,len(lista_geral)):
    print(f'{c:>4}    {lista_geral[c]["gols"]}    {lista_geral[c]["nome"]}    {lista_geral[c]["total_gols"]}')
print('-='*30)

while True:
    j = int(input('Deseja ver os dados de qual jogador ? [999 para parar]'))
    if j == 999:
        break
    if j >= len(lista_geral):
        print(f'''Erro...
O jogador com código {j} não existe, tente novamente.''')
    else:
        print(f'Levantamento do jogador {lista_geral[j]["nome"]}: ')
        for g in range(0,len(lista_geral[j]['gols'])):
            print(f'No jogo {g+1} fez {lista_geral[j]["gols"][g]} gols.')
