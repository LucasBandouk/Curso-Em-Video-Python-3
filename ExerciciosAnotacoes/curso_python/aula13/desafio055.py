#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

'''menor = 10000
maior = 0
for c in range (1,6):
    peso = int(input(f'Peso da {c}º pessoa:'))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior} Kg')
print(f'O menor peso lido foi {menor} kg')'''

menor = 0
maior = 0
for c in range (1,6):
    peso = int(input(f'Peso da {c}º pessoa:'))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior} Kg')
print(f'O menor peso lido foi {menor} kg')

