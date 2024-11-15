# Meu jeito de resolver * da certo, porem fica "pesado"
#termo = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#contadora = 0
#tamanho = (termo + razao) * 10
#for c in range (termo,tamanho,razao):
#    contadora += 1
#    if contadora < 11:
#        print(' ' ,c, '➡', end = ' ')

# Resolução abaixo adaptando com o metodo do professor, uma logica melhor.
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contadora = 0
decimo = termo + (10-1) * razao
for c in range (termo, decimo + razao, razao):
    contadora += 1
    if contadora < 11:
        print(c, end = ' ')
        print('→ ' if contadora < 10 else '', end = '')
