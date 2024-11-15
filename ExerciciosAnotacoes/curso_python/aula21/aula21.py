help(print)                     #Comando help mostra como aquela função que esta entre parenteses funciona
help(input)
print(input.__doc__)            #Este comando de print, função, __doc__, tambem mostra como a função funciona

print('~~'*60)



def contador(i,f,p):                        #Aqui eu fiz uma documentação para ensinar como a função que eu criei finciona assim que eu chamar ela no help. tem que estar entre 3 aspas dulpas.
    """"
    Faz contagem e mostra na tela         
    Função criado pelo Lucas

    """
    c = i
    while c <= f:
        print(f'{c}', end ='')
        c+= 1 
    print('Fim!')
    
contador(2,5,6)
help(contador)


print('~~'*60)

def soma(a=0,b=1,c=1):          #Ja defini os valores dos parametros na função, se eu não passar os paramentros na chamada da função, ele vai usar os valores que eu defini.
    resultado = a + b + c         #Nesta função ele aceita de 0 ate 3 parametros. Se eu passar o valor do parametro na chamada da função ele substitui aquele valor que eu ja havia defido na função.
    print(f'O resultado da soma vale {resultado}')

soma(2,2)
soma()

print('~~'*60)

def escopo():            
    x = 9        #Esta variavel x só existe apenas aqui no escopo local desta função.
    chocolate = 74  #Mesmo ja existindo uma variavel global chamada chocolate uma nao tem nada haver com a outra. Ao criar uma variavel no escopo da função, ele so exite aqui no local.
    print(f'Na função teste a variavel numero vale {numero}')   #Atraves deste print é possivel ver que a variavel numero que esta no escopo global, é reconhecida dentro da função tambem.
    print(f'Na função teste a variavel x vale {x}')
    print(f'A variavel chocolate na funcao tem o valor {chocolate}')

chocolate = 99
numero = 6
print(f'No programa principal a variavel numero vale {numero}')
print(f'No programa principal a variavel chocolate tem o valor {chocolate}')
escopo()
#print(f'No programa principal a variavel x numero vale {x}')  #Este teste para testar as variaveis dentro de cada escopo, mostra que a variavel x não existe para o escopo global, entao se eu descomentar o começo desta linha da erro.


print('~~'*60)

def funcao():
    global n1   #Agora neste caso, quando eu coloco a palavra global e o nome da variavel na frente, ele passa a usar a mesma variavel que ja existe na global, entao qualquer alteração fica no escopo global e da função, seguindo a ordem do codigo.
    n1 = 4 
    print(f'O valor de n1 dentro do escopo da funcao é {n1}')


n1 = 10
funcao()
print(f'O valor de n1 dentro do escopo global é {n1}')


print('~~'*60)


def divisao(a=0,b=0):   
    result = a/b
    return result  #Aqui mostra que o return serve para retornar uma resultado para a variavel que chamou a função.

resposta = divisao(8,2) #O resultado da chamada da função foi atribuido a varivel resposta
print(resposta)