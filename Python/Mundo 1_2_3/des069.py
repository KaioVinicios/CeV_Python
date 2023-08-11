
h = 0
maiores = 0
m_abaixo = 0

while True:
    sexo = input('Digite o sexo [M/F]: ').upper()
    while sexo not in 'MF':
        sexo = input('Digite o sexo [M/F]: ').upper()
    if sexo == 'M':
        h += 1
    idade = int(input('Digite a idade: '))
    while idade not in range(0,200):
        idade = int(input('Digite a idade: '))
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        m_abaixo += 1
    menu = input('Quer continuar [S/N] ? ').upper()
    if menu == 'N':
        break

print(f'''Total de pessoas com mais de 18 anos foi de: {maiores}.
Ao todo temos {h} homens cadastrados.
{m_abaixo} mulheres abaixo dos 20 anos.''')      
