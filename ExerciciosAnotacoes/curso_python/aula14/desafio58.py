'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''


from random import randrange
from time import sleep
print("-="*30)
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar...")
print("-="*30)
pc = randrange(11)
numero = int(input("Em que numero eu pensei? "))
tentativas = 1
print("PROCESANDO...")
sleep(1)
while numero != pc:
        if numero < pc:
                print('O numero é Maior... tente novamente')
                tentativas += 1
        elif numero > pc:
                print('O numero é Menor... tente novamente')
                tentativas += 1
        numero = int(input("Em que numero eu pensei? "))
print(f"Parabens, voce conseguiu me vencer! com {tentativas} tentativas")
