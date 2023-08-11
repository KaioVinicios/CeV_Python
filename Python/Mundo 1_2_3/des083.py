expression = []
a = 0 
f = 0 

inteiro = (input('Digite a expressão: ')).replace(' ', '')

for i in inteiro:
    expression.append(i)

for n in expression:
    if n == '(':
        a += 1
    elif n == ')':
        f += 1

if a == f:
    print(f'A expressão {inteiro} é válida.')
else:
    print(f'A expressão {inteiro} está incorreta.')
