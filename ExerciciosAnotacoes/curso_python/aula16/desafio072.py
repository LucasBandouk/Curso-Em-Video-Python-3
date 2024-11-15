'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input(f'Digite um numero entre 0 e 20: '))
    if valor >= 0 and valor <= 20:
        print(f'Você digitou o numero {numeros[valor]}')
        resposta = ''
        while resposta != 'S' and resposta != 'N':
            resposta = str(input('Voce quer continuar? [S/N] ')).upper().strip()
        if resposta == 'N':
            break
    else:
        print('O Valor digitado não esta entre 0 e 20. Tente novamente ↓')
