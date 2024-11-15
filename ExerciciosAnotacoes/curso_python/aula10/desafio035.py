print("-=-"*20)
print("Analisador de triangulos")
print("-=-"*20)
primeiro = float(input("Primeiro seguimento: "))
segundo = float(input("Segundo seguimento: "))
terceiro = float(input("Segundo seguimento: "))
if primeiro + segundo > terceiro and segundo + terceiro > primeiro and primeiro + terceiro > segundo :
    print("Os seguimentos acima podem formar um tringulo")
else:
    print("O seguimentos acima não podem formar um triangulo")