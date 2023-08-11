speed = int(input('Qual a velocidade do carro em KM/H ? '))

if(speed >= 70):
    print('Você foi multado !')
    print('A multa é de R$07,00 para cada KM/H acima do limite, então sua multa vai custar R${:.2f}.' .format((speed-70)*7))
else:
    print('Você não foi multado.')
    