s = []
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        s.append(c)
print('A soma dos números {} é {}.' .format(s, sum(s)))
