soma = 0
valores = 0
for c in range (0, 501):
    if c % 2 != 0 and c % 3 == 0:
        valores += 1
        soma += c
print(f'A soma de todos os {valores} valores solicitados é {soma}')
