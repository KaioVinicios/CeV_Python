import math 
oposto = float(input('Qual o valor do cateto oposto ? '))
adjacente = float(input('Qual p valor da adjacente ? '))

hipotenusa = math.hypot(oposto,adjacente)

print('Se o valor do cateto oposto é {:.2f} e o adjacente é {:.2f} a hipotenusa mede {:.2f}.' .format(oposto,adjacente,hipotenusa))
