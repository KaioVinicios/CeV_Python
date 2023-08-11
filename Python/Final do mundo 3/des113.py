def leiaint():
    while True:
        try:
            n0 = int(input('Digite um número inteiro: '))
        except (ValueError,TypeError):
            print('\033[31mErro: dado inválido, tente novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar esse número.\033[m')
        else:
            return n0


def leiafloat():
    while True:
        try:
            n1 = float(input('Digite um número real: '))
        except (ValueError,TypeError):
            print('\033[31mErro: dado inválido, tente novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        else:
            return n1    
        
        
inteiro = leiaint()
real = leiafloat()
print(f'O número inteiro informado foi {inteiro} e o real foi {real}.')
