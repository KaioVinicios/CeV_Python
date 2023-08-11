import random
num = random.randint(0, 10)
resp = int(input('Qual o número de 0 a 10 que o computador escolheu ? '))
tentativas = 1

while resp != num:
    print('Que pena, você errou.')
    tentativas += 1 
    if resp > num:
        print('Menos... Tente novamente.')
    elif resp < num:
        print('Mais... Tente novamente.')
    resp = int(input('Tente outro número: '))

print(f'Parabéns você acertou com {tentativas} tentativas.')
