print('-='*15,'TABUADA', '-='*15)
num = int(input('Digite um número inteiro para ver sua tabuada de 0 a 100: '))

for c in range(1,101):
    print('{} x {} = {} \n' .format(num, c, num*c))
