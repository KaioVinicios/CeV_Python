import random
num = random.randint(0, 5)
resp = int(input('Qual o número de 0 a 5 que o computador escolheu ? '))

if(num == resp):
    print('Parabéns, você acertou !')
else:
    print('Que pena, você errou.')
