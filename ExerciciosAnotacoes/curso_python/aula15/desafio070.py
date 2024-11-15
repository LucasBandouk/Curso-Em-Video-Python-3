'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

preco_barato = preco_total = cont_itens = cont_mais1000 = 0
produto_barato = ''
print('=' * 40)
print('             LOJA BANDOUK')
print('=' * 40)
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if cont_itens == 0 or preco < preco_barato:
        preco_barato = preco
        produto_barato = nome_produto
    preco_total += preco
    if preco > 1000:
        cont_mais1000 += 1
    escolha = ''
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
    cont_itens += 1
    if escolha == 'N':
        break
print('=' * 10, ' FIM DO PROGRAMA ', '=' * 10)
print(f'O total da compra foi R${preco_total:.2f} reais')
print(f'Temos {cont_mais1000} produtos custando mais de R$1.000 reais')
print(f'O produto mais barato foi {produto_barato} que custa R${preco_barato:.2f} reais')