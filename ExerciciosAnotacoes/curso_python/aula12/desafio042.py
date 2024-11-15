print("-=-"*20)
print("Analisador de triangulos")
print("-=-"*20)
primeiro = float(input("Primeiro seguimento: "))
segundo = float(input("Segundo seguimento: "))
terceiro = float(input("Terceiro seguimento: "))
if primeiro + segundo > terceiro and segundo + terceiro > primeiro and primeiro + terceiro > segundo :
    print("Os seguimentos acima podem formar um tringulo")
    if primeiro == segundo and primeiro == terceiro and segundo == terceiro:
        print('Do tipo EQUILÁTERO')
    elif primeiro != segundo and primeiro != terceiro and segundo != terceiro:
        print('Do tipo ESCALENO')
    elif primeiro == segundo != terceiro or primeiro == terceiro != segundo or segundo == terceiro != primeiro:
        print('Do tipo ISÓSCELES')
else:
    print("O seguimentos acima não podem formar um triangulo")
