frase = str(input('Digite uma palavra: ')).replace(' ', '')

lista = list(frase)
lista.reverse()
frase_invert = ''.join(lista)

print(frase)
print(lista)    

if frase_invert == frase:
    print('A frase escrita é um palíndromo. ')
else:
    print('A frase não é um palindromo. ')
    