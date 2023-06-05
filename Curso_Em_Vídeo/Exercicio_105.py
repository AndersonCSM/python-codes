# Exercicio_105
def notas(*n, sit=False):
   """
   -> FUNÇÃO NOTAS: avaliar as notas que foram repassadas, sendo quantas forem necessárias
   - n: são as notas a serem repassadas.
   - sit=True  apresenta a situação do aluno de acordo com a média das notas
   """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    
    if sit:
        if r['média'] >=7:
            r['situação'] = 'boa'
        
        elif r['média'] >= 5:
            r['situação'] = 'razoável'
        
        else:
            r['situação'] = 'ruim'

    return r


resp = notas(5.5, 2.6, 9, 8.5, sit = True)
print(resp)
