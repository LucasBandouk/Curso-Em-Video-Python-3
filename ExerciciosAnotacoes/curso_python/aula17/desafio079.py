'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
while True:
    n = int(input('Digite um valor inteiro para ser gardado na lista: '))
    if n in valores:
        print('Você ja adicionou esse valor na lista antes')
    else:
        valores.append(n)
    decisao = ''
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('Quer adicionar mais valores? [S/N] ')).upper().strip()
    if decisao == 'N':
        break
valores.sort()
print('='*40)
print(f'Você digitou os valores {valores}')
