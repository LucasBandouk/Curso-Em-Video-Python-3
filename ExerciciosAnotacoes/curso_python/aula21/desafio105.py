''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
 um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*valores,sit = False):
    """
    => Funcao para analisar notas e situacoes de diversos alunos.
    para valores: um ou mais notas dos alunos(pode ser varias)
    para sit: valores opcional, para mostrar ou nao a situacao no aluno.
    return: dicionario com varias informacoes sobre a situcao do aluno.
    """
    ficha = {}
    ficha['total'] = len(valores)
    ficha['maior'] = max(valores)
    ficha['menor'] = min(valores)
    ficha['media'] = sum(valores)/len(valores)
    if sit == True:
        if ficha['media'] < 6:
            ficha['situacao'] = 'Ruim'
        elif 7 > ficha['media'] >= 6:
            ficha['situacao'] = 'Regular'
        else:
            ficha['situacao'] = 'Boa'
    return ficha

resp = notas(5,2.5,10,6.5,sit=True)
print(resp)
help(notas)

