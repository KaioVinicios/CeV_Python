dados = {}
total = 0
gols = []

dados['nome'] = input('Nome do jogador: ')
n_jogos = int(input(f'Quantas partidadas {dados["nome"]} jogou ? '))

for j in range(1, n_jogos + 1):
    gols.append(int(input(f'Quantos gols na partida {j} ? ')))

dados['gols'] = gols    
dados['total'] = sum(gols)

print('+=' * 30)
print(dados)
print('+=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem valor: {v}')

print('+=' * 30)
print(f'{dados["nome"]} jogou {n_jogos} partidas.')
for a in range(0, len(gols)):
    print(f' => No jogo {a + 1} ele marcou {dados["gols"][a]} gols')
print('+=' * 30)
