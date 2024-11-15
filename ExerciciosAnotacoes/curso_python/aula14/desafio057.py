'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

resposta = str(input('Informe seu sexo: [M/F]: ')).upper().strip()
while resposta != 'M' and  resposta != 'F':
    resposta = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()
print(f'Sexo {resposta} registrado com sucesso')
    