import random

p = input('Digite o nome do primeiro aluno: ')
s = input('Digite o nome do segundo aluno: ')
t = input('Digite o nome do terceiro aluno: ')
q = input('Digite o nome do quarto aluno: ')

l = [p,s,t,q]

random.shuffle(l)

print('A ordem de escolha é a seguinte: ')
print(l)
