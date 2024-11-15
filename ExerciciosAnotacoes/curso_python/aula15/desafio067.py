'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-='*20)
    valor = int(input('Você quer ver a tabuada de qual valor? '))
    print('-='*20)
    if valor < 0:
        break
    cont = 1
    while cont < 11:
        print(f'{valor} X {cont} = {valor * cont}')
        cont += 1
print('Programa de Tabuada encerrado!')
