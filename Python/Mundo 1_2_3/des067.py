r = 0
m = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n <= -1:
        break
    for m in range(0,11):
        r = m*n
        print(f'{n} x {m} = {r}')
        m += 1 
print('Programa encerrado')