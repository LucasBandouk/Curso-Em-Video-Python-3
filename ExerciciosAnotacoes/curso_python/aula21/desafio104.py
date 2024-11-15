'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(txt):
   while True:
        numero = input(txt)
        numero = numero.strip()
        if not numero.isnumeric():
            print('\033[0;31m(Erro) digite um numero inteiro valido!\033[m')
        else:
            return numero
print('=-'*30)
n = leiaInt("Digite um numero: ")
print(f'Voce acaba de digitar o numero {n}')