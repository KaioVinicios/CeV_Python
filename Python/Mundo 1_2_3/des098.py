
def contagem(i,f,p):
    num = []
    ff = f
    if p <= -1:
        f -= 1
    elif p >= 1:
        f += 1
    elif p == 0:
        p = 1
    for c in range(i, f, p):
        num.append(c)
    print('+=' * 30)
    print(f'''Contagem de {i} a {ff} de {p} em {p}:
{num} FIM!''')
    print('+='*30)


contagem(1, 10, 1)
contagem(20, 10, -1)

print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
