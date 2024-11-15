'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(*valores):
    n_maior = cont = 0
    print('-='*20)
    print('Analisando os valores passsados...')
    for a in valores:
        print(a, end = ' ',flush=True)
        sleep(0.5)
        if cont == 0:
            n_maior = a
        else:
             if a > n_maior:
                n_maior = a
        cont += 1
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {n_maior}.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
maior(-3,-2,-5)