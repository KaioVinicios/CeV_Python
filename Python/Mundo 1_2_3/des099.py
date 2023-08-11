
def maior(*n):
    print('-='*30)
    print(f'{n}. Foram informados {len(n)} números.')
    print(f'O maior número entre {n} é {max(n)}')
    print('-='*30)


maior(2,4,9,8,7,10)
maior(4,7,0)