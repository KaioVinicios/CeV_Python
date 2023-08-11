import math
o = float(input('Qual o valor do cateto oposto ? '))
a = float(input('Qual o valor do cateto adjascente ? '))

h = math.sqrt((o**2)+(a**2))

print('A hipotenusa do seu triângulo retângulo é: {:.3f}' .format(h))
