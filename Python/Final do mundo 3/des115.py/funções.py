
def leiaint(frase):
    while True:
        try:
            n0 = int(input(frase))
        except (ValueError,TypeError):
            print('\033[31mErro: dado inválido, tente novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar esse número.\033[m')
        else:
            return n0
        

def cabeçalho(txt):
    print('-'*30)
    print(txt.center(30))
    print('-'*30)

def menu(lista):
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-'*30)
    opc = leiaint('Sua opção: ')
    return opc


