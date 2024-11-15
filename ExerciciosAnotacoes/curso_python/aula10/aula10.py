# CONDIÇOES COMPOSTA

tempo = int(input("Quanto tempo tem seu carro? "))
if tempo <= 3:
    print("Seu carro esta novo")
else:
    print("Seu carro esta antigo")
print("------Fim------")

# CONDIÇOES SIMPLES

nome = str(input("Qual é seu nome? "))
if nome == "Lucas":
    print("Que nome lindo!")
print(f"Bom dia {nome}, Prazer em conhece-lo")

# CONDIÇAO SIMPLIFICADA

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua media foi {media:.1f}")
print("Aprovado!" if media >= 6 else "Reprovado, estude mais!")