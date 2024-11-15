'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

vogais = ('A','E','I','O','U')
palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR')
for i in palavras:
    print(f'\nNa palavra {i} temos as vogais: ', end ='')
    for letra in i:
        if  letra in vogais:
            print(f'{letra}',end =' ')
