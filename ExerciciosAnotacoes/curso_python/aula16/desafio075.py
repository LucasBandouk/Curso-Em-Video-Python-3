'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
n3 = int(input('Digite o penultimo numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1,n2,n3,n4)
print(f'Você digitou os numeros {numeros}')
print(f'O valor 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
        print(f'O valor 3 apareceu na {numeros.index(3)+1}º possição')
else:
     print('Não foi digitado nenhum valor 3')
print(f'Os valores pares digitados foi: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c,end=' ')
