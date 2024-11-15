from datetime import date
#Verificação de genero
genero = str(input('Informe seu genero com "M" para maculino e "F" para feminino: ')).upper().strip()
if genero != "M" and genero != "F":
    print('Você nao digitou a letra "M" ou "F". Tente novamente')
    exit()
elif genero == "M":
    print("Vamos verificar seu ano de alistamento")
elif genero == "F":
    print("Você nao é obrigada a se alistar")
    decisao = int(input('Ainda sim deseja se alistar? Digite "1" para SIM e "2" para Não: '))
    if decisao == 1:
        print('Continue preenchendo o formulario')
    else:
        print("Ok, tenha um bom dia!")
        exit()
#Programa para verificar ano de alistamento
atual = date.today().year
ano = int(input("Informe seu ano de nascimento: "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {atual}")
if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o seu alistamento\nSeu alistamento será em {ano + 18}")
elif idade > 18:
    print(f"Você ja deveria ter se alistado há {idade - 18} anos\nSeu alistamento foi em {ano + 18}")
elif idade == 18:
    print(f"Você tem que se alistar IMEDIATAMENTE!")
