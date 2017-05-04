from .FIxture import Fixture
class Torneo(object):

    Equipos=[]

    Fixtures=Fixture()

    def agregarEquipos(self, n):
        for variable in self.Equipos:
            if variable.Nombre==n.Nombre:
                return False
        self.Equipos.append(n)
        return True
