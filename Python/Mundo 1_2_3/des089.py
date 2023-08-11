
geral = []

while True:
    estudante = []
    notas = []
    med = []

    estudante.append(input('Nome do aluno: ').strip())
    notas.append(float(input('Nota 01: ')))
    notas.append(float(input('Nota 02: ')))
    estudante.append(notas[:])
    med.append(sum(notas) / 2)
    estudante.append(med)
    geral.append(estudante[:])

    del notas, estudante, med
    while True:
        menu = input('Quer continuar [S/N] ? ').strip().upper()
        if menu in 'SN':
            break
    if menu == 'N':
        break

print('No. Nome   Média')
for c in range(0,len(geral)):
    print(c,   geral[c][0],   geral[c][2])

while True:
    aluno = int(input('[999] Para encerrar. \nDeseja ver a nota de qual aluno [No.]: '))
    if aluno == 999:
        break
    print(f'As notas de {geral[aluno][0]} são: {geral[aluno][1]}')
