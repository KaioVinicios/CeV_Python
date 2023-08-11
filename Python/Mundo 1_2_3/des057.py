sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    print('Opção inválida. \nTente novamente.')
    sexo = input('Digite seu sexo [M/F] ').upper().strip()[0]

if sexo == 'M':
    print('Sexo masculino registrado com sucesso. Bem vindo!')
else:
    print('Sexo feminino registrado com sucesso. Bem vinda!')