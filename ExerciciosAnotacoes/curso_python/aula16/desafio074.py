'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#Minha Resolução ↓

maior = 0
menor = 101
from random import randint
n1 = randint(1,100)
n2 = randint(1,100)
n3 = randint(1,100)
n4 = randint(1,100)
n5 = randint(1,100)
numeros = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados forom: {numeros}')
for c in numeros:
    if c > maior:
        maior = c
print(f'O maior numero sorteado foi {maior}')
for c in numeros:
    if c < menor:
        menor = c
print(f'O menor numero sorteado foi {menor}')

#Resolução do Guanabara ↓

from random import randint
numeros = (randint(1,100), randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print('Os valores sorteados foram: ', end = '')
for n in numeros:
    print(f'{n} ', end = '')
print(f'\nO maior numero sorteado foi {max(numeros)}')
print(f'O menor numero sorteado foi {min(numeros)}')
