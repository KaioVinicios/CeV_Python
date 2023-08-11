d = int(input('Quantos dias ficou com o carro ? '))
km = float(input('Quantos quilômetros foram rodados ? '))

v = d*60 + km*0.15

print('O valor total a pagar é de R${:.2f}' .format(v))
