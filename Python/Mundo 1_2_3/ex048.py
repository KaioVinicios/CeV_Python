soma = 0
quant_numeros = 0 

for c in range(1,501,2):
    if c % 3 == 0: 
        quant_numeros += 1
        soma += c 
 
print(f'A soma de todos os {quant_numeros} valores é {soma}')