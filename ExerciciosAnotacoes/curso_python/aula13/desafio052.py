numero = int(input('Digite um numero: '))
acumuladora = 0
for c in range (1, numero + 1):
    resultado = numero % c
    if resultado == 0:
        print('\033[;32m',c,'\033[m', end = ' ')
        acumuladora += 1
    else:
        print('\033[;31m',c,'\033[m', end = ' ')
if acumuladora == 2:
    print('\nO numero nao é primo')
else:
    print('\nO numero é primo')
