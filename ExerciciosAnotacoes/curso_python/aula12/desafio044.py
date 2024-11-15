print(f'{" Loja do Lucas ":=^40}')
preco = float(input('Preço das compras: '))
print('''FORMA DE PAGAMENTO
[1] À VISTA DINEHIRO/CHEQUE
[2] À VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO tem 20% de juros''')
opcao = int(input('Qual é a opção escolhida? '))
if opcao == 1:
    print(f'Sua compra de R${preco:.2f} reais com desconto ficou R${preco - (preco*10/100):.2f} reais')
elif opcao == 2:
    print(f'Sua compra de R${preco:.2f} reais com desconto ficou R${preco - (preco*5/100):.2f} reais')
elif opcao == 3:
    print(f'Sua compra de R${preco:.2f} reais não tem desconto e será parcelada em 2x de R${preco / 2:.2f} reais ')
elif opcao == 4:
    vezes = int(input("Em quantas parcelas? "))
    comjuros = preco + (preco * 20/100)
    print(f'''Sua compra será parcelada em {vezes}x de R${comjuros / vezes:.2f} reais
Sua compra de R${preco:.2f} reais com juros ficara R${comjuros:.2f} reais ao total''')
else:
    print("Opção INVALIDA tente novamente.")
