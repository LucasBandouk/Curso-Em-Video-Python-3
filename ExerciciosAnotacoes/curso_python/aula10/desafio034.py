salario = float(input("Qual é seu salario? "))
if salario > 1250:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${(salario*0.10)+salario:.2f} agora")
else:
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${(salario*0.15)+salario:.2f} agora")