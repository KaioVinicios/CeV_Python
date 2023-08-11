

valor = float(input('Qual o valor do produto ? '))
pagamento = input('Qual a forma de pagamento ? \nDinheiro, 1x no cartão, 2x no cartão ou 3x no cartão. ').upper().strip()

if pagamento == 'DINHEIRO':
    print('Você tem 10%'' de desconto no valor do produto, portanto você terá de pagar {:.2f}' .format(valor - (valor/100)*10))
elif pagamento == '1X NO CARTÃO':
    print('Você tem 5%'' de desconto crédito para 1x, portanto você terá de pagar {:.2f}' .format(valor - (valor/100)*5))
elif pagamento == '2X NO CARTÃO':
    print(f'Você pagará o valor normal do produto de R${valor:.2f}.')
else:
    print('Para pagamento com parcelamento de 3x ou mais há um juros de 20%'', portanto você pagará {:.2f}' .format((valor/100)*20 + valor))
