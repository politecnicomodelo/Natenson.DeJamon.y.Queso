from .Persona import Persona
class Alumno(Persona):

    Division=None

    def setDivision(self, Division):
        self.Division=Division
