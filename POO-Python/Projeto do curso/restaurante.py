# atributos
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        Restaurante.restaurantes.append(self)

    #Exibindo de uma forma diferente o endereço do objeto

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    

    def listarRestaurentes():
        for restaurante in Restaurante.restaurantes:
            print(f"Nome: {restaurante.nome}\n Categoria: {restaurante.categoria}\n Ativo: {restaurante.ativo}")



restaurante = Restaurante("Sabor verdadeiro","Diversos")
Restaurante.listarRestaurentes()










































# restaurante_praca = Restaurante("Praça","Italiana")
# print(restaurante_praca.nome)
# print(restaurante_praca.categoria)
# restaurante_praca.ativo = False



# if restaurante_praca.ativo == True:
#     print(f"O restaurante {restaurante_praca.nome} está ativo")
# else:
#     print(f"O restaurante {restaurante_praca.nome} está inativo")
    
# categoria = restaurante_praca.categoria


# restaurante_praca.nome = "Bistrô"

# restaurante_pizza = Restaurante("Pizza Place","Fast Food")
# print(restaurante_pizza.nome) 
# print(restaurante_pizza.categoria)


# if restaurante_pizza.categoria == 'Fast Food':
#     print(f"O restaurante {restaurante_pizza.nome} é da categoria {restaurante_pizza.categoria}")
# else:
#     print(f"O restaurante {restaurante_pizza.nome}  não é da categoria Fast Food")

# restaurante_pizza.ativo = True

# print(f"Restaurante {restaurante_praca.nome}, categoria: {restaurante_praca.categoria}")

# print()
# print(restaurante_praca)
# print(restaurante_pizza)



