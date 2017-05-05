class Partido(object):

    Dia=0

    Turno=0

    Equipo1=None

    Equipo2=None

    Ganador=None

    def setDia(self, n):
        self.Dia=n

    def setTurno(self, n):
        self.Turno=n

    def setEquipos(self, e1, e2):
        self.Equipo1=e1
        self.Equipo2=e2

    def setGanador(self, n):
        self.Ganador=n