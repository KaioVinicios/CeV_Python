
prod = float(input('Qual o preço do produto ? R$ '))

print('O produto que custa R$ {:.2f}, com desconto de 5% vai custar {:.2f}' .format(prod, prod-5*(prod/100)))
