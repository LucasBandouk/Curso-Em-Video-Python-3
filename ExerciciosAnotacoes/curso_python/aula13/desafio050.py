soma = 0
for c in range (1,7):
    numeros = int(input(f'Escreva seis numeros inteiro {c}º: '))
    if numeros % 2 == 0:
        soma += numeros 
print(f'A soma somente dos numeros pares digitados foi {soma}')