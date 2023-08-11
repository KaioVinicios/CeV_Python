
def leiadinheiro(f):
    while True:
        v = input(f).strip().replace(',','.')
        if v.isalpha() or v == '':
            print(f'\033[0;31mO valor "{v}" é inválido, tente novamente.\033[m')
        else:
            return float(v)
