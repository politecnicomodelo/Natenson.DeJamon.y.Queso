from datetime import date
class Persona(object):

    Nombre=" "

    Apellido=" "

    FechaN=None

    ListaPesosyAlturas=[]

    def setNombre(self, n):
        self.Nombre=n

    def setApellido(self, n):
        self.Apellido=n

    def setFechaN(self, anio, mes, dia):
        self.FechaN=date(anio,mes,dia)

    def agregarPesoyAltura(self, n):
        self.ListaPesosyAlturas.append(n)

    def promedioPeso(self, anio):
        Auxiliar=None
        for item in self.ListaPesosyAlturas:
            if item.FechaMedida.year==anio:
                Auxiliar+=item.Peso
        return Auxiliar/12

    def promedioAltura(self, anio):
        Auxiliar=None
        for item in self.ListaPesosyAlturas:
            if item.FechaMedida.year==anio:
                Auxiliar+=item.Altura
        return Auxiliar/12

    def Crecimiento(self, anio1, anio2):
        ListaAux1=[]
        ListaAux2=[]
        for item in self.ListaPesosyAlturas:
            if item.FechaMedida.year==anio1:
                ListaAux1.append(item.Altura)
        for item in self.ListaPesosyAlturas:
            if item.FechaMedida.year==anio2:
                ListaAux2.append(item.Altura)
        Aux1=max(ListaAux1)
        Aux2=max(ListaAux2)
        return (Aux2*100)/Aux1