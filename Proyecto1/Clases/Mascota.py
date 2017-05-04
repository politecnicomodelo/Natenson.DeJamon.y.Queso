class Mascota(object):
    Nombre=" "
    Tipo=" "
    def setNombre(self, n):
        self.Nombre=n
    def setTipo(self, n):
        self.Tipo=n
    def quienSoy(self):
        return "Soy "+self.Nombre+" un "+self.Tipo

