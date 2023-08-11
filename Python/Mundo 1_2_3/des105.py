def notas(*n, sit = False):
    notas = []
    dados = {}
    for u in n:
        notas.append(u)
    dados['Total'] = len(notas)
    dados['Maior'] = max(notas)
    dados['Menor'] = min(notas)
    dados['Média'] = (sum(notas))/(len(notas))
    if sit == True:
        if dados['Média'] >= 7.5:
            dados['Situação'] = 'Boa'
        elif dados ['Média'] <= 5.0:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Ruim'
    return dados
    

resp = notas(5.4, 5.6, 10, 8, 9, sit=True)
print(resp)