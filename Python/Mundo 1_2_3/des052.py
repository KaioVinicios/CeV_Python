num = int(input('Digite um número: '))

if num == 3:
    print(f'O número {num} é primo.')
elif num%2 == 0 or num%3 == 0:
    print(f'O número {num} não é um número primo.')
else:
    print(f'O número {num} é um número primo.')