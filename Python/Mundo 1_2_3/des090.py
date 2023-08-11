dados = {}

dados['nome'] = str(input('Nome: '))
dados['média'] = float(input('Média: '))

for k, v in dados.items():
    print(f'O {k} é igual a {v}.')

if dados['média'] <= 5.99:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'

print(f'A situação é {dados["situação"]}')
