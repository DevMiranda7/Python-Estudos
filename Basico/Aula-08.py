# QuantidadeDeAlunos = int(input("Digite a quantidade de alunos:"))
# soma = 0
# contador = 0
# while(QuantidadeDeAlunos > contador):
#     nota = float(input(f"Digite a nota do {contador} aluno: "))
#     soma = soma + nota
#     contador = contador+1
# print(f"Média da turma: {soma/QuantidadeDeAlunos}")
    


# contador = 0
# while(contador <= 10):
#     print(contador)
#     contador +=1


alunos = int(input("Quantos alunos serão avaliados?"))
print("Alunos realizando as provas...")
contador = 1

while(alunos >= contador ):
    print(f"Digite a nota do aluno {contador}: ")
    nota = float(input("Prova A: "))
    nota2 = float(input("Prova B: "))
    media = (nota + nota2) / 2
    print(f"Media do {contador} aluno: {media}")
    contador+=1