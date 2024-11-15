'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''

c = ('\033[m', #0 - padrao
    '\033[0;30;41m', #1 - vermelho
    '\033[0;30;42m', #2 - verde 
    '\033[0;30;43m', #3 - amarelo
    '\033[0;30;44m', #4 - azul
    '\033[0;30;45m', #5 - roxo 
    '\033[7;30m' #6 - branco
)

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'',4)
    print(c[6], end = '')
    help(comando)
    print(c[0], end = '')

def titulo(msg, cor= 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end = '')

resposta = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    resposta = str(input('Funcao ou Biblioteca > '))
    if resposta.upper().strip() == "FIM":
        break
    else:
        ajuda(resposta)
titulo('Ate Logo!',1)