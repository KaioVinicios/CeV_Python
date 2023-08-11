import datetime
nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.date.today().year

if ano_atual-nascimento > 18:
    print('Já deveria ter se alistado no serviço militar. ')
    print('Você deveria estar alistado há {} anos atrás.' .format((ano_atual-nascimento)-18))

elif ano_atual-nascimento < 18:
    print('Ainda não está pronto para se alistar no serviço militar. ')
    print('Você deve se alistar daqui a {} anos. ' .format(18 - (ano_atual-nascimento)))
else: 
    print('Está no tempo certo para se alistar no serviço militar. ')
