peso = float(input('Qual o seu peso ? '))
altura = float(input('Qual a sua altura ? '))

imc = peso/altura**2
print('Seu índicie de massa corporal é de {:.2f}.' .format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25: 
    print('Você está no peso ideal.')
elif imc >= 25.1 and imc <= 30:
    print('Você está no sobrepeso.')
elif imc >= 30.1 and imc <= 40:
    print('Você está dentro da faixa de obesidade.')
else:
    print('Você está na faixa de obesidade mórbida.')
