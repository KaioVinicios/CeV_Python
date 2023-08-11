import funções
from time import sleep
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = funções.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        funções.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = funções.leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro: dado inválido, tente novamente.\033[m')
    sleep(1)
