'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[],[],[]]
for m in range(0,3):
    for c in range(0,3):
        matriz[m].append(int(input(f'Digite um valor para {m,c}: ')))
print('-=-'*30)
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]', end = '')
    print()