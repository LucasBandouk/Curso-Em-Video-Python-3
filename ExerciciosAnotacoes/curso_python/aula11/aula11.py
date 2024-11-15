print('\033[7;33;44mOla Mundo!\033[m')

a = 5
b = -1

print(f"O valor \033[32m{a}\033[m e o valor \033[31m{b}\033[m!!!")

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

print(f"O valor {cores['verde']}{a}{cores['limpa']} e o valor {cores['vermelho']}{b}{cores['limpa']}!!!")