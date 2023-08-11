estoque = ('Argafort AC-1', 9.00, 'Poty 50KG', 40.00, 'Tubo SOLD 20 mm', 16.00)

print(f'{"Listagem de preços":^40}')
for pos in range(0, len(estoque)):
    if pos % 2 == 0:
        print(f'{estoque[pos]:.<30}', end='')
    else:
        print(f'R${estoque[pos]:>7.2f}')
        