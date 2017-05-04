class Album(object):
    Titulo=" "

    ListaCanciones=[]

    def setTitulo(self, n):
        self.Titulo=n

    def agregarCancion(self, n):
        self.ListaCanciones.append(n)

