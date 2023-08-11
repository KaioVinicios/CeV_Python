
resposta = input('Digite algo:')

print('o tipo primitivo desse valor é:', type(resposta)) 
print('Só tem espaços ?', resposta.isspace())
print('É um número ?', resposta.isnumeric())
print('É alphanumérico ?', resposta.isalnum())
print('Está apenas em maiúsculas ?', resposta.isupper())
print('Está somente espaços ?', resposta.isspace())
print('Está capitalizada ?', resposta.istitle())
