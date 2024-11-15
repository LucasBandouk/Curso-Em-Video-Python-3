'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Japão','China','França','Australia','Coreia do Sul','Estados Unidos',
         'Gra Bretanha','Italia','Canada','Hong Kong','Alemanha','Cazaquistao','Africa do Sul',
         'Belgica','Azerbaijao','Romenia','Eslovenia','Servia','Uzbequistao','Brasil')
print('-=' * 20)
print(f'Lista de Times das Olimpiedas: {times}')
print('-=' * 20)
print(f'OS 5 primeiros são: {times[:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O Brasil esta na {times.index('Brasil')+1}º posição')