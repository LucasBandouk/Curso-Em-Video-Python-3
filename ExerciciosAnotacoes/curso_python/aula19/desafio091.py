'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
jogadores = {}
cont = 1
for j in range(1,5):
    jogadores[f'Jogador{j}'] = randint(1,6)
for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado')
print('-='*40)
jogadores_ordenados = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print('   == RANKING DOS JOGADORES ==')
for k,v in jogadores_ordenados.items():
        print(f'    {cont}º lugar: {k} com {v}')
        cont += 1
        