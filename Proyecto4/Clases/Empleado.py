from datetime import date
class Empleado(object):
    Nombre=" "

    Apellido=" "

    Telefono=None

    FechaNacimiento=None

    ListaDias=[False, False, False, False, False]

    ListaAsistencia=[]

    def setNombre(self, Nombre):
        self.Nombre=Nombre

    def setApellido(self, Apellido):
        self.Apellido=Apellido

    def setTelefono(self, Telefono):
        self.Telefono=Telefono

    def setFechaNacimiento(self, Ano, Mes, Dia):
        self.FechaNacimiento=date(int(Ano), int(Mes), int(Dia))

    def setDiasDeTrabajo(self, Lunes, Martes, Miercoles, Jueves, Viernes):
        if Lunes==True:
            self.ListaDias[0]=True
        if Martes==True:
            self.ListaDias[1]=True
        if Miercoles==True:
            self.ListaDias[2]=True
        if Jueves==True:
            self.ListaDias[3]=True
        if Viernes==True:
            self.ListaDias[4]=True

    def calcularAsistencia(self, Mes):
        DiasQueTrabajo=None
        DiasLaborables=None

        for item in self.ListaDias:
            if item==True:
                DiasLaborables+=1
        DiasLaborables*=4

        for variable in self.ListaAsistencia:
            if variable.month==Mes:
                DiasQueTrabajo+=1
        return DiasQueTrabajo/DiasLaborables