'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
data_atual = datetime.now().year
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = data_atual - int(input('Ano de nascimento: '))
trabalhador['CTPS'] = int(input('Carteira de trabalho (0 se nao tiver): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = (trabalhador['Contratação'] + 30) - (data_atual - trabalhador['Idade'])
print('=-'*20)
for k,v in trabalhador.items():
    print(f'    - {k} tem o valor {v}')
