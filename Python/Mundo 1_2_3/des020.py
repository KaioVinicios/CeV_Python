import random

a = str(input('Digite um aluno: '))
b = str(input('Digite outro aluno: '))
c = str(input('Digite outro aluno: '))
d = str(input('Digite o ultimo aluno do grupo: '))

p = (a,b,c,d)

sorteados = random.sample(p, 4)

print('O primeiro a apresentar será {}, o segundo {}, o terceiro {} e por último {}.' .format(sorteados[0], sorteados[1], sorteados[2], sorteados[3]))
