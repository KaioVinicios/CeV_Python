primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
termos_desejados = 10

while termos_desejados != 0:
    print(termo,' -> ', end='')
    termo += razao
    termos_desejados -= 1 
    if termos_desejados == 0:
        print('PAUSA')
        termos_desejados = int(input('Quantos termos mais devo mostrar ? \nDigite [0] para encerrar.\n'))

print('FIM')

