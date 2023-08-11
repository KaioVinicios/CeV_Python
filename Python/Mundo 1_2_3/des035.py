print('Analizador de triângulos')
print('-='*20)
r1 = int(input('Digite o primeiro segmento: '))
r2 = int(input('Digite o segundo segmento: '))
r3 = int(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triângulo.')
else: 
    print('Os segmentos acima não podem formar um triângulo.')
    