'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.         

Ex: escreva(‘Olá, Mundo!’) 

Saída:       ~~~~~~~~~                                                  
             Olá, Mundo!             
              ~~~~~~~~~    '''


def escreva(t):
    print('~'*(len(t)+4))
    print(f'{t}'.center(len(t)+4))
    print('~'*(len(t)+4))

mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)