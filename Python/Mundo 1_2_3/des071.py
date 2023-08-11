
valor = int(input('Quanto você quer sacar ? '))
total = valor
ced = 50
tot_ced = 0

while True:
    if total >= ced:
        total -=ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} de R${ced:.2f}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0 
        if tot_ced == 0:
            break  
