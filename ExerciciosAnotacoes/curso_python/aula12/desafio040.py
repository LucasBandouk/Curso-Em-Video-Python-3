n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} a média do aluno é {media}')
if media < 5:
    print('O aluno está \033[31mREPROVADO\033[m!')
elif media >= 5 and media < 7:
    print('O aluno está em \033[;33mRECUPERAÇÃO\033[m!')
elif media >= 7:
    print('O aluno está \033[;32mAPROVADO\033[m!')