'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    sleep(2)
    print('〰'*22)
    print('''O que você deseja fazer com esses valores?
[1] somar
[2] mutiplicar
[3] maior
[4] novos numeros
[5] encerrar programa''')
    print('〰'*22)
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        print(f'A soma do primeiro e segundo valor é {primeiro+segundo}')
    elif opcao == 2:
        print(f'A mutiplicação do primeiro e do segundo valor é {primeiro*segundo}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O maior valor entre eles é {primeiro}')
        elif segundo > primeiro:
            print(f'O maior valor entre eles é {segundo}')
        else:
            print('Os valores são iguais!')
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    else:
        print('Opção invalida. tente novamente')
print('Programa encerrado.')
