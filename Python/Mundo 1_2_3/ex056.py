somaidade = 0
mediaidade = 0 
maioridadehomem = 0
nomevelho = ''
mulheres20 = 0

for c in range(1,3):
    print(f'--------{c}º PESSOA--------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ')
    print('-------------------------')
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and maioridadehomem < idade:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

mediaidade = somaidade/4

print(f'A idade média do grupo é de {mediaidade} anos.')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos.')
print(f'Existem {mulheres20} mulheres abaixo dos 20 anos nesse grupo.')
