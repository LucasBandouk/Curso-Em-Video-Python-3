'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.  
C) O maior valor da segunda linha'''

totalpares = totalterceira= 0
matriz = [[],[],[]]
for m in range(0,3):
    for c in range(0,3):
        matriz[m].append(int(input(f'Digite um valor para {m,c}: ')))
print('-=-'*30)
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]', end = '')
        if matriz[i][c] % 2 == 0:
            totalpares += matriz[i][c]
    print()
for l in range(0,3):
    totalterceira += matriz[l][2]
print('-=-'*30)
print(f'A soma dos valores pares é {totalpares}')
print(f'A soma dos valores da terceira coluna é {totalterceira}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')