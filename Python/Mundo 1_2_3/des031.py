dist = int(input('Digite a distância da viagem em KM: '))

if(dist<=200):
    print('A viagem custará R${:.2f}.' .format(dist*0.5))
else:
    print('A viagem custará R${:.2f}.' .format(dist*0.45))
    