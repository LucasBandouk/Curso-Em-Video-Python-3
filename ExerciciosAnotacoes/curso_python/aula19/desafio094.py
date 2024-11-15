'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

todoscadastros = []
cadastro = {}
resposta = ''
totalidade = 0
mulheres = ''
while resposta != 'N':
    cadastro['sexo'] = ''
    resposta = ''
    cadastro['nome'] = str(input('Nome: '))
    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    if cadastro['sexo'] == 'F':
        mulheres += cadastro['nome'] + ' '
    cadastro['idade'] = int(input('Idade: '))
    todoscadastros.append(cadastro.copy())
    totalidade += cadastro['idade'] 
    cadastro.clear()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? ')).upper().strip()
print('-='*30)
print(f'A) Ao todo temos {len(todoscadastros)} pessoas cadastradas.')
print(f'B) A média de idade é de {totalidade/len(todoscadastros):.2f} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista de pessoas que estão acima da média de idade:')
for a in todoscadastros:
    if a['idade'] >= (totalidade/len(todoscadastros)):
        for k,v in a.items():
            print(f'   {k} = {v};', end = ' ')
        print('')
