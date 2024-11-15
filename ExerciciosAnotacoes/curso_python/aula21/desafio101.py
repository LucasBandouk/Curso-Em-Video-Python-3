'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
 de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
   nas eleições.'''

from datetime import datetime

def voto(nascimento):
    atual = datetime.now().year
    idade = atual - nascimento
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif idade == 16 or idade == 17 or idade > 70:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatorio.'
    
print('='*30)
nascimento = int(input('Em que ano voce nasceu? '))
resultado = voto(nascimento)
print(resultado)