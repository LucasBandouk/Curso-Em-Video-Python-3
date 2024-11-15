'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from time import sleep
from random import randint
cont = 0
print('-'*40)
print('          Jogo Par ou Ímpar       ')
print('-'*40)
while True:
    print('-='*20)
    escolha = str(input('Você escolhe Par ou Ímpar? (Digite apenas "P" ou "I") ')).upper().strip()
    jogador = int(input('Digite um valor do 1 ao 10: '))
    if jogador > 10 or jogador < 1:
        print(f'Você digitou {jogador} Por favor digite numeros apenas entre 1 e 10.')
        break
    else:
        print('Ok, vamos analisar')
        sleep(2)
    print('-='*20)
    computador = randint(1,10)
    soma = (jogador + computador) % 2
    print(f'''Você Escolheu {'Par' if escolha == 'P' else 'Ímpar'}
Sua jogada {jogador}
Jogada do computador {computador}
Total {computador + jogador}''')
    if escolha == 'P' and soma == 0:
        print('Você venceu!')
        print('Vamos jogar novamente')
        cont += 1
    elif escolha == 'P' and soma != 0:
        print('Você perdeu')
        break
    elif escolha == 'I' and soma == 0:
        print('Você perdeu')
        break
    elif escolha == 'I' and soma != 0:
        print('Você venceu!')
        print('Vamos jogar novamente')
        cont += 1
    else:
        print('Você nao digitou "P" ou "I". Digite novamente.')
print('-='*20)
print(f'Você ganhou {cont} vezes consecutivas.')
        



