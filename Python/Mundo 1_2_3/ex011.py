largura = float(input('Qual a largura da sua parede em metros ? '))
altura = float(input('Qual a altura da sua parede em metros ? '))

m2 = largura*altura

print('A sua parede tem dimensão de {}X{}, ou seja {:.2f} m², para pintar essa parede é nescessário {:.2f} litros de tinta.' .format(largura,altura,m2, (m2/2)))
