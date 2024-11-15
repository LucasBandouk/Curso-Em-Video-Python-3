'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

todos_jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for a in range(0,quantidade):
        gols.append(int(input(f'    Quantos gols na partida {a+1}? ')))
    totalgols = sum(gols)
    jogador['gols'] = gols[:]
    jogador['total'] = totalgols
    todos_jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    continuar = ''
    while continuar != "S" and continuar != "N":
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == "N":
        break
print('-='*31)
print('cod   nome                 gols                 total')
print('-='*31)
for n,a in enumerate(todos_jogadores):
    print(f'{n}', end = '     ')
    for v in a.values():
        print(f'{str(v):<20}',end = ' ')
    print(' ')
while True:
    print('-'*62)
    mostrar = int(input('Digite o cod do jogador para mostar dados (999 para parar): '))
    if mostrar == 999:
        print('<<< PROGRAMA ENCERRADO, VOLTE SEMPRE! >>>')
        break
    elif mostrar >= len(todos_jogadores) or mostrar < 0:
        print(f'Erro! Não existe jogador com o codigo {mostrar}!')
    else: 
        print(f'--- Levantamento do jogador {todos_jogadores[mostrar]['nome']}')
        for q, g in enumerate(todos_jogadores[mostrar]['gols']):
            print(f'    => No jogo {q+1}, fez {g} gols.')
print('-'*62)
