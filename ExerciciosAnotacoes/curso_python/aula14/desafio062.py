'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contadora = 0
final = 10
total = 0
while contadora != final:
    print(termo, end = '')
    print(' → ' if contadora < final-1 else ' Pausa', end = '')
    contadora += 1
    termo += razao
    total += 1
    if contadora == final:
        amais = int(input('\nQuantos termos a mais voce quer mostrar: '))
        contadora = 0
        final = amais
        if amais == 0:
            print(f'Progressão finalizada com {total} termos mostrados')
