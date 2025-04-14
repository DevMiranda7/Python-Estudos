# atributos
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = True
        Restaurante.restaurantes.append(self)

    #Exibindo de uma forma diferente o endereço do objeto

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listarRestaurentes(csl):
        print(f'{"NOME DO RESTAURANTE".ljust(25)} | {"Categoria".ljust(25)} |    {"STATUS"}')
        for restaurante in csl.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} |  {restaurante.ativo}")


    @property
    def ativo(self):
     return 'verdadeiro' if self._ativo else 'false'
    
    def alterarEstado(self):
        self._ativo = not self._ativo

restaurante = Restaurante("sabor verdadeiro","Diversos")
restaurante.alterarEstado()

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



