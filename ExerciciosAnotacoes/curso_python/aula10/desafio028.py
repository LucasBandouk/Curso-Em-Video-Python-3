from random import randrange
from time import sleep
print("-="*30)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-="*30)
pc = randrange(6)
numero = int(input("Em que numero eu pensei? "))
print("PROCESANDO...")
sleep(2)
if numero == pc:
    print("Parabens, voce conseguiu me vencer!")
else:
    print("Errou, nao foi dessa vez")
print(f"O numero era {pc}")