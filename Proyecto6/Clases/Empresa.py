class Empresa(object):
    Nombre = " "

    ListaAutos = []

    ListaCamiones = []

    def setNombre(self, n):
        self.Nombre = n

    def agregarCamiones(self, n):
        self.ListaCamiones.append(n)

    def agregarAutos(self, n):
        self.ListaAutos.append(n)

