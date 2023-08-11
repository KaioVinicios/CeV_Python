'JOKENPO COM O COMPUTADOR'
import random

print('Jokenpo')
print('-='*30)

escolhas_possíveis = ['PEDRA','PAPEL','TESOURA']

escolha_usuário = input('Escolha pedra, papel ou tesoura: ').upper().strip()
escolha_cpu = random.choice(escolhas_possíveis)

print(f'O usuário escolheu {escolha_usuário} e o computador escolheu {escolha_cpu}.')

if escolha_usuário == escolha_cpu:
    print('Empate!')

if escolha_usuário == 'PEDRA':
    if escolha_cpu == 'TESOURA':
        print('O usuário venceu!')
    else:
        print('O computador venceu!')

if escolha_usuário == 'PAPEL':
    if escolha_cpu == 'PEDRA':
        print('O usuário venceu!')
    else:
        print('O computador venceu!')

if escolha_usuário == 'TESOURA':
    if escolha_cpu == 'PAPEL':
        print('O usuário venceu!')
    else:
        print('O computador venceu!')


