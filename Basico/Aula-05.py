nome = input("Escreva seu nome: ")
print(nome)

anoDeEntrada = input("Digite seu ano de entrada em Harvard: ")
print(type(anoDeEntrada))

print(type(int(anoDeEntrada)))


notaDeEntrada = float(input("Digite sua nota que te fez entrar em Harvard: "))
print(type(notaDeEntrada))


print(f"{nome}, Parabéns por entrar em Harvard em {int(anoDeEntrada)} com a nota máxima de {notaDeEntrada}%")

#Maneira alternativa de escrever um print usando as variáveis
print("%s, Parabéns por entrar em Harvard em %d com a nota máxima de %.2f"% (nome,int(anoDeEntrada),notaDeEntrada))

#Outra maneira alternativa de escrever um print usando as variáveis
print("{}, Parabéns por entrar em Harvard em {} com a nota máxima de {}".format(nome,int(anoDeEntrada),notaDeEntrada))

# a vantagem do format é a questão de não ter problemas com questões de pontos flutuantes, mas a melhor opção seria usando o f-string (f"{}") pois ele também
#Não tem esse problema


# \n usando para pular linha no print:

print(f"{nome},\n Parabéns por entrar em Harvard\n em {int(anoDeEntrada)}\n com a nota máxima de {notaDeEntrada}%")

# /t usando para adicionar espaço de tabulação no texto:

print(f"{nome},\tParabéns por entrar em Harvard\tem\t{int(anoDeEntrada)}\tcom\ta\tnota\tmáxima\tde\t{notaDeEntrada}\t%")

# \\ usando para imprimir uma barra invertida, python considera apenas uma \ como caractere especial no caso chamar comando.
print("\\") 

# \" ou \' Usado para imprimir aspas duplas  ("") ou simples ('') 

print(f"\'{nome}\', Parabéns por entrar em Harvard em \"{int(anoDeEntrada)}\" com a nota máxima de \'{notaDeEntrada}%\'")

