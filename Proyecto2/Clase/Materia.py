class Materia(object):

    def __init__(self):
        self.ListaDeNotas=[]

    Nombre=" "

    def setNombre(self, n):
        self.Nombre=n

    def agregarNota(self, nota):
        self.ListaDeNotas.append(nota)

    def Promedio(self):
        if len(self.ListaDeNotas)==0:
            return 1
        return sum(self.ListaDeNotas)/len(self.ListaDeNotas)
