'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

listacompleta = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        listacompleta[0].append(n)
    else:
        listacompleta[1].append(n)
listacompleta[0].sort()
listacompleta[1].sort()
print('-=-' * 30)
print(f'Os valores pares digitados foram: {listacompleta[0]}')
print(f'Os valores impares digitados foram: {listacompleta[1]}')
