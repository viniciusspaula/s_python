class Conta:
    
#Atributos
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'


# Métodos
    def extrato(self):
        print("saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo +self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
           self.__saldo -= valor
        else: print("O valor passou do limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, limite):
        return  self.__limite == limite



    @staticmethod
    def codigos_banco():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}