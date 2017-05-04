from .Persona import Persona
class Profesores(Persona):

    PorcentajeDescuento=None

    def setDescuento(self, Descuento):
        self.PorcentajeDescuento=Descuento

    def getDescuento(self):
        return self.PorcentajeDescuento

