'''Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while 
no Python.'''


'''for c in range (1,11):
    print(c)
print('Fim')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
print('Fim') '''

'''n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('Fim')'''

'''r = 'S'
n = 1
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Você quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Quantidade de numeros pare {par}')
print(f'Quantidade de numeros impares {impar}')
