'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados 
na ordem correta.'''

pilha = []
expressao = str(input('Digite a expressao: '))
for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')
