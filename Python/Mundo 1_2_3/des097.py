def escreva(msg):
    t = len(msg)+4
    print('-'*(len(msg)+4))
    print(f'{msg:^{t}}')
    print('-'*(len(msg)+4))


escreva('Olá mundo!')
escreva('Gustavo Guanabara')
escreva('Curso Python no youtube')
escreva('CeV')