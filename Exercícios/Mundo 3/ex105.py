def notas(*notas, sit=False):
    '''
        → Faz uma analise de notas
    :param notas: Notas a serem a anlisadas
    :param sit: Valor lógico, opcional, que mostra a situação da turma sendo:
            média < 7.0 = BOA
            6.0 < média < 7.0 = RAZOÁVEL
            média > 6.0 = RUIM
    :return: Relátorio com o total de notas, a maior e a menor e a média da turma
    '''
    rel = {}
    rel['Total'] = len(notas)
    rel['Maior Nota'] = sorted(notas,reverse=True)[0]
    rel['Menor Nota'] = sorted(notas)[0]
    rel['Média'] = sum(notas)/len(notas)
    if sit:
        if rel['Média'] >= 7:
            rel['Situação'] = 'BOA'
        elif 6 <= rel['Média'] < 7:
            rel['Situação'] = 'RAZOÁVEL'
        elif rel['Média'] < 6:
            rel['Situação'] = 'RUIM'
    print(rel)

notas(7, 7, 1, sit=True)