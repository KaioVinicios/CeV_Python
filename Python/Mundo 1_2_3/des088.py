from random import *
from time import * 

cont = 0
jogos = []

quant = int(input('Quantos jogos você deseja fazer ? '))

for c in range(0, quant):
    bilhete = []
    while cont != 6:
        num = randint(1,60)
        if num not in bilhete:
            bilhete.append(num)
            cont += 1
    jogos.append(bilhete[:])
    del bilhete
    cont = 0

print('+='*15,'MEGA SENA','+='*15)

for j in range(0, len(jogos)):
    sleep(0.2)
    print(f'Seu {j + 1}° jogo:', jogos[j])

print('+='*15,'BOA SORTE','+='*14)
