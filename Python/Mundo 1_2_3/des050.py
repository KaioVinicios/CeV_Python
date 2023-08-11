s = 0 
par = []
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num%2 == 0: 
        par.append(num)
print(sum(par))
