valor = float(input('Qual o valor da casa ? '))
salário = float(input('Qual o seu salário ? '))
tempo = int(input('Em quantos anos pretende pagar ? '))

parcela = valor/(tempo*12)

if parcela <= 30*(salário/100):
    print(f'Empréstimo autorizado, sua prestação será de R${parcela:.2f}')
else:
    print('Empréstimo negado pois seu salário de R${:.2f} corresponde a mais de 30 por cento do valor da parcela.' .format(salário))

