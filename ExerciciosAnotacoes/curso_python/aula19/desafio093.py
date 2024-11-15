'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for a in range(0,quantidade):
    gols.append(int(input(f'    Quantos gols na partida {a}? ')))
totalgols = sum(gols)
jogador['gols'] = gols[:]
jogador['total'] = totalgols
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for q, g in enumerate(jogador['gols']):
    print(f'    => Na partida {q}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
