s1 = "Alura"
print(type(s1))



#Métodos

texto = "   Geovana Alessandra dias Sanyos"


# Deixando tudo em maiúsculas 
print(texto.upper())

# Deixandotudo em minúsculas
print(texto.lower())

# Deixando a primeira Letra da frase em maiúsculas caso seja minúsculas e mantém o restante minúsculo exemplo: santos - Santos
print(texto.capitalize())

# Removendo espaços em branco

print(texto.strip())


# Substituir texto primeiro parâmetro é o antigo e o segundo o novo, sendo assim iremos substituir o que era antigo pelo novo.

print(texto.replace("Sanyos","Santos"))

# Esses métodos não mudam de fato o valor original da variável, são apenas visuais

# Caso sejá necessário mudar de fato o conteúdo original definitivamente basta atribuir novamente na mesma variável
#Exemplo:

texto = texto.strip().replace("y","t").upper()
print(texto)