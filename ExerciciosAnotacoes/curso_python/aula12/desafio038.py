primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))
if primeiro > segundo:
    print("O primeio valor é maior")
elif segundo > primeiro:
    print("O segundo numero é maior")
else:
    print('Não existe valor maior, os dois são iguais')