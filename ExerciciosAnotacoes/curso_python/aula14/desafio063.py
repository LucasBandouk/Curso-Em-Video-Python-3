'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8'''

termos = int(input('Quantos termos você quer mostrar? '))
controladora = 1
primeiro = 0
segundo = 1
while controladora <= termos:
        if controladora == 1:
            print(primeiro, ' → ',end = '')
            controladora += 1
        elif controladora == 2:
            print(segundo, ' → ',end = '')
            controladora += 1
        else:
            seguinte = primeiro + segundo
            print(seguinte, ' → ',end = '')
            primeiro = segundo
            segundo = seguinte
            controladora += 1
print('Fim')

    
 