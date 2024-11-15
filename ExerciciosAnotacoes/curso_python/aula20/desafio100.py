'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteia():
    numeros = []
    print('Sorteando 5 valores da lista:',end =' ')
    for a in range(0,5):
        n = randint(1,10)
        print(f'{n}', end = ' ', flush=True)
        sleep(0.5)
        numeros.append(n)
    print('Pronto!')
    return numeros


def somapar(l):
    print(f'Somando os valores pares de {l},', end = ' ')
    totalpar = 0
    for a in l:
        if a % 2 == 0:
            totalpar += a
    print(f'temos {totalpar}')


numeros = sorteia()
somapar(numeros)