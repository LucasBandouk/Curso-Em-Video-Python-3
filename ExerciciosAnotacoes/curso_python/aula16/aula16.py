'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. 
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.'''

lanches = ('Hamburger','Suco','Pizza','Pudim')
print(lanches[-2])
print(lanches[0])
print(lanches[1:3])
print(lanches[1:])
print(lanches[:2])
print(lanches[-3:])
print(len(lanches))
print('=-' * 40)
for comida in lanches:
    print(f'Vou comer um {comida}')
print('Nossa comi demais')
print('=-' * 40)
for cont in range(0, len(lanches)):
    print(lanches[cont])
print('=-' * 40)
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')
print('=-' * 40)
print(sorted(lanches))
a = (1, 8, 7) 
b = (3, 7, 5, 7, 6, 8)
c = a + b
print(c)
print(len(c))
print(c.count(7))
print(c.index(8))
pessoa = ('Lucas', 26, 'M', 96)
print(pessoa)
del(pessoa) #Deleta a tupla ou qualquer outra coisa.