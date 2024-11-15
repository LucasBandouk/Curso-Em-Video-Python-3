'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em  Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. 
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

def lin():                 #def vem de definir. Ou seja definir uma função.
    print('=-'*30)         #Essa função foi criada sem precisar passar parametros.

lin()
print('Curso em Video')
lin()

def msg(a):              #Essa função foi criado esperando receber 1 parametro.
    print('=-'*30)
    print(a)
    print('=-'*30)


msg('Criei a funcao')

print('Teste da função soma') 

def soma(a,b):       #Função recebendo dois parametros.
    t = a+b
    print(t)

soma(7,2)
soma(3,1)          #Se você não deixar explicido a qual dos parametros vai ser atribuido ele coloca na mesma seguencia.
soma(a=3,b=1)      #Você pode deixar expicito em qual parametro(variavel) vai ser atribuido o valor.
soma(b=3,a=1)      #Independente da ordem

print('Teste da fução contador sem especificar parametros')

def contador(*num):  #Neta função eu nao especifiquei o numero de parametros, posso passar quantos eu quiser 
    print(len(num))

contador(5,6,4,5,7)
contador(3,7,2)
contador(1)

print('Teste da fução dobra passando lista')

def dobra(l):     #Passsando uma lista como parametro.
    pos = 0
    while pos < len(l):
        l[pos] *= 2
        pos += 1



valores = [6,3,9,0,1,2]
dobra(valores)
print(valores)