numero = int(input("Digite um numero inteiro: "))
print("""Escolha uma das bases para a conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL""")
escolha = int(input('Sua opção:'))
if escolha == 1:
    print(f"O numero {numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}") 
elif escolha == 2:
    print(f"O numero {numero} covertido para OCTAL é igual a {oct(numero)[2:]}")
elif escolha == 3:
    print(f"O numero {numero} covertido para Hexadecimal {hex(numero)[2:]}")
else:
    print("Opção invalida. Tente novamente")