# Aula sobre if,elif,else.


nome = str(input("Digite seu nome: "))
if nome == 'Lucas':
    print("Que nome bonito!")
elif nome == 'Maria' or nome == 'Joao' or nome == 'Jose':
    print("Seu nome é bem popular no Brasil")
elif nome in 'Carol Marcia':
    print('Nome feminino bonito')
else:
    print('Seu nome não é bonito KKKK')
print(f"Tenha um bom dia, {nome}! ")