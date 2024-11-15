'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []
pos_menor = []
pos_maior = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
for pos,i in enumerate(valores):
    if i == maior:
        pos_maior.append(pos)
    if i == menor:
        pos_menor.append(pos)
print('='*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições {pos_maior}')
print(f'O menor valor digitado foi {min(valores)} nas posições {pos_menor}')
print('='*40)
