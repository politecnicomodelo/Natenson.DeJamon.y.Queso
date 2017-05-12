import os
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
    print("0-Guardar archivo")
    print("1-Cargar Archivo")
    print("2-Crear alumnos")
    print("3-Crear profesores")
    print("4-Crear platos")
    print("5-Crear pedidos")
    print("6-Modificar alumnos")
    print("7-Modificar profesores")
    print("8-Modificar platos")
    print("9-Modificar pedidos")
    print("10-Eliminar alumnos")
    print("11-Eliminar profesores")
    print("12-Eliminar platos")
    print("13-Eliminar pedidos")
    print("14-Listado pedidos del dia")
    print("15-Salir")

    x=input()

    if x == '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        f=open("ArchivoAlumnos.txt", "w")

        for item in ListaPersonas:
            if type(item) is Alumno:
                f.write(item.DNI+"/"+item.Nombre+"/"+item.Apellido+"/"+item.Division+'\n')
        f.close()

        p=open("ArchivoProfesores.txt", "w")
        for item in ListaPersonas:
            if type(item) is Profesores:
                p.write(item.DNI+"/"+item.Nombre+"/"+item.Apellido+"/"+str(item.PorcentajeDescuento)+'\n')
        p.close()

        a=open("ArchivoPlatos.txt", "w")
        for item in ListaPlatos:
            a.write(item.Nombre+"/"+str(item.Precio)+'\n')
        a.close()

        j=open("ArchivoPedidos.txt", "w")
        for item in ListaPedidos:
            j.write(str(idPedido) + '\n')
            j.write(str(item.idPedido)+"/"+
                    str(item.FechaCreacion.year)+"/"+
                    str(item.FechaCreacion.month)+"/"+
                    str(item.FechaCreacion.day)+"/"+
                    item.Persona.DNI+"/"+
                    str(item.FechaEntrega.year)+"/"+
                    str(item.FechaEntrega.month)+"/"+
                    str(item.FechaEntrega.day)+"/"+
                    item.Plato.Nombre+"/"+
                    item.SeEntrego)
            j.write('\n')
        j.close()

        print("Archivo guardado con exito")
        input()


    if x == '1':
        os.system('cls' if os.name == 'nt' else 'clear')

        Aux = None

        p=open("ArchivoAlumnos.txt", "r")
        for line in p:
            if line == "":
                break
            Aux=line.split("/")
            unAlumnoAux=Alumno()
            unAlumnoAux.setDNI(Aux[0])
            unAlumnoAux.setNombre(Aux[1])
            unAlumnoAux.setApellido(Aux[2])
            unAlumnoAux.setDivision(Aux[3])
            ListaPersonas.append(unAlumnoAux)
        p.close()

        j=open("ArchivoProfesores.txt", "r")
        for line in j:
            if line == "":
                break
            Aux=line.split("/")
            unProfesorAux=Profesores()
            unProfesorAux.setDNI(Aux[0])
            unProfesorAux.setNombre(Aux[1])
            unProfesorAux.setApellido(Aux[2])
            unProfesorAux.setDescuento(int(Aux[3]))
            ListaPersonas.append(unProfesorAux)
        j.close()

        l=open("ArchivoPlatos.txt", "r")
        for line in l:
            if line == "":
                break
            Aux=line.split("/")
            unPlatoAux=Platos()
            unPlatoAux.setNombre(Aux[0])
            unPlatoAux.setPrecio(int(Aux[1]))
            ListaPlatos.append(unPlatoAux)
        l.close()

        k=open("ArchivoPedidos.txt", "r")
        for line in k:
            if line == "":
                break
            Aux=line.split("/")

            idPedido=Aux[-1]

            unPedidoAux=Pedido()
            unPedidoAux.idPedido=int(Aux[0])
            unPedidoAux.setFechaCreacion(int(Aux[1]), int(Aux[2]), int(Aux[3]))
            for item in ListaPersonas:
                if item.DNI == Aux[4]:
                    unPedidoAux.agregarPersona(item)
            unPedidoAux.setFechaEntrega(int(Aux[5]), int(Aux[6]), int(Aux[7]))
            for item in ListaPlatos:
                if item.Nombre == Aux[8]:
                    unPedidoAux.Plato=item
            unPedidoAux.setSeEntrego(Aux[9])
            ListaPedidos.append(unPedidoAux)
        k.close()

        idPedido=ListaPedidos[-1].idPedido

        print("Archivo Cargado Satosfactoriamente")
        input()


    if x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        unAlumno=Alumno()

        DNI = input("Ingresar DNI: ")
        unAlumno.setDNI(DNI)

        Nombre = input("Ingresar nombre: ")
        unAlumno.setNombre(Nombre)

        Apellido = input("Ingresar apellido: ")
        unAlumno.setApellido(Apellido)

        Division = input("Ingresar division: ")
        unAlumno.setDivision(Division)

        ListaPersonas.append(unAlumno)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno creado")
        print("Enter para continuar")
        input()


    if x == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        unProfesor=Profesores()

        DNI = input("Ingresar DNI: ")
        unProfesor.setDNI(DNI)

        Nombre=input("Ingresar nombre: ")
        unProfesor.setNombre(Nombre)

        Apellido=input("Ingresar apellido: ")
        unProfesor.setApellido(Apellido)

        Descuento=input("Ingresar Descuento: ")
        unProfesor.setDescuento(Descuento)

        ListaPersonas.append(unProfesor)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor creado")
        print("Enter para continuar")
        input()


    if x == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        unPlato=Platos()

        Nombre=input("Ingresar nombre: ")
        unPlato.setNombre(Nombre)

        Precio=input("Ingresar precio: ")
        unPlato.setPrecio(int(Precio))

        ListaPlatos.append(unPlato)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato creado")
        print("Enter para continuar")
        input()


    if x == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        unPedido=Pedido()

        idPedido+=1
        unPedido.idPedido = idPedido

        print("El id del pedido es %d" %(unPedido.idPedido))
        print("Enter para continuar")
        input()

        DNI=input("Ingresar DNI de la persona del pedido: ")
        for item in ListaPersonas:
            if item.DNI==DNI:
                unPedido.agregarPersona(item)

        print("Ingresar la fecha de creacion: ")
        Anio=input("Ingresar el anio: ")
        Mes=input("Ingresar el Mes: ")
        Dia=input("Ingresar el dia: ")
        unPedido.setFechaCreacion(int(Anio),int(Mes),int(Dia))

        print("Ingresar la fecha de entrega: ")
        Anio=input("Ingresar el anio: ")
        Mes=input("Ingresar el Mes: ")
        Dia=input("Ingresar el dia: ")
        unPedido.setFechaEntrega(int(Anio),int(Mes),int(Dia))

        Nombre=input("Ingresar nombre del plato del pedido: ")
        for item in ListaPlatos:
            if item.Nombre==Nombre:
                unPedido.setPlato(item)

        Entrega=input("Se entrego el pedido?: ")
        unPedido.setSeEntrego(Entrega)

        print("El precio del plato es de %d pesos" %(unPedido.calcularPrecio()))
        input()

        ListaPedidos.append(unPedido)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido creado")
        print("Enter para continuar")
        input()


    if x == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        DNI=input("DNI del alumno a modificar: ")

        Auxiliar=None
        for item in ListaPersonas:
            if item.DNI == DNI:
                Auxiliar=item

        DNI = input("Ingresar DNI: ")
        Auxiliar.setDNI(DNI)

        Nombre = input("Ingresar nombre: ")
        Auxiliar.setNombre(Nombre)

        Apellido = input("Ingresar apellido: ")
        Auxiliar.setApellido(Apellido)

        Division = input("Ingresar division: ")
        Auxiliar.setDivision(Division)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno Modificado")
        print("Enter para continuar")
        input()


    if x == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        DNI = input("DNI del Profesor a modificar: ")

        Auxiliar = None
        for item in ListaPersonas:
            if item.DNI == DNI:
                Auxiliar = item

        DNI = input("Ingresar DNI: ")
        Auxiliar.setDNI(DNI)

        Nombre = input("Ingresar nombre: ")
        Auxiliar.setNombre(Nombre)

        Apellido = input("Ingresar apellido: ")
        Auxiliar.setApellido(Apellido)

        Descuento = input("Ingresar Descuento: ")
        Auxiliar.setDescuento(Descuento)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor Modificado")
        print("Enter para continuar")
        input()


    if x == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        Auxiliar=None
        Nombre=input("Nombre del plato a modificar: ")
        for item in ListaPlatos:
            if item.Nombre == Nombre:
                Auxiliar=item

        Nombre=input("Ingresar nombre: ")
        Auxiliar.setNombre(Nombre)

        Precio=input("Ingresar precio: ")
        Auxiliar.setPrecio(int(Precio))

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato creado")
        print("Enter para continuar")
        input()


    if x == '9':
        os.system('cls' if os.name == 'nt' else 'clear')
        Auxiliar=None
        id=input("Ingresar el id del pedido a modificar: ")
        for item in ListaPedidos:
            if item.idPedido==id:
                Auxiliar=item


        print("El id del pedido es %d" %(Auxiliar.idPedido))
        print("Enter para continuar")
        input()

        DNI=input("Ingresar DNI de la persona del DNI: ")
        for item in ListaPersonas:
            if item.DNI==DNI:
                Auxiliar.agregarPersona(item)

        print("Ingresar la fecha de creacion")
        Anio=input("Ingresar el anio: ")
        Mes=input("Ingresar el Mes: ")
        Dia=input("Ingresar el dia: ")
        Auxiliar.setFechaCreacion(int(Anio),int(Mes),int(Dia))

        print("Ingresar la fecha de entrega: ")
        Anio=input("Ingresar el anio: ")
        Mes=input("Ingresar el Mes: ")
        Dia=input("Ingresar el dia: ")
        Auxiliar.setFechaEntrega(int(Anio),int(Mes),int(Dia))

        Nombre=input("Ingresar nombre del plato del pedido: ")
        for item in ListaPlatos:
            if item.Nombre==Nombre:
                Auxiliar.setPlato(Platos)

        Entrega=input("Se entrego el pedido?: ")
        Auxiliar.setSeEntrego(Entrega)

        print("El precio del plato es de %d pesos" %(Auxiliar.calcularPrecio()))
        input()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido modificado")
        print("Enter para continuar")
        input()


    if x == '10':
        os.system('cls' if os.name == 'nt' else 'clear')
        DNI=input("Ingresar DNI del alumno a eliminar: ")
        Auxiliar=None
        for item in ListaPersonas:
            if DNI==item.DNI:
                Auxiliar=item
        ListaPersonas.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alumno eliminado exitosamente")
        input()


    if x == '11':
        os.system('cls' if os.name == 'nt' else 'clear')
        DNI=input("Ingresar DNI del profesor a eliminar: ")
        Auxiliar=None
        for item in ListaPersonas:
            if DNI==item.DNI:
                Auxiliar=item
        ListaPersonas.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Profesor eliminado exitosamente")
        input()


    if x == '12':
        os.system('cls' if os.name == 'nt' else 'clear')
        Nombre=input("Ingresar nombre del plato a eliminar: ")
        Auxiliar=None
        for item in ListaPlatos:
            if Nombre==item.Nombre:
                Auxiliar=item
        ListaPlatos.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Plato eliminado exitosamente")
        input()


    if x == '13':
        os.system('cls' if os.name == 'nt' else 'clear')
        id=input("Ingresar id del pedido a eliminar: ")
        Auxiliar=None
        for item in ListaPedidos:
            if id==item.idPedido:
                Auxiliar=item
        ListaPedidos.remove(Auxiliar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pedido eliminado exitosamente")
        input()


    if x == '14':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Ingresar fecha: ")
        Anio=input("Ingresar anio: ")
        Mes=input("Ingresar Mes: ")
        Dia=input("Ingresar Dia: ")

        j=0
        for item in ListaPedidos:
            if item.FechaEntrega.year == int(Anio) and item.FechaEntrega.month == int(Mes) and item.FechaEntrega.day == int(Dia):
                print("Id del pedido: %d" % (item.idPedido))
                print("Persona que lo ordeno es: %s %s" % (
                item.Persona.Nombre, item.Persona.Apellido))
                print("La fecha de creacion del plato es: %d %d %d" % (
                item.FechaCreacion.year, item.FechaCreacion.month,
                item.FechaCreacion.day))
                print("La fecha de entrega del plato es: %d %d %d" % (
                item.FechaEntrega.year, item.FechaEntrega.month,
                item.FechaEntrega.day))
                print("Id del pedido: %d" % (item.idPedido))
                print("Se entrego?: %s" % (item.SeEntrego))
                print(" ")
                print(" ")
                print("Entrer para continuar")
                input()
            else:
                j+=1
        if j>=1:
            print("No hay pedidos para ese dia")
            input()

    if x == '15':
        break