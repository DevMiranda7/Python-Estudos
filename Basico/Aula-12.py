# #1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel 
# # [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
# # Com esses valores, 
# # faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().


# lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# # gastos = sum(lista)

# # media = gastos / len(lista)
# # print(f"Média de gastos: {media:.2f}")


# #2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
# gastosAcimade3000 = len(lista)
# quantidade = 0
# for i in range(len(lista)):
#     if lista[i] > 3000:
#         quantidade += 1


# porcentagem =  (gastosAcimade3000 /quantidade ) * 100 

# print(f"Foram realizadas {quantidade} compras acima de 3000")
# print(f"Porcentagem do total de compras: {porcentagem:.2f}%")


# lista = [43,4,7,2,4]
# tamanho = len(lista)-1
# for i in range(tamanho,-1,-1):
#     print(lista[i])




# numero = int(input("Digite qualquer número "))
# listaPrimos = []

# for i in range(1,numero):
#     if i % 2 == 0:
#         listaPrimos.append(i)

# for i in listaPrimos:
#     print(i)


dia = int(input("Digite o dia desejado para análise:"))
mes = int(input("Digite o mês desejado para análise:"))
ano =  int(input("Digite o ano desejado para análise:"))

if mes == 1 or mes == 3 or mes == 5  or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 0 and dia <= 31:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("Válida para uma análise!")
    else:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("inválida para uma análise!")
elif mes == 2:
    if dia > 0 and dia <= 28:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("Válida para uma análise!")
    else:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("inválida para uma análise!")
elif mes == 4 or mes == 6 or mes == 9  or mes == 11:
     if dia > 0 and dia <= 30:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("Válida para uma análise!")
     else:
        print(f"Data inserida: {dia}/{mes}/{ano}")
        print("inválida para uma análise!")