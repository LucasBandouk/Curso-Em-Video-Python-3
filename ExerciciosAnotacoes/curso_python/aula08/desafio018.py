from math import radians,sin,cos,tan
a = float(input("Digite o valor do angulo: "))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print("O seno do angulo é {:.2f}\nO cosseno do angulo é {:.2f}\nA tangente do angulo é {:.2f}".format(s,c,t))