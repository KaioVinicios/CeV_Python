import math

ang = float(input('Qual o valor do ângulo ? '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O seu cosseno é {:.3f}. \nO seu seno é {:.3f}. \nA sua tangente é {:.3f}.' .format(cos,sen,tang))
