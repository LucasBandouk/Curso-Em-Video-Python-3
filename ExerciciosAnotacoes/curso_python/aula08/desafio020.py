from random import shuffle
p = input("Digite o nome do primeiro aluno: ")
s = input("Digite o nome do segundo aluno: ")
t = input("Digite o nome do terceiro aluno: ")
q = input("Digite o nome do quarto aluno: ")
l = [p,s,t,q]
shuffle(l)
print("A oredem vai ser : {}".format(l))