'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='*40)
print('             BANCO BANDOUK')
print('='*40)
valor = int(input('Qual valor você quer sacar? R$'))
while valor != 0:
    nota_50 = valor//50
    valor = valor - (nota_50 * 50)
    if nota_50 != 0:
        print(f'{nota_50} notas de 50,00')
    nota_20 = valor//20
    valor = valor - (nota_20 * 20)
    if nota_20 != 0:
        print(f'{nota_20} notas de 20,00')
    nota_10 = valor//10
    valor = valor - (nota_10 * 10)
    if nota_10 != 0:
        print(f'{nota_10} notas de 10,00')
    nota_1 = valor//1
    valor = valor - (nota_1 * 1)
    if nota_1 != 0:
        print(f'{nota_1} notas de 1,00')
print('='*40)
print('        OBRIGADO, VOLTE SEMPRE!')
print('='*40)