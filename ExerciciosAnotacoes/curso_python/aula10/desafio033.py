numero1 = int(input("Digite o primero valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))
# PARA VERIFICAR O MAIOR
if numero1 > numero2 and numero1 > numero3:
    print(f"O maior numero digitado foi {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O maior numero digitado foi {numero2}")
else:
    print(f"O maior numero digitado foi {numero3}")
# PARA VERIFICAR O MENOR
if numero1 < numero2 and numero1 < numero3:
    print(f"O menor numero digitado foi {numero1}")
elif numero2 < numero1 and numero2 < numero3:
    print(f"O menor numero digitado foi {numero2}")
else:
    print(f"O menor numero digitado foi {numero3}")