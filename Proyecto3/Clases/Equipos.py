from .Jugadores import Jugadores
class Equipos(object):

    Nombre=" "

    Barrio=" "

    Capitan=None

    Disponibilidad=[[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]

    Jugadores=[]

    def setNombre(self, n):
        self.Nombre=n

    def setBarrio(self, n):
        self.Barrio=n

    def setCapitan(self, n):
        for jugador in self.Jugadores:
            if jugador==n:
                self.Capitan=jugador
                return True
        return False

    def setDisponibilidad(self, dia, turno, disponible):
        self.Disponibilidad[dia][turno]=disponible

    def agregarJugador(self, n):
        for item in self.Jugadores:
            if item.Numero==n.Numero:
                return False
        self.Jugadores.append(n)
        return True