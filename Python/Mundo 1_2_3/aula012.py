nome = str(input('Qual o seu nome ? ')).lower().strip()

if nome == 'kaio':
    print('Que homi gostoso.')
elif nome in 'lucas guilherme nathan cauã':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Creuza':
    print('Seu nome é de velha.')
else:
    print('Seu nome é normal.')

print(f'Bom dia {nome}')
