
n = 0
c = -1
total = n

while n != 999:
    n = int(input('Digite um número: [999] para parar.'))
    c += 1
    total += n

total -= 999
print(f'Você digitou {c} números e a soma entre eles é de {total}')
