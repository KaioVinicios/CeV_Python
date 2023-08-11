
lista = []

for c in range(0,5):
    peso = float(input('Digite seu peso: '))
    lista.append(peso)
        
print(f'O maior peso é {max(lista)} e o menor peso é {min(lista)}')