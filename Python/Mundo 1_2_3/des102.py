
def fatorial(num, show = False):
    """ fatorial() recebe uma variável de número (num) e realizará o cálculo fatorial, enquanto (show) é uma variável que determina se o processo para o cálculo será revelado quando lhe for atribuído o valor booleano True.  
    """
    cont = num
    if show == True:
        print(f'{num}! = ', end=' ')
        for c in range(cont, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:    
                print(f'{c} x ', end='')
    while cont != 1:
        cont -= 1
        num *= cont
    print(num)


fatorial(10, show= True)
help(fatorial)
