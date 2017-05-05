from datetime import date
class Jugadores(object):

    Nombre=" "

    FechaN=None

    Numero=None

    def setNombre(self, n):
        self.Nombre=n

    def setNacimiento(self, a, m, d):
        self.FechaN=date(int(a), int(m), int(d))

    def setNumero(self, n):
        self.Numero=n

