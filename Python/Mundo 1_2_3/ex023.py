num = int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o número {}.' .format(num))
print('Unidade:',u)
print('Denzena:',d)
print('Centena:',c)
print('Milhar:',m)
