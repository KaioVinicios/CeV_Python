print('SEQUÊNCIA DE FIBONACCI')
print('-='*11)

n = int(input('Quantos termos de Fibonacci você quer ? '))
t1 = 0
t2 = 1
cont = 3
t3 = 0

print(f'{t1} -> {t2} -> ', end='')

while cont <= n:
    t3 = t1 + t2    
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1

print('FIM')