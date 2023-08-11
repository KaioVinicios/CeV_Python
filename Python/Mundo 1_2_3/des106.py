from time import sleep

c = ('\033[m',         # Sem cor
     '\033[0;30;41m',  # Vermelho
     '\033[0;30;42m',  # Azul
     '\033[7;30m');     # Branco


def ajuda(com):
  título(f'Acessando o manual do comando \'{com}\'')
  print(c[3], end='')
  help(com)
  print(c[0], end='')
  sleep(1)


def título(msg, cor=0):
  tam = len(msg) + 4
  print(c[cor], end='')
  print('~'*tam)
  print(f'  {msg}  ')
  print('~'*tam)
  print(c[0], end='')
  sleep(1)

comando = ''
while True:
  título('SISTEMA DE AJUDA PyHELP', 2)
  comando = str(input('Função ou Biblioteca > '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
título('ATÉ LOGO!', 1)
