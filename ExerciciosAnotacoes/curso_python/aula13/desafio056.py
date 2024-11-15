'''''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

idade_f = 0
media = 0
for c in range (1,5):
    print(f'----- {c}º pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade
    if sexo == 'M':
        if c == 1:
            idade_m = idade
            nome_velho = nome
        elif idade_m < idade:
            idade_m = idade
            nome_velho = nome
    elif sexo == 'F':
        if idade < 20:
            idade_f += 1
    else:
        print('O sexo não esta compativel com "M" ou "F".')
        exit()           
print(f'A media da idade do grupo é de {media/4} anos')
print(f'O homem mais velho tem {idade_m} e se chama {nome_velho}')
print(f'Ao todo são {idade_f} mulheres com menos de 20 anos')
