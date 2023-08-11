termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

c = 10

while c != 0:
    print(termo,' -> ', end='')
    termo += razao
    c -= 1 

print('FIM')

