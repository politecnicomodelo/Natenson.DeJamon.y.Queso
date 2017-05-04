from datetime import date
class Pedido (object):

    FechaCreacion=None

    Persona=None

    HoraEntrega=None

    Plato=None

    SeEntrego=None

    def setFechaCreacion(self, Anio, Mes, Dia):
        self.FechaCreacion=date(Anio,Mes,Dia)

    def agregarPersona(self, Persona):
        self.Persona=Persona

    def setHoraEntrega(self, Hora):
        self.HoraEntrega=Hora

    def setPlato(self, Plato):
        self.Plato=Plato

    def setSeEntrego(self, Entrego):
        self.SeEntrego=Entrego

    def calcularPrecio(self):
        return (self.Plato.Precio*(100-self.Persona.getDescuento))/100