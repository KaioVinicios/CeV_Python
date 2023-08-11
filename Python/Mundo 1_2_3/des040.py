nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

média = (nota1+nota2)/2

if média >= 7.0:
    print(f'O aluno está aprovado com média {média}.')
elif média <= 4.9:
    print(f'O aluno está reprovado com média {média}.')
else:
    print(f'O aluno está de recuperação com média {média}.')
    