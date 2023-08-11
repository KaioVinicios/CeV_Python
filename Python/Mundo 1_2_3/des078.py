
valores = []

for c in range(1,6):
    valores.append(int(input(f'Digite o {c}° valor: ')))

pos_min = []
pos_max = []
pos = -1 

for c in range(0,5):
    pos += 1
    num = valores[c]
    if num == max(valores):
        pos_max.append(pos)
    elif num == min(valores):
        pos_min.append(pos)


print(f'O maior valor foi {max(valores)} e está na posição {pos_max}. \nO menor valor foi {min(valores)} localizado na posição {pos_min}.')
