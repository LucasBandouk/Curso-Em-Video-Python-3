'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2  
c) uma contagem personalizada'''

from time import sleep
def contagem(i,f,p):
    print(f'Contagem de {i} ate {f} de {abs(p)} em {abs(p)}')
    for a in range(i,f+1,p):
        print(a,end =' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-='*15)

print('-='*15)
contagem(1,10,1)
contagem(10,0,-2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passos = 0
while passos == 0:
    passos = int(input('Passos: '))
    if passos == 0:
        print('Digite o numero de passos diferente de 0')
contagem(inicio,fim,passos)