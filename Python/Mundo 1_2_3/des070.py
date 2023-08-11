total = 0
menu = ' '
lowlest = 0
acima = 0
contador = 0


while True:
    name = input('Nome do produto: ')
    price = float(input('Preço do produto: R$'))
    total += price
    contador +=1 
    if price > 1000:
        acima += 1 
    if contador == 1 or price < lowlest:
        lowlest = price
        mbarato = name
    while menu not in 'SN':
        menu = input('Quer continuar ? [S/N] ').upper()
    if menu == 'N':
        break    

print(f'''O total da compra foi de R${total:.2f}.
Temos {acima} produtos acima de R$1000,00. 
O produto mais barato foi "{mbarato} custando {lowlest}" ''')