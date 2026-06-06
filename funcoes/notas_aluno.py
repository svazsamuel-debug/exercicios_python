def notas(*n, sit=False):
    ''' notas(*n, sit = False)
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou maios notas (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações do aluno
    '''
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n)/len(n)
    if sit:
        if aluno['media'] < 6:
            aluno['situação'] = 'Ruim'
        elif 6 <= aluno['media'] < 7:
            aluno['situação'] = 'Razoável'
        else:
            aluno['situação'] = 'Boa'
    return aluno

#Programa Principal
resp = notas(0, 5, 8, 6, sit = True)
print(resp)
