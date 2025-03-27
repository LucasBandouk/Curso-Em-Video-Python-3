def aumenta(preco = 0,taxa = 0, formato = False):
    res = preco+(preco*taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0,taxa = 0, formato = False):
    res = preco-(preco*taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco*2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato = False):
    res = preco/2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco = 0, taxa_aumenta = 0, taxa_diminui= 0):
    print("-"*36)
    print("RESUMO DO VALOR".center(36))
    print("-"*36)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco,True)}")
    print(f"Metade do preço: \t{metade(preco,True)}")
    print(f"{taxa_aumenta}% de aumento: \t{aumenta(preco,taxa_aumenta,True)}")
    print(f"{taxa_diminui}% de redução: \t{diminuir(preco,taxa_diminui,True)}")
    print("-"*36)