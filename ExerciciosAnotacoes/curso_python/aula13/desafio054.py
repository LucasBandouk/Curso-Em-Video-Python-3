'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range (1,8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E tambem tivemos {menor} pessoas menores de idade')


