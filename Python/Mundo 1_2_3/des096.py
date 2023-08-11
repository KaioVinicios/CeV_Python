def área(largura, comprimento):
    a = largura*comprimento
    print(f'A área desse terreno que mede {largura}m de largura e {comprimento}m é igual a: {a:.2f}m².')


l = float(input('Quantos metros de largura mede o terreno ? '))
c = float(input('Quantos metros de comprimento mede o terreno ? '))

área(l, c)
