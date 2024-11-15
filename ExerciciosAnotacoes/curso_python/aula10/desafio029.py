velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    multa = (velocidade - 80) * 7
    print("Multado! Você exedeu o limite permitido que é de 80km/h")
    print(f"Voce deve pagar uma multa de R${multa:.2f}!")
    print("Tenha um bom dia! Dirija com segurança!")