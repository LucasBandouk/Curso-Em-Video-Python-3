casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é seu salario? "))
anos = int(input("Em quantos anos vai ser o pagamento? ")) 
prestacao = casa / (anos*12)
verificacao = salario * 0.30
if prestacao < verificacao:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2F} \nEmprestimo pode ser \033[0;32mCONCEDIDO\033[m!")
else:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2F} \nEmprestimo \033[0;31mNEGADO\033[m!")