from datetime import date
class PesoyAltura(object):

    Peso=None

    Altura=None

    FechaMedida=None

    def setPeso(self, n):
        self.Peso=n

    def setAltura(self, n):
        self.Altura=n

    def setFechaMedida(self, anio, mes, dia):
        self.FechaMedida=date(anio,mes,dia)