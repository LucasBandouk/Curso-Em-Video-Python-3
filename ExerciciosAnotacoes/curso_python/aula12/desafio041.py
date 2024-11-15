from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos')
if idade < 10:
    print('Classificação: MIRIM')
elif 10 <= idade < 15:
    print('Classificação: INfANTIL')
elif 15 <= idade < 20:
    print('Classificação: JÚNIOR')
elif 20 <= idade < 26:
    print('Classificação: SÊNIOR')
else: 
    print('Classificação: MASTER')