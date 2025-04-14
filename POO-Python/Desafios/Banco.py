class ContaBancaria:
    def __init__(self,titular,saldo,active):
        self._titular = titular
        self._saldo = saldo        
        self._active = active
    
    def __str__(self):
        return f"Welcome Mr. {self._titular} your wallet has US$:{self._saldo}"

    def activeAccount(self):
        self._active = True

    


conta = ContaBancaria("Luan Miranda",1000000,True)


print(conta)



class ClienteBanco:
    def __init__(self, nome, idade, naturalidade, profissao, endereco):
        self.nome = nome
        self.idade = idade        
        self.naturalidade = naturalidade
        self.profissao = profissao
        self.endereco = endereco        

    def __str__(self):
        return f" Mr. {self.nome}\n Age: {self.idade}\n Naturalidade: {self.naturalidade}\n Profissão: {self.profissao}\n Endereço: {self.endereco} "
    

cliente = ClienteBanco("Miranda",20,"Brasileiro","Engenheiro de Software","Vancouver")

print(cliente)