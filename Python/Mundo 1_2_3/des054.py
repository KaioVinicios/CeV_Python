import datetime

ano_atual = datetime.datetime.now().year 
menores = 0
maiores = 0 

for c in range(0, 7):
    idades = int(input('Digite o ano do seu nascimento: '))
    if ano_atual - idades < 18: 
        menores += 1
    else:
        maiores += 1    

print(f'''Existem {maiores} maiores de idade nesse grupo 
e existem {menores} menores de idade nesse grupo.''')
