QuantidadeDeSeguranca= int(input("Qual a quantidade de seguranças da empresa?"))
SalarioDeSeguranca = float(input("Qual salário de segurança?"))

QuantidadeDeDocentes = int(input("Qual a quantidade de docentes da empresa?"))
SalarioDeDocente = float(input("Qual salário de Docente?"))

QuantidadeDeDiretores = int(input("Qual a quantidade de diretores da empresa?"))
SalarioDeDiretor = float(input("Qual salário de diretor?"))
maior = 0
menor = 0

QuantidadeDeFuncionarios = QuantidadeDeSeguranca + QuantidadeDeDocentes + QuantidadeDeDiretores
print(QuantidadeDeFuncionarios)

if SalarioDeSeguranca > SalarioDeDocente and SalarioDeSeguranca > SalarioDeDiretor:
    maior = SalarioDeSeguranca
    print("O maior salário é de segurança")
elif SalarioDeDocente > SalarioDeSeguranca and SalarioDeDocente > SalarioDeDiretor:
    maior = SalarioDeDocente
    print("O maior salário é de docente")
else:
    maior = SalarioDeDiretor
    print("O maior salário é do diretor")


if SalarioDeSeguranca < SalarioDeDocente and SalarioDeSeguranca < SalarioDeDiretor:
    menor = SalarioDeSeguranca
    print("O menor salário é de segurança")
elif SalarioDeDocente < SalarioDeSeguranca and SalarioDeDocente < SalarioDeDiretor:
    menor = SalarioDeDocente
    print("O menor salário é de docente")
else:
    menor = SalarioDeDiretor
    print("O menor salário é do diretor")   


diferenca = maior - menor

print(f"A diferença entre o salário mais baixo e mais alto é: {diferenca} ")

mediaPonderadaSalarial = (SalarioDeSeguranca*QuantidadeDeSeguranca + SalarioDeDocente*QuantidadeDeDocentes + SalarioDeDiretor*QuantidadeDeDiretores)
print(f"Média salária da empresa: {mediaPonderadaSalarial/QuantidadeDeFuncionarios:.2f}")


#Potenciação

operador = 2
potencia = 3

print(operador ** potencia)

#Resto da divisão

print(7%3)

#Divisão inteira

print(7//3)