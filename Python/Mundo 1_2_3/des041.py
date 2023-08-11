import datetime

nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.date.today().year

idade = ano_atual - nascimento

if idade <= 9:
    print(f'Atleta mirim com {idade} anos.')
elif idade <= 14:
    print(f'Atleta infantil com {idade} anos.')
elif idade <= 19:
    print(f'Atleta junior com {idade} anos.')
elif idade <= 20:
    print(f'Atleta sênior com {idade} anos.')
else:
    print(f'Atleta master com {idade}.')
    