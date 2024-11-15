#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#Minha resolução
'''frase = str(input('Digite uma frase para saber se ela é um palindromo: ')).strip().upper()
dividido = frase.split()
frasec = ''.join(dividido)
quantidade = len(frase)
contrario = ''
n = 1
for c in range (0,quantidade):
    contrario += frase[-n].strip()
    n += 1 
if frasec == contrario:
    print(f'A frase "{frasec}" sendo lida ao contrario "{contrario}" Forma um palindromo')
else:
    print(f'A frase "{frasec}" sendo lida ao contrario "{contrario}" NÃO forma um palindromo')'''

#Resolução sem usar for
frase = str(input('Digite uma frase para saber se ela é um palindromo: ')).strip().upper()
dividido = frase.split()
frasec = ''.join(dividido)
quantidade = len(frase)
contrario = frasec[::-1]
if frasec == contrario:
    print(f'A frase "{frasec}" sendo lida ao contrario "{contrario}" Forma um palindromo')
else:
    print(f'A frase "{frasec}" sendo lida ao contrario "{contrario}" NÃO forma um palindromo')