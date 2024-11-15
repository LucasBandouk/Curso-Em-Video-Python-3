'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

mutiplicação = 1
numero = int(input('Digite um numero para calcular seu Fatorial: '))
print(f'Calculando {numero}!')
while numero != 0:
    mutiplicação *= numero
    print(f'{numero}', end = '')
    print(' x ' if numero > 1 else ' =', end = '')
    numero -= 1
print(f' {mutiplicação}')