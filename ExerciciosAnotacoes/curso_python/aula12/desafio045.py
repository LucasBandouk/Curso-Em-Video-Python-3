from random import choice
from time import sleep
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é sua jogada? '))
computador = ['PEDRA','PAPEL','TESOURA']
resultado = choice(computador)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*20)
#Escolhendo pedra
if jogada == 0 and resultado == 'PEDRA':
    print('Empatou')
elif jogada == 0 and resultado == 'PAPEL':
    print('O computador ganhou')
elif jogada == 0 and resultado == 'TESOURA':
    print('Você ganhou!')
#Escolhendo papel
elif jogada == 1 and resultado == 'PEDRA':
    print('Você ganhou!')
elif jogada == 1 and resultado == 'PAPEL':
    print('Empatou')
elif jogada == 1 and resultado == 'TESOURA':
    print('O computador ganhou')
#Escolhendo tesoura
elif jogada == 2 and resultado == 'PEDRA':
    print('O computador ganhou')
elif jogada == 2 and resultado == 'PAPEL':
    print('Voê ganhou!')
elif jogada == 2 and resultado == 'TESOURA':
    print('Empatou')
else:
    print('Jogada Invalida. Escolha um numero entre "0, 1 ou 2"')
    print('-=-'*20)
    exit()
print(f'Você escolheu {opcoes[jogada]} e o computador {resultado}')
print('-=-'*20)
