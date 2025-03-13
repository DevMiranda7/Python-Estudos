# idade = 15
# nome = "Marcos"

# print(f"{nome} tem {idade} anos de idade!")
# print(type(nome),type(idade))


# i = 5
# print(type(i))

# f = 9.7
# print(type(f))

# s = "Luan"
# print(type(s))

# b = True
# print(type(b))
# print(" ")


nome = str(input("Digite o nome do aluno:"))
idade = int(input(f"Digite a idade do {nome}"))
notaFinal = float(input(f"Qual a média do {nome}"))
situacaoEscolar = False


if notaFinal > 6 :
    situacaoEscolar = True
    print(f"Situação de aprovação: {situacaoEscolar}")
else:
    print(f"Situação de aprovação {situacaoEscolar}")