'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em  Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.'''

pessoas = {'Nome': 'Lucas', 'Sexo' : 'M', 'Idade' : 26}   #Criação de um dicionario
print(pessoas['Idade'])    #Printando o valor dentro da chave "Idade"
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.') 
print(pessoas.keys())  #Printando todas chaves
print(pessoas.values())  #Printando todos os valores
print(pessoas.items())   #Printando todos os itens, ou seja, chaves e valores

print('=-='*20)
for k in pessoas.keys():  #Usando o for para rodar dentro das chaves
    print(k)
print('=-='*20)
for k in pessoas.values():  #Usando o for para rodar dentro dos valores
    print(k)
print('=-='*20)
for l,k in pessoas.items(): #Rodando por todos os itens e printando suas chaves e valores
    print(f'A chave é {l} e o valor é {k}')
print('=-='*20)

del pessoas['Sexo']  #Deletando a chave "Sexo" e consequentemente seu valor
print(pessoas)
print('=-='*20)

pessoas['Nome'] = 'Carol' #Atribuindo o valor "Carol" para a chave "Nome" do dicionario  'pessoas'  
print(pessoas)
print('=-='*20)

brasil = []    #Adicionando dicionarios dentro da lista Brasil
estado1 = {'UF': 'Rio de Janeiro', 'sigla' : 'RJ'} 
estado2 = {'UF': 'São Paulo', 'sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['sigla']) #Printando o indice 0 a chave "sigla"
print('-=-'*20)

pais = []   #Criando um dicionario e adicionando em uma lista  
estados = {}
for c in range(0,2):
    estados['uf'] = str(input('Digite a uf do estado: '))
    estados['sigla'] = str(input('Digite a sigla do estado: '))
    pais.append(estados.copy())    #O comando ".copy()" copia o dicionario dentro de uma lista sem vincular os dois
for e in pais:
    for v in e.values():
        print(v , end = ' ')
    print()



