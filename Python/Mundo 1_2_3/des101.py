from datetime import *

def voto(nasc):
    ano = datetime.now().year
    idade = ano - nasc
    if idade >= 18 and idade <= 70 :
        resp = 'O voto é obrigatório.'
        return resp
    elif idade <= 16:
        resp = 'Ainda não pode votar.'
        return resp
    else:
        resp = 'O voto é opcional.'
        return resp

resposta = voto(int(input('Digite o seu ano de nascimento: ')))
print(resposta)
