class Conta:
    
#Atributos
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


# Métodos
    def extrato(self):
        print("saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self,valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor