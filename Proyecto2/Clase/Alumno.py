from datetime import date
from .Materia import Materia
class Alumno(object):
    def __init__(self):
        self.ListaMaterias=[]

    Nombre=" "

    Apellido=" "

    FechaN=None

    def setMaterias(self, n):
        self.ListaMaterias.append(n)

    def setNombre(self, n):
        self.Nombre=n

    def setApellido(self, n):
        self.Apellido=n

    def setFecha(self, a, m, d):
        self.FechaN=date(int(a),int(m),int(d))

    def menorNota(self, n):
        for Variable in self.ListaMaterias:
            if Variable==n:
                return min(self.ListaMaterias[Variable].ListaDeNotas)

    def mayorNota(self, n):
        for Variable in self.ListaMaterias:
            if Variable==n:
                return max(self.ListaMaterias[Variable].ListaDeNotas)

    def promedioNotasAlumno(self):
        Suma=0
        for Variable in self.ListaMaterias:
            Suma+=Variable.Promedio()
        return Suma/len(self.ListaMaterias)

    def promedioMinimo(self):
        ListaPromedios=[]
        for Variable in self.ListaMaterias:
            ListaPromedios.append(Variable.Promedio())
        return min(ListaPromedios)

    def promedioMaximo(self):
        ListaPromedios = []
        for Variable in self.ListaMaterias:
            ListaPromedios.append(Variable.Promedio())
        return max(ListaPromedios)

