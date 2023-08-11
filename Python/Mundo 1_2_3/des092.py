
dados = {}

dados['Nome'] = input('Nome: ')
dados['idade'] = 2023 - int(input('Data nascimento: '))
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    if (2023 - dados['Contratação']) >= 15:
        dados['Aposentadoria'] = 'Já pode se aposentar'
    else:
        dados['Aposentadoria'] = ((15 - (2023 - dados['Contratação']))) + dados['idade']

for k , v in dados.items():
    print(f'{k} tem o valor: {v}')
