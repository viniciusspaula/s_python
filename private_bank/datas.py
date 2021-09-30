from datetime import date, datetime

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        #self.data = datetime.strptime(self.data, '%d/%m/%Y')
    
    def formatada(self):
        print("{}".format(str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano)))