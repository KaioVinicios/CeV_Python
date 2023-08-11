from random import randint

num = []

def aleatorio():
    for n in range(1,6):
        num.append(randint(0,999))
    print(f'Os números aleatórios sorteados foram: {num}')

def soma_pares(x):
    soma_p = 0
    for n in x:
        if n % 2 == 0:
            soma_p += n
    print(f'A soma dos números pares contidos em {x} é {soma_p}.')
    num.clear()

aleatorio()
soma_pares(num)

