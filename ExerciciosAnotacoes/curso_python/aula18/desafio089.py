'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
de cada aluno individualmente.'''

todosalunos = []
listaprovisoria = []
continuar = ''
while continuar != 'N':
    listaprovisoria.append(str(input("Nome: ")))
    listaprovisoria.append(float(input('Nota1: ')))
    listaprovisoria.append(float(input('Nota2: ')))
    todosalunos.append(listaprovisoria[:])
    listaprovisoria.clear()
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
print('=-='*15)
print('Nº      NOME      MÉDIA')
print('-'*40)
for a in range(0, len(todosalunos)):
    media = (todosalunos[a][1]+todosalunos[a][2])/2
    print(f'{a}',f'{todosalunos[a][0]}'.center(13),f'{media:.2f}'.center(11))
print('=-='*15)
interromper = 0
while interromper != 999:
    interromper = int(input('Mostrar notas de qual aluno? Informe a posição (999 para interromper): '))
    if interromper < len(todosalunos) and interromper >= 0:
        print(f'Notas de {todosalunos[interromper][0]} são {todosalunos[interromper][1]} e {todosalunos[interromper][2]}')
        print('=-='*15)
    elif interromper == 999:
        print('Programa finalizado!')
        break
    else:
        print('Nenhum aluno nessa possição')
