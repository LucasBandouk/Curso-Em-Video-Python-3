'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''


termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contadora = 0
while contadora < 10:
    print(termo, end = '')
    print(' → ' if contadora < 9 else ' Fim', end = '')
    contadora += 1
    termo += razao



