'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:         
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.     
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = ''
    while continuar != 'S' and continuar != 'N': 
        continuar = str(input('Quer acresentar mais valores a lista? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('=-'*30)
print(f'Foi acresentado a lista {len(lista)} valores')
print(f'Os valores ordenados de forma decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e incluido na lista')
else:
    print('O Valor 5 não foi digitado e incluido na lista')