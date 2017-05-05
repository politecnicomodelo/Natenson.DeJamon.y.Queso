from .Partido import Partido
#from .Torneo import Torneo
class Fixture(object):

    ListaPartidos=[]

    def crearPartidos(self, e1, e2, dia, turno, gano):
        Auxiliar=Partido()
        Auxiliar.setEquipos(e1, e2)
        Auxiliar.setDia(dia)
        Auxiliar.setTurno(turno)
        Auxiliar.setGanador(gano)
        self.ListaPartidos.append(Auxiliar)

    #def crearPartidosAutomatico(self):
