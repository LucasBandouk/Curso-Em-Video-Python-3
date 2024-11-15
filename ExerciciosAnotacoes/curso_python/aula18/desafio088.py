'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint
print('='*40)
print('JOGA NA MEGA SENA'.center(40))
print('='*40)
todosjogos = []
listajogo =[]
quantidade = int(input("Quantos jogos você quer que eu sorteie? "))
for i in range(0,quantidade):
    for l in range(0,6):
        jogo = randint(1,60)
        if jogo not in listajogo:
            listajogo.append(jogo)
        if l == 5:
            listajogo.sort()
            todosjogos.append(listajogo[:])
            listajogo.clear()
print('=-='*3,f'  SORTEANDO {quantidade} JOGOS  ','=-='*3)
for p in range(0,len(todosjogos)):
    print(f'Jogo {p+1}: {todosjogos[p]}')
    sleep(1)
print('=-='*4,'   BOA SORTE!   ','=-='*4)