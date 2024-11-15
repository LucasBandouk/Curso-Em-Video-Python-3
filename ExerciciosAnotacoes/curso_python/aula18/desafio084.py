'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
dados = []
nome_maiorpeso = []
nome_menorpeso = []
pesomaior = pesomenor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        pesomaior = pesomenor = dados[1]
        nome_maiorpeso.append(dados[0])
        nome_menorpeso.append(dados[0])
    else:
        if dados[1] > pesomaior:
            pesomaior = dados[1]
            nome_maiorpeso.clear()
            nome_maiorpeso.append(dados[0])
        elif dados[1] == pesomaior:
            nome_maiorpeso.append(dados[0])
        elif dados[1] < pesomenor:
            pesomenor = dados[1]
            nome_menorpeso.clear()
            nome_menorpeso.append(dados[0])
        elif dados[1] == pesomenor:
            nome_menorpeso.append(dados[0])
    dados.clear()
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print('=-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso registrado foi {pesomaior}Kg. Peso de {nome_maiorpeso}')
print(f'O menor peso registrado foi {pesomenor}Kg. Peso de {nome_menorpeso}')
