'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = contador = 0
escolha = 'S'
while escolha != 'N':
    numero = int(input('Digite um numero inteiro: '))
    if contador == 0:
        maior = menor = numero
    contador += 1    
    soma += numero
    media = soma / contador
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()
print(f'''Você digitou {contador} numeros
A média entre eles foi {media}
Maior valor digitado {maior}
Menor valor digitado {menor}''')

