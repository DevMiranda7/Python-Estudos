import random as rd, datetime


matricula = rd.randint(1000000,99999999)
turma = rd.choice(["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D"])
diaDoCadastro = datetime.datetime.now().strftime("%d")
mesDoCadastro = datetime.datetime.now().strftime("%m")


registro = {
    'matricula':matricula,
    'dia de cadastro':diaDoCadastro,
    'mês do cadastro':mesDoCadastro,
    'turma':turma
}

registro["turma"] = '2A'



registro['modalidade'] = 'EAD'



# Método pop() remova a chave do dicionario

registro.pop('turma')



# Método items(), ele retorna a lista, tudo que tem no dicionario


print(registro.items())
print()

# Método keys(), ele retorna as chaves do dicionario sem os valores
print(registro.keys())
print()
# Métodos values(), ele retorna uma lista dos valores do dicionario, apenas os valores
print(registro.values())
print()

# Pegando os valores de cada chave
for chaves in registro.keys():
    print(registro[chaves])
print()
# Mesmo que o anterior, apenas sendo mais simples
for valores in registro.values():
    print(valores)

# Pegando as chaves do dicionario
print()
for chaves in registro.keys():
    print(chaves)

# Pegando todos os dados do dicionario
print()
for chaves, valores in registro.items():
    print(f"{chaves}: {valores}")