'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''

def area(a,b):
    resultado = a*b
    print(f'A area de um terreno {a}x{b} é de {resultado}m²')

print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)
