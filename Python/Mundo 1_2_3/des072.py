num = 21
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while num not in range(0,21):
    num = int(input('Escolha um número de 0 a 20: '))

print('Você digitou o número {}' .format(extenso[num]))
