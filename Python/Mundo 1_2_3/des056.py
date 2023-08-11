lista_nomes = []
lista_idades = []
lista_sexos = []

idade_homens = 0
nome_homens = ''
f_abaixo_20 = 0

for c in range(0,2):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F]'))
    lista_nomes.append(nome)
    lista_idades.append(idade)
    lista_sexos.append(sexo)
    if c == 1 and sexo == 'M':
       idade_homens = idade
       nome_homens = nome
    elif sexo == 'M' and idade > idade_homens:
        idade_homens = idade
        nome_homens = nome
    elif 'F' in sexo and idade < 20:
        f_abaixo_20 += 1    

idade_media = (sum(lista_idades)/len(lista_idades))

print(f'A média do grupo é {idade_media:.1f}.')
print(f'O homem mais velho é {nome_homens} e tem {idade_homens} anos.')
print(f'Existem {f_abaixo_20} mulheres abaixo de 20 anos nesse grupo.')


