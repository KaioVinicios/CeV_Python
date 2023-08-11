linha_0 = []
linha_1 = []
linha_2 = []
geral = []
pares = []

for c in range(0,3):
    linha_0.append(int(input(f'Digite um valor para [0,{c}]: ')))

for c in range(0,3):
    linha_1.append(int(input(f'Digite um valor para [1,{c}]: ')))

for c in range(0,3):
    linha_2.append(int(input(f'Digite um valor para [2,{c}]: ')))

geral.append(linha_0)
geral.append(linha_1)
geral.append(linha_2)

for g in geral:
    for n in g:
        if n % 2 == 0:
            pares.append(n)

stc = 0
for c in range(0,3):
    stc += geral[c][2]

print('+='*30)

print(f''' {linha_0[0]} {linha_0[1]} {linha_0[2]}
 {linha_1[0]} {linha_1[1]} {linha_1[2]}
 {linha_2[0]} {linha_2[1]} {linha_2[2]}''')

print('+='*30)

print(f'''A soma dos valores pares é {sum(pares)}
A soma dos valores da terceira coluna é {stc}
O maior valor da segunda linha é {max(linha_1)}''')
