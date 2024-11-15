from math import hypot
co = float(input("Informe o cateto oposto: "))
ca = float(input("Informe o cateto adjacente: "))
h = hypot(co,ca)
print(" O valor da hipotenusa é {:.2f}".format(h))

'''co = float(input("Informe o cateto oposto: "))
ca = float(input("Informe o cateto adjacente: "))
h = co**2 + ca**2
r = h**(1/2)
print("A hipotenusa é {}".format(r))'''


