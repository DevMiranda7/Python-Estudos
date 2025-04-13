# ESTRUTURAS DE DADOS   


# Como criar uma lista

# Lista com valores
lista = ["Fabricio Daniel",9.5,8.2,2.9,True]
# mudando valor da lista usado o index
lista[2] = 5

# Imprimindo valores da lista
for elemento in lista:
    print(elemento)


quantidadeDeElementos = len(lista)

print(quantidadeDeElementos)

# Partição
print()
print(lista[3:])

# Inserir elementos na lista

lista.append(10)

# Inserir varios elementos na lista



print(lista[:])

lista.append([10,22,33])
print()

# acessando lista dentro de lista
print(lista[6][2])


lista.remove(10)

print()
print(lista[:])