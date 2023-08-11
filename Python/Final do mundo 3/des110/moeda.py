def moeda(v):
    v = (f'R${v:.2f}').replace('.',',')
    return v 


def aumentar(v, aumento, show = False):
    v += (v/100)*aumento
    if show == True:
        v = moeda(v)
    return v


def diminuir(v, dimin, show = False):
    v -= (v/100)*dimin
    if show == True:
        v = moeda(v)
    return v


def dobro(v, show = False):
    v *= 2
    if show == True:
        v = moeda(v)
    return v 


def metade(v, show = False):
    v = v/2
    if show == True:
        v = moeda(v)
    return v 


def resumo(valor, porc_a, porc_d):
    print('-'*30)
    print(f'{"Resumo do valor":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{porc_a}% de aumento: \t{aumentar(valor, porc_a, True)}')
    print(f'{porc_d}% de redução: \t{diminuir(valor, porc_d, True)}')
    print('-'*30)

