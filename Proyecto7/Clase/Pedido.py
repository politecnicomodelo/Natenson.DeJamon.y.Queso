from datetime import date
class Pedido (object):

    idPedido=None

    FechaCreacion=None

    Persona=None

    FechaEntrega=None

    Plato=None

    SeEntrego=None

    def setFechaCreacion(self, Anio, Mes, Dia):
        self.FechaCreacion=date(Anio,Mes,Dia)

    def agregarPersona(self, Persona):
        self.Persona=Persona

    def setFechaEntrega(self, Anio, Mes, Dia):
        self.FechaEntrega=date(Anio,Mes,Dia)

    def setPlato(self, Plato):
        self.Plato=Plato

    def setSeEntrego(self, Entrego):
        self.SeEntrego=Entrego

    def calcularPrecio(self):
        return (self.Plato.Precio*((100-self.Persona.getDescuento()))/100)