import math
a = int(input('Digite o valor do ângulo: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tang = math.tan(math.radians(a))

print('O seno do ângulo é {:.3f}, o cosseno é {:.3f}, e a tangente é {:.3f}' .format(sen, cos, tang))
