num_list = []
cont = 1

for c in range(1,6):
    num = int(input(f'Digite o {c}° valor: '))
    num_list.append(num)
    cont -= 1 + c
    if num_list[cont] > num:
        num_list.insert(cont, num)

print(num_list)
