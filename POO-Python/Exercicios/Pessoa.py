class Pessoa:

    def __init__(self,nome,idade,profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f" Nome: {self._nome}\n Idade: {self._idade}\n Profissão: {self._profissao}"
    
    def aniversario(self,aniversario):
        self._idade += aniversario

    def saudacao(self):
        return f"Olá {self._nome} como vai no trabalho de {self._profissao}"
    


miranda = Pessoa("Luan",20,"Engenheiro de software")

miranda.aniversario(1)

print(miranda)