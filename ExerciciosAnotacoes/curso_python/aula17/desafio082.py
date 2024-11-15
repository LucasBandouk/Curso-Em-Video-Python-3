'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

listacompleta = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    listacompleta.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar ? [S/N] ')).upper().strip()
    if continuar == "N":
        break
print('=-=' * 20)
print(f'A lista completa é {listacompleta}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
    