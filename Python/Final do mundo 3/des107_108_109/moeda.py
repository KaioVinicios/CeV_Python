def moeda(v):
    v = (f'R${v:.2f}')
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


