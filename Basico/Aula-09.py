import time as tm
# for i in range(0,11):
#     print(i)



alunos = int(input("Quantos alunos vão realizar a prova: "))
print("Alunos em avaliação...")
tm.sleep(3)
print("Fim de prova")
for contador in range(1,alunos+1):
    print(f"Aluno {contador}")
    nota = float(input("Digite a 1° nota: "))
    nota2 = float(input("Digite a 2° nota: "))
    media = (nota + nota2) / 2
    print(f"Média final do aluno {contador}: {media}")
    