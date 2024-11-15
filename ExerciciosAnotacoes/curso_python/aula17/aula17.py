'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em  Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
acessíveis por chaves individuais.'''

num = [4,8,6,3,4]#Criação de uma lista
print(num)

num[1] = 2      #A posição 1 da lista vai ser alterada pelo valor 2
print(num)

num.append(7)   #Adiciona o valor 7 no final na lista
print(num)

num.sort()      #Ordena a lista em ordem crecente ou alfabetica.
print(num)

num.sort(reverse = True)  #Ordena a lista de forma decrecente
print(num)

print(f'Essa lista tem {len(num)} elementos')  #O comando len conta quantos elementos existe naquela lista

num.insert(2,0)   #Insere na posição 2 o valor 0. 
print(num)

num.pop(2)         #Remove o elemento que esta nqa posição 2. Caso não passe a possição a ser removida, sera removida o valor da ultima posição
print(num)

num.remove(4)      #Remove o primeiro valor 4 que aparece na lista. Apenas o primeiro valor que foi passado mesmo que tenha dois valor 4 pro exemplo, so sera removido um deles
print(num)

if 4 in num:         #Exemplo de uso do if com o metodo remove.
    num.remove(4)
    print(num)
else:
    print('Não achei o valor 4')

valores = []                #Exemplo de começar com a lista vazia e ir preenchendo com o append.
valores.append(5)
valores.append(8)
valores.append(3)

for c, v in enumerate(valores):                               #Printando os valor usando o for e declarando as posições dos valores
    print(f'Na posição {c} encontrei o valor {v}')
print('Pronto, cheguei no final da lista')



lista = []                #Exemplo de começar com a lista vazia e ir preenchendo com o append, mas nesse caso usando o for para solicitar os valor pro usuario
for c in range(0,3):
    lista.append(int(input('Digite um valor para adiciona lo a lista: ')))

for c, v in enumerate(lista):                               #Printando os valor usando o for e declarando as posições dos valores
    print(f'Na posição {c} encontrei o valor {v}')
print('Pronto, cheguei no final da lista')

a = [44,88,65]          #Exemplo que onde mostra que uma variavel pode receber uma lista ja existente.
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')


b[1] = 77    #Ao alterar a posição 1 para o valor 77, as duas listas são alteradas tanto A como B, ↓
print(a)     #pois eles criam uma ligação entre eles. O B não fez apenas uma copia dos valores e sim uma ligação com A 
print(b)

b = a[:1]     #Se tivesse coloca desta forma com os dois pontos indicando quais elementos eu desejo receber de A, ai sim ele apenas copia os valor e não cria a ligação entre os dois
print(a)
print(b)
