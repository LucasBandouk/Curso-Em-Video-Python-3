peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso / altura**2

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obsidade Mórbita')
