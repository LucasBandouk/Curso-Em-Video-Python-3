d = int(input("Quantos dias foi alugado o carro? "))
km= float(input("Quantos km rodados? "))
t= d*60 + km*0.15
print("O preço total a pagar é de R${:.2f} reais".format(t))