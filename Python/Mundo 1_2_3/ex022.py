nome = input('Digite seu nome completo: ')

print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minúsculas é: ', nome.lower())
print('Seu nome tem ao todo {} letras.' .format(len(nome.replace(' ', ''))))

partes_nome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.' .format(partes_nome[0], len(partes_nome[0])))
