'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será 
mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n,show = False):
    """
    -> Calcula o Fatorial de um número.
    para n: O número a ser calculado.
    para show: (Opcional) mostrar ou não a conta.
    return: o valor Fatorial de um numero n.
    """
    print('-'*30)
    resultado = 1
    for a in range(n,0,-1):
        resultado *= a
        if show == True:
            if a == 1:
                print(f'{a} =', end = ' ')
                break
            print(f'{a} x', end = ' ')
    return resultado
    

print(fatorial(5, True))
help(fatorial)
