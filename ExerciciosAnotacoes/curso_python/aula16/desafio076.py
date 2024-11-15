'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('Lapis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for item in produtos:
    if type(item) is str:
        print(f'{item:.<30}',end='')
    else:
        print(f'R${item:.2f}')
print('='*40)