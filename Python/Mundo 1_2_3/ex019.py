import random

p = input('Digite o nome do primeiro aluno: ')
s = input('Digite o nome do segundo aluno: ')
t = input('Digite o nome do terceiro aluno: ')
q = input('Digite o nome do quarto aluno: ')

e = [p,s,t,q]

print('O aluno escolhido foi {}.' .format(random.choice(e)))
