import random
v = 0
e = ''
while True:
    n = int(input('Escolha um número: '))
    while e not in 'PI':
        e = input('Par ou ímpar [P/I]: ').upper()
    n_cpu = random.randint(1,1000)
    if e == 'P':
        if (n_cpu + n) % 2 == 0:
            print(f'VOCÊ VENCEU, o computador escolheu {n_cpu}')
            v += 1
        else:
            print(f'Que pena VOCÊ PERDEU, o computador escolheu {n_cpu}')
            break 
    if e == 'I':
        if (n_cpu + n) % 2 == 1:
            print(f'VOCÊ VENCEU, o computador escolheu {n_cpu}')
            v += 1
        else:
            print(f'Que pena VOCÊ PERDEU, o computador escolheu {n_cpu}')
            break

print(f'Você ganhou o computador {v} vezes.')
