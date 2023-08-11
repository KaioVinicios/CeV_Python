
times = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Atlético-PR', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da gama', 'América-MG')

print(f'Os primeiros 5 colocados são {times[0:5]}')
print(f'Os 4 últimos são {times[-1:1:-5]}')
print(f'A lista em ordem alfabética fica: {sorted(times)}')

corin = times.index('Corinthians') + 1

print(f'O Corinthians está na colocação {corin}º')
