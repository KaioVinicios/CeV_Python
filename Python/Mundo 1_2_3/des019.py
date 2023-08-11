import random

k = str('Kaio')
j = str('Jacó')
d = str('Dannyel')
c = str('Cauã')

o = (k,j,d,c)

print('Dentre os alunos {}, {}, {} e {}. O escolhido para limpar o quadro foi {}.' .format(k,j,d,c, random.choice(o)))
