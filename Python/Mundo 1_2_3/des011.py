
altura = float(input('Qual a altura da sua parede em metros ?'))
largura = float(input('Qual a largura da sua parede em metros ?'))

area = altura*largura
tinta = area/2

print('A sua parede tem {} metros quadrados, portanto é necessário {} litros de tinta para pinta-la.' .format(area,tinta))
