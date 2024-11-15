distancia = float(input("Qual é a distacia da sua viagem? "))
if distancia <= 200:
    curta = distancia * 0.50
    print(f"Voce esta presetes a começar uma viagem de {distancia:.1f}km")
    print(f"E o preço da sua pasagem sera de R${curta:.2f}")
else:
    longa = distancia * 0.45
    print(f"Voce esta presetes a começar uma viagem de {distancia:.1f}km")
    print(f"E o preço da sua pasagem sera de R${longa:.2f}")
