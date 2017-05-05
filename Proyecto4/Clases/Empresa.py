from .Empleado import Empleado
class Empresa(object):
    Nombre=" "

    ListaEmpleados=[]

    def agregarEmpleado(self, Empleado):
        self.ListaEmpleados.append(Empleado)