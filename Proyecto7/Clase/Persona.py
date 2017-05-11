class Persona(object):

    DNI=None

    Nombre=" "

    Apellido=" "

    def setDNI(self, DNI):
        self.DNI=DNI

    def setNombre(self, Nombre):
        self.Nombre=Nombre

    def setApellido(self, Apellido):
        self.Apellido=Apellido

    def getDescuento(self):
        return 0