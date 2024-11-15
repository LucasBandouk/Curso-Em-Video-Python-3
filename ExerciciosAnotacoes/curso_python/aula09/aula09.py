#Fatiamento

frase = "Curso em Video Python"
print(frase[3]) 
print(frase[0:14]) 
print(frase[0:14:2])
print(frase[:5]) 
print(frase[9:]) 
print(frase[9::2])
print(frase[::2])
print(len(frase))
print(frase.count('o'))
print(frase.count('e',0,10))
print(frase.find('em'))
print("Curso" in frase)


#Transformação

print(frase.replace("Video","123"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.lower().find("video"))

#Divisão

print(frase.split())
print('-'.join(frase))

frase2 = "   Apenda Phython  "

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())


print("""Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().""")