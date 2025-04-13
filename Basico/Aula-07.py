t1 = t2 = True
f1 = f2 = False

# Para ser verdadeiro é necessário que os dois parâmetros sejam verdadeiros
print("AND")
if t1 and f2:
    print("Expressão verdadeira")
else:
    print("Expressão falsa")
    print(f"Valor atual do primeiro parâmetro: {str(t1)}")
    print(f"Valor atual do segundo parâmetro: {str(f2)}")
print("\n")
# Para ser verdadeiro é necessário que um dos dois parâmetros sejam verdadeiros, caso um seja false será verdadeiro o resultado
print("OR")
if t1 or f2:
    print("Expressão verdadeira")
    print(f"Valor atual do primeiro parâmetro: {str(t1)}")
    print(f"Valor atual do segundo parâmetro: {str(f2)}")
    
else:
    print("Expressão falsa")    
print("\n")
# operador logíco not, basicamente nega o valor armazenado ou seja, se for verdadeiro será falso, se for falso será verdadeiro
print("NOT com AND")
if t1 and not f2:
    print("Expressão verdadeira")
    print(f"Valor antigo do segundo parâmetro: \"Antes do not\" {str(f2)}")
    print(f"Valor novo do segundo parâmetro: \"depois de utilizar o not\" {str(not f2)}")
    
else:
    print("Expressão falsa")
print("\n")
print("NOT com OR")
if not t1 or not t2:
    print("Expressão verdadeira")
    
    
else:
    print("Expressão falsa")
    print(f"Valor antigo do segundo parâmetro: \"Antes do not\" {str(f2)}")
    print(f"Valor novo do segundo parâmetro: \"depois de utilizar o not\" {str(not f2)}")
print("\n")


# Operador IN, utilizado para verificar se um determinado elemento está em um conjunto
print("IN")
lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes,' \
'Beatriz Costa, Felipe Almeida, Mariana Fernandes, ' \
'João Pinto, Luísa Nascimento, Gabriel Souza, Manuela ' \
'Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, ' \
'Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, ' \
'Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'


nome_1 = "João Ferreira"
nome_2 = "Osvaldo Luiz"

if nome_1 in lista:
    print("Aluno {}, presente na lista ".format(nome_1))
else:
    print("Aluno {}, não está presente na lista ".format(nome_2))

if nome_2 in lista:
    print("Aluno {}, presente na lista ".format(nome_2))
else:
    print("Aluno {}, não está presente na lista ".format(nome_2))





