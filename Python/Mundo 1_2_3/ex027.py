nome = input('Digite seu nome: ').strip()

lista_nome = nome.split()

print('Primeiro nome: {}' .format(lista_nome[0]))
print('Ultimo nome {}' .format(lista_nome[len(lista_nome)-1]))
