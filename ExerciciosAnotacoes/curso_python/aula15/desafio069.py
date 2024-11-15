'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior_idade = total_masculino = mulheres_menores = 0
while True:
    print('-' * 40)
    print('          CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade > 18:
        maior_idade += 1
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'M':
        total_masculino += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menores += 1
    continua = ''
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continua == 'N':
        break
print('-=' * 20)
print(f'''Total de pessoas com mais de 18 anos: {maior_idade}
Ao todo temos {total_masculino} homens cadastrados
E temos {mulheres_menores} mulheres com menos de 20 anos''')
print('-=' * 20)



