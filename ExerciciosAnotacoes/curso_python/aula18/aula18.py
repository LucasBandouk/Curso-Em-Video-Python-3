'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em  Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
acessíveis por chaves individuais.'''

teste = list()                  #Criando lista e adicionado dados a ela.
teste.append('Lucas')
teste.append(26)
print(teste)

galera = []                #Criando uma nova lista e copiando a lista ''teste'' para dentro da lista "galera". 
galera.append(teste[:])
print(galera)

teste[0] = 'Carol'       #Modificando os dados da lista "teste"  e copiando novamente para lsita "galeria".      
teste[1] = 32
galera.append(teste[:])
print(galera)

print('-='*40)

pessoas = [['Lucas',26],['Carol',32],['Jorge',74],['Marcia',63]]
print(pessoas)
print(pessoas[1][1])    #Criando lista "pessoas" e escolhendo printar apenas algumas informações.
print(pessoas[0])
print(pessoas[3][0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-='*40)

turma = []  #Exemplo de programa que coleta dados de diferentes pessoas e printa informações baseadas na idade.
dados = []
totalmenor = totalmaior = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    turma.append(dados[:])
    dados.clear()
for p in turma:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Essa turma tem {totalmaior} maiores de idade e {totalmenor} menores.')
