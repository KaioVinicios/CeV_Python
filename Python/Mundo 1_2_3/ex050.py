s = 0
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num%2 == 0:
        s += c

print(f'A soma dos números pares escolhidos é {s}') 
