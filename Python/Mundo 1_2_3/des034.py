salário = float(input('Qual o valor do salário: '))

if(salário>1200.00):
    print('O salário com aumento fica com valor de R${:.2f}.' .format((salário/100)*10+salário))
else: 
    print('O salário com aumento fica com valor de R${:.2f}.' .format((salário/100)*15+salário))
          