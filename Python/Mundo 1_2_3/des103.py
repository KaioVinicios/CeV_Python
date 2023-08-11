
def ficha(n = '<desconhecido>', g = 0):
    print(f'O jogador {n} fez {g} gol(s).')

    
nome = input('Nome: ') 
gol = input('Gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)
