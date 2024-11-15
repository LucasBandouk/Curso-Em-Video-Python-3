'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.'''

dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input(f'Média de {dicionario['Nome']}: '))
if dicionario['Média'] >= 5 and dicionario['Média'] <7:
    dicionario['Situação'] = 'Recuperação'
elif dicionario['Média'] < 5:
    dicionario['Situação'] = 'Reprovado'
else:
    dicionario['Situação'] = 'Aprovado'
print('=-='*20)
for k,v in dicionario.items():
    print(f'   - {k} é igual a {v}')
