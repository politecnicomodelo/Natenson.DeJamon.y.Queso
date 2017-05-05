import os
from datetime import date
from Clase.Pedido import Pedido
from Clase.Profesores import Profesores
from Clase.Platos import Platos
from Clase.Alumno import Alumno
ListaPlatos=[]
ListaPersonas=[]
ListaPedidos=[]

idPedido=0

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1-Crear alumnos")
    print("2-Crear profesores")
    print("3-Crear platos")
    print("4-Crear pedidos")
    print("5-Modificar alumnos")
    print("6-Modificar profesores")
    print("7-Modificar platos")
    print("8-Modificar pedidos")
    print("9-Eliminar alumnos")
    print("10-Eliminar profesores")
    print("11-Eliminar platos")
    print("12-Eliminar pedidos")
    print("13-Listado pedidos del dia")
    print("14-Salir")

    x=input()

    if x == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        unAlumno=Alumno()

        print("Ingresar nombre")
        Nombre = input()
        unAlumno.setNombre(Nombre)

        print("Ingresar apellido")
        Apellido = input()
        unAlumno.setApellido(Apellido)

        print("Ingresar division")
        Division = input()
        unAlumno.setDivision(Division)

        ListaPersonas.append(unAlumno)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno creado")
        print("Enter para continuar")
        input()


    if x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        unProfesor=Profesores()

        print("Ingresar nombre")
        Nombre=input()
        unProfesor.setNombre(Nombre)

        print("Ingresar apellido")
        Apellido=input()
        unProfesor.setApellido(Apellido)

        print("Ingresar Descuento")
        Descuento=input()
        unProfesor.setDescuento(Descuento)

        ListaPersonas.append(unProfesor)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor creado")
        print("Enter para continuar")
        input()


    if x == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        unPlato=Platos()

        print("Ingresar nombre")
        Nombre=input()
        unPlato.setNombre(Nombre)

        print("Ingresar precio")
        Precio=input()
        unPlato.setPrecio(int(Precio))

        ListaPlatos.append(unPlato)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato creado")
        print("Enter para continuar")
        input()


    if x == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        unPedido=Pedido()

        idPedido+=1
        unPedido.idPedido = idPedido

        print("El id del pedido es %d" %(unPedido.idPedido))
        print("Enter para continuar")
        input()

        print("Ingresar Apellido de la persona del pedido")
        Nombre=input()
        for item in ListaPersonas:
            if item.Apellido==Nombre:
                unPedido.agregarPersona(item)

        print("Ingresar la fecha de creacion")
        print("Ingresar el anio")
        Anio=input()
        print("Ingresar el Mes")
        Mes=input()
        print("Ingresar el dia")
        Dia=input()
        unPedido.setFechaCreacion(int(Anio),int(Mes),int(Dia))

        print("Ingresar la fecha de entrega")
        print("Ingresar el anio")
        Anio=input()
        print("Ingresar el Mes")
        Mes=input()
        print("Ingresar el dia")
        Dia=input()
        unPedido.setFechaEntrega(int(Anio),int(Mes),int(Dia))

        print("Ingresar nombre del plato del pedido")
        Nombre=input()
        for item in ListaPlatos:
            if item.Nombre==Nombre:
                unPedido.setPlato(item)

        print("Se entrego el pedido?")
        Entrega=input()
        unPedido.setSeEntrego(Entrega)

        print("El precio del plato es de %f pesos" %(unPedido.calcularPrecio()))
        input()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido creado")
        print("Enter para continuar")
        input()


    if x == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Apellido del alumno a modificar")
        NombreAl=input()

        Auxiliar=None
        for item in ListaPersonas:
            if item.Apellido == NombreAl:
                Auxiliar=item

        print("Ingresar nombre")
        Nombre = input()
        Auxiliar.setNombre(Nombre)

        print("Ingresar apellido")
        Apellido = input()
        Auxiliar.setApellido(Apellido)

        print("Ingresar division")
        Division = input()
        Auxiliar.setDivision(Division)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno Modificado")
        print("Enter para continuar")
        input()


    if x == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Apellido del Profesor a modificar")
        NombreAl = input()

        Auxiliar = None
        for item in ListaPersonas:
            if item.Apellido == NombreAl:
                Auxiliar = item

        print("Ingresar nombre")
        Nombre = input()
        Auxiliar.setNombre(Nombre)

        print("Ingresar apellido")
        Apellido = input()
        Auxiliar.setApellido(Apellido)

        print("Ingresar Descuento")
        Descuento = input()
        Auxiliar.setDescuento(Descuento)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor Modificado")
        print("Enter para continuar")
        input()


    if x == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nombre del plato a modificar")
        Auxiliar=None
        Nombre=input()
        for item in ListaPlatos:
            if item.Nombre == Nombre:
                Auxiliar=item

        print("Ingresar nombre")
        Nombre=input()
        Auxiliar.setNombre(Nombre)

        print("Ingresar precio")
        Precio=input()
        Auxiliar.setPrecio(int(Precio))

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato creado")
        print("Enter para continuar")
        input()


    if x == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ingrear el id del pedido a modificar")
        Auxiliar=None
        id=input()
        for item in ListaPedidos:
            if item.idPedido==id:
                Auxiliar=item


        print("El id del pedido es %d" %(Auxiliar.idPedido))
        print("Enter para continuar")
        input()

        print("Ingresar nombre de la persona del pedido")
        Nombre=input()
        for item in ListaPersonas:
            if item.Nombre==Nombre:
                Auxiliar.agregarPersona(item)

        print("Ingresar la fecha de creacion")
        print("Ingresar el anio")
        Anio=input()
        print("Ingresar el Mes")
        Mes=input()
        print("Ingresar el dia")
        Dia=input()
        Auxiliar.setFechaCreacion(int(Anio),int(Mes),int(Dia))

        print("Ingresar la fecha de entrega")
        print("Ingresar el anio")
        Anio=input()
        print("Ingresar el Mes")
        Mes=input()
        print("Ingresar el dia")
        Dia=input()
        Auxiliar.setFechaEntrega(int(Anio),int(Mes),int(Dia))

        print("Ingresar nombre del plato del pedido")
        Nombre=input()
        for item in ListaPlatos:
            if item.Nombre==Nombre:
                Auxiliar.setPlato(Platos)

        print("Se entrego el pedido?")
        Entrega=input()
        Auxiliar.setSeEntrego(Entrega)

        print("El precio del plato es de %f pesos" %(Auxiliar.calcularPrecio()))
        input()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido modificado")
        print("Enter para continuar")
        input()


    if x == '9':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ingresar apellido del alumno a eliminar")
        Apellido=input()
        Auxiliar=None
        for item in ListaPersonas:
            if Apellido==item.Apellido:
                Auxiliar=item
        ListaPersonas.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno eliminado exitosamente")
        input()


    if x == '10':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ingresar apellido del profesor a eliminar")
        Apellido=input()
        Auxiliar=None
        for item in ListaPersonas:
            if Apellido==item.Apellido:
                Auxiliar=item
        ListaPersonas.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor eliminado exitosamente")
        input()


    if x == '11':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ingresar nombre del plato a eliminar")
        Nombre=input()
        Auxiliar=None
        for item in ListaPlatos:
            if Nombre==item.Nombre:
                Auxiliar=item
        ListaPlatos.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato eliminado exitosamente")
        input()


    if x == '12':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ingresar id del pedido a eliminar")
        id=input()
        Auxiliar=None
        for item in ListaPedidos:
            if id==item.idPedido:
                Auxiliar=item
        ListaPedidos.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido eliminado exitosamente")
        input()


    if x == '13':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Ingresar fecha")
        print("Ingresar anio")
        Anio=input()
        print("Ingresar Mes")
        Mes=input()
        print("Ingresar Dia")
        Dia=input()

        j=0
        Auxiliar=None
        for item in ListaPedidos:
            if item.FechaEntrega.year == int(Anio) and item.FechaEntrega.month == int(Mes) and item.FechaEntrega.day == int(Dia):
                print("Id del pedido: %d" % (Auxiliar.idPedido))
                print("Persona que lo ordeno es: %s %s" % (
                Auxiliar.Persona.Nombre, Auxiliar.Persona.Apellido))
                print("La fecha de creacion del plato es: %d %d %d" % (
                Auxiliar.FechaCreacion.year, Auxiliar.FechaCreacion.month,
                Auxiliar.FechaCreacion.day))
                print("La fecha de entrega del plato es: %d %d %d" % (
                Auxiliar.FechaEntrega.year, Auxiliar.FechaEntrega.month,
                Auxiliar.FechaEntrega.day))
                print("Id del pedido: %d" % (Auxiliar.idPedido))
                print("Se entrego?: %s" % (Auxiliar.seEntrego))
                print(" ")
                print(" ")
                print("Entrer para continuar")
                input()


    if x == '14':
        break

