linha_0 = []
linha_1 = []
linha_2 = []

for c in range(0,3):
    linha_0.append(int(input(f'Digite um valor para [0,{c}]: ')))

for c in range(0,3):
    linha_1.append(int(input(f'Digite um valor para [1,{c}]: ')))

for c in range(0,3):
    linha_2.append(int(input(f'Digite um valor para [2,{c}]: ')))

print('+='*30)

print(f''' {linha_0[0]} {linha_0[1]} {linha_0[2]}
 {linha_1[0]} {linha_1[1]} {linha_1[2]}
 {linha_2[0]} {linha_2[1]} {linha_2[2]}           
''')