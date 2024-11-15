'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome = '<desconhecido>', gols = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

print('-'*30)
nome = input('Nome do Jogador: ')
gols = input('Numero de Gols: ')
if nome.strip() == '' and gols.isnumeric():
    print(ficha(gols=gols))
elif nome.strip() != '' and not gols.isnumeric():
    print(ficha(nome))
else:
    print(ficha())
